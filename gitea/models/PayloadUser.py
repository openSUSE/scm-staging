from typing import *

from pydantic import BaseModel, Field


class PayloadUser(BaseModel):
    """
    None model
        PayloadUser represents the author or committer of a commit

    """

    email: Optional[str] = Field(alias="email", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    username: Optional[str] = Field(alias="username", default=None)
