from typing import *

from pydantic import BaseModel, Field


class ExternalTracker(BaseModel):
    """
    None model
        ExternalTracker represents settings for external tracker

    """

    external_tracker_format: Optional[str] = Field(
        alias="external_tracker_format", default=None
    )

    external_tracker_regexp_pattern: Optional[str] = Field(
        alias="external_tracker_regexp_pattern", default=None
    )

    external_tracker_style: Optional[str] = Field(
        alias="external_tracker_style", default=None
    )

    external_tracker_url: Optional[str] = Field(
        alias="external_tracker_url", default=None
    )
