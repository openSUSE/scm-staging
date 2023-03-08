from typing import *

from pydantic import BaseModel, Field


class GitEntry(BaseModel):
    """
    None model
        GitEntry represents a git tree

    """

    mode: Optional[str] = Field(alias="mode", default=None)

    path: Optional[str] = Field(alias="path", default=None)

    sha: Optional[str] = Field(alias="sha", default=None)

    size: Optional[int] = Field(alias="size", default=None)

    type: Optional[str] = Field(alias="type", default=None)

    url: Optional[str] = Field(alias="url", default=None)
