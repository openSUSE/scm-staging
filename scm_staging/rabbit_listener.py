"""This module holds the functions listening to the rabbitmq bus of OBS for
package build results and updating the commit status.

"""

import asyncio
import json
from typing import TypedDict
from pika.adapters.blocking_connection import BlockingChannel
from pika.exchange_type import ExchangeType
from pika.spec import Basic
import pika
import pika.exceptions
from py_gitea_opensuse_org import ApiClient


from typing import NotRequired, TypedDict
from py_gitea_opensuse_org import MergePullRequestOption
from py_gitea_opensuse_org.api.repository_api import RepositoryApi
from py_gitea_opensuse_org.models.pull_request import PullRequest


from scm_staging.ci_status import set_commit_status_from_obs
from scm_staging.db import (
    PullRequestToSubmitRequest,
    create_db,
    find_submitrequests,
    remove_submit_request,
)
from scm_staging.logger import LOGGER
from scm_staging.webhook import DEFAULT_DB_NAME, AppConfig


_PREFIX = "opensuse.obs"


class PackageBuildSuccessPayload(TypedDict):
    project: str
    package: str
    repository: str
    arch: str
    release: str
    readytime: str
    srcmd5: str
    rev: str
    reason: str
    bcnt: str
    verifymd5: str
    starttime: str
    endtime: str
    workerid: str
    versrel: str
    buildtype: str


class PackageBuildFailurePayload(PackageBuildSuccessPayload):
    previouslyfailed: str


class PackageBuildUnchangedPayload(PackageBuildSuccessPayload):
    pass


class ActionPayload(TypedDict):
    action_id: int
    type: str
    sourceproject: str
    sourcepackage: str
    sourcerevision: str
    targetproject: str
    targetpackage: str
    makeoriginolder: NotRequired[bool]
    sourceupdate: NotRequired[str]


class RequestStateChangedPayload(TypedDict):
    author: str
    comment: str
    description: str
    id: int
    number: int
    actions: list[ActionPayload]
    state: str
    when: str
    who: str
    oldstate: str
    namespace: str
    duration: int


async def pr_from_pkg_name(
    payload: PackageBuildSuccessPayload
    | PackageBuildFailurePayload
    | PackageBuildUnchangedPayload,
    osc_username: str,
    api_client: ApiClient,
) -> PullRequest | None:
    if not f"home:{osc_username}:SCM_STAGING:Factory" in payload["project"]:
        return None

    repo_api = RepositoryApi(api_client)

    repo_name, pr_num = payload["project"].split(":")[-2:]
    if repo_name != payload["package"]:
        raise ValueError(
            f"Mismatch in the package name, got {repo_name} from the project and {payload['package']} from the package itself."
        )
    return await repo_api.repo_get_pull_request(
        "rpm",
        repo_name,
        int(pr_num),
    )


async def merge_pr(pr: PullRequestToSubmitRequest, api_client: ApiClient) -> None:
    repo_api = RepositoryApi(api_client)
    await repo_api.repo_merge_pull_request(
        owner=pr.gitea_repo_owner,
        repo=pr.gitea_repo_name,
        index=pr.pull_request_number,
        body=MergePullRequestOption(Do="merge"),
    )


#: routing key of the message that a request change its state
_SR_ACK_ROUTING_KEY = f"{_PREFIX}.request.state_change"


def rabbit_listener(db_file: str) -> None:
    loop = asyncio.get_event_loop()
    app_config = AppConfig.from_env()

    def callback(
        ch: BlockingChannel,
        method: Basic.Deliver,
        properties: pika.BasicProperties,
        body: bytes,
    ) -> None:
        if (method.routing_key or "") not in (
            f"{_PREFIX}.package.build_success",
            f"{_PREFIX}.package.build_fail",
            f"{_PREFIX}.package.build_unchanged",
            _SR_ACK_ROUTING_KEY,
        ):
            return

        if method.routing_key == _SR_ACK_ROUTING_KEY:
            try:
                rq_payload: RequestStateChangedPayload = json.loads(body.decode())
                if rq_payload["state"] == "accepted" and (
                    prs := find_submitrequests(db_file, sr_id=rq_payload["number"])
                ):
                    assert len(prs) == 1
                    if prs[0].merge_pr:
                        loop.run_until_complete(
                            merge_pr(prs[0], app_config._api_client)
                        )
                    remove_submit_request(db_file, prs[0].submit_request_id)

            except Exception as exc:
                LOGGER.debug(
                    "Failed to process message with the body '%s', got the exception '%s'",
                    body.decode(),
                    exc,
                )
                pass
            return

        try:
            payload: PackageBuildSuccessPayload | PackageBuildFailurePayload = (
                json.loads(body.decode())
            )
            prs = find_submitrequests(
                db_file,
                obs_project_name=payload["project"],
                obs_package_name=payload["package"],
            )
            if len(prs) == 1:
                LOGGER.debug(
                    "package %s got built in %s", payload["package"], payload["project"]
                )
                repo_api = RepositoryApi(app_config._api_client)
                # get the pr for the commit sha
                pr = loop.run_until_complete(
                    repo_api.repo_get_pull_request(
                        owner=prs[0].gitea_repo_owner,
                        repo=prs[0].gitea_repo_name,
                        index=prs[0].pull_request_number,
                    )
                )
                loop.run_until_complete(
                    set_commit_status_from_obs(
                        app_config.osc,
                        app_config._api_client,
                        commit_sha=pr.head.sha,
                        repo_name=prs[0].gitea_repo_name,
                        repo_owner=prs[0].gitea_repo_owner,
                        pkg_name=payload["package"],
                        project_name=payload["project"],
                    )
                )
        except Exception:
            pass

    while True:
        connection: pika.BlockingConnection | None = None
        channel: BlockingChannel | None = None
        try:
            connection = pika.BlockingConnection(
                pika.URLParameters("amqps://opensuse:opensuse@rabbit.opensuse.org")
            )
            channel = connection.channel()

            channel.exchange_declare(
                exchange="pubsub",
                exchange_type=ExchangeType.topic,
                passive=True,
                durable=True,
            )

            result = channel.queue_declare("", exclusive=True)
            queue_name = result.method.queue
            assert queue_name

            channel.queue_bind(exchange="pubsub", queue=queue_name, routing_key="#")

            channel.basic_consume(queue_name, callback, auto_ack=True)

            channel.start_consuming()

        except pika.exceptions.ConnectionClosedByBroker:
            LOGGER.debug("Broker closed connection, retrying")
            continue

        except pika.exceptions.AMQPChannelError as err:
            # Do not recover on channel errors
            LOGGER.error("Caught a channel error: %s, stopping!", err)
            break

        except pika.exceptions.AMQPConnectionError as err:
            # Recover on all other connection errors
            LOGGER.debug("Connection was closed: %s, retrying", err)
            continue

        finally:
            if channel:
                channel.close()
                channel = None
            if connection:
                connection.close()
                connection = None


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--db-file",
        nargs=1,
        default=[DEFAULT_DB_NAME],
        help="SQLite3 database tracking the submitrequests",
    )

    args = parser.parse_args()
    db_file = args.db_file[0]

    create_db(db_file)
    rabbit_listener(db_file)
