from typing import *

from pydantic import BaseModel, Field

from .IssueFormField import IssueFormField
from .IssueTemplateLabels import IssueTemplateLabels


class IssueTemplate(BaseModel):
    """
    None model
        IssueTemplate represents an issue template for a repository

    """

    about: Optional[str] = Field(alias="about", default=None)

    body: Optional[List[Optional[IssueFormField]]] = Field(alias="body", default=None)

    content: Optional[str] = Field(alias="content", default=None)

    file_name: Optional[str] = Field(alias="file_name", default=None)

    labels: Optional[IssueTemplateLabels] = Field(alias="labels", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    ref: Optional[str] = Field(alias="ref", default=None)

    title: Optional[str] = Field(alias="title", default=None)
