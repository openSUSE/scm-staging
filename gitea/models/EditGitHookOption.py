from typing import *

from pydantic import BaseModel, Field


class EditGitHookOption(BaseModel):
    """
    None model
        EditGitHookOption options when modifying one Git hook

    """

    content: Optional[str] = Field(alias="content", default=None)
