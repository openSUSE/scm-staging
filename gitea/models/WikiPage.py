from typing import *

from pydantic import BaseModel, Field

from .WikiCommit import WikiCommit


class WikiPage(BaseModel):
    """
    None model
        WikiPage a wiki page

    """

    commit_count: Optional[int] = Field(alias="commit_count", default=None)

    content_base64: Optional[str] = Field(alias="content_base64", default=None)

    footer: Optional[str] = Field(alias="footer", default=None)

    html_url: Optional[str] = Field(alias="html_url", default=None)

    last_commit: Optional[WikiCommit] = Field(alias="last_commit", default=None)

    sidebar: Optional[str] = Field(alias="sidebar", default=None)

    sub_url: Optional[str] = Field(alias="sub_url", default=None)

    title: Optional[str] = Field(alias="title", default=None)
