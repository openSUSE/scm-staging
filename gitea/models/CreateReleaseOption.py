from typing import *

from pydantic import BaseModel, Field


class CreateReleaseOption(BaseModel):
    """
    None model
        CreateReleaseOption options when creating a release

    """

    body: Optional[str] = Field(alias="body", default=None)

    draft: Optional[bool] = Field(alias="draft", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    prerelease: Optional[bool] = Field(alias="prerelease", default=None)

    tag_name: str = Field(alias="tag_name")

    target_commitish: Optional[str] = Field(alias="target_commitish", default=None)
