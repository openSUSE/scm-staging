from typing import *

from pydantic import BaseModel, Field


class PullReviewRequestOptions(BaseModel):
    """
    None model
        PullReviewRequestOptions are options to add or remove pull review requests

    """

    reviewers: Optional[List[str]] = Field(alias="reviewers", default=None)

    team_reviewers: Optional[List[str]] = Field(alias="team_reviewers", default=None)
