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


from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

class AddScimResponse(BaseModel):
    """
    AddScimResponse
    """
    base_url: Optional[StrictStr] = Field(None, alias="baseUrl")
    api_token: Optional[StrictStr] = Field(None, alias="apiToken")
    __properties = ["baseUrl", "apiToken"]

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
    def from_json(cls, json_str: str) -> AddScimResponse:
        """Create an instance of AddScimResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if base_url (nullable) is None
        # and __fields_set__ contains the field
        if self.base_url is None and "base_url" in self.__fields_set__:
            _dict['baseUrl'] = None

        # set to None if api_token (nullable) is None
        # and __fields_set__ contains the field
        if self.api_token is None and "api_token" in self.__fields_set__:
            _dict['apiToken'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AddScimResponse:
        """Create an instance of AddScimResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AddScimResponse.parse_obj(obj)

        _obj = AddScimResponse.parse_obj({
            "base_url": obj.get("baseUrl"),
            "api_token": obj.get("apiToken")
        })
        return _obj
