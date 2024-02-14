# coding: utf-8

"""
    Timeseries Metadata

    Timeseries Metadata offers the capability to create, update, delete and search for metadata information about each timeseries data.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class TypeTimeZone(BaseModel):
    """
    Represents a time zone from the [IANA Time Zone Database](https://www.iana.org/time-zones).
    """
    id: Optional[StrictStr] = Field(None, description="IANA Time Zone Database time zone, e.g. \"America/New_York\".")
    version: Optional[StrictStr] = Field(None, description="Optional. IANA Time Zone Database version number, e.g. \"2019a\".")
    __properties = ["id", "version"]

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
    def from_json(cls, json_str: str) -> TypeTimeZone:
        """Create an instance of TypeTimeZone from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TypeTimeZone:
        """Create an instance of TypeTimeZone from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TypeTimeZone.parse_obj(obj)

        _obj = TypeTimeZone.parse_obj({
            "id": obj.get("id"),
            "version": obj.get("version")
        })
        return _obj

