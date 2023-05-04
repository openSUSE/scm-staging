# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    The version of the OpenAPI document: 1.19.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr, conlist


class Hook(BaseModel):
    """
    Hook a hook is a web hook when one repository changed
    """

    active: Optional[StrictBool] = None
    authorization_header: Optional[StrictStr] = None
    config: Optional[Dict[str, StrictStr]] = None
    created_at: Optional[datetime] = None
    events: Optional[conlist(StrictStr)] = None
    id: Optional[StrictInt] = None
    type: Optional[StrictStr] = None
    updated_at: Optional[datetime] = None
    __properties = [
        "active",
        "authorization_header",
        "config",
        "created_at",
        "events",
        "id",
        "type",
        "updated_at",
    ]

    class Config:
        """Pydantic configuration"""

        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Hook:
        """Create an instance of Hook from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Hook:
        """Create an instance of Hook from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Hook.parse_obj(obj)

        _obj = Hook.parse_obj(
            {
                "active": obj.get("active"),
                "authorization_header": obj.get("authorization_header"),
                "config": obj.get("config"),
                "created_at": obj.get("created_at"),
                "events": obj.get("events"),
                "id": obj.get("id"),
                "type": obj.get("type"),
                "updated_at": obj.get("updated_at"),
            }
        )
        return _obj
