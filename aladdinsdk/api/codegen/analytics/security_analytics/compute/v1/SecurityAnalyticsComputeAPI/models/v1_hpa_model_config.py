# coding: utf-8

"""
    Security Analytics Compute

    Compute security level analytics, cash flows and scenario analytics with custom valuation settings.  # noqa: E501

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
from aladdinsdk.api.codegen.analytics.security_analytics.compute.v1.SecurityAnalyticsComputeAPI.models.v1_model_input import V1ModelInput

class V1HPAModelConfig(BaseModel):
    """
    V1HPAModelConfig
    """
    model_version: Optional[StrictStr] = Field(None, alias="modelVersion")
    absolute_rate: Optional[V1ModelInput] = Field(None, alias="absoluteRate")
    rate_shift: Optional[V1ModelInput] = Field(None, alias="rateShift")
    rate_multiplier: Optional[V1ModelInput] = Field(None, alias="rateMultiplier")
    __properties = ["modelVersion", "absoluteRate", "rateShift", "rateMultiplier"]

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
    def from_json(cls, json_str: str) -> V1HPAModelConfig:
        """Create an instance of V1HPAModelConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of absolute_rate
        if self.absolute_rate:
            _dict['absoluteRate'] = self.absolute_rate.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rate_shift
        if self.rate_shift:
            _dict['rateShift'] = self.rate_shift.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rate_multiplier
        if self.rate_multiplier:
            _dict['rateMultiplier'] = self.rate_multiplier.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1HPAModelConfig:
        """Create an instance of V1HPAModelConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1HPAModelConfig.parse_obj(obj)

        _obj = V1HPAModelConfig.parse_obj({
            "model_version": obj.get("modelVersion"),
            "absolute_rate": V1ModelInput.from_dict(obj.get("absoluteRate")) if obj.get("absoluteRate") is not None else None,
            "rate_shift": V1ModelInput.from_dict(obj.get("rateShift")) if obj.get("rateShift") is not None else None,
            "rate_multiplier": V1ModelInput.from_dict(obj.get("rateMultiplier")) if obj.get("rateMultiplier") is not None else None
        })
        return _obj

