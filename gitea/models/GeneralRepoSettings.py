from typing import *

from pydantic import BaseModel, Field


class GeneralRepoSettings(BaseModel):
    """
    None model
        GeneralRepoSettings contains global repository settings exposed by API

    """

    http_git_disabled: Optional[bool] = Field(alias="http_git_disabled", default=None)

    lfs_disabled: Optional[bool] = Field(alias="lfs_disabled", default=None)

    migrations_disabled: Optional[bool] = Field(
        alias="migrations_disabled", default=None
    )

    mirrors_disabled: Optional[bool] = Field(alias="mirrors_disabled", default=None)

    stars_disabled: Optional[bool] = Field(alias="stars_disabled", default=None)

    time_tracking_disabled: Optional[bool] = Field(
        alias="time_tracking_disabled", default=None
    )
