from typing import *

from pydantic import BaseModel, Field


class TopicName(BaseModel):
    """
    None model
        TopicName a list of repo topic names

    """

    topics: Optional[List[str]] = Field(alias="topics", default=None)
