from typing import *

from pydantic import BaseModel, Field


class EditMilestoneOption(BaseModel):
    """
    None model
        EditMilestoneOption options for editing a milestone

    """

    description: Optional[str] = Field(alias="description", default=None)

    due_on: Optional[str] = Field(alias="due_on", default=None)

    state: Optional[str] = Field(alias="state", default=None)

    title: Optional[str] = Field(alias="title", default=None)
