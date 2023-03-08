from typing import *

from pydantic import BaseModel, Field


class GeneralAttachmentSettings(BaseModel):
    """
    None model
        GeneralAttachmentSettings contains global Attachment settings exposed by API

    """

    allowed_types: Optional[str] = Field(alias="allowed_types", default=None)

    enabled: Optional[bool] = Field(alias="enabled", default=None)

    max_files: Optional[int] = Field(alias="max_files", default=None)

    max_size: Optional[int] = Field(alias="max_size", default=None)
