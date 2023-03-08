from typing import *

from pydantic import BaseModel, Field


class Attachment(BaseModel):
    """
    None model
        Attachment a generic attachment

    """

    browser_download_url: Optional[str] = Field(
        alias="browser_download_url", default=None
    )

    created_at: Optional[str] = Field(alias="created_at", default=None)

    download_count: Optional[int] = Field(alias="download_count", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    size: Optional[int] = Field(alias="size", default=None)

    uuid: Optional[str] = Field(alias="uuid", default=None)
