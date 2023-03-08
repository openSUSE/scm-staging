from typing import *

from pydantic import BaseModel, Field


class GitObject(BaseModel):
    """
    GitObject represents a Git object. model

    """

    sha: Optional[str] = Field(alias="sha", default=None)

    type: Optional[str] = Field(alias="type", default=None)

    url: Optional[str] = Field(alias="url", default=None)
