from typing import *

from pydantic import BaseModel, Field

from .FileCommitResponse import FileCommitResponse
from .PayloadCommitVerification import PayloadCommitVerification


class FileDeleteResponse(BaseModel):
    """
    None model
        FileDeleteResponse contains information about a repo&#39;s file that was deleted

    """

    commit: Optional[FileCommitResponse] = Field(alias="commit", default=None)

    content: Optional[Dict[str, Any]] = Field(alias="content", default=None)

    verification: Optional[PayloadCommitVerification] = Field(
        alias="verification", default=None
    )
