# coding: utf-8

"""
    Climate

    The Aladdin Climate Data API exposes physical, transition, and temperature alignment analytics as of a given date. Users can retrieve data for selected entity types by specifying the desired datapoints for each climate risk type and scenario. The Aladdin Climate Meta Data API outlines the datapoints available across physical, transition, and temperature alignment analytics.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist

class V1IdAttributes(BaseModel):
    """
    V1IdAttributes
    """
    name: Optional[StrictStr] = None
    attribute_values: Optional[conlist(StrictStr)] = Field(None, alias="attributeValues")
    __properties = ["name", "attributeValues"]

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
    def from_json(cls, json_str: str) -> V1IdAttributes:
        """Create an instance of V1IdAttributes from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1IdAttributes:
        """Create an instance of V1IdAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1IdAttributes.parse_obj(obj)

        _obj = V1IdAttributes.parse_obj({
            "name": obj.get("name"),
            "attribute_values": obj.get("attributeValues")
        })
        return _obj
