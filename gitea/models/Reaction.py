from typing import *

from pydantic import BaseModel, Field

from .User import User


class Reaction(BaseModel):
    """
    None model
        Reaction contain one reaction

    """

    content: Optional[str] = Field(alias="content", default=None)

    created_at: Optional[str] = Field(alias="created_at", default=None)

    user: Optional[User] = Field(alias="user", default=None)
