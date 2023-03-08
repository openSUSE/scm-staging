from typing import *

from pydantic import BaseModel, Field

from .NotifySubjectType import NotifySubjectType
from .StateType import StateType


class NotificationSubject(BaseModel):
    """
    None model
        NotificationSubject contains the notification subject (Issue/Pull/Commit)

    """

    html_url: Optional[str] = Field(alias="html_url", default=None)

    latest_comment_html_url: Optional[str] = Field(
        alias="latest_comment_html_url", default=None
    )

    latest_comment_url: Optional[str] = Field(alias="latest_comment_url", default=None)

    state: Optional[StateType] = Field(alias="state", default=None)

    title: Optional[str] = Field(alias="title", default=None)

    type: Optional[NotifySubjectType] = Field(alias="type", default=None)

    url: Optional[str] = Field(alias="url", default=None)
