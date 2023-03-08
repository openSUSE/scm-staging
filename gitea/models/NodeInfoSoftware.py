from typing import *

from pydantic import BaseModel, Field


class NodeInfoSoftware(BaseModel):
    """
    None model
        NodeInfoSoftware contains Metadata about server software in use

    """

    homepage: Optional[str] = Field(alias="homepage", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    repository: Optional[str] = Field(alias="repository", default=None)

    version: Optional[str] = Field(alias="version", default=None)
