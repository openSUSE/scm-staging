from typing import *

from pydantic import BaseModel, Field


class CreateEmailOption(BaseModel):
    """
    None model
        CreateEmailOption options when creating email addresses

    """

    emails: Optional[List[str]] = Field(alias="emails", default=None)
