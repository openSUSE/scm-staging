from typing import *

from pydantic import BaseModel, Field

from .User import User


class userSearch_200_response(BaseModel):
    """
    None model

    """

    data: Optional[List[Optional[User]]] = Field(alias="data", default=None)

    ok: Optional[bool] = Field(alias="ok", default=None)
