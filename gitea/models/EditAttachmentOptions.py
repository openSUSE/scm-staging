from typing import *

from pydantic import BaseModel, Field


class EditAttachmentOptions(BaseModel):
    """
    None model
        EditAttachmentOptions options for editing attachments

    """

    name: Optional[str] = Field(alias="name", default=None)
