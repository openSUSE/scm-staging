from typing import *

from pydantic import BaseModel, Field


class DismissPullReviewOptions(BaseModel):
    """
    None model
        DismissPullReviewOptions are options to dismiss a pull review

    """

    message: Optional[str] = Field(alias="message", default=None)

    priors: Optional[bool] = Field(alias="priors", default=None)
