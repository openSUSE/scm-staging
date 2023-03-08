from typing import *

from pydantic import BaseModel, Field

from .User import User


class Comment(BaseModel):
    """
    None model
        Comment represents a comment on a commit or issue

    """

    body: Optional[str] = Field(alias="body", default=None)

    created_at: Optional[str] = Field(alias="created_at", default=None)

    html_url: Optional[str] = Field(alias="html_url", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    issue_url: Optional[str] = Field(alias="issue_url", default=None)

    original_author: Optional[str] = Field(alias="original_author", default=None)

    original_author_id: Optional[int] = Field(alias="original_author_id", default=None)

    pull_request_url: Optional[str] = Field(alias="pull_request_url", default=None)

    updated_at: Optional[str] = Field(alias="updated_at", default=None)

    user: Optional[User] = Field(alias="user", default=None)
