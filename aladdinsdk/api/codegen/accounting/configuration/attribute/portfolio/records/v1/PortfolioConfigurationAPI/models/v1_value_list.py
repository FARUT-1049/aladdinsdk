# coding: utf-8

"""
    Portfolio Configuration Record For Accounting

    Configurations API for Aladdin Accounting allows you to access accounting configuration attributes for process types that portfolios are setup on. Data can be sourced in aggregate and filtered to improve oversight and scale of configuration monitoring. This API allows for retrieval of key data points for portfolio configurations by various parameters, including portfolio tickers, processCodes, and more.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, StrictStr, conlist

class V1ValueList(BaseModel):
    """
    Denote the attribute name to filter by here. For example, update \"property1\" in the call body to be \"alpha_price_group\" if you'd like to filter by this attribute, or any other attributes. Add more attributes as needed if you would like to filter on more attributes.
    """
    values: Optional[conlist(StrictStr)] = None
    __properties = ["values"]

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
    def from_json(cls, json_str: str) -> V1ValueList:
        """Create an instance of V1ValueList from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1ValueList:
        """Create an instance of V1ValueList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1ValueList.parse_obj(obj)

        _obj = V1ValueList.parse_obj({
            "values": obj.get("values")
        })
        return _obj
