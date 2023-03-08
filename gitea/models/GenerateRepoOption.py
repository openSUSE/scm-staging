from typing import *

from pydantic import BaseModel, Field


class GenerateRepoOption(BaseModel):
    """
    None model
        GenerateRepoOption options when creating repository using a template

    """

    avatar: Optional[bool] = Field(alias="avatar", default=None)

    default_branch: Optional[str] = Field(alias="default_branch", default=None)

    description: Optional[str] = Field(alias="description", default=None)

    git_content: Optional[bool] = Field(alias="git_content", default=None)

    git_hooks: Optional[bool] = Field(alias="git_hooks", default=None)

    labels: Optional[bool] = Field(alias="labels", default=None)

    name: str = Field(alias="name")

    owner: str = Field(alias="owner")

    private: Optional[bool] = Field(alias="private", default=None)

    topics: Optional[bool] = Field(alias="topics", default=None)

    webhooks: Optional[bool] = Field(alias="webhooks", default=None)
