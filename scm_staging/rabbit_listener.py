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
from py_gitea_opensuse_org import (
    CreateIssueCommentOption,
    MergePullRequestOption,
    RepositoryApi,
    EditPullRequestOption,
    IssueApi,
)
from py_obs.request import RequestStatus
from pydantic import BaseModel, ValidationError

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


class PackageBuildSuccessPayload(BaseModel):
    project: str
    package: str
    repository: str
    arch: str
    release: str | None
    readytime: str
    srcmd5: str
    rev: str | None
    reason: str
    bcnt: str | None
    verifymd5: str | None
    starttime: str
    endtime: str
    workerid: str
    versrel: str | None
    buildtype: str


class PackageBuildFailurePayload(PackageBuildSuccessPayload):
    previouslyfailed: str


class PackageBuildUnchangedPayload(PackageBuildSuccessPayload):
    pass


class ActionPayload(BaseModel):
    action_id: int
    type: str
    sourceproject: str | None
    sourcepackage: str | None
    sourcerevision: str | None
    targetproject: str
    targetpackage: str | None
    makeoriginolder: bool | None
    sourceupdate: str | None


class RequestChangedPayload(BaseModel):
    author: str
    comment: str | None
    description: str | None
    number: int
    actions: list[ActionPayload]
    state: str
    when: str
    who: str


class RequestStateChangedPayload(RequestChangedPayload):
    id: int
    oldstate: str
    namespace: str
    duration: int | None


class RequestReviewChangedPayload(BaseModel):
    reviewers: str | None
    by_user: str | None
    by_group: str | None
    by_project: str | None
    by_package: str | None


class RequestReviewsDonePayload(RequestReviewChangedPayload):
    author: str
    comment: str
    description: str | None
    number: int
    actions: list[ActionPayload]
    state: str
    when: str
    who: str


class RequestCommentPayload(RequestChangedPayload):
    commenters: list[str]
    commenter: str
    comment_body: str
    comment_title: str | None
    # useless field, use number instead
    request_number: int | None


#: routing key of the message that a request change its state
# _SR_ACK_ROUTING_KEY = f"{_PREFIX}.request.state_change"

_SR_CREATE_RK = f"{_PREFIX}.request.create"
_SR_CHANGE_RK = f"{_PREFIX}.request.change"
_SR_DELETE_RK = f"{_PREFIX}.request.delete"
_SR_STATE_CHANGE_RK = f"{_PREFIX}.request.state_change"
_SR_REVIEW_WANTED_RK = f"{_PREFIX}.request.review_wanted"
_SR_REVIEW_CHANGED_RK = f"{_PREFIX}.request.review_changed"
_SR_REVIEWS_DONE_RK = f"{_PREFIX}.request.reviews_done"
_SR_COMMENT_RK = f"{_PREFIX}.request.comment"


_RT_TO_TYPE_MAPPING = {
    _SR_CREATE_RK: RequestChangedPayload,
    _SR_CHANGE_RK: RequestChangedPayload,
    _SR_DELETE_RK: RequestChangedPayload,
    _SR_STATE_CHANGE_RK: RequestStateChangedPayload,
    # _SR_REVIEW_WANTED_RK: Revie
    _SR_REVIEW_CHANGED_RK: RequestReviewChangedPayload,
    _SR_REVIEWS_DONE_RK: RequestReviewsDonePayload,
    _SR_COMMENT_RK: RequestCommentPayload,
}


def _process_message(routing_key: str, body: str) -> None:
    if routing_key not in _RT_TO_TYPE_MAPPING.keys():
        return

    payload_type = _RT_TO_TYPE_MAPPING[routing_key]
    payload = payload_type(**json.loads(body))

    if routing_key in (_SR_COMMENT_RK, _SR_STATE_CHANGE_RK):
        LOGGER.info(payload)


def rabbit_listener(db_file: str) -> None:
    loop = asyncio.get_event_loop()
    app_config = AppConfig.from_env()

    def callback(
        ch: BlockingChannel,
        method: Basic.Deliver,
        properties: pika.BasicProperties,
        body: bytes,
    ) -> None:
        try:
            _process_message(method.routing_key or "", body.decode())
        except ValidationError as err:
            LOGGER.error(
                "Failed to process '%s' with payload: '%s', got error: %s",
                method.routing_key,
                body.decode(),
                err,
            )

        if (method.routing_key or "") not in (
            f"{_PREFIX}.package.build_success",
            f"{_PREFIX}.package.build_fail",
            f"{_PREFIX}.package.build_unchanged",
            _SR_STATE_CHANGE_RK,
            _SR_COMMENT_RK,
        ):
            return

        repo_api = RepositoryApi(app_config._api_client)
        issue_api = IssueApi(app_config._api_client)

        class Kwargs(TypedDict):
            owner: str
            repo: str
            index: int

        def gitea_api_kwargs_from_pr_list(
            prs: list[PullRequestToSubmitRequest],
        ) -> Kwargs:
            return {
                "owner": prs[0].gitea_repo_owner,
                "repo": prs[0].gitea_repo_name,
                "index": prs[0].pull_request_number,
            }

        if method.routing_key == _SR_STATE_CHANGE_RK:
            rq_payload = RequestStateChangedPayload(**json.loads(body.decode()))
            if prs := find_submitrequests(db_file, sr_id=rq_payload.number):
                assert len(prs) == 1

                kwargs = gitea_api_kwargs_from_pr_list(prs)

                if rq_payload.state == RequestStatus.ACCEPTED:
                    if prs[0].merge_pr:
                        loop.run_until_complete(
                            repo_api.repo_merge_pull_request(
                                **kwargs, body=MergePullRequestOption(Do="merge")
                            )
                        )
                elif rq_payload.state == RequestStatus.DECLINED:
                    loop.run_until_complete(
                        repo_api.repo_edit_pull_request(
                            **kwargs, body=EditPullRequestOption(state="closed")
                        )
                    )

                    loop.run_until_complete(
                        issue_api.issue_create_comment(
                            **kwargs,
                            body=CreateIssueCommentOption(
                                body=f"""Submit Request [sr#{prs[0].submit_request_id}](https://build.opensuse.org/request/show/{prs[0].submit_request_id}) has been declined by {rq_payload.who}:
{rq_payload.comment}"""
                            ),
                        )
                    )

                else:
                    return

                remove_submit_request(db_file, prs[0].submit_request_id)
            return

        elif method.routing_key == _SR_COMMENT_RK:
            comment_payload = RequestCommentPayload(**json.loads(body.decode()))

            # don't mirror comments by the bot (these are just SR closed/created
            # messages and similar ones)
            if comment_payload.commenter == app_config.osc.username:
                return

            if prs := find_submitrequests(db_file, sr_id=comment_payload.number):
                assert len(prs) == 1

                kwargs = gitea_api_kwargs_from_pr_list(prs)

                loop.run_until_complete(
                    issue_api.issue_create_comment(
                        **kwargs,
                        body=CreateIssueCommentOption(
                            body=f"""New comment by {comment_payload.commenter}:
{comment_payload.comment_body}
"""
                        ),
                    )
                )
            return

        try:
            kwargs = json.loads(body.decode())
            try:
                payload = PackageBuildFailurePayload(**kwargs)
            except ValidationError:
                payload = PackageBuildSuccessPayload(**kwargs)

            prs = find_submitrequests(
                db_file,
                obs_project_name=payload.project,
                obs_package_name=payload.package,
            )
            if len(prs) == 1:
                LOGGER.debug(
                    "package %s got built in %s", payload.package, payload.project
                )

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
                        pkg_name=payload.package,
                        project_name=payload.project,
                    )
                )
        except Exception as exc:
            LOGGER.error(
                "Failed to set commit status from msg '%s': '%s', got: %s",
                method.routing_key,
                kwargs,
                exc,
            )

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
                if channel.is_open:
                    channel.close()
                channel = None
            if connection:
                if connection.is_open:
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

    LOGGER.configure_log_files()
    create_db(db_file)
    rabbit_listener(db_file)
