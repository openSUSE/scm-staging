from typing import *

from pydantic import BaseModel, Field

from .GitObject import GitObject


class Reference(BaseModel):
    """
    Reference represents a Git reference. model

    """

    object: Optional[GitObject] = Field(alias="object", default=None)

    ref: Optional[str] = Field(alias="ref", default=None)

    url: Optional[str] = Field(alias="url", default=None)
