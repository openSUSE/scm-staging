from typing import *

from pydantic import BaseModel, Field

from .Label import Label
from .Milestone import Milestone
from .PullRequestMeta import PullRequestMeta
from .RepositoryMeta import RepositoryMeta
from .StateType import StateType
from .User import User


class Issue(BaseModel):
    """
    None model
        Issue represents an issue in a repository

    """

    assignee: Optional[User] = Field(alias="assignee", default=None)

    assignees: Optional[List[Optional[User]]] = Field(alias="assignees", default=None)

    body: Optional[str] = Field(alias="body", default=None)

    closed_at: Optional[str] = Field(alias="closed_at", default=None)

    comments: Optional[int] = Field(alias="comments", default=None)

    created_at: Optional[str] = Field(alias="created_at", default=None)

    due_date: Optional[str] = Field(alias="due_date", default=None)

    html_url: Optional[str] = Field(alias="html_url", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    is_locked: Optional[bool] = Field(alias="is_locked", default=None)

    labels: Optional[List[Optional[Label]]] = Field(alias="labels", default=None)

    milestone: Optional[Milestone] = Field(alias="milestone", default=None)

    number: Optional[int] = Field(alias="number", default=None)

    original_author: Optional[str] = Field(alias="original_author", default=None)

    original_author_id: Optional[int] = Field(alias="original_author_id", default=None)

    pull_request: Optional[PullRequestMeta] = Field(alias="pull_request", default=None)

    ref: Optional[str] = Field(alias="ref", default=None)

    repository: Optional[RepositoryMeta] = Field(alias="repository", default=None)

    state: Optional[StateType] = Field(alias="state", default=None)

    title: Optional[str] = Field(alias="title", default=None)

    updated_at: Optional[str] = Field(alias="updated_at", default=None)

    url: Optional[str] = Field(alias="url", default=None)

    user: Optional[User] = Field(alias="user", default=None)
