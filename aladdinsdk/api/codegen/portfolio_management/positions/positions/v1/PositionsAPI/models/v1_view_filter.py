# coding: utf-8

"""
    Positions

    API to retrieve and monitor managed positions for Start of Day Positions. Managed positions are positions enriched with additional context such as restrictions and substitutions.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, conlist
from aladdinsdk.api.codegen.portfolio_management.positions.positions.v1.PositionsAPI.models.v1_sort import V1Sort

class V1ViewFilter(BaseModel):
    """
    V1ViewFilter
    """
    top_n: Optional[StrictInt] = Field(None, alias="topN")
    bottom_n: Optional[StrictInt] = Field(None, alias="bottomN")
    sorts: Optional[conlist(V1Sort)] = None
    __properties = ["topN", "bottomN", "sorts"]

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
    def from_json(cls, json_str: str) -> V1ViewFilter:
        """Create an instance of V1ViewFilter from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in sorts (list)
        _items = []
        if self.sorts:
            for _item in self.sorts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['sorts'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1ViewFilter:
        """Create an instance of V1ViewFilter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1ViewFilter.parse_obj(obj)

        _obj = V1ViewFilter.parse_obj({
            "top_n": obj.get("topN"),
            "bottom_n": obj.get("bottomN"),
            "sorts": [V1Sort.from_dict(_item) for _item in obj.get("sorts")] if obj.get("sorts") is not None else None
        })
        return _obj
