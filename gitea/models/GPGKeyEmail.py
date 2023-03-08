from typing import *

from pydantic import BaseModel, Field


class GPGKeyEmail(BaseModel):
    """
    None model
        GPGKeyEmail an email attached to a GPGKey

    """

    email: Optional[str] = Field(alias="email", default=None)

    verified: Optional[bool] = Field(alias="verified", default=None)
