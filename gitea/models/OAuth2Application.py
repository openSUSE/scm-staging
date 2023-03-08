from typing import *

from pydantic import BaseModel, Field


class OAuth2Application(BaseModel):
    """
    OAuth2Application represents an OAuth2 application. model

    """

    client_id: Optional[str] = Field(alias="client_id", default=None)

    client_secret: Optional[str] = Field(alias="client_secret", default=None)

    confidential_client: Optional[bool] = Field(
        alias="confidential_client", default=None
    )

    created: Optional[str] = Field(alias="created", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    redirect_uris: Optional[List[str]] = Field(alias="redirect_uris", default=None)
