from typing import *

from pydantic import BaseModel, Field

from .CommitStatusState import CommitStatusState
from .User import User


class CommitStatus(BaseModel):
    """
    None model
        CommitStatus holds a single status of a single Commit

    """

    context: Optional[str] = Field(alias="context", default=None)

    created_at: Optional[str] = Field(alias="created_at", default=None)

    creator: Optional[User] = Field(alias="creator", default=None)

    description: Optional[str] = Field(alias="description", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    status: Optional[CommitStatusState] = Field(alias="status", default=None)

    target_url: Optional[str] = Field(alias="target_url", default=None)

    updated_at: Optional[str] = Field(alias="updated_at", default=None)

    url: Optional[str] = Field(alias="url", default=None)
