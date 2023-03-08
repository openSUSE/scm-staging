from typing import *

from pydantic import BaseModel, Field


class CreateIssueCommentOption(BaseModel):
    """
    None model
        CreateIssueCommentOption options for creating a comment on an issue

    """

    body: str = Field(alias="body")
