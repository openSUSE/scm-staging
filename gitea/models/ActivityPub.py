from typing import *

from pydantic import BaseModel, Field


class ActivityPub(BaseModel):
    """
    None model
        ActivityPub type

    """

    context: Optional[str] = Field(alias="@context", default=None)
