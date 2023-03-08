from typing import *

from pydantic import BaseModel, Field


class GeneralAPISettings(BaseModel):
    """
    None model
        GeneralAPISettings contains global api settings exposed by it

    """

    default_git_trees_per_page: Optional[int] = Field(
        alias="default_git_trees_per_page", default=None
    )

    default_max_blob_size: Optional[int] = Field(
        alias="default_max_blob_size", default=None
    )

    default_paging_num: Optional[int] = Field(alias="default_paging_num", default=None)

    max_response_items: Optional[int] = Field(alias="max_response_items", default=None)
