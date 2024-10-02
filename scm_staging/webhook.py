"""This module contains the tornado web-application with the webhook listening
for gitea events.

"""

import asyncio
import json
from dataclasses import dataclass, field
from enum import StrEnum, unique
from multiprocessing import Process
import os
from aiohttp import ClientResponseError

from pydantic import BaseModel, ValidationError
import tornado
from tornado.options import define, options

from py_gitea_opensuse_org import (
    Configuration,
    ApiClient,
    IssueApi,
    CreateIssueCommentOption,
    RepositoryApi,
)
from py_obs.osc import Osc
from py_obs import request
from py_obs.request import RequestActionType
from py_obs.request import RequestStatus
from py_obs.service import service_wait
from py_obs.xml_factory import StrElementField
from py_obs import project
from tornado.web import Application

from scm_staging.ci_status import set_commit_status_from_obs
from scm_staging.config import BranchConfig, SubmissionStyle, load_config
from scm_staging.logger import LOGGER
from scm_staging.db import (
    DEFAULT_DB_NAME,
    PullRequestToBuild,
    PullRequestToSubmitRequest,
    create_db,
    insert_submit_request,
    remove_submit_request,
    insert_build_project,
    remove_build_project,
)


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


class Comment(BaseModel):
    id: int
    user: User
    body: str


class IssueRepository(BaseModel):
    id: int
    name: str
    owner: str
    full_name: str


class Issue(BaseModel):
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
    repository: IssueRepository
    # FIXME: is a date
    created_at: str
    # FIXME: is a date
    updated_at: str


class CommentPayload(BaseModel):
    action: str
    comment: Comment
    sender: User
    repository: Repository
    issue: Issue
    is_pull: bool


@dataclass(frozen=True)
class AppConfig:
    gitea_user: str
    branch_config: list[BranchConfig]
    osc: Osc
    db_file_name: str = DEFAULT_DB_NAME
    build_project_prefix: str = ""

    _conf: Configuration = field(default_factory=Configuration)
    _api_client: ApiClient = field(default_factory=lambda: ApiClient(Configuration()))

    @staticmethod
    def from_env() -> "AppConfig":
        api_key = os.getenv("GITEA_API_KEY")
        if not api_key:
            raise ValueError("GITEA_API_KEY environment variable must be set")

        build_project_prefix = os.getenv("BUILD_PREFIX", "")

        conf = Configuration(
            api_key={"AuthorizationHeaderToken": api_key},
            api_key_prefix={"AuthorizationHeaderToken": "token"},
            host="https://src.opensuse.org/api/v1",
        )

        return AppConfig(
            osc=(osc := Osc.from_env()),
            gitea_user=os.getenv("BOT_USER", osc.username),
            branch_config=load_config(os.getenv("BRANCH_CONFIG", "config.json")),
            db_file_name=os.getenv("DB_FILE_NAME", DEFAULT_DB_NAME),
            build_project_prefix=build_project_prefix,
            _conf=conf,
            _api_client=ApiClient(conf),
        )


def package_from_pull_request(
    payload: PullRequestPayload | CommentPayload,
    pr: PullRequest | None = None,
) -> project.Package:
    if pr is None:
        pr = payload.pull_request
    return project.Package(
        name=payload.repository.name,
        title=StrElementField(f"The {payload.repository.name} package"),
        url=StrElementField(pr.url),
        scmsync=StrElementField(
            f"{pr.head.repo.clone_url}#{pr.head.sha}"
        ),
    )


async def find_devel_project(
    osc: Osc, project_name: str, package_name: str
) -> project.DevelProject | None:
    """Retrieve the develproject of the package with the supplied
    ``package_name`` from the project ``project_name``.

    Returns:
        - the devel project or ``None`` if there is none

    """
    pkg = await project.fetch_meta(osc, prj=project_name, pkg=package_name)
    if pkg.devel:
        return pkg.devel
    return None


class MainHandler(tornado.web.RequestHandler):
    def initialize(self, app_config: AppConfig) -> None:
        self.app_config = app_config

    async def project_from_pull_request(
        self,
        payload: PullRequestPayload,
        project_prefix: str | None,
        project_to_copy_repos_from: str | None = None,
        pr_number: int | None = None,
        pr_url: str | None = None,
    ) -> project.Project:
        if pr_number is None:
            pr_number = payload.pull_request.number
        if pr_url is None:
            pr_url = payload.pull_request.url

        prj_name = (
            project_prefix if project_prefix else f"home:{self.app_config.osc.username}"
        ) + f":{payload.sender.login}:{payload.repository.name}:{pr_number}"

        repos = []
        if project_to_copy_repos_from:
            repos = (
                await project.fetch_meta(
                    self.app_config.osc, prj=project_to_copy_repos_from
                )
            ).repository

        if not repos:
            repos = [
                project.Repository(
                    name="openSUSE_Factory",
                    arch=["x86_64"],
                    path=[
                        project.PathEntry(
                            project="openSUSE:Factory", repository="snapshot"
                        )
                    ],
                )
            ]

        return project.Project(
            name=prj_name,
            title=StrElementField(f"Project for Pull Request {pr_number}"),
            description=StrElementField(f"Project for Pull Request {pr_url}"),
            person=[
                project.Person(
                    userid=self.app_config.osc.username,
                    role=project.PersonRole.MAINTAINER,
                )
            ],
            repository=repos,
        )

    async def check_if_pr_approved(
        self,
        api_client: ApiClient,
        owner: str,
        repo_name: str,
        pr_number: int,
        pkg_name: str,
        pr_creator: str,
    ) -> bool:
        """Checks if the pull request $owner/$repo_name/$pr_number has been
        approved by at least one maintainer of the package `pkg_name` (and no
        changes have been requested) or if the pull request has been submitted
        by one of the maintainers of that package.

        """
        repo_api = RepositoryApi(api_client)

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

        if pr_creator in usernames:
            return True

        reviews = await repo_api.repo_list_pull_reviews(owner, repo_name, pr_number)

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
        payload = None

        if not self.request.body:
            return

        try:
            payload = PullRequestPayload(**json.loads(self.request.body))
        except ValidationError:
            pass
        else:
            # New PR
            await self.handle_pull_request(payload)
            return

        try:
            payload = CommentPayload(**json.loads(self.request.body))
        except ValidationError:
            pass
        else:
            # New PR comment
            await self.handle_comment(payload)
            return

    async def handle_comment(self, payload: CommentPayload) -> None:
        """
        Wait for bot commands and run specific tasks:
         + bot build -> creates a new build project in OBS
        """

        if not payload.is_pull:
            return
        if payload.issue.state == "closed":
            return

        try:
            comment = payload.comment.body.strip()
            bot, command, *args = comment.split(" ")
        except ValueError:
            return

        # All commands should start with bot
        if bot != "bot":
            return

        # Custom build
        if command == "build":
            if args:
                devel_prj = args[0]
            else:
                devel_prj = "openSUSE:Factory"

            osc = self.app_config.osc
            api_client = self.app_config._api_client
            owner = payload.issue.repository.owner
            name = payload.issue.repository.name
            number = payload.issue.number
            url = payload.issue.url
            repo_api = RepositoryApi(api_client)
            pr = await repo_api.repo_get_pull_request(owner, name, number)

            prj = await self.project_from_pull_request(
                payload,
                self.app_config.build_project_prefix,
                project_to_copy_repos_from=devel_prj,
                pr_number=number,
                pr_url=url,
            )
            pkg = package_from_pull_request(payload, pr)

            await project.send_meta(osc, prj=prj)
            await project.send_meta(osc, prj=prj, pkg=pkg)
            await service_wait(osc, prj, pkg)

            create_db(self.app_config.db_file_name)
            remove_build_project(self.app_config.db_file_name, prj.name)
            insert_build_project(
                self.app_config.db_file_name,
                PullRequestToBuild(
                    obs_package_name=pkg.name,
                    obs_project_name=prj.name,
                    gitea_repo_owner=owner,
                    gitea_repo_name=name,
                    pull_request_number=number,
                ),
            )

            # comment on the PR with a link to the Project
            issue_api = IssueApi(api_client)
            await issue_api.issue_create_comment(
                owner,
                name,
                number,
                body=CreateIssueCommentOption(
                    body=f"build project [{prj.name}](https://build.opensuse.org/package/show/{prj.name}/{pkg.name})"
                ),
            )
            await osc.api_request(
                f"/build/{prj.name}",
                params={"cmd": "rebuild"},
                method="POST",
            )

    async def handle_pull_request(self, payload: PullRequestPayload) -> None:
        LOGGER.debug(payload)

        matching_branch_conf: BranchConfig | None = None

        base = payload.pull_request.base
        for conf in self.app_config.branch_config:
            if (
                base.ref == conf.target_branch_name
                or base.label == conf.target_branch_name
            ) and payload.repository.owner.login == conf.organization:
                LOGGER.debug(
                    "Matched config %s for PR: %s", conf, payload.pull_request.url
                )
                matching_branch_conf = conf
                break

        if matching_branch_conf is None:
            LOGGER.debug(
                "wrong branch name %s or wrong organization %s",
                base.ref,
                payload.repository.owner.login,
            )
            return

        osc = self.app_config.osc
        pkg = package_from_pull_request(payload)

        # find out if we want to send the SR directly to the destination or via
        # the devel project
        devel_prj = await find_devel_project(
            osc, matching_branch_conf.destination_project, pkg.name
        )

        if (
            sr_style := matching_branch_conf.submission_style
        ) == SubmissionStyle.DIRECT:
            dest_prj = matching_branch_conf.destination_project
            dest_pkg = None

        elif sr_style == SubmissionStyle.FACTORY_DEVEL:
            if not devel_prj:
                raise ValueError(
                    f"Could not find the develproject for {pkg.name} in {matching_branch_conf.destination_project}"
                )
            dest_prj = devel_prj.project
            dest_pkg = devel_prj.package
        else:
            assert False, f"Invalid submission style {sr_style}"

        prj = await self.project_from_pull_request(
            payload,
            matching_branch_conf.project_prefix,
            project_to_copy_repos_from=devel_prj.project if devel_prj else dest_prj,
        )

        # previously opened requests from the existing project for this specific
        # PR
        pending_rqs = await request.search_for_requests(
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

        # Close all requests that were opened from the staging project if the PR
        # is merged or closed and finally delete the staging project.
        if payload.action in ("closed", "merged"):
            tasks = []

            remove_build_project(self.app_config.db_file_name, prj.name)
            for req in pending_rqs:
                if req.id and req.creator == osc.username:
                    tasks.append(
                        request.change_state(
                            osc,
                            request=req,
                            new_state=RequestStatus.REVOKED,
                            comment=f"pull request #{payload.pull_request.number} has been closed",
                        )
                    )
                    remove_submit_request(self.app_config.db_file_name, req.id)

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
        if matching_branch_conf.require_approval:
            if not await self.check_if_pr_approved(
                self.app_config._api_client,
                owner=owner,
                repo_name=repo_name,
                pr_number=pr_num,
                pkg_name=pkg.name,
                pr_creator=payload.pull_request.user.login,
            ):
                LOGGER.debug("PR has not been approved, approval required")
                return
            else:
                LOGGER.debug("PR is approved, proceeding")

        await project.send_meta(osc, prj=prj)
        await project.send_meta(osc, prj=prj, pkg=pkg)
        await service_wait(osc, prj, pkg)

        new_req = await request.submit_package(
            osc,
            source_prj=prj,
            pkg=pkg,
            supersede_old_request=False,
            requests_to_supersede=pending_rqs,
            dest_prj=dest_prj,
            dest_pkg=dest_pkg,
            description=f"""{payload.pull_request.title}

{payload.pull_request.body}

(🤖: Submission of {pkg.name} via {payload.pull_request.url} by {payload.sender.login})""",
        )

        create_db(self.app_config.db_file_name)

        insert_submit_request(
            self.app_config.db_file_name,
            PullRequestToSubmitRequest(
                submit_request_id=new_req.id,
                obs_package_name=pkg.name,
                obs_project_name=prj.name,
                gitea_repo_owner=base.repo.owner.login,
                gitea_repo_name=base.repo.name,
                pull_request_number=payload.pull_request.number,
                merge_pr=matching_branch_conf.merge_pr,
            ),
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


"""
Tornado options and define from command line e.g. --port 8000
"""
define("port", default=8000, help="Tornado web service port listen on")
define("log", default=None, help="Filename for scm_staging log, default to console")
define(
    "access_log",
    default=None,
    help="Filename for Tornado access log, default to console",
)
define(
    "app_log",
    default=None,
    help="Filename for Tornado application log, default to console",
)
define(
    "general_log",
    default=None,
    help="Filename for Tornado general log, default to console",
)
define(
    "db_file",
    default="submit_requests.db",
    help="SQLite3 database tracking the submitrequests",
)


def main():
    from scm_staging.cleanup import process_all_stored_srs
    from scm_staging import rabbit_listener as mq

    options.parse_command_line()
    LOGGER.configure_log_files(
        options.log, options.access_log, options.app_log, options.general_log
    )
    app_config = AppConfig.from_env()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        process_all_stored_srs(
            app_config.osc, app_config._api_client, app_config.db_file_name
        )
    )

    app = make_app(app_config)
    app.listen(options.port)
    LOGGER.info(f"app listent to port {options.port}")
    shutdown_event = asyncio.Event()

    create_db(options.db_file)
    LOGGER.info("Database opened")
    mqp = Process(target=mq.rabbit_listener, args=(options.db_file,))
    mqp.start()
    LOGGER.info("Rabbitmq forked")
    try:
        loop.run_until_complete(shutdown_event.wait())
    finally:
        loop.run_until_complete(app_config.osc.teardown())
