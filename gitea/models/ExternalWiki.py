from typing import *

from pydantic import BaseModel, Field


class ExternalWiki(BaseModel):
    """
    None model
        ExternalWiki represents setting for external wiki

    """

    external_wiki_url: Optional[str] = Field(alias="external_wiki_url", default=None)
