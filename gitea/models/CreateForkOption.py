from typing import *

from pydantic import BaseModel, Field


class CreateForkOption(BaseModel):
    """
    None model
        CreateForkOption options for creating a fork

    """

    name: Optional[str] = Field(alias="name", default=None)

    organization: Optional[str] = Field(alias="organization", default=None)
