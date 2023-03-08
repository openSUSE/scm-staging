from typing import *

from pydantic import BaseModel, Field

from .WikiCommit import WikiCommit


class WikiPageMetaData(BaseModel):
    """
    None model
        WikiPageMetaData wiki page meta information

    """

    html_url: Optional[str] = Field(alias="html_url", default=None)

    last_commit: Optional[WikiCommit] = Field(alias="last_commit", default=None)

    sub_url: Optional[str] = Field(alias="sub_url", default=None)

    title: Optional[str] = Field(alias="title", default=None)
