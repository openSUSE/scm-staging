from typing import *

from pydantic import BaseModel, Field


class TopicResponse(BaseModel):
    """
    None model
        TopicResponse for returning topics

    """

    created: Optional[str] = Field(alias="created", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    repo_count: Optional[int] = Field(alias="repo_count", default=None)

    topic_name: Optional[str] = Field(alias="topic_name", default=None)

    updated: Optional[str] = Field(alias="updated", default=None)
