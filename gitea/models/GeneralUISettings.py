from typing import *

from pydantic import BaseModel, Field


class GeneralUISettings(BaseModel):
    """
    None model
        GeneralUISettings contains global ui settings exposed by API

    """

    allowed_reactions: Optional[List[str]] = Field(
        alias="allowed_reactions", default=None
    )

    custom_emojis: Optional[List[str]] = Field(alias="custom_emojis", default=None)

    default_theme: Optional[str] = Field(alias="default_theme", default=None)
