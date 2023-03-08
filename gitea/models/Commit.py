from typing import *

from pydantic import BaseModel, Field

from .CommitAffectedFiles import CommitAffectedFiles
from .CommitMeta import CommitMeta
from .CommitStats import CommitStats
from .RepoCommit import RepoCommit
from .User import User


class Commit(BaseModel):
    """
    Commit contains information generated from a Git commit. model

    """

    author: Optional[User] = Field(alias="author", default=None)

    commit: Optional[RepoCommit] = Field(alias="commit", default=None)

    committer: Optional[User] = Field(alias="committer", default=None)

    created: Optional[str] = Field(alias="created", default=None)

    files: Optional[List[Optional[CommitAffectedFiles]]] = Field(
        alias="files", default=None
    )

    html_url: Optional[str] = Field(alias="html_url", default=None)

    parents: Optional[List[Optional[CommitMeta]]] = Field(alias="parents", default=None)

    sha: Optional[str] = Field(alias="sha", default=None)

    stats: Optional[CommitStats] = Field(alias="stats", default=None)

    url: Optional[str] = Field(alias="url", default=None)
