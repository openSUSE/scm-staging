from typing import *

from pydantic import BaseModel, Field


class CommitAffectedFiles(BaseModel):
    """
    None model
        CommitAffectedFiles store information about files affected by the commit

    """

    filename: Optional[str] = Field(alias="filename", default=None)
