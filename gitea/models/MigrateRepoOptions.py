from typing import *

from pydantic import BaseModel, Field


class MigrateRepoOptions(BaseModel):
    """
        None model
            MigrateRepoOptions options for migrating repository&#39;s
    this is used to interact with api v1

    """

    auth_password: Optional[str] = Field(alias="auth_password", default=None)

    auth_token: Optional[str] = Field(alias="auth_token", default=None)

    auth_username: Optional[str] = Field(alias="auth_username", default=None)

    clone_addr: str = Field(alias="clone_addr")

    description: Optional[str] = Field(alias="description", default=None)

    issues: Optional[bool] = Field(alias="issues", default=None)

    labels: Optional[bool] = Field(alias="labels", default=None)

    lfs: Optional[bool] = Field(alias="lfs", default=None)

    lfs_endpoint: Optional[str] = Field(alias="lfs_endpoint", default=None)

    milestones: Optional[bool] = Field(alias="milestones", default=None)

    mirror: Optional[bool] = Field(alias="mirror", default=None)

    mirror_interval: Optional[str] = Field(alias="mirror_interval", default=None)

    private: Optional[bool] = Field(alias="private", default=None)

    pull_requests: Optional[bool] = Field(alias="pull_requests", default=None)

    releases: Optional[bool] = Field(alias="releases", default=None)

    repo_name: str = Field(alias="repo_name")

    repo_owner: Optional[str] = Field(alias="repo_owner", default=None)

    service: Optional[str] = Field(alias="service", default=None)

    uid: Optional[int] = Field(alias="uid", default=None)

    wiki: Optional[bool] = Field(alias="wiki", default=None)
