from typing import *

from pydantic import BaseModel, Field


class APIError(BaseModel):
    """
    None model
        APIError is an api error with a message

    """

    message: Optional[str] = Field(alias="message", default=None)

    url: Optional[str] = Field(alias="url", default=None)
