"""This module has a helper function to automatically create a pull request from
``gitea.opensuse.org/rpm/$pkg`` to ``gitea.opensuse.org/pool/$pkg``.

"""

import asyncio
import tempfile
from git.remote import Remote
from py_gitea_opensuse_org import (
    CreatePullRequestOption,
    RepositoryApi,
)
from git.repo import Repo
from py_gitea_opensuse_org.exceptions import ApiException

from scm_staging.webhook import AppConfig


async def create_pr_to_pool(
    pkg_name: str, gitea_user: str, repo_api: RepositoryApi
) -> None:
    try:
        await repo_api.create_fork(owner="pool", repo=pkg_name)
    except ApiException:
        # If the repo has already been forked, then reading it would succeed => continue
        # If another error occurred and the repo doesn't exist => this will fail
        # as well and abort
        await repo_api.repo_get(owner="pool", repo=pkg_name)

    with tempfile.TemporaryDirectory() as tmp_dir:
        repo = Repo.clone_from(
            url=f"gitea@gitea.opensuse.org:{gitea_user}/{pkg_name}.git", to_path=tmp_dir
        )
        remote = Remote.create(
            repo=repo, name="rpm", url=f"https://gitea.opensuse.org/rpm/{pkg_name}"
        )
        remote.fetch()

        rpm_factory = repo.commit("rpm/factory")

        repo.git.reset("--hard", rpm_factory.hexsha)
        origin = repo.remote("origin")
        origin.push(force=True)

    await repo_api.repo_create_pull_request(
        "pool",
        pkg_name,
        CreatePullRequestOption(
            base="factory", head=f"{gitea_user}:factory", title="Sync package with rpm/"
        ),
    )


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "package_name",
        nargs=1,
        type=str,
        help="The name of the package for which a PR will be created",
    )

    args = parser.parse_args()

    conf = AppConfig.from_env()
    repo_api = RepositoryApi(api_client=conf._api_client)

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            create_pr_to_pool(args.package_name[0], conf.gitea_user, repo_api)
        )
    finally:
        loop.run_until_complete(conf.osc.teardown())
