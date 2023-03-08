from typing import *

from pydantic import BaseModel, Field


class Identity(BaseModel):
    """
    None model
        Identity for a person&#39;s identity like an author or committer

    """

    email: Optional[str] = Field(alias="email", default=None)

    name: Optional[str] = Field(alias="name", default=None)
