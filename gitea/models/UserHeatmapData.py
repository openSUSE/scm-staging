from typing import *

from pydantic import BaseModel, Field

from .TimeStamp import TimeStamp


class UserHeatmapData(BaseModel):
    """
    None model
        UserHeatmapData represents the data needed to create a heatmap

    """

    contributions: Optional[int] = Field(alias="contributions", default=None)

    timestamp: Optional[TimeStamp] = Field(alias="timestamp", default=None)
