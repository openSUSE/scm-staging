from typing import *

from pydantic import BaseModel, Field

from .Commit import Commit


class Note(BaseModel):
    """
    None model
        Note contains information related to a git note

    """

    commit: Optional[Commit] = Field(alias="commit", default=None)

    message: Optional[str] = Field(alias="message", default=None)
