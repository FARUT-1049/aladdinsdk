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


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr
from aladdinsdk.api.codegen.portfolio_management.target.investment_target.v1.InvestmentTargetAPI.models.v1_investment_targets_by_portfolios_query import V1InvestmentTargetsByPortfoliosQuery

class V1FilterInvestmentTargetsByPortfoliosRequest(BaseModel):
    """
    V1FilterInvestmentTargetsByPortfoliosRequest
    """
    investment_targets_by_portfolios_query: Optional[V1InvestmentTargetsByPortfoliosQuery] = Field(None, alias="investmentTargetsByPortfoliosQuery")
    page_size: Optional[StrictInt] = Field(None, alias="pageSize")
    page_token: Optional[StrictStr] = Field(None, alias="pageToken", description="A page token, received from a previous 'FilterInvestmentTargets' call. Provide this to retrieve the subsequent page.")
    __properties = ["investmentTargetsByPortfoliosQuery", "pageSize", "pageToken"]

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
    def from_json(cls, json_str: str) -> V1FilterInvestmentTargetsByPortfoliosRequest:
        """Create an instance of V1FilterInvestmentTargetsByPortfoliosRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of investment_targets_by_portfolios_query
        if self.investment_targets_by_portfolios_query:
            _dict['investmentTargetsByPortfoliosQuery'] = self.investment_targets_by_portfolios_query.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1FilterInvestmentTargetsByPortfoliosRequest:
        """Create an instance of V1FilterInvestmentTargetsByPortfoliosRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1FilterInvestmentTargetsByPortfoliosRequest.parse_obj(obj)

        _obj = V1FilterInvestmentTargetsByPortfoliosRequest.parse_obj({
            "investment_targets_by_portfolios_query": V1InvestmentTargetsByPortfoliosQuery.from_dict(obj.get("investmentTargetsByPortfoliosQuery")) if obj.get("investmentTargetsByPortfoliosQuery") is not None else None,
            "page_size": obj.get("pageSize"),
            "page_token": obj.get("pageToken")
        })
        return _obj
