from typing import *

from pydantic import BaseModel, Field

from .CommitUser import CommitUser


class WikiCommit(BaseModel):
    """
    None model
        WikiCommit page commit/revision

    """

    author: Optional[CommitUser] = Field(alias="author", default=None)

    commiter: Optional[CommitUser] = Field(alias="commiter", default=None)

    message: Optional[str] = Field(alias="message", default=None)

    sha: Optional[str] = Field(alias="sha", default=None)
