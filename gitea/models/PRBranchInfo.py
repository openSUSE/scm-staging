from typing import *

from pydantic import BaseModel, Field

from .Repository import Repository


class PRBranchInfo(BaseModel):
    """
    None model
        PRBranchInfo information about a branch

    """

    label: Optional[str] = Field(alias="label", default=None)

    ref: Optional[str] = Field(alias="ref", default=None)

    repo: Optional[Repository] = Field(alias="repo", default=None)

    repo_id: Optional[int] = Field(alias="repo_id", default=None)

    sha: Optional[str] = Field(alias="sha", default=None)
