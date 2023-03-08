from typing import *

from pydantic import BaseModel, Field


class PushMirror(BaseModel):
    """
    None model
        PushMirror represents information of a push mirror

    """

    created: Optional[str] = Field(alias="created", default=None)

    interval: Optional[str] = Field(alias="interval", default=None)

    last_error: Optional[str] = Field(alias="last_error", default=None)

    last_update: Optional[str] = Field(alias="last_update", default=None)

    remote_address: Optional[str] = Field(alias="remote_address", default=None)

    remote_name: Optional[str] = Field(alias="remote_name", default=None)

    repo_name: Optional[str] = Field(alias="repo_name", default=None)

    sync_on_commit: Optional[bool] = Field(alias="sync_on_commit", default=None)
