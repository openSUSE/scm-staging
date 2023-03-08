from typing import *

from pydantic import BaseModel, Field


class GitBlobResponse(BaseModel):
    """
    None model
        GitBlobResponse represents a git blob

    """

    content: Optional[str] = Field(alias="content", default=None)

    encoding: Optional[str] = Field(alias="encoding", default=None)

    sha: Optional[str] = Field(alias="sha", default=None)

    size: Optional[int] = Field(alias="size", default=None)

    url: Optional[str] = Field(alias="url", default=None)
