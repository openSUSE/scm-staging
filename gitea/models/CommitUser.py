from typing import *

from pydantic import BaseModel, Field


class CommitUser(BaseModel):
    """
    CommitUser contains information of a user in the context of a commit. model

    """

    date: Optional[str] = Field(alias="date", default=None)

    email: Optional[str] = Field(alias="email", default=None)

    name: Optional[str] = Field(alias="name", default=None)
