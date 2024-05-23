# coding: utf-8

"""
    FINBOURNE Identity Service API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictInt, conlist, constr
from finbourne_identity.models.link import Link

class IdentifierPartSchema(BaseModel):
    """
    IdentifierPartSchema
    """
    index: StrictInt = Field(...)
    name: constr(strict=True, min_length=1) = Field(...)
    display_name: constr(strict=True, min_length=1) = Field(..., alias="displayName")
    description: constr(strict=True, min_length=1) = Field(...)
    required: StrictBool = Field(...)
    links: Optional[conlist(Link)] = None
    __properties = ["index", "name", "displayName", "description", "required", "links"]

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
    def from_json(cls, json_str: str) -> IdentifierPartSchema:
        """Create an instance of IdentifierPartSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IdentifierPartSchema:
        """Create an instance of IdentifierPartSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IdentifierPartSchema.parse_obj(obj)

        _obj = IdentifierPartSchema.parse_obj({
            "index": obj.get("index"),
            "name": obj.get("name"),
            "display_name": obj.get("displayName"),
            "description": obj.get("description"),
            "required": obj.get("required"),
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj
