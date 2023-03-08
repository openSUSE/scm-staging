from typing import *

from pydantic import BaseModel, Field


class RepositoryMeta(BaseModel):
    """
    None model
        RepositoryMeta basic repository information

    """

    full_name: Optional[str] = Field(alias="full_name", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    owner: Optional[str] = Field(alias="owner", default=None)
