from typing import *

from pydantic import BaseModel, Field


class CreateTeamOption(BaseModel):
    """
    None model
        CreateTeamOption options for creating a team

    """

    can_create_org_repo: Optional[bool] = Field(
        alias="can_create_org_repo", default=None
    )

    description: Optional[str] = Field(alias="description", default=None)

    includes_all_repositories: Optional[bool] = Field(
        alias="includes_all_repositories", default=None
    )

    name: str = Field(alias="name")

    permission: Optional[str] = Field(alias="permission", default=None)

    units: Optional[List[str]] = Field(alias="units", default=None)

    units_map: Optional[Dict[str, Any]] = Field(alias="units_map", default=None)
