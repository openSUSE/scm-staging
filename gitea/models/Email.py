from typing import *

from pydantic import BaseModel, Field


class Email(BaseModel):
    """
    None model
        Email an email address belonging to a user

    """

    email: Optional[str] = Field(alias="email", default=None)

    primary: Optional[bool] = Field(alias="primary", default=None)

    verified: Optional[bool] = Field(alias="verified", default=None)
