from typing import *

from pydantic import BaseModel, Field


class CommitStats(BaseModel):
    """
    None model
        CommitStats is statistics for a RepoCommit

    """

    additions: Optional[int] = Field(alias="additions", default=None)

    deletions: Optional[int] = Field(alias="deletions", default=None)

    total: Optional[int] = Field(alias="total", default=None)
