from typing import *

from pydantic import BaseModel, Field


class CreateLabelOption(BaseModel):
    """
    None model
        CreateLabelOption options for creating a label

    """

    color: str = Field(alias="color")

    description: Optional[str] = Field(alias="description", default=None)

    name: str = Field(alias="name")
