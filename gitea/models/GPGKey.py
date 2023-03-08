from typing import *

from pydantic import BaseModel, Field

from .GPGKeyEmail import GPGKeyEmail


class GPGKey(BaseModel):
    """
    None model
        GPGKey a user GPG key to sign commit and tag in repository

    """

    can_certify: Optional[bool] = Field(alias="can_certify", default=None)

    can_encrypt_comms: Optional[bool] = Field(alias="can_encrypt_comms", default=None)

    can_encrypt_storage: Optional[bool] = Field(
        alias="can_encrypt_storage", default=None
    )

    can_sign: Optional[bool] = Field(alias="can_sign", default=None)

    created_at: Optional[str] = Field(alias="created_at", default=None)

    emails: Optional[List[Optional[GPGKeyEmail]]] = Field(alias="emails", default=None)

    expires_at: Optional[str] = Field(alias="expires_at", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    key_id: Optional[str] = Field(alias="key_id", default=None)

    primary_key_id: Optional[str] = Field(alias="primary_key_id", default=None)

    public_key: Optional[str] = Field(alias="public_key", default=None)

    subkeys: Optional[List[Optional["GPGKey"]]] = Field(alias="subkeys", default=None)

    verified: Optional[bool] = Field(alias="verified", default=None)
