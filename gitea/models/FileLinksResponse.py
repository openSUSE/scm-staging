from typing import *

from pydantic import BaseModel, Field


class FileLinksResponse(BaseModel):
    """
    None model
        FileLinksResponse contains the links for a repo&#39;s file

    """

    git: Optional[str] = Field(alias="git", default=None)

    html: Optional[str] = Field(alias="html", default=None)

    self: Optional[str] = Field(alias="self", default=None)
