from typing import *

from pydantic import BaseModel, Field

from .NodeInfoUsageUsers import NodeInfoUsageUsers


class NodeInfoUsage(BaseModel):
    """
    None model
        NodeInfoUsage contains usage statistics for this server

    """

    localComments: Optional[int] = Field(alias="localComments", default=None)

    localPosts: Optional[int] = Field(alias="localPosts", default=None)

    users: Optional[NodeInfoUsageUsers] = Field(alias="users", default=None)
