from typing import *

from pydantic import BaseModel, Field

from .Attachment import Attachment
from .User import User


class Release(BaseModel):
    """
    None model
        Release represents a repository release

    """

    assets: Optional[List[Optional[Attachment]]] = Field(alias="assets", default=None)

    author: Optional[User] = Field(alias="author", default=None)

    body: Optional[str] = Field(alias="body", default=None)

    created_at: Optional[str] = Field(alias="created_at", default=None)

    draft: Optional[bool] = Field(alias="draft", default=None)

    html_url: Optional[str] = Field(alias="html_url", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    prerelease: Optional[bool] = Field(alias="prerelease", default=None)

    published_at: Optional[str] = Field(alias="published_at", default=None)

    tag_name: Optional[str] = Field(alias="tag_name", default=None)

    tarball_url: Optional[str] = Field(alias="tarball_url", default=None)

    target_commitish: Optional[str] = Field(alias="target_commitish", default=None)

    url: Optional[str] = Field(alias="url", default=None)

    zipball_url: Optional[str] = Field(alias="zipball_url", default=None)
