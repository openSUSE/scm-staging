from typing import *

from pydantic import BaseModel, Field


class AnnotatedTagObject(BaseModel):
    """
    None model
        AnnotatedTagObject contains meta information of the tag object

    """

    sha: Optional[str] = Field(alias="sha", default=None)

    type: Optional[str] = Field(alias="type", default=None)

    url: Optional[str] = Field(alias="url", default=None)
