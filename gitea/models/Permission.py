from typing import *

from pydantic import BaseModel, Field


class Permission(BaseModel):
    """
    None model
        Permission represents a set of permissions

    """

    admin: Optional[bool] = Field(alias="admin", default=None)

    pull: Optional[bool] = Field(alias="pull", default=None)

    push: Optional[bool] = Field(alias="push", default=None)
