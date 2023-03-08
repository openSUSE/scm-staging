from typing import *

from pydantic import BaseModel, Field

from .CommitMeta import CommitMeta
from .CommitUser import CommitUser
from .PayloadCommitVerification import PayloadCommitVerification


class RepoCommit(BaseModel):
    """
    RepoCommit contains information of a commit in the context of a repository. model

    """

    author: Optional[CommitUser] = Field(alias="author", default=None)

    committer: Optional[CommitUser] = Field(alias="committer", default=None)

    message: Optional[str] = Field(alias="message", default=None)

    tree: Optional[CommitMeta] = Field(alias="tree", default=None)

    url: Optional[str] = Field(alias="url", default=None)

    verification: Optional[PayloadCommitVerification] = Field(
        alias="verification", default=None
    )
