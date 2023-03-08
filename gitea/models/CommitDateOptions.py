from typing import *

from pydantic import BaseModel, Field


class CommitDateOptions(BaseModel):
    """
    None model
        CommitDateOptions store dates for GIT_AUTHOR_DATE and GIT_COMMITTER_DATE

    """

    author: Optional[str] = Field(alias="author", default=None)

    committer: Optional[str] = Field(alias="committer", default=None)
