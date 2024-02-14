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

class V1TimeseriesFilter(BaseModel):
    """
    V1TimeseriesFilter
    """
    filter_code: Optional[StrictStr] = Field(None, alias="filterCode")
    filter_value: Optional[StrictStr] = Field(None, alias="filterValue")
    filter_operator: Optional[StrictStr] = Field(None, alias="filterOperator")
    __properties = ["filterCode", "filterValue", "filterOperator"]

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
    def from_json(cls, json_str: str) -> V1TimeseriesFilter:
        """Create an instance of V1TimeseriesFilter from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1TimeseriesFilter:
        """Create an instance of V1TimeseriesFilter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1TimeseriesFilter.parse_obj(obj)

        _obj = V1TimeseriesFilter.parse_obj({
            "filter_code": obj.get("filterCode"),
            "filter_value": obj.get("filterValue"),
            "filter_operator": obj.get("filterOperator")
        })
        return _obj

