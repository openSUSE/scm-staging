from typing import *

from pydantic import BaseModel, Field


class EditUserOption(BaseModel):
    """
    None model
        EditUserOption edit user options

    """

    active: Optional[bool] = Field(alias="active", default=None)

    admin: Optional[bool] = Field(alias="admin", default=None)

    allow_create_organization: Optional[bool] = Field(
        alias="allow_create_organization", default=None
    )

    allow_git_hook: Optional[bool] = Field(alias="allow_git_hook", default=None)

    allow_import_local: Optional[bool] = Field(alias="allow_import_local", default=None)

    description: Optional[str] = Field(alias="description", default=None)

    email: Optional[str] = Field(alias="email", default=None)

    full_name: Optional[str] = Field(alias="full_name", default=None)

    location: Optional[str] = Field(alias="location", default=None)

    login_name: str = Field(alias="login_name")

    max_repo_creation: Optional[int] = Field(alias="max_repo_creation", default=None)

    must_change_password: Optional[bool] = Field(
        alias="must_change_password", default=None
    )

    password: Optional[str] = Field(alias="password", default=None)

    prohibit_login: Optional[bool] = Field(alias="prohibit_login", default=None)

    restricted: Optional[bool] = Field(alias="restricted", default=None)

    source_id: int = Field(alias="source_id")

    visibility: Optional[str] = Field(alias="visibility", default=None)

    website: Optional[str] = Field(alias="website", default=None)
