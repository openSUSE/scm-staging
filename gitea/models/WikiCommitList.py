from typing import *

from pydantic import BaseModel, Field

from .WikiCommit import WikiCommit


class WikiCommitList(BaseModel):
    """
    None model
        WikiCommitList commit/revision list

    """

    commits: Optional[List[Optional[WikiCommit]]] = Field(alias="commits", default=None)

    count: Optional[int] = Field(alias="count", default=None)
