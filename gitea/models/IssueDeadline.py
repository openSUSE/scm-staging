from typing import *

from pydantic import BaseModel, Field


class IssueDeadline(BaseModel):
    """
    None model
        IssueDeadline represents an issue deadline

    """

    due_date: Optional[str] = Field(alias="due_date", default=None)
