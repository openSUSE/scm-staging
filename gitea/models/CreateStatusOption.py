from typing import *

from pydantic import BaseModel, Field

from .CommitStatusState import CommitStatusState


class CreateStatusOption(BaseModel):
    """
    None model
        CreateStatusOption holds the information needed to create a new CommitStatus for a Commit

    """

    context: Optional[str] = Field(alias="context", default=None)

    description: Optional[str] = Field(alias="description", default=None)

    state: Optional[CommitStatusState] = Field(alias="state", default=None)

    target_url: Optional[str] = Field(alias="target_url", default=None)
