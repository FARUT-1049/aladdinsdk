# coding: utf-8

"""
    Compliance Levels

    Retrieves start-of-day and intraday Compliance levels across portfolio and portfolio groups.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist
from aladdinsdk.api.codegen.compliance.state.level.v1.LevelAPI.models.enums_compliance_rule_state import EnumsComplianceRuleState

class V1LevelFilter(BaseModel):
    """
    V1LevelFilter
    """
    portfolio_ticker: StrictStr = Field(..., alias="portfolioTicker", description="A shorthand name which this portfolio was assigned in Aladdin. This is a mandatory field.")
    include_portfolio_group_result: Optional[StrictBool] = Field(None, alias="includePortfolioGroupResult", description="When set to true, results returned will be limited to rules assigned directly to the portfolio or portfolio group provided, and exclude rules assigned to underlying portfolios.")
    level_date: Optional[date] = Field(None, alias="levelDate", description="Date parameter to retrieve historical data. No supplied value will return the most recent data.")
    rule_assignment_ids: Optional[conlist(StrictInt)] = Field(None, alias="ruleAssignmentIds", description="Unique primary key identifiers of an Aladdin rule assignment.")
    rule_ids: Optional[conlist(StrictInt)] = Field(None, alias="ruleIds", description="Id associated with the rules.")
    condition_state: Optional[StrictBool] = Field(None, alias="conditionState", description="Indicates the rule's state. If the rule is in violation condition state will be false otherwise it will return true.")
    groups: Optional[conlist(StrictStr)] = Field(None, description="This is a search parameter to filter down results to specific groups. Groups should be provided in array-format, e.g. ['USD','GBP','JPY'].")
    compliance_rule_state: Optional[EnumsComplianceRuleState] = Field(None, alias="complianceRuleState")
    as_traded: Optional[StrictBool] = Field(None, alias="asTraded")
    __properties = ["portfolioTicker", "includePortfolioGroupResult", "levelDate", "ruleAssignmentIds", "ruleIds", "conditionState", "groups", "complianceRuleState", "asTraded"]

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
    def from_json(cls, json_str: str) -> V1LevelFilter:
        """Create an instance of V1LevelFilter from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1LevelFilter:
        """Create an instance of V1LevelFilter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1LevelFilter.parse_obj(obj)

        _obj = V1LevelFilter.parse_obj({
            "portfolio_ticker": obj.get("portfolioTicker"),
            "include_portfolio_group_result": obj.get("includePortfolioGroupResult"),
            "level_date": obj.get("levelDate"),
            "rule_assignment_ids": obj.get("ruleAssignmentIds"),
            "rule_ids": obj.get("ruleIds"),
            "condition_state": obj.get("conditionState"),
            "groups": obj.get("groups"),
            "compliance_rule_state": obj.get("complianceRuleState"),
            "as_traded": obj.get("asTraded")
        })
        return _obj
