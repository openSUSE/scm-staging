from typing import *

from pydantic import BaseModel, Field

from .User import User


class PullReviewComment(BaseModel):
    """
    None model
        PullReviewComment represents a comment on a pull request review

    """

    body: Optional[str] = Field(alias="body", default=None)

    commit_id: Optional[str] = Field(alias="commit_id", default=None)

    created_at: Optional[str] = Field(alias="created_at", default=None)

    diff_hunk: Optional[str] = Field(alias="diff_hunk", default=None)

    html_url: Optional[str] = Field(alias="html_url", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    original_commit_id: Optional[str] = Field(alias="original_commit_id", default=None)

    original_position: Optional[int] = Field(alias="original_position", default=None)

    path: Optional[str] = Field(alias="path", default=None)

    position: Optional[int] = Field(alias="position", default=None)

    pull_request_review_id: Optional[int] = Field(
        alias="pull_request_review_id", default=None
    )

    pull_request_url: Optional[str] = Field(alias="pull_request_url", default=None)

    resolver: Optional[User] = Field(alias="resolver", default=None)

    updated_at: Optional[str] = Field(alias="updated_at", default=None)

    user: Optional[User] = Field(alias="user", default=None)
