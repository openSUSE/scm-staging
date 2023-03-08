from typing import *

from pydantic import BaseModel, Field

from .User import User


class RepoCollaboratorPermission(BaseModel):
    """
    None model
        RepoCollaboratorPermission to get repository permission for a collaborator

    """

    permission: Optional[str] = Field(alias="permission", default=None)

    role_name: Optional[str] = Field(alias="role_name", default=None)

    user: Optional[User] = Field(alias="user", default=None)
