from typing import *

from pydantic import BaseModel, Field

from .Organization import Organization


class Team(BaseModel):
    """
    None model
        Team represents a team in an organization

    """

    can_create_org_repo: Optional[bool] = Field(
        alias="can_create_org_repo", default=None
    )

    description: Optional[str] = Field(alias="description", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    includes_all_repositories: Optional[bool] = Field(
        alias="includes_all_repositories", default=None
    )

    name: Optional[str] = Field(alias="name", default=None)

    organization: Optional[Organization] = Field(alias="organization", default=None)

    permission: Optional[str] = Field(alias="permission", default=None)

    units: Optional[List[str]] = Field(alias="units", default=None)

    units_map: Optional[Dict[str, Any]] = Field(alias="units_map", default=None)
