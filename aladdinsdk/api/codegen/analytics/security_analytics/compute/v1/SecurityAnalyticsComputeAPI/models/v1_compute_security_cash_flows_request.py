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
from aladdinsdk.api.codegen.analytics.security_analytics.compute.v1.SecurityAnalyticsComputeAPI.models.v1_security_cash_flows_request_config import V1SecurityCashFlowsRequestConfig
from aladdinsdk.api.codegen.analytics.security_analytics.compute.v1.SecurityAnalyticsComputeAPI.models.v1_security_valuation_config import V1SecurityValuationConfig

class V1ComputeSecurityCashFlowsRequest(BaseModel):
    """
    The request message for SecurityAnalyticsComputeAPI.computeSecurityCashFlows.
    """
    asset_id: StrictStr = Field(..., alias="assetId")
    valuation_config: Optional[V1SecurityValuationConfig] = Field(None, alias="valuationConfig")
    cashflows_request_config: Optional[V1SecurityCashFlowsRequestConfig] = Field(None, alias="cashflowsRequestConfig")
    __properties = ["assetId", "valuationConfig", "cashflowsRequestConfig"]

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
    def from_json(cls, json_str: str) -> V1ComputeSecurityCashFlowsRequest:
        """Create an instance of V1ComputeSecurityCashFlowsRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of valuation_config
        if self.valuation_config:
            _dict['valuationConfig'] = self.valuation_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cashflows_request_config
        if self.cashflows_request_config:
            _dict['cashflowsRequestConfig'] = self.cashflows_request_config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1ComputeSecurityCashFlowsRequest:
        """Create an instance of V1ComputeSecurityCashFlowsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1ComputeSecurityCashFlowsRequest.parse_obj(obj)

        _obj = V1ComputeSecurityCashFlowsRequest.parse_obj({
            "asset_id": obj.get("assetId"),
            "valuation_config": V1SecurityValuationConfig.from_dict(obj.get("valuationConfig")) if obj.get("valuationConfig") is not None else None,
            "cashflows_request_config": V1SecurityCashFlowsRequestConfig.from_dict(obj.get("cashflowsRequestConfig")) if obj.get("cashflowsRequestConfig") is not None else None
        })
        return _obj

