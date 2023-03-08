from typing import *

from pydantic import BaseModel, Field


class CreatePullReviewComment(BaseModel):
    """
    None model
        CreatePullReviewComment represent a review comment for creation api

    """

    body: Optional[str] = Field(alias="body", default=None)

    new_position: Optional[int] = Field(alias="new_position", default=None)

    old_position: Optional[int] = Field(alias="old_position", default=None)

    path: Optional[str] = Field(alias="path", default=None)
