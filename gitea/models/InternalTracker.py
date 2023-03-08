from typing import *

from pydantic import BaseModel, Field


class InternalTracker(BaseModel):
    """
    None model
        InternalTracker represents settings for internal tracker

    """

    allow_only_contributors_to_track_time: Optional[bool] = Field(
        alias="allow_only_contributors_to_track_time", default=None
    )

    enable_issue_dependencies: Optional[bool] = Field(
        alias="enable_issue_dependencies", default=None
    )

    enable_time_tracker: Optional[bool] = Field(
        alias="enable_time_tracker", default=None
    )
