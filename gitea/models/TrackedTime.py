from typing import *

from pydantic import BaseModel, Field

from .Issue import Issue


class TrackedTime(BaseModel):
    """
    None model
        TrackedTime worked time for an issue / pr

    """

    created: Optional[str] = Field(alias="created", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    issue: Optional[Issue] = Field(alias="issue", default=None)

    issue_id: Optional[int] = Field(alias="issue_id", default=None)

    time: Optional[int] = Field(alias="time", default=None)

    user_id: Optional[int] = Field(alias="user_id", default=None)

    user_name: Optional[str] = Field(alias="user_name", default=None)
