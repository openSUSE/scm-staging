from typing import *

from pydantic import BaseModel, Field


class CreateRepoOption(BaseModel):
    """
    None model
        CreateRepoOption options when creating repository

    """

    auto_init: Optional[bool] = Field(alias="auto_init", default=None)

    default_branch: Optional[str] = Field(alias="default_branch", default=None)

    description: Optional[str] = Field(alias="description", default=None)

    gitignores: Optional[str] = Field(alias="gitignores", default=None)

    issue_labels: Optional[str] = Field(alias="issue_labels", default=None)

    license: Optional[str] = Field(alias="license", default=None)

    name: str = Field(alias="name")

    private: Optional[bool] = Field(alias="private", default=None)

    readme: Optional[str] = Field(alias="readme", default=None)

    template: Optional[bool] = Field(alias="template", default=None)

    trust_model: Optional[str] = Field(alias="trust_model", default=None)
