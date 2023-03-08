from typing import *

from pydantic import BaseModel, Field


class CreatePullRequestOption(BaseModel):
    """
    None model
        CreatePullRequestOption options when creating a pull request

    """

    assignee: Optional[str] = Field(alias="assignee", default=None)

    assignees: Optional[List[str]] = Field(alias="assignees", default=None)

    base: Optional[str] = Field(alias="base", default=None)

    body: Optional[str] = Field(alias="body", default=None)

    due_date: Optional[str] = Field(alias="due_date", default=None)

    head: Optional[str] = Field(alias="head", default=None)

    labels: Optional[List[int]] = Field(alias="labels", default=None)

    milestone: Optional[int] = Field(alias="milestone", default=None)

    title: Optional[str] = Field(alias="title", default=None)
