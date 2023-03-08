from typing import *

from pydantic import BaseModel, Field


class EditHookOption(BaseModel):
    """
    None model
        EditHookOption options when modify one hook

    """

    active: Optional[bool] = Field(alias="active", default=None)

    branch_filter: Optional[str] = Field(alias="branch_filter", default=None)

    config: Optional[Dict[str, Any]] = Field(alias="config", default=None)

    events: Optional[List[str]] = Field(alias="events", default=None)
