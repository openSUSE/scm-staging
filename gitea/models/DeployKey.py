from typing import *

from pydantic import BaseModel, Field

from .Repository import Repository


class DeployKey(BaseModel):
    """
    None model
        DeployKey a deploy key

    """

    created_at: Optional[str] = Field(alias="created_at", default=None)

    fingerprint: Optional[str] = Field(alias="fingerprint", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    key: Optional[str] = Field(alias="key", default=None)

    key_id: Optional[int] = Field(alias="key_id", default=None)

    read_only: Optional[bool] = Field(alias="read_only", default=None)

    repository: Optional[Repository] = Field(alias="repository", default=None)

    title: Optional[str] = Field(alias="title", default=None)

    url: Optional[str] = Field(alias="url", default=None)
