from typing import *

from pydantic import BaseModel, Field


class CreateGPGKeyOption(BaseModel):
    """
    None model
        CreateGPGKeyOption options create user GPG key

    """

    armored_public_key: str = Field(alias="armored_public_key")

    armored_signature: Optional[str] = Field(alias="armored_signature", default=None)
