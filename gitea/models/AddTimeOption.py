from typing import *

from pydantic import BaseModel, Field


class AddTimeOption(BaseModel):
    """
    None model
        AddTimeOption options for adding time to an issue

    """

    created: Optional[str] = Field(alias="created", default=None)

    time: int = Field(alias="time")

    user_name: Optional[str] = Field(alias="user_name", default=None)
