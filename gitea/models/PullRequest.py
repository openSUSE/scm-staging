from typing import *

from pydantic import BaseModel, Field

from .Label import Label
from .Milestone import Milestone
from .PRBranchInfo import PRBranchInfo
from .StateType import StateType
from .User import User


class PullRequest(BaseModel):
    """
    None model
        PullRequest represents a pull request

    """

    allow_maintainer_edit: Optional[bool] = Field(
        alias="allow_maintainer_edit", default=None
    )

    assignee: Optional[User] = Field(alias="assignee", default=None)

    assignees: Optional[List[Optional[User]]] = Field(alias="assignees", default=None)

    base: Optional[PRBranchInfo] = Field(alias="base", default=None)

    body: Optional[str] = Field(alias="body", default=None)

    closed_at: Optional[str] = Field(alias="closed_at", default=None)

    comments: Optional[int] = Field(alias="comments", default=None)

    created_at: Optional[str] = Field(alias="created_at", default=None)

    diff_url: Optional[str] = Field(alias="diff_url", default=None)

    due_date: Optional[str] = Field(alias="due_date", default=None)

    head: Optional[PRBranchInfo] = Field(alias="head", default=None)

    html_url: Optional[str] = Field(alias="html_url", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    is_locked: Optional[bool] = Field(alias="is_locked", default=None)

    labels: Optional[List[Optional[Label]]] = Field(alias="labels", default=None)

    merge_base: Optional[str] = Field(alias="merge_base", default=None)

    merge_commit_sha: Optional[str] = Field(alias="merge_commit_sha", default=None)

    mergeable: Optional[bool] = Field(alias="mergeable", default=None)

    merged: Optional[bool] = Field(alias="merged", default=None)

    merged_at: Optional[str] = Field(alias="merged_at", default=None)

    merged_by: Optional[User] = Field(alias="merged_by", default=None)

    milestone: Optional[Milestone] = Field(alias="milestone", default=None)

    number: Optional[int] = Field(alias="number", default=None)

    patch_url: Optional[str] = Field(alias="patch_url", default=None)

    state: Optional[StateType] = Field(alias="state", default=None)

    title: Optional[str] = Field(alias="title", default=None)

    updated_at: Optional[str] = Field(alias="updated_at", default=None)

    url: Optional[str] = Field(alias="url", default=None)

    user: Optional[User] = Field(alias="user", default=None)
