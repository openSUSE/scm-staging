from typing import *

from pydantic import BaseModel, Field

from .PayloadCommitVerification import PayloadCommitVerification
from .PayloadUser import PayloadUser


class PayloadCommit(BaseModel):
    """
    None model
        PayloadCommit represents a commit

    """

    added: Optional[List[str]] = Field(alias="added", default=None)

    author: Optional[PayloadUser] = Field(alias="author", default=None)

    committer: Optional[PayloadUser] = Field(alias="committer", default=None)

    id: Optional[str] = Field(alias="id", default=None)

    message: Optional[str] = Field(alias="message", default=None)

    modified: Optional[List[str]] = Field(alias="modified", default=None)

    removed: Optional[List[str]] = Field(alias="removed", default=None)

    timestamp: Optional[str] = Field(alias="timestamp", default=None)

    url: Optional[str] = Field(alias="url", default=None)

    verification: Optional[PayloadCommitVerification] = Field(
        alias="verification", default=None
    )
