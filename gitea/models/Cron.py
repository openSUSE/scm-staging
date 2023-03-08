from typing import *

from pydantic import BaseModel, Field


class Cron(BaseModel):
    """
    None model
        Cron represents a Cron task

    """

    exec_times: Optional[int] = Field(alias="exec_times", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    next: Optional[str] = Field(alias="next", default=None)

    prev: Optional[str] = Field(alias="prev", default=None)

    schedule: Optional[str] = Field(alias="schedule", default=None)
