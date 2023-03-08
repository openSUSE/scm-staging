from typing import *

from pydantic import BaseModel, Field


class Label(BaseModel):
    """
    None model
        Label a label to an issue or a pr

    """

    color: Optional[str] = Field(alias="color", default=None)

    description: Optional[str] = Field(alias="description", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    url: Optional[str] = Field(alias="url", default=None)
