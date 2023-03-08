from typing import *

from pydantic import BaseModel, Field

from .Comment import Comment
from .Issue import Issue
from .Label import Label
from .Milestone import Milestone
from .Team import Team
from .TrackedTime import TrackedTime
from .User import User


class TimelineComment(BaseModel):
    """
    None model
        TimelineComment represents a timeline comment (comment of any type) on a commit or issue

    """

    assignee: Optional[User] = Field(alias="assignee", default=None)

    assignee_team: Optional[Team] = Field(alias="assignee_team", default=None)

    body: Optional[str] = Field(alias="body", default=None)

    created_at: Optional[str] = Field(alias="created_at", default=None)

    dependent_issue: Optional[Issue] = Field(alias="dependent_issue", default=None)

    html_url: Optional[str] = Field(alias="html_url", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    issue_url: Optional[str] = Field(alias="issue_url", default=None)

    label: Optional[Label] = Field(alias="label", default=None)

    milestone: Optional[Milestone] = Field(alias="milestone", default=None)

    new_ref: Optional[str] = Field(alias="new_ref", default=None)

    new_title: Optional[str] = Field(alias="new_title", default=None)

    old_milestone: Optional[Milestone] = Field(alias="old_milestone", default=None)

    old_project_id: Optional[int] = Field(alias="old_project_id", default=None)

    old_ref: Optional[str] = Field(alias="old_ref", default=None)

    old_title: Optional[str] = Field(alias="old_title", default=None)

    project_id: Optional[int] = Field(alias="project_id", default=None)

    pull_request_url: Optional[str] = Field(alias="pull_request_url", default=None)

    ref_action: Optional[str] = Field(alias="ref_action", default=None)

    ref_comment: Optional[Comment] = Field(alias="ref_comment", default=None)

    ref_commit_sha: Optional[str] = Field(alias="ref_commit_sha", default=None)

    ref_issue: Optional[Issue] = Field(alias="ref_issue", default=None)

    removed_assignee: Optional[bool] = Field(alias="removed_assignee", default=None)

    resolve_doer: Optional[User] = Field(alias="resolve_doer", default=None)

    review_id: Optional[int] = Field(alias="review_id", default=None)

    tracked_time: Optional[TrackedTime] = Field(alias="tracked_time", default=None)

    type: Optional[str] = Field(alias="type", default=None)

    updated_at: Optional[str] = Field(alias="updated_at", default=None)

    user: Optional[User] = Field(alias="user", default=None)
