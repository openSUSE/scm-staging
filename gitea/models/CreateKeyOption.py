from typing import *

from pydantic import BaseModel, Field


class CreateKeyOption(BaseModel):
    """
    None model
        CreateKeyOption options when creating a key

    """

    key: str = Field(alias="key")

    read_only: Optional[bool] = Field(alias="read_only", default=None)

    title: str = Field(alias="title")
