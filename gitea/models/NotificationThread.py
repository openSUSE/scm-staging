from typing import *

from pydantic import BaseModel, Field

from .NotificationSubject import NotificationSubject
from .Repository import Repository


class NotificationThread(BaseModel):
    """
    None model
        NotificationThread expose Notification on API

    """

    id: Optional[int] = Field(alias="id", default=None)

    pinned: Optional[bool] = Field(alias="pinned", default=None)

    repository: Optional[Repository] = Field(alias="repository", default=None)

    subject: Optional[NotificationSubject] = Field(alias="subject", default=None)

    unread: Optional[bool] = Field(alias="unread", default=None)

    updated_at: Optional[str] = Field(alias="updated_at", default=None)

    url: Optional[str] = Field(alias="url", default=None)
