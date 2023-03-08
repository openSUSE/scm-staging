from typing import *

from pydantic import BaseModel, Field

from .IssueFormFieldType import IssueFormFieldType


class IssueFormField(BaseModel):
    """
    None model
        IssueFormField represents a form field

    """

    attributes: Optional[Dict[str, Any]] = Field(alias="attributes", default=None)

    id: Optional[str] = Field(alias="id", default=None)

    type: Optional[IssueFormFieldType] = Field(alias="type", default=None)

    validations: Optional[Dict[str, Any]] = Field(alias="validations", default=None)
