from typing import *

from pydantic import BaseModel, Field

from .CreateHookOptionConfig import CreateHookOptionConfig


class CreateHookOption(BaseModel):
    """
    None model
        CreateHookOption options when create a hook

    """

    active: Optional[bool] = Field(alias="active", default=None)

    branch_filter: Optional[str] = Field(alias="branch_filter", default=None)

    config: CreateHookOptionConfig = Field(alias="config")

    events: Optional[List[str]] = Field(alias="events", default=None)

    type: str = Field(alias="type")
