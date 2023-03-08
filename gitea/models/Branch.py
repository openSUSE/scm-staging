from typing import *

from pydantic import BaseModel, Field

from .PayloadCommit import PayloadCommit


class Branch(BaseModel):
    """
    None model
        Branch represents a repository branch

    """

    commit: Optional[PayloadCommit] = Field(alias="commit", default=None)

    effective_branch_protection_name: Optional[str] = Field(
        alias="effective_branch_protection_name", default=None
    )

    enable_status_check: Optional[bool] = Field(
        alias="enable_status_check", default=None
    )

    name: Optional[str] = Field(alias="name", default=None)

    protected: Optional[bool] = Field(alias="protected", default=None)

    required_approvals: Optional[int] = Field(alias="required_approvals", default=None)

    status_check_contexts: Optional[List[str]] = Field(
        alias="status_check_contexts", default=None
    )

    user_can_merge: Optional[bool] = Field(alias="user_can_merge", default=None)

    user_can_push: Optional[bool] = Field(alias="user_can_push", default=None)
