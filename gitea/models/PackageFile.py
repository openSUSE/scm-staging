from typing import *

from pydantic import BaseModel, Field


class PackageFile(BaseModel):
    """
    None model
        PackageFile represents a package file

    """

    Size: Optional[int] = Field(alias="Size", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    md5: Optional[str] = Field(alias="md5", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    sha1: Optional[str] = Field(alias="sha1", default=None)

    sha256: Optional[str] = Field(alias="sha256", default=None)

    sha512: Optional[str] = Field(alias="sha512", default=None)
