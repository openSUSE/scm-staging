from typing import *

from pydantic import BaseModel, Field


class IssueLabelsOption(BaseModel):
    """
    None model
        IssueLabelsOption a collection of labels

    """

    labels: Optional[List[int]] = Field(alias="labels", default=None)
