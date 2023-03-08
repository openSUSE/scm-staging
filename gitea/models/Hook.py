from typing import *

from pydantic import BaseModel, Field


class Hook(BaseModel):
    """
    None model
        Hook a hook is a web hook when one repository changed

    """

    active: Optional[bool] = Field(alias="active", default=None)

    config: Optional[Dict[str, Any]] = Field(alias="config", default=None)

    created_at: Optional[str] = Field(alias="created_at", default=None)

    events: Optional[List[str]] = Field(alias="events", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    type: Optional[str] = Field(alias="type", default=None)

    updated_at: Optional[str] = Field(alias="updated_at", default=None)
