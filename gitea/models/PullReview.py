from typing import *

from pydantic import BaseModel, Field

from .ReviewStateType import ReviewStateType
from .Team import Team
from .User import User


class PullReview(BaseModel):
    """
    None model
        PullReview represents a pull request review

    """

    body: Optional[str] = Field(alias="body", default=None)

    comments_count: Optional[int] = Field(alias="comments_count", default=None)

    commit_id: Optional[str] = Field(alias="commit_id", default=None)

    dismissed: Optional[bool] = Field(alias="dismissed", default=None)

    html_url: Optional[str] = Field(alias="html_url", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    official: Optional[bool] = Field(alias="official", default=None)

    pull_request_url: Optional[str] = Field(alias="pull_request_url", default=None)

    stale: Optional[bool] = Field(alias="stale", default=None)

    state: Optional[ReviewStateType] = Field(alias="state", default=None)

    submitted_at: Optional[str] = Field(alias="submitted_at", default=None)

    team: Optional[Team] = Field(alias="team", default=None)

    user: Optional[User] = Field(alias="user", default=None)
