from typing import *

from pydantic import BaseModel, Field


class PullRequestMeta(BaseModel):
    """
    None model
        PullRequestMeta PR info if an issue is a PR

    """

    merged: Optional[bool] = Field(alias="merged", default=None)

    merged_at: Optional[str] = Field(alias="merged_at", default=None)
