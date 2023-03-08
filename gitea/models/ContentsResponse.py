from typing import *

from pydantic import BaseModel, Field

from .FileLinksResponse import FileLinksResponse


class ContentsResponse(BaseModel):
    """
    None model
        ContentsResponse contains information about a repo&#39;s entry&#39;s (dir, file, symlink, submodule) metadata and content

    """

    _links: Optional[FileLinksResponse] = Field(alias="_links", default=None)

    content: Optional[str] = Field(alias="content", default=None)

    download_url: Optional[str] = Field(alias="download_url", default=None)

    encoding: Optional[str] = Field(alias="encoding", default=None)

    git_url: Optional[str] = Field(alias="git_url", default=None)

    html_url: Optional[str] = Field(alias="html_url", default=None)

    last_commit_sha: Optional[str] = Field(alias="last_commit_sha", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    path: Optional[str] = Field(alias="path", default=None)

    sha: Optional[str] = Field(alias="sha", default=None)

    size: Optional[int] = Field(alias="size", default=None)

    submodule_git_url: Optional[str] = Field(alias="submodule_git_url", default=None)

    target: Optional[str] = Field(alias="target", default=None)

    type: Optional[str] = Field(alias="type", default=None)

    url: Optional[str] = Field(alias="url", default=None)
