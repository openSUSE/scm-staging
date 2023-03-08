from typing import *

from pydantic import BaseModel, Field


class ServerVersion(BaseModel):
    """
    None model
        ServerVersion wraps the version of the server

    """

    version: Optional[str] = Field(alias="version", default=None)
