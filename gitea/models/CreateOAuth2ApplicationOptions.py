from typing import *

from pydantic import BaseModel, Field


class CreateOAuth2ApplicationOptions(BaseModel):
    """
    None model
        CreateOAuth2ApplicationOptions holds options to create an oauth2 application

    """

    confidential_client: Optional[bool] = Field(
        alias="confidential_client", default=None
    )

    name: Optional[str] = Field(alias="name", default=None)

    redirect_uris: Optional[List[str]] = Field(alias="redirect_uris", default=None)
