from typing import *

from pydantic import BaseModel, Field

from .CommitStatus import CommitStatus
from .CommitStatusState import CommitStatusState
from .Repository import Repository


class CombinedStatus(BaseModel):
    """
    None model
        CombinedStatus holds the combined state of several statuses for a single commit

    """

    commit_url: Optional[str] = Field(alias="commit_url", default=None)

    repository: Optional[Repository] = Field(alias="repository", default=None)

    sha: Optional[str] = Field(alias="sha", default=None)

    state: Optional[CommitStatusState] = Field(alias="state", default=None)

    statuses: Optional[List[Optional[CommitStatus]]] = Field(
        alias="statuses", default=None
    )

    total_count: Optional[int] = Field(alias="total_count", default=None)

    url: Optional[str] = Field(alias="url", default=None)
