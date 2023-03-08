from typing import *

from pydantic import BaseModel, Field

from .Repository import Repository
from .User import User


class Package(BaseModel):
    """
    None model
        Package represents a package

    """

    created_at: Optional[str] = Field(alias="created_at", default=None)

    creator: Optional[User] = Field(alias="creator", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    owner: Optional[User] = Field(alias="owner", default=None)

    repository: Optional[Repository] = Field(alias="repository", default=None)

    type: Optional[str] = Field(alias="type", default=None)

    version: Optional[str] = Field(alias="version", default=None)
