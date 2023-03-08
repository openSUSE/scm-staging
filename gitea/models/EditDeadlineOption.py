from typing import *

from pydantic import BaseModel, Field


class EditDeadlineOption(BaseModel):
    """
    None model
        EditDeadlineOption options for creating a deadline

    """

    due_date: str = Field(alias="due_date")
