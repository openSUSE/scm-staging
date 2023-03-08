from typing import *

from pydantic import BaseModel, Field


class StopWatch(BaseModel):
    """
    None model
        StopWatch represent a running stopwatch

    """

    created: Optional[str] = Field(alias="created", default=None)

    duration: Optional[str] = Field(alias="duration", default=None)

    issue_index: Optional[int] = Field(alias="issue_index", default=None)

    issue_title: Optional[str] = Field(alias="issue_title", default=None)

    repo_name: Optional[str] = Field(alias="repo_name", default=None)

    repo_owner_name: Optional[str] = Field(alias="repo_owner_name", default=None)

    seconds: Optional[int] = Field(alias="seconds", default=None)
