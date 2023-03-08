from typing import *

from pydantic import BaseModel, Field

from .CommitMeta import CommitMeta
from .CommitUser import CommitUser


class FileCommitResponse(BaseModel):
    """
    FileCommitResponse contains information generated from a Git commit for a repo&#39;s file. model

    """

    author: Optional[CommitUser] = Field(alias="author", default=None)

    committer: Optional[CommitUser] = Field(alias="committer", default=None)

    created: Optional[str] = Field(alias="created", default=None)

    html_url: Optional[str] = Field(alias="html_url", default=None)

    message: Optional[str] = Field(alias="message", default=None)

    parents: Optional[List[Optional[CommitMeta]]] = Field(alias="parents", default=None)

    sha: Optional[str] = Field(alias="sha", default=None)

    tree: Optional[CommitMeta] = Field(alias="tree", default=None)

    url: Optional[str] = Field(alias="url", default=None)
