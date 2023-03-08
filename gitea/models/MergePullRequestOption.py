from typing import *

from pydantic import BaseModel, Field


class MergePullRequestOption(BaseModel):
    """
    None model
        MergePullRequestForm form for merging Pull Request

    """

    Do: str = Field(alias="Do")

    MergeCommitID: Optional[str] = Field(alias="MergeCommitID", default=None)

    MergeMessageField: Optional[str] = Field(alias="MergeMessageField", default=None)

    MergeTitleField: Optional[str] = Field(alias="MergeTitleField", default=None)

    delete_branch_after_merge: Optional[bool] = Field(
        alias="delete_branch_after_merge", default=None
    )

    force_merge: Optional[bool] = Field(alias="force_merge", default=None)

    head_commit_id: Optional[str] = Field(alias="head_commit_id", default=None)

    merge_when_checks_succeed: Optional[bool] = Field(
        alias="merge_when_checks_succeed", default=None
    )
