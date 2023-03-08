from typing import *

from pydantic import BaseModel, Field


class repoCreateReleaseAttachment_request(BaseModel):
    """
    None model

    """

    attachment: str = Field(alias="attachment")
