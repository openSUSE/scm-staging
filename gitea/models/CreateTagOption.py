from typing import *

from pydantic import BaseModel, Field


class CreateTagOption(BaseModel):
    """
    None model
        CreateTagOption options when creating a tag

    """

    message: Optional[str] = Field(alias="message", default=None)

    tag_name: str = Field(alias="tag_name")

    target: Optional[str] = Field(alias="target", default=None)
