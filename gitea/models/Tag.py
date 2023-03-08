from typing import *

from pydantic import BaseModel, Field

from .CommitMeta import CommitMeta


class Tag(BaseModel):
    """
    None model
        Tag represents a repository tag

    """

    commit: Optional[CommitMeta] = Field(alias="commit", default=None)

    id: Optional[str] = Field(alias="id", default=None)

    message: Optional[str] = Field(alias="message", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    tarball_url: Optional[str] = Field(alias="tarball_url", default=None)

    zipball_url: Optional[str] = Field(alias="zipball_url", default=None)
