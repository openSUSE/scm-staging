from typing import *

from pydantic import BaseModel, Field


class NodeInfoUsageUsers(BaseModel):
    """
    None model
        NodeInfoUsageUsers contains statistics about the users of this server

    """

    activeHalfyear: Optional[int] = Field(alias="activeHalfyear", default=None)

    activeMonth: Optional[int] = Field(alias="activeMonth", default=None)

    total: Optional[int] = Field(alias="total", default=None)
