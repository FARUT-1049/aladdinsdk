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
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class V2AlphaModel(BaseModel):
    """
    V2AlphaModel
    """
    asset_alphas: Optional[Dict[str, Union[StrictFloat, StrictInt]]] = Field(None, alias="assetAlphas")
    stress_scenario_name: Optional[StrictStr] = Field(None, alias="stressScenarioName")
    stress_scenario_purpose: Optional[StrictStr] = Field(None, alias="stressScenarioPurpose")
    factor_exposure_as_alpha: Optional[StrictStr] = Field(None, alias="factorExposureAsAlpha")
    __properties = ["assetAlphas", "stressScenarioName", "stressScenarioPurpose", "factorExposureAsAlpha"]

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
    def from_json(cls, json_str: str) -> V2AlphaModel:
        """Create an instance of V2AlphaModel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V2AlphaModel:
        """Create an instance of V2AlphaModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V2AlphaModel.parse_obj(obj)

        _obj = V2AlphaModel.parse_obj({
            "asset_alphas": obj.get("assetAlphas"),
            "stress_scenario_name": obj.get("stressScenarioName"),
            "stress_scenario_purpose": obj.get("stressScenarioPurpose"),
            "factor_exposure_as_alpha": obj.get("factorExposureAsAlpha")
        })
        return _obj
