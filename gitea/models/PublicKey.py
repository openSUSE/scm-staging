from typing import *

from pydantic import BaseModel, Field

from .User import User


class PublicKey(BaseModel):
    """
    None model
        PublicKey publickey is a user key to push code to repository

    """

    created_at: Optional[str] = Field(alias="created_at", default=None)

    fingerprint: Optional[str] = Field(alias="fingerprint", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    key: Optional[str] = Field(alias="key", default=None)

    key_type: Optional[str] = Field(alias="key_type", default=None)

    read_only: Optional[bool] = Field(alias="read_only", default=None)

    title: Optional[str] = Field(alias="title", default=None)

    url: Optional[str] = Field(alias="url", default=None)

    user: Optional[User] = Field(alias="user", default=None)
