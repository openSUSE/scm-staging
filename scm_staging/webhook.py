import asyncio
from dataclasses import dataclass
from enum import StrEnum, unique
import os
from gitea.api_config import APIConfig

from fastapi import FastAPI
from pydantic import BaseModel
from gitea.services.async_repository_service import repoListPullReviews

# from swagger_client import (
#     Configuration,
#     ApiClient,
#     IssueApi,
#     CreateIssueCommentOption,
#     RepositoryApi,
#     PullReview,
# )

from scm_staging.ci_status import set_commit_status_from_obs

from scm_staging.obs import Osc
from . import request
from .request import RequestActionType
from .request import RequestStatus
from scm_staging.xml_factory import StrElementField
from . import project
from scm_staging.logger import LOGGER

app = FastAPI()


class User(BaseModel):
    id: int
    login: str
    full_name: str
    email: str


class Label(BaseModel):
    id: int
    name: str
    color: str
    description: str
    url: str


class Milestone(BaseModel):
    id: int
    title: str
    description: str
    state: str
    open_issues: int
    closed_issues: int


class Repository(BaseModel):
    id: int
    owner: User
    name: str
    full_name: str
    description: str
    html_url: str
    ssh_url: str
    clone_url: str


class Ref(BaseModel):
    label: str
    ref: str
    sha: str
    repo_id: int
    repo: Repository


@unique
class PullRequestReviewType(StrEnum):
    APPROVED = "pull_request_review_approved"
    REJECTED = "pull_request_review_rejected"
    COMMENT = "pull_request_comment"


class Review(BaseModel):
    type: PullRequestReviewType | str
    content: str


class PullRequest(BaseModel):
    id: int
    url: str
    number: int
    user: User
    title: str
    body: str
    labels: list[Label]
    milestone: Milestone | None
    assignee: User | None
    assignees: list[User] | None
    state: str
    is_locked: bool
    base: Ref
    head: Ref
    merge_base: str
    # FIXME: is a date
    created_at: str
    # FIXME: is a date
    updated_at: str


class PullRequestPayload(BaseModel):
    action: str
    number: int
    pull_request: PullRequest
    sender: User
    repository: Repository
    review: Review | None


@dataclass(frozen=True)
class AppConfig:
    bot_user: str
    branch_name: str
    osc: Osc
    destination_project: str

    _conf: APIConfig  # Configuration
    # _api_client: ApiClient

    async def teardown(self) -> None:
        await self.osc.teardown()

    @staticmethod
    def from_env() -> "AppConfig":
        # api_key = os.getenv("GITEA_API_KEY")
        # if not api_key:
        #     raise ValueError("GITEA_API_KEY environment variable must be set")

        conf = APIConfig(
            base_path="https://gitea.opensuse.org/api/v1"
        )  # Configuration(host="https://gitea.opensuse.org/api/v1", api_key=api_key)
        # conf.

        return AppConfig(
            osc=(osc := Osc.from_env()),
            bot_user=os.getenv("BOT_USER", osc.username),
            branch_name=os.getenv("BRANCH_NAME", "factory"),
            destination_project=os.getenv(
                "DESTINATION_PROJECT", "devel:Factory:git-workflow:mold:core"
            ),
            _conf=conf,
            # _api_client=ApiClient(conf),
        )


_app_config: AppConfig | None = None


@app.on_event("startup")
def load_app_config():
    global _app_config
    _app_config = AppConfig.from_env()


@app.on_event("shutdown")
async def teardown_osc():
    global _app_config
    if _app_config is not None:
        await _app_config.teardown()
        _app_config = None


def package_from_pull_request(payload: PullRequestPayload) -> project.Package:
    return project.Package(
        name=payload.repository.name,
        title=f"The {payload.repository.name} package",
        scmsync=f"{payload.pull_request.head.repo.clone_url}#{payload.pull_request.head.sha}",
    )


def project_from_pull_request(payload: PullRequestPayload) -> project.Project:
    assert _app_config
    return project.Project(
        name=f"home:{_app_config.bot_user}:SCM_STAGING:Factory:{payload.repository.name}:{payload.pull_request.number}",
        title=StrElementField(
            f"Project for Pull Request {payload.pull_request.number}"
        ),
        description=StrElementField(
            f"Project for Pull Request {payload.pull_request.url}"
        ),
        person=[
            project.Person(
                userid=_app_config.bot_user, role=project.PersonRole.MAINTAINER
            )
        ],
        repository=[
            project.Repository(
                name="openSUSE_Factory",
                arch=["x86_64"],
                path=[
                    project.PathEntry(project="openSUSE:Factory", repository="snapshot")
                ],
            )
        ],
    )


@app.get("/alive")
async def am_i_alive():
    return {}


async def check_if_pr_approved(
    osc: Osc,
    # api_client: ApiClient,
    api_config: APIConfig,
    owner: str,
    repo_name: str,
    pr_number: int,
    pkg_name: str,
) -> bool:
    """Checks if the pull request $owner/$repo_name/$pr_number has been approved
    by at least one maintainer of the package `pkg_name` and no changes have
    been requested.

    """
    reviews = await repoListPullReviews(
        owner, repo_name, pr_number, api_config_override=api_config
    )
    # repo_api = RepositoryApi(api_client)
    # reviews: list[PullReview] = await repo_api.repo_list_pull_reviews(
    #     owner, repo_name, pr_number
    # )

    maintainers = await project.search_for_maintainers(
        osc, pkg_name=pkg_name, groups_to_ignore=["factory-maintainers"]
    )
    usernames: list[str] = []
    if maintainers.package:
        usernames.extend(pers.name for pers in maintainers.package)
    if maintainers.project:
        usernames.extend(pers.name for pers in maintainers.project)

    usernames = list(set(usernames))

    valid_reviews = []
    for review in reviews:
        if not review.stale and review.user.login in usernames:
            valid_reviews.append(review)

    if any(review.state == "REQUEST_CHANGES" for review in valid_reviews):
        return False

    if any(review.state == "APPROVED" for review in valid_reviews):
        return True

    return False


@app.post("/hook")
async def webhook(payload: PullRequestPayload):
    assert _app_config

    LOGGER.debug(payload)

    if (
        base := payload.pull_request.base
    ).ref != _app_config.branch_name and base.label != _app_config.branch_name:
        LOGGER.debug("wrong branch name %s", base.ref)
        return {}

    pkg = package_from_pull_request(payload)
    prj = project_from_pull_request(payload)

    osc = _app_config.osc

    if payload.action in ("closed", "merged"):
        tasks = []

        reqs_to_close = await request.search_for_requests(
            osc,
            user=osc.username,
            package=pkg,
            project=prj,
            types=[RequestActionType.SUBMIT],
            states=[RequestStatus.NEW, RequestStatus.DECLINED, RequestStatus.REVIEW],
        )

        for req in reqs_to_close:
            if req.id and req.creator == osc.username:
                tasks.append(
                    request.change_state(
                        osc,
                        request=req,
                        new_state=RequestStatus.REVOKED,
                        comment=f"pull request #{payload.pull_request.number} has been closed",
                    )
                )

        await asyncio.gather(*tasks)
        await project.delete(osc, prj=prj, force=True)
        return {}

    owner = payload.repository.owner.login
    repo_name = payload.repository.name
    pr_num = payload.pull_request.number

    await set_commit_status_from_obs(
        _app_config.osc,
        _app_config._api_client,
        # use "upstream" here, otherwise the commit status will not show up in
        # the PR and will not gate it
        repo_owner=base.repo.owner.login,
        repo_name=base.repo.name,
        commit_sha=payload.pull_request.head.sha,
        pkg_name=pkg.name,
        project_name=prj.name,
    )

    # don't create SRs for not approved PRs
    if not await check_if_pr_approved(
        _app_config.osc,
        _app_config._api_client,
        owner=owner,
        repo_name=repo_name,
        pr_number=pr_num,
        pkg_name=pkg.name,
    ):
        return {}

    LOGGER.debug("PR has been approved, creating package")
    await project.send_meta(osc, prj=prj)
    await project.send_meta(osc, prj=prj, pkg=pkg)

    new_req = await request.submit_package(
        osc=osc,
        source_prj=prj.name,
        pkg_name=pkg.name,
        dest_prj=_app_config.destination_project,
        supersede_old_request=True,
    )

    # comment on the PR with a link to the SR
    issue_api = IssueApi(_app_config._api_client)
    await issue_api.issue_create_comment(
        payload.repository.owner.login,
        payload.repository.name,
        payload.pull_request.number,
        body=CreateIssueCommentOption(
            body=f"Created submit request [sr#{new_req.id}](https://build.opensuse.org/request/show/{new_req.id})"
        ),
    )

    return {}
