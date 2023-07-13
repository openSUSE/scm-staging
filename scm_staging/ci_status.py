"""This module contains helper functions to set the commit status (= CI status)
on gitea based on the package build on OBS.

"""

from enum import StrEnum, auto
from aiohttp import ClientResponseError
from py_gitea_opensuse_org.api.repository_api import RepositoryApi
from py_gitea_opensuse_org.api_client import ApiClient

from py_gitea_opensuse_org.models.create_status_option import CreateStatusOption
from py_gitea_opensuse_org.models.branch import Branch
from py_obs.build_result import PackageCode, fetch_build_result
from osctiny import Osc


class CommitStatusState(StrEnum):
    PENDING = auto()
    SUCCESS = auto()
    ERROR = auto()
    FAILURE = auto()
    WARNING = auto()


OBS_CI_CTX = "obs/scm/build"


async def set_commit_status_from_obs(
    osc: Osc,
    api_client: ApiClient,
    repo_owner: str,
    repo_name: str,
    commit_sha: str,
    pkg_name: str,
    project_name: str,
) -> None:
    # there's no build results (e.g. because the project & package do not exist)
    # => do nothing
    try:
        build_results = await fetch_build_result(
            osc, project_name=project_name, package_name=pkg_name
        )
    except ClientResponseError as cre_exc:
        if cre_exc.status == 404:
            return None
        raise

    pkg_status_codes = set()
    for build_res in build_results:
        for st in build_res.status:
            if st.package != pkg_name:
                continue
            pkg_status_codes.add(st.code)

    # excluded & disabled don't count towards the CI status
    pkg_status_codes -= {PackageCode.EXCLUDED, PackageCode.DISABLED}

    ci_state = CommitStatusState.FAILURE

    if (
        PackageCode.FAILED in pkg_status_codes
        or PackageCode.UNRESOLVABLE in pkg_status_codes
        or PackageCode.UNKNOWN in pkg_status_codes
    ):
        ci_state = CommitStatusState.FAILURE
    elif (
        PackageCode.BROKEN in pkg_status_codes
        or PackageCode.UNKNOWN in pkg_status_codes
    ):
        ci_state = CommitStatusState.ERROR
    elif (
        PackageCode.BLOCKED in pkg_status_codes
        or PackageCode.SCHEDULED in pkg_status_codes
        or PackageCode.BUILDING in pkg_status_codes
        or PackageCode.FINISHED in pkg_status_codes
    ):
        ci_state = CommitStatusState.PENDING
    elif pkg_status_codes == set([PackageCode.SUCCEEDED]):
        ci_state = CommitStatusState.SUCCESS

    repo_api = RepositoryApi(api_client)
    await repo_api.repo_create_status(
        owner=repo_owner,
        repo=repo_name,
        sha=commit_sha,
        body=CreateStatusOption(
            context=OBS_CI_CTX,
            target_url=f"https://build.opensuse.org/package/show/{project_name}/{pkg_name}",
            state=str(ci_state),
        ),
    )


async def fetch_hash_of_head_of_branch(
    api_client: ApiClient, repo_owner: str, repo_name: str, branch_name: str = "main"
) -> str:
    repo_api = RepositoryApi(api_client)
    branch: Branch = await repo_api.repo_get_branch(
        owner=repo_owner, repo=repo_name, branch=branch_name
    )
    return branch.commit.id


def main() -> None:
    import asyncio
    from argparse import ArgumentParser
    from scm_staging.webhook import AppConfig

    conf = AppConfig.from_env()

    parser = ArgumentParser()
    parser.add_argument(
        "--obs-pkg",
        "-p",
        type=str,
        nargs=1,
        required=True,
        help="package on OBS in the format $project/$package",
    )

    parser.add_argument(
        "--repository",
        "-r",
        type=str,
        nargs=1,
        required=True,
        help="repository on src.opensuse.org in the format $repo_owner/$repo_name",
    )
    parser.add_argument(
        "--commit-sha",
        "-c",
        type=str,
        nargs="+",
        default=[None],
        help="optional sha of the commit to set the status",
    )
    parser.add_argument(
        "--branch",
        "-b",
        type=str,
        nargs="+",
        default=["factory"],
        help="branch which' HEAD commit's status should be set (defaults to 'factory')",
    )

    args = parser.parse_args()

    project_name, pkg_name = args.obs_pkg[0].split("/")
    repo_owner, repo_name = args.repository[0].split("/")

    loop = asyncio.get_event_loop()
    if not (commit := args.commit_sha[0]):
        commit = loop.run_until_complete(
            fetch_hash_of_head_of_branch(
                conf._api_client,
                repo_owner=repo_owner,
                repo_name=repo_name,
                branch_name=args.branch[0],
            )
        )

    try:
        loop.run_until_complete(
            set_commit_status_from_obs(
                conf.osc,
                conf._api_client,
                repo_owner=repo_owner,
                repo_name=repo_name,
                commit_sha=commit,
                project_name=project_name,
                pkg_name=pkg_name,
            )
        )
    finally:
        loop.run_until_complete(conf.osc.__del__())
