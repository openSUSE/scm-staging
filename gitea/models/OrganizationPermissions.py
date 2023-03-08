from typing import *

from pydantic import BaseModel, Field


class OrganizationPermissions(BaseModel):
    """
    None model
        OrganizationPermissions list different users permissions on an organization

    """

    can_create_repository: Optional[bool] = Field(
        alias="can_create_repository", default=None
    )

    can_read: Optional[bool] = Field(alias="can_read", default=None)

    can_write: Optional[bool] = Field(alias="can_write", default=None)

    is_admin: Optional[bool] = Field(alias="is_admin", default=None)

    is_owner: Optional[bool] = Field(alias="is_owner", default=None)
