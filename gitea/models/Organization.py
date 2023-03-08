from typing import *

from pydantic import BaseModel, Field


class Organization(BaseModel):
    """
    None model
        Organization represents an organization

    """

    avatar_url: Optional[str] = Field(alias="avatar_url", default=None)

    description: Optional[str] = Field(alias="description", default=None)

    full_name: Optional[str] = Field(alias="full_name", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    location: Optional[str] = Field(alias="location", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    repo_admin_change_team_access: Optional[bool] = Field(
        alias="repo_admin_change_team_access", default=None
    )

    username: Optional[str] = Field(alias="username", default=None)

    visibility: Optional[str] = Field(alias="visibility", default=None)

    website: Optional[str] = Field(alias="website", default=None)
