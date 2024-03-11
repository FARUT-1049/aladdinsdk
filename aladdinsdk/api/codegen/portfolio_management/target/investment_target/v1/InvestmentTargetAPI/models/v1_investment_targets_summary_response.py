# coding: utf-8

"""
    Aladdin Investment Target

    This service provides advance capabilities to create and manage all types of Aladdin Investment Targets and their associated subscriptions.  # noqa: E501

    The version of the OpenAPI document: 1.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, conlist
from aladdinsdk.api.codegen.portfolio_management.target.investment_target.v1.InvestmentTargetAPI.models.rpc_status import RpcStatus
from aladdinsdk.api.codegen.portfolio_management.target.investment_target.v1.InvestmentTargetAPI.models.v1_investment_target_response import V1InvestmentTargetResponse

class V1InvestmentTargetsSummaryResponse(BaseModel):
    """
    V1InvestmentTargetsSummaryResponse
    """
    investment_target_responses: conlist(V1InvestmentTargetResponse) = Field(..., alias="investmentTargetResponses")
    final_response_status: Optional[RpcStatus] = Field(None, alias="finalResponseStatus")
    __properties = ["investmentTargetResponses", "finalResponseStatus"]

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
    def from_json(cls, json_str: str) -> V1InvestmentTargetsSummaryResponse:
        """Create an instance of V1InvestmentTargetsSummaryResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in investment_target_responses (list)
        _items = []
        if self.investment_target_responses:
            for _item in self.investment_target_responses:
                if _item:
                    _items.append(_item.to_dict())
            _dict['investmentTargetResponses'] = _items
        # override the default output from pydantic by calling `to_dict()` of final_response_status
        if self.final_response_status:
            _dict['finalResponseStatus'] = self.final_response_status.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1InvestmentTargetsSummaryResponse:
        """Create an instance of V1InvestmentTargetsSummaryResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1InvestmentTargetsSummaryResponse.parse_obj(obj)

        _obj = V1InvestmentTargetsSummaryResponse.parse_obj({
            "investment_target_responses": [V1InvestmentTargetResponse.from_dict(_item) for _item in obj.get("investmentTargetResponses")] if obj.get("investmentTargetResponses") is not None else None,
            "final_response_status": RpcStatus.from_dict(obj.get("finalResponseStatus")) if obj.get("finalResponseStatus") is not None else None
        })
        return _obj

