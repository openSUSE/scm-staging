from typing import *

from pydantic import BaseModel, Field


class MarkdownOption(BaseModel):
    """
    None model
        MarkdownOption markdown options

    """

    Context: Optional[str] = Field(alias="Context", default=None)

    Mode: Optional[str] = Field(alias="Mode", default=None)

    Text: Optional[str] = Field(alias="Text", default=None)

    Wiki: Optional[bool] = Field(alias="Wiki", default=None)
