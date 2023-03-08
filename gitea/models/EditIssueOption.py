from typing import *

from pydantic import BaseModel, Field


class EditIssueOption(BaseModel):
    """
    None model
        EditIssueOption options for editing an issue

    """

    assignee: Optional[str] = Field(alias="assignee", default=None)

    assignees: Optional[List[str]] = Field(alias="assignees", default=None)

    body: Optional[str] = Field(alias="body", default=None)

    due_date: Optional[str] = Field(alias="due_date", default=None)

    milestone: Optional[int] = Field(alias="milestone", default=None)

    ref: Optional[str] = Field(alias="ref", default=None)

    state: Optional[str] = Field(alias="state", default=None)

    title: Optional[str] = Field(alias="title", default=None)

    unset_due_date: Optional[bool] = Field(alias="unset_due_date", default=None)
