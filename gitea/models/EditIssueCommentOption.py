from typing import *

from pydantic import BaseModel, Field


class EditIssueCommentOption(BaseModel):
    """
    None model
        EditIssueCommentOption options for editing a comment

    """

    body: str = Field(alias="body")
