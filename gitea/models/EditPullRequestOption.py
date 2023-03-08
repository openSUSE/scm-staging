from typing import *

from pydantic import BaseModel, Field


class EditPullRequestOption(BaseModel):
    """
    None model
        EditPullRequestOption options when modify pull request

    """

    allow_maintainer_edit: Optional[bool] = Field(
        alias="allow_maintainer_edit", default=None
    )

    assignee: Optional[str] = Field(alias="assignee", default=None)

    assignees: Optional[List[str]] = Field(alias="assignees", default=None)

    base: Optional[str] = Field(alias="base", default=None)

    body: Optional[str] = Field(alias="body", default=None)

    due_date: Optional[str] = Field(alias="due_date", default=None)

    labels: Optional[List[int]] = Field(alias="labels", default=None)

    milestone: Optional[int] = Field(alias="milestone", default=None)

    state: Optional[str] = Field(alias="state", default=None)

    title: Optional[str] = Field(alias="title", default=None)

    unset_due_date: Optional[bool] = Field(alias="unset_due_date", default=None)
