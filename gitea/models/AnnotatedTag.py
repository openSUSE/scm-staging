from typing import *

from pydantic import BaseModel, Field

from .AnnotatedTagObject import AnnotatedTagObject
from .CommitUser import CommitUser
from .PayloadCommitVerification import PayloadCommitVerification


class AnnotatedTag(BaseModel):
    """
    None model
        AnnotatedTag represents an annotated tag

    """

    message: Optional[str] = Field(alias="message", default=None)

    object: Optional[AnnotatedTagObject] = Field(alias="object", default=None)

    sha: Optional[str] = Field(alias="sha", default=None)

    tag: Optional[str] = Field(alias="tag", default=None)

    tagger: Optional[CommitUser] = Field(alias="tagger", default=None)

    url: Optional[str] = Field(alias="url", default=None)

    verification: Optional[PayloadCommitVerification] = Field(
        alias="verification", default=None
    )
