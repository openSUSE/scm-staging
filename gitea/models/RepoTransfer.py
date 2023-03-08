from typing import *

from pydantic import BaseModel, Field

from .Team import Team
from .User import User


class RepoTransfer(BaseModel):
    """
    None model
        RepoTransfer represents a pending repo transfer

    """

    doer: Optional[User] = Field(alias="doer", default=None)

    recipient: Optional[User] = Field(alias="recipient", default=None)

    teams: Optional[List[Optional[Team]]] = Field(alias="teams", default=None)
