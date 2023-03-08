from typing import *

from pydantic import BaseModel, Field


class NotificationCount(BaseModel):
    """
    None model
        NotificationCount number of unread notifications

    """

    new: Optional[int] = Field(alias="new", default=None)
