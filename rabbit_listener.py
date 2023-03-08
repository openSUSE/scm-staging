#!/usr/bin/env python3

import asyncio
import json
from typing import TypedDict

import aio_pika
from swagger_client.api.repository_api import RepositoryApi
from swagger_client.models.pull_request import PullRequest

from scm_staging.ci_status import set_commit_status_from_obs
from scm_staging.webhook import AppConfig


_PREFIX = "opensuse.obs"

_app_config = AppConfig.from_env()


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


async def update_commit_status(pr: PullRequest, pkg_name: str, prj_name: str) -> None:
    await set_commit_status_from_obs(
        _app_config.osc,
        _app_config._api_client,
        commit_sha=(head := pr.head).sha,
        repo_name=(repo := head.repo).name,
        repo_owner=repo.owner.login,
        pkg_name=pkg_name,
        project_name=prj_name,
    )


async def pr_from_pkg_name(
    payload: PackageBuildSuccessPayload
    | PackageBuildFailurePayload
    | PackageBuildUnchangedPayload,
) -> PullRequest | None:
    if not f"home:{_app_config.bot_user}:SCM_STAGING:Factory" in payload["project"]:
        return None

    repo_api = RepositoryApi(_app_config._api_client)

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


async def main() -> None:
    connection = await aio_pika.connect(
        "amqps://opensuse:opensuse@rabbit.opensuse.org",
    )

    channel = await connection.channel()
    queue = await channel.declare_queue(exclusive=True, auto_delete=True)

    exchange = await channel.declare_exchange(
        "pubsub", type=aio_pika.ExchangeType.TOPIC, passive=True, durable=True
    )
    await queue.bind(exchange, routing_key="#")

    # Maximum message count which will be processing at the same time.
    await channel.set_qos(prefetch_count=10)

    async with queue.iterator() as queue_iter:
        async for message in queue_iter:
            async with message.process():
                if (message.routing_key or "") not in (
                    f"{_PREFIX}.package.build_success",
                    f"{_PREFIX}.package.build_fail",
                    f"{_PREFIX}.package.build_unchanged",
                ):
                    continue

                try:
                    payload: PackageBuildSuccessPayload | PackageBuildFailurePayload = (
                        json.loads(message.body.decode())
                    )
                    pr = await pr_from_pkg_name(payload)
                    if pr:
                        await update_commit_status(
                            pr, pkg_name=payload["package"], prj_name=payload["project"]
                        )
                except Exception:
                    pass

    # try:
    #     # Wait until terminate
    #     await asyncio.Future()
    # finally:
    await connection.close()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
