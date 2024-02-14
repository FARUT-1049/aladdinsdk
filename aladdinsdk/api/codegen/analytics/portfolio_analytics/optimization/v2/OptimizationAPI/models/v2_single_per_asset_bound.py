# coding: utf-8

"""
    Portfolio Optimization 2.0

    Optimize portfolio positions to maximize expected returns and minimize risk and transaction costs.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Dict, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_bound_unit import V2BoundUnit

class V2SinglePerAssetBound(BaseModel):
    """
    V2SinglePerAssetBound
    """
    default_value: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="defaultValue")
    per_asset_values: Optional[Dict[str, Union[StrictFloat, StrictInt]]] = Field(None, alias="perAssetValues")
    relaxation: Optional[Union[StrictFloat, StrictInt]] = None
    bound_unit: Optional[V2BoundUnit] = Field(None, alias="boundUnit")
    __properties = ["defaultValue", "perAssetValues", "relaxation", "boundUnit"]

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
    def from_json(cls, json_str: str) -> V2SinglePerAssetBound:
        """Create an instance of V2SinglePerAssetBound from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V2SinglePerAssetBound:
        """Create an instance of V2SinglePerAssetBound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V2SinglePerAssetBound.parse_obj(obj)

        _obj = V2SinglePerAssetBound.parse_obj({
            "default_value": obj.get("defaultValue"),
            "per_asset_values": obj.get("perAssetValues"),
            "relaxation": obj.get("relaxation"),
            "bound_unit": obj.get("boundUnit")
        })
        return _obj

