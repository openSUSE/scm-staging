from typing import *

from pydantic import BaseModel, Field

from .Repository import Repository


class SearchResults(BaseModel):
    """
    None model
        SearchResults results of a successful search

    """

    data: Optional[List[Optional[Repository]]] = Field(alias="data", default=None)

    ok: Optional[bool] = Field(alias="ok", default=None)
