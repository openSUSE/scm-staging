from typing import *

from pydantic import BaseModel, Field


class CommitMeta(BaseModel):
    """
    CommitMeta contains meta information of a commit in terms of API. model

    """

    created: Optional[str] = Field(alias="created", default=None)

    sha: Optional[str] = Field(alias="sha", default=None)

    url: Optional[str] = Field(alias="url", default=None)
