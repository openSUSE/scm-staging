from typing import *

from pydantic import BaseModel, Field


class IssueFormFieldType(BaseModel):
    """
    IssueFormFieldType defines issue form field type, can be &#34;markdown&#34;, &#34;textarea&#34;, &#34;input&#34;, &#34;dropdown&#34; or &#34;checkboxes&#34; model

    """
