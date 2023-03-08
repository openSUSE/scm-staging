from typing import *

from pydantic import BaseModel, Field


class EditReleaseOption(BaseModel):
    """
    None model
        EditReleaseOption options when editing a release

    """

    body: Optional[str] = Field(alias="body", default=None)

    draft: Optional[bool] = Field(alias="draft", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    prerelease: Optional[bool] = Field(alias="prerelease", default=None)

    tag_name: Optional[str] = Field(alias="tag_name", default=None)

    target_commitish: Optional[str] = Field(alias="target_commitish", default=None)
