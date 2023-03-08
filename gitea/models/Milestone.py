from typing import *

from pydantic import BaseModel, Field

from .StateType import StateType


class Milestone(BaseModel):
    """
    None model
        Milestone milestone is a collection of issues on one repository

    """

    closed_at: Optional[str] = Field(alias="closed_at", default=None)

    closed_issues: Optional[int] = Field(alias="closed_issues", default=None)

    created_at: Optional[str] = Field(alias="created_at", default=None)

    description: Optional[str] = Field(alias="description", default=None)

    due_on: Optional[str] = Field(alias="due_on", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    open_issues: Optional[int] = Field(alias="open_issues", default=None)

    state: Optional[StateType] = Field(alias="state", default=None)

    title: Optional[str] = Field(alias="title", default=None)

    updated_at: Optional[str] = Field(alias="updated_at", default=None)
