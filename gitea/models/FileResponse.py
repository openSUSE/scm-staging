from typing import *

from pydantic import BaseModel, Field

from .ContentsResponse import ContentsResponse
from .FileCommitResponse import FileCommitResponse
from .PayloadCommitVerification import PayloadCommitVerification


class FileResponse(BaseModel):
    """
    None model
        FileResponse contains information about a repo&#39;s file

    """

    commit: Optional[FileCommitResponse] = Field(alias="commit", default=None)

    content: Optional[ContentsResponse] = Field(alias="content", default=None)

    verification: Optional[PayloadCommitVerification] = Field(
        alias="verification", default=None
    )
