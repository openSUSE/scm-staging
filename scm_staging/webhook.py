import asyncio
from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel

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


PR_APPROVED = "pull_request_review_approved"
PR_REJECTED = "pull_request_review_rejected"
_PR_TYPE = Literal["pull_request_review_approved", "pull_request_review_rejected"]


class Review(BaseModel):
    type: _PR_TYPE | str
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


_TARGET_BRANCH_NAME = "factory"
_BOT_USER = "defolos"


def package_from_pull_request(payload: PullRequestPayload) -> project.Package:
    return project.Package(
        name=payload.repository.name,
        title=f"The {payload.repository.name} package",
        scmsync=f"{payload.pull_request.head.repo.clone_url}#{payload.pull_request.head.ref}",
    )


def project_from_pull_request(payload: PullRequestPayload) -> project.Project:
    return project.Project(
        name=f"home:{_BOT_USER}:SCM_STAGING:Factory:{payload.repository.name}:{payload.pull_request.number}",
        title=StrElementField(
            f"Project for Pull Request {payload.pull_request.number}"
        ),
        person=[project.Person(userid=_BOT_USER, role=project.PersonRole.MAINTAINER)],
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


osc: Osc | None = None


@app.post("/hook")
async def webhook(payload: PullRequestPayload):
    global osc
    if not osc:
        osc = Osc.from_env()

    LOGGER.debug(payload)

    if (
        base := payload.pull_request.base
    ).ref != _TARGET_BRANCH_NAME and base.label != _TARGET_BRANCH_NAME:
        LOGGER.debug("wrong branch name %s", base.ref)
        return {}

    pkg = package_from_pull_request(payload)
    prj = project_from_pull_request(payload)

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

    if (review := payload.review) and review.type == PR_APPROVED:
        LOGGER.debug("PR has been approved, creating package")
        await project.send_meta(osc, prj=prj)
        await project.send_meta(osc, prj=prj, pkg=pkg)
        await request.submit_package(
            osc=osc,
            source_prj=prj.name,
            pkg_name=pkg.name,
            dest_prj="devel:Factory:git-workflow:mold:core",
        )

    # raise ValueError("pr was not approved")
    return {}
