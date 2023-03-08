from typing import *

from pydantic import BaseModel, Field


class User(BaseModel):
    """
    None model
        User represents a user

    """

    active: Optional[bool] = Field(alias="active", default=None)

    avatar_url: Optional[str] = Field(alias="avatar_url", default=None)

    created: Optional[str] = Field(alias="created", default=None)

    description: Optional[str] = Field(alias="description", default=None)

    email: Optional[str] = Field(alias="email", default=None)

    followers_count: Optional[int] = Field(alias="followers_count", default=None)

    following_count: Optional[int] = Field(alias="following_count", default=None)

    full_name: Optional[str] = Field(alias="full_name", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    is_admin: Optional[bool] = Field(alias="is_admin", default=None)

    language: Optional[str] = Field(alias="language", default=None)

    last_login: Optional[str] = Field(alias="last_login", default=None)

    location: Optional[str] = Field(alias="location", default=None)

    login: Optional[str] = Field(alias="login", default=None)

    login_name: Optional[str] = Field(alias="login_name", default=None)

    prohibit_login: Optional[bool] = Field(alias="prohibit_login", default=None)

    restricted: Optional[bool] = Field(alias="restricted", default=None)

    starred_repos_count: Optional[int] = Field(
        alias="starred_repos_count", default=None
    )

    visibility: Optional[str] = Field(alias="visibility", default=None)

    website: Optional[str] = Field(alias="website", default=None)
