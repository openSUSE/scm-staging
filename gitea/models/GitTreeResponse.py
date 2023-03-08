from typing import *

from pydantic import BaseModel, Field

from .GitEntry import GitEntry


class GitTreeResponse(BaseModel):
    """
    None model
        GitTreeResponse returns a git tree

    """

    page: Optional[int] = Field(alias="page", default=None)

    sha: Optional[str] = Field(alias="sha", default=None)

    total_count: Optional[int] = Field(alias="total_count", default=None)

    tree: Optional[List[Optional[GitEntry]]] = Field(alias="tree", default=None)

    truncated: Optional[bool] = Field(alias="truncated", default=None)

    url: Optional[str] = Field(alias="url", default=None)
