from typing import *

from pydantic import BaseModel, Field


class CreatePushMirrorOption(BaseModel):
    """
    CreatePushMirrorOption represents need information to create a push mirror of a repository. model

    """

    interval: Optional[str] = Field(alias="interval", default=None)

    remote_address: Optional[str] = Field(alias="remote_address", default=None)

    remote_password: Optional[str] = Field(alias="remote_password", default=None)

    remote_username: Optional[str] = Field(alias="remote_username", default=None)

    sync_on_commit: Optional[bool] = Field(alias="sync_on_commit", default=None)
