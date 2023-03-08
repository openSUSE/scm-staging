from typing import *

from pydantic import BaseModel, Field


class TransferRepoOption(BaseModel):
    """
    None model
        TransferRepoOption options when transfer a repository&#39;s ownership

    """

    new_owner: str = Field(alias="new_owner")

    team_ids: Optional[List[int]] = Field(alias="team_ids", default=None)
