from typing import *

from pydantic import BaseModel, Field

from .ReviewStateType import ReviewStateType


class SubmitPullReviewOptions(BaseModel):
    """
    None model
        SubmitPullReviewOptions are options to submit a pending pull review

    """

    body: Optional[str] = Field(alias="body", default=None)

    event: Optional[ReviewStateType] = Field(alias="event", default=None)
