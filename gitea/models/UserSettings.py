from typing import *

from pydantic import BaseModel, Field


class UserSettings(BaseModel):
    """
    None model
        UserSettings represents user settings

    """

    description: Optional[str] = Field(alias="description", default=None)

    diff_view_style: Optional[str] = Field(alias="diff_view_style", default=None)

    full_name: Optional[str] = Field(alias="full_name", default=None)

    hide_activity: Optional[bool] = Field(alias="hide_activity", default=None)

    hide_email: Optional[bool] = Field(alias="hide_email", default=None)

    language: Optional[str] = Field(alias="language", default=None)

    location: Optional[str] = Field(alias="location", default=None)

    theme: Optional[str] = Field(alias="theme", default=None)

    website: Optional[str] = Field(alias="website", default=None)
