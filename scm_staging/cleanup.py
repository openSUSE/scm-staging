import argparse
import asyncio
from py_gitea_opensuse_org import (
    ApiClient,
    CreateIssueCommentOption,
    EditPullRequestOption,
    IssueApi,
    MergePullRequestOption,
    RepositoryApi,
)
from py_obs.logger import LOGGER
from py_obs.osc import Osc

# from py_obs.project import Package, Project
from py_obs.request import RequestStatus, fetch_request

from scm_staging.db import (
    PullRequestToSubmitRequest,
    create_db,
    find_submitrequests,
    remove_submit_request,
)
from scm_staging.db import add_db_file_arg


async def process_sr(
    sr_state: RequestStatus, pr_to_sr: PullRequestToSubmitRequest, api_client: ApiClient
) -> bool:
    """Perform the actions on a submit request and return whether it can be
    removed from the database.

    The following actions are performed:
    - nothing for superseded requests
    - accepted submit requests with the merge flag set result in the
      corresponding pull request being merged
    - declined submit requests have the pull request closed with a comment that
      the submit request has been declined added to the pull request
    """
    if sr_state == RequestStatus.SUPERSEDED:
        return True

    if sr_state not in (RequestStatus.ACCEPTED, RequestStatus.DECLINED):
        return False

    kwargs = {
        "owner": (owner := pr_to_sr.gitea_repo_owner),
        "repo": (repo := pr_to_sr.gitea_repo_name),
        "index": (pr_num := pr_to_sr.pull_request_number),
    }

    repo_api = RepositoryApi(api_client)
    issue_api = IssueApi(api_client)

    if sr_state == RequestStatus.ACCEPTED and pr_to_sr.merge_pr:
        pr = await repo_api.repo_get_pull_request(**kwargs)
        if pr.state == "open":
            try:
                await repo_api.repo_merge_pull_request(
                    **kwargs, body=MergePullRequestOption(Do="merge")
                )
            except Exception as exc:
                LOGGER.error(
                    "Could not merge pr %s/%s:%s, got: %s", owner, repo, pr_num, exc
                )
                return False

    if sr_state == RequestStatus.DECLINED:
        await repo_api.repo_edit_pull_request(
            **kwargs, body=EditPullRequestOption(state="closed")
        )
        await issue_api.issue_create_comment(
            **kwargs,
            body=CreateIssueCommentOption(
                body=f"""Submit Request [sr#{pr_to_sr.submit_request_id}](https://build.opensuse.org/request/show/{pr_to_sr.submit_request_id}) has been declined."""
            ),
        )

    return True


async def process_all_stored_srs(
    osc: Osc, api_client: ApiClient, db_file_name: str
) -> None:
    """General cleanup task of the db: process all stored submitrequests and
    optionally close/merge the corresponding pull requests.

    """
    create_db(db_file_name)
    srs = find_submitrequests(db_file_name)

    for pr_to_sr in srs:
        try:
            req = await fetch_request(
                osc, request_id=(sr_id := pr_to_sr.submit_request_id)
            )
            if (rq_state := req.state) and await process_sr(
                rq_state.state, pr_to_sr, api_client
            ):
                remove_submit_request(db_file_name, sr_id=sr_id)
        except Exception as exc:
            LOGGER.error(
                "Failed to process SR/PR (%s): %s", pr_to_sr, exc, exc.with_traceback
            )


def cleanup() -> None:
    from scm_staging.webhook import AppConfig

    loop = asyncio.get_event_loop()

    parser = argparse.ArgumentParser(
        description="Process all stored submitrequests in the database"
    )
    parser = add_db_file_arg(parser)
    args = parser.parse_args()

    app_conf = AppConfig.from_env()
    loop.run_until_complete(
        process_all_stored_srs(app_conf.osc, app_conf._api_client, args.db_file[0])
    )
