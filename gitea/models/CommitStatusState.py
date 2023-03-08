from typing import *

from pydantic import BaseModel, Field


class CommitStatusState(BaseModel):
    """
        None model
            CommitStatusState holds the state of a CommitStatus
    It can be &#34;pending&#34;, &#34;success&#34;, &#34;error&#34;, &#34;failure&#34;, and &#34;warning&#34;

    """
