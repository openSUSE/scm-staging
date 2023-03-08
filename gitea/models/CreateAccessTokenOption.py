from typing import *

from pydantic import BaseModel, Field


class CreateAccessTokenOption(BaseModel):
    """
    None model
        CreateAccessTokenOption options when create access token

    """

    name: Optional[str] = Field(alias="name", default=None)
