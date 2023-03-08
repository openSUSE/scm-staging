from typing import *

from pydantic import BaseModel, Field


class CreateMilestoneOption(BaseModel):
    """
    None model
        CreateMilestoneOption options for creating a milestone

    """

    description: Optional[str] = Field(alias="description", default=None)

    due_on: Optional[str] = Field(alias="due_on", default=None)

    state: Optional[str] = Field(alias="state", default=None)

    title: Optional[str] = Field(alias="title", default=None)
