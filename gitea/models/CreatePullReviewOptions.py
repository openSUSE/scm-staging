from typing import *

from pydantic import BaseModel, Field

from .CreatePullReviewComment import CreatePullReviewComment
from .ReviewStateType import ReviewStateType


class CreatePullReviewOptions(BaseModel):
    """
    None model
        CreatePullReviewOptions are options to create a pull review

    """

    body: Optional[str] = Field(alias="body", default=None)

    comments: Optional[List[Optional[CreatePullReviewComment]]] = Field(
        alias="comments", default=None
    )

    commit_id: Optional[str] = Field(alias="commit_id", default=None)

    event: Optional[ReviewStateType] = Field(alias="event", default=None)
