from typing import *

from pydantic import BaseModel, Field


class NodeInfoServices(BaseModel):
    """
    None model
        NodeInfoServices contains the third party sites this server can connect to via their application API

    """

    inbound: Optional[List[str]] = Field(alias="inbound", default=None)

    outbound: Optional[List[str]] = Field(alias="outbound", default=None)
