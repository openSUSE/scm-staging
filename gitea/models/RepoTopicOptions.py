from typing import *

from pydantic import BaseModel, Field


class RepoTopicOptions(BaseModel):
    """
    None model
        RepoTopicOptions a collection of repo topic names

    """

    topics: Optional[List[str]] = Field(alias="topics", default=None)
