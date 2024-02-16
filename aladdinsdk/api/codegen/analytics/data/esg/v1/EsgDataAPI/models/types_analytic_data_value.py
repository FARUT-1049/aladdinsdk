# coding: utf-8

"""
    ESG Data

    The ESG Data API offers a centralized source of ESG data and meta data across multiple vendors. The API retrieves ESG data by asset and issuer from multiple vendors, providing the data in one digestible schema. Retrieve ESG data for selected assets and issuers by providing entity id, provider id, date(s) and measure name. Meta data on ESG data measures can be retrieved by selecting a provider, provider category and unique measure names. Time Series API in alpha version, changes may be made at any time.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class TypesAnalyticDataValue(BaseModel):
    """
    TypesAnalyticDataValue
    """
    value_string: Optional[StrictStr] = Field(None, alias="valueString")
    value_numeric: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="valueNumeric")
    value_integer: Optional[StrictStr] = Field(None, alias="valueInteger")
    value_date: Optional[date] = Field(None, alias="valueDate")
    __properties = ["valueString", "valueNumeric", "valueInteger", "valueDate"]

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
    def from_json(cls, json_str: str) -> TypesAnalyticDataValue:
        """Create an instance of TypesAnalyticDataValue from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TypesAnalyticDataValue:
        """Create an instance of TypesAnalyticDataValue from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TypesAnalyticDataValue.parse_obj(obj)

        _obj = TypesAnalyticDataValue.parse_obj({
            "value_string": obj.get("valueString"),
            "value_numeric": obj.get("valueNumeric"),
            "value_integer": obj.get("valueInteger"),
            "value_date": obj.get("valueDate")
        })
        return _obj
