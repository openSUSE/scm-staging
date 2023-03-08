from typing import *

from pydantic import BaseModel, Field


class CreateBranchRepoOption(BaseModel):
    """
    None model
        CreateBranchRepoOption options when creating a branch in a repository

    """

    new_branch_name: str = Field(alias="new_branch_name")

    old_branch_name: Optional[str] = Field(alias="old_branch_name", default=None)
