from typing import *

from pydantic import BaseModel, Field


class EditReactionOption(BaseModel):
    """
    None model
        EditReactionOption contain the reaction type

    """

    content: Optional[str] = Field(alias="content", default=None)
