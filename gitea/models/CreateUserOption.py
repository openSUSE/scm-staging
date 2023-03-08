from typing import *

from pydantic import BaseModel, Field


class CreateUserOption(BaseModel):
    """
    None model
        CreateUserOption create user options

    """

    email: str = Field(alias="email")

    full_name: Optional[str] = Field(alias="full_name", default=None)

    login_name: Optional[str] = Field(alias="login_name", default=None)

    must_change_password: Optional[bool] = Field(
        alias="must_change_password", default=None
    )

    password: str = Field(alias="password")

    restricted: Optional[bool] = Field(alias="restricted", default=None)

    send_notify: Optional[bool] = Field(alias="send_notify", default=None)

    source_id: Optional[int] = Field(alias="source_id", default=None)

    username: str = Field(alias="username")

    visibility: Optional[str] = Field(alias="visibility", default=None)
