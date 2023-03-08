from typing import *

from pydantic import BaseModel, Field


class GitHook(BaseModel):
    """
    None model
        GitHook represents a Git repository hook

    """

    content: Optional[str] = Field(alias="content", default=None)

    is_active: Optional[bool] = Field(alias="is_active", default=None)

    name: Optional[str] = Field(alias="name", default=None)
