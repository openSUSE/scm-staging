from typing import *

from pydantic import BaseModel, Field


class DeleteEmailOption(BaseModel):
    """
    None model
        DeleteEmailOption options when deleting email addresses

    """

    emails: Optional[List[str]] = Field(alias="emails", default=None)
