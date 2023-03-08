from typing import *

from pydantic import BaseModel, Field


class CreateIssueOption(BaseModel):
    """
    None model
        CreateIssueOption options to create one issue

    """

    assignee: Optional[str] = Field(alias="assignee", default=None)

    assignees: Optional[List[str]] = Field(alias="assignees", default=None)

    body: Optional[str] = Field(alias="body", default=None)

    closed: Optional[bool] = Field(alias="closed", default=None)

    due_date: Optional[str] = Field(alias="due_date", default=None)

    labels: Optional[List[int]] = Field(alias="labels", default=None)

    milestone: Optional[int] = Field(alias="milestone", default=None)

    ref: Optional[str] = Field(alias="ref", default=None)

    title: str = Field(alias="title")
