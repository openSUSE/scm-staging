from typing import *

from pydantic import BaseModel, Field

from .NodeInfoServices import NodeInfoServices
from .NodeInfoSoftware import NodeInfoSoftware
from .NodeInfoUsage import NodeInfoUsage


class NodeInfo(BaseModel):
    """
    None model
        NodeInfo contains standardized way of exposing metadata about a server running one of the distributed social networks

    """

    metadata: Optional[Dict[str, Any]] = Field(alias="metadata", default=None)

    openRegistrations: Optional[bool] = Field(alias="openRegistrations", default=None)

    protocols: Optional[List[str]] = Field(alias="protocols", default=None)

    services: Optional[NodeInfoServices] = Field(alias="services", default=None)

    software: Optional[NodeInfoSoftware] = Field(alias="software", default=None)

    usage: Optional[NodeInfoUsage] = Field(alias="usage", default=None)

    version: Optional[str] = Field(alias="version", default=None)
