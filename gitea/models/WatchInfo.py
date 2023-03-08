from typing import *

from pydantic import BaseModel, Field


class WatchInfo(BaseModel):
    """
    None model
        WatchInfo represents an API watch status of one repository

    """

    created_at: Optional[str] = Field(alias="created_at", default=None)

    ignored: Optional[bool] = Field(alias="ignored", default=None)

    reason: Optional[Dict[str, Any]] = Field(alias="reason", default=None)

    repository_url: Optional[str] = Field(alias="repository_url", default=None)

    subscribed: Optional[bool] = Field(alias="subscribed", default=None)

    url: Optional[str] = Field(alias="url", default=None)
