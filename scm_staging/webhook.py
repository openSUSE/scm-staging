import asyncio
import json
from dataclasses import dataclass
from enum import StrEnum, unique
import os
from aiohttp import ClientResponseError

from pydantic import BaseModel, ValidationError
import tornado

from py_gitea_opensuse_org import (
    Configuration,
    ApiClient,
    IssueApi,
    CreateIssueCommentOption,
    RepositoryApi,
    PullReview,
)
from py_obs.osc import Osc
from py_obs import request
from py_obs.request import RequestActionType
from py_obs.request import RequestStatus
from py_obs.xml_factory import StrElementField
from py_obs import project
from tornado.web import Application

from scm_staging.ci_status import set_commit_status_from_obs
from scm_staging.logger import LOGGER


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
    gitea_user: str
    branch_name: str
    osc: Osc
    destination_project: str

    _conf: Configuration
    _api_client: ApiClient

    @staticmethod
    def from_env() -> "AppConfig":
        api_key = os.getenv("GITEA_API_KEY")
        if not api_key:
            raise ValueError("GITEA_API_KEY environment variable must be set")

        conf = Configuration(
            api_key={"AuthorizationHeaderToken": api_key},
            api_key_prefix={"AuthorizationHeaderToken": "token"},
            host="https://gitea.opensuse.org/api/v1",
        )

        return AppConfig(
            osc=(osc := Osc.from_env()),
            gitea_user=os.getenv("BOT_USER", osc.username),
            branch_name=os.getenv("BRANCH_NAME", "factory"),
            destination_project=os.getenv(
                "DESTINATION_PROJECT", "devel:Factory:git-workflow:mold:core"
            ),
            _conf=conf,
            _api_client=ApiClient(conf),
        )


def package_from_pull_request(payload: PullRequestPayload) -> project.Package:
    return project.Package(
        name=payload.repository.name,
        title=f"The {payload.repository.name} package",
        scmsync=f"{payload.pull_request.head.repo.clone_url}#{payload.pull_request.head.sha}",
    )


class MainHandler(tornado.web.RequestHandler):
    def initialize(self, app_config: AppConfig) -> None:
        self.app_config = app_config

    def project_from_pull_request(self, payload: PullRequestPayload) -> project.Project:
        return project.Project(
            name=f"home:{self.app_config.osc.username}:SCM_STAGING:Factory:{payload.repository.name}:{payload.pull_request.number}",
            title=StrElementField(
                f"Project for Pull Request {payload.pull_request.number}"
            ),
            description=StrElementField(
                f"Project for Pull Request {payload.pull_request.url}"
            ),
            person=[
                project.Person(
                    userid=self.app_config.osc.username,
                    role=project.PersonRole.MAINTAINER,
                )
            ],
            repository=[
                project.Repository(
                    name="openSUSE_Factory",
                    arch=["x86_64"],
                    path=[
                        project.PathEntry(
                            project="openSUSE:Factory", repository="snapshot"
                        )
                    ],
                )
            ],
        )

    async def check_if_pr_approved(
        self,
        api_client: ApiClient,
        owner: str,
        repo_name: str,
        pr_number: int,
        pkg_name: str,
    ) -> bool:
        """Checks if the pull request $owner/$repo_name/$pr_number has been approved
        by at least one maintainer of the package `pkg_name` and no changes have
        been requested.

        """
        repo_api = RepositoryApi(api_client)
        reviews: list[PullReview] = await repo_api.repo_list_pull_reviews(
            owner, repo_name, pr_number
        )

        maintainers = await project.search_for_maintainers(
            self.app_config.osc,
            pkg_name=pkg_name,
            groups_to_ignore=["factory-maintainers"],
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

    async def post(self) -> None:
        if not self.request.body:
            return

        try:
            payload = PullRequestPayload(**json.loads(self.request.body))
        except ValidationError:
            return

        LOGGER.debug(payload)

        if (
            (base := payload.pull_request.base).ref != self.app_config.branch_name
            and base.label != self.app_config.branch_name
        ):
            LOGGER.debug("wrong branch name %s", base.ref)
            return

        pkg = package_from_pull_request(payload)
        prj = self.project_from_pull_request(payload)

        osc = self.app_config.osc

        if payload.action in ("closed", "merged"):
            tasks = []

            reqs_to_close = await request.search_for_requests(
                osc,
                user=osc.username,
                package=pkg,
                project=prj,
                types=[RequestActionType.SUBMIT],
                states=[
                    RequestStatus.NEW,
                    RequestStatus.DECLINED,
                    RequestStatus.REVIEW,
                ],
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
            try:
                await project.delete(osc, prj=prj, force=True)
            except ClientResponseError as cre_exc:
                if cre_exc.status == 404:
                    LOGGER.debug("Not deleting project %s, it doesn't exist", prj.name)
                else:
                    raise
            return

        owner = payload.repository.owner.login
        repo_name = payload.repository.name
        pr_num = payload.pull_request.number

        await set_commit_status_from_obs(
            self.app_config.osc,
            self.app_config._api_client,
            # use "upstream" here, otherwise the commit status will not show up in
            # the PR and will not gate it
            repo_owner=base.repo.owner.login,
            repo_name=base.repo.name,
            commit_sha=payload.pull_request.head.sha,
            pkg_name=pkg.name,
            project_name=prj.name,
        )

        # don't create SRs for not approved PRs
        if not await self.check_if_pr_approved(
            self.app_config._api_client,
            owner=owner,
            repo_name=repo_name,
            pr_number=pr_num,
            pkg_name=pkg.name,
        ):
            return

        LOGGER.debug("PR has been approved, creating package")
        await project.send_meta(osc, prj=prj)
        await project.send_meta(osc, prj=prj, pkg=pkg)

        new_req = await request.submit_package(
            osc=osc,
            source_prj=prj.name,
            pkg_name=pkg.name,
            dest_prj=self.app_config.destination_project,
            supersede_old_request=True,
        )

        # comment on the PR with a link to the SR
        issue_api = IssueApi(self.app_config._api_client)
        await issue_api.issue_create_comment(
            payload.repository.owner.login,
            payload.repository.name,
            payload.pull_request.number,
            body=CreateIssueCommentOption(
                body=f"Created submit request [sr#{new_req.id}](https://build.opensuse.org/request/show/{new_req.id})"
            ),
        )


def make_app(app_config: AppConfig) -> Application:
    return Application([(r"/hook", MainHandler, {"app_config": app_config})])


async def main():
    app_config = AppConfig.from_env()
    app = make_app(app_config)
    app.listen(8000)
    shutdown_event = asyncio.Event()
    await shutdown_event.wait()
    await app_config.osc.teardown()
