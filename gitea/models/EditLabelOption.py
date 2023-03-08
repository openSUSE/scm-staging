from typing import *

from pydantic import BaseModel, Field


class EditLabelOption(BaseModel):
    """
    None model
        EditLabelOption options for editing a label

    """

    color: Optional[str] = Field(alias="color", default=None)

    description: Optional[str] = Field(alias="description", default=None)

    name: Optional[str] = Field(alias="name", default=None)
