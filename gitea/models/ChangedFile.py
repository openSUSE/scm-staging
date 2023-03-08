from typing import *

from pydantic import BaseModel, Field


class ChangedFile(BaseModel):
    """
    None model
        ChangedFile store information about files affected by the pull request

    """

    additions: Optional[int] = Field(alias="additions", default=None)

    changes: Optional[int] = Field(alias="changes", default=None)

    contents_url: Optional[str] = Field(alias="contents_url", default=None)

    deletions: Optional[int] = Field(alias="deletions", default=None)

    filename: Optional[str] = Field(alias="filename", default=None)

    html_url: Optional[str] = Field(alias="html_url", default=None)

    previous_filename: Optional[str] = Field(alias="previous_filename", default=None)

    raw_url: Optional[str] = Field(alias="raw_url", default=None)

    status: Optional[str] = Field(alias="status", default=None)
