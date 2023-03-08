from typing import *

from pydantic import BaseModel, Field


class AccessToken(BaseModel):
    """
    AccessToken represents an API access token. model

    """

    id: Optional[int] = Field(alias="id", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    sha1: Optional[str] = Field(alias="sha1", default=None)

    token_last_eight: Optional[str] = Field(alias="token_last_eight", default=None)
