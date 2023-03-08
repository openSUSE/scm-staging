from typing import *

from pydantic import BaseModel, Field


class CreateWikiPageOptions(BaseModel):
    """
    None model
        CreateWikiPageOptions form for creating wiki

    """

    content_base64: Optional[str] = Field(alias="content_base64", default=None)

    message: Optional[str] = Field(alias="message", default=None)

    title: Optional[str] = Field(alias="title", default=None)
