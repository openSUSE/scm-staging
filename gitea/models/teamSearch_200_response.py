from typing import *

from pydantic import BaseModel, Field

from .Team import Team


class teamSearch_200_response(BaseModel):
    """
    None model

    """

    data: Optional[List[Optional[Team]]] = Field(alias="data", default=None)

    ok: Optional[bool] = Field(alias="ok", default=None)
