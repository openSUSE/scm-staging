from typing import *

from pydantic import BaseModel, Field

from .PayloadUser import PayloadUser


class PayloadCommitVerification(BaseModel):
    """
    None model
        PayloadCommitVerification represents the GPG verification of a commit

    """

    payload: Optional[str] = Field(alias="payload", default=None)

    reason: Optional[str] = Field(alias="reason", default=None)

    signature: Optional[str] = Field(alias="signature", default=None)

    signer: Optional[PayloadUser] = Field(alias="signer", default=None)

    verified: Optional[bool] = Field(alias="verified", default=None)
