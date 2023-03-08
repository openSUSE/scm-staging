from typing import *

from pydantic import BaseModel, Field


class AddCollaboratorOption(BaseModel):
    """
    None model
        AddCollaboratorOption options when adding a user as a collaborator of a repository

    """

    permission: Optional[str] = Field(alias="permission", default=None)
