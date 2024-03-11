# coding: utf-8

"""
    Compliance Rule

    Compliance Rules are used to automatically monitor whether a fund adheres to a regulation, client mandate, or internal guideline.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr
from aladdinsdk.api.codegen.compliance.state.compliance_rule.v1.ComplianceRuleAPI.models.enums_compliance_severity import EnumsComplianceSeverity
from aladdinsdk.api.codegen.compliance.state.compliance_rule.v1.ComplianceRuleAPI.models.v1_abacus_mode import V1AbacusMode
from aladdinsdk.api.codegen.compliance.state.compliance_rule.v1.ComplianceRuleAPI.models.v1_disaggregate_positions import V1DisaggregatePositions

class V1ProhibitionRule(BaseModel):
    """
    ProhibitionRule Rule type.
    """
    severity: Optional[EnumsComplianceSeverity] = None
    filter: StrictStr = Field(..., description="The rule's filter is the condition, which identifies the securities that are subject to the rule's test.")
    run_overnight: StrictBool = Field(..., alias="runOvernight", description="The rule's run_overnight field instructs the system that rule should be applied overnight.")
    run_intraday: StrictBool = Field(..., alias="runIntraday", description="The rule's run_intraday field instructs the system that rule should be applied intraday.")
    manual: Optional[StrictBool] = Field(None, description="A Boolean flag identifying that a compliance guideline is implemented manually.")
    settled_positions_only: Optional[StrictBool] = Field(None, alias="settledPositionsOnly", description="A Boolean flag to remove positions that have yet to settle from rule evaluation on an overnight basis.")
    include_non_investment_position: Optional[StrictBool] = Field(None, alias="includeNonInvestmentPosition", description="A Boolean flag to include non-investment positions such as collateral and security lending positions.")
    suppress_violation: Optional[StrictBool] = Field(None, alias="suppressViolation", description="A Boolean flag that indicates that violations on positions of zero will be suppressed.")
    disaggregate_positions: Optional[V1DisaggregatePositions] = Field(None, alias="disaggregatePositions")
    abacus_mode: Optional[V1AbacusMode] = Field(None, alias="abacusMode")
    disable_directionality: Optional[StrictBool] = Field(None, alias="disableDirectionality")
    __properties = ["severity", "filter", "runOvernight", "runIntraday", "manual", "settledPositionsOnly", "includeNonInvestmentPosition", "suppressViolation", "disaggregatePositions", "abacusMode", "disableDirectionality"]

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
    def from_json(cls, json_str: str) -> V1ProhibitionRule:
        """Create an instance of V1ProhibitionRule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1ProhibitionRule:
        """Create an instance of V1ProhibitionRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1ProhibitionRule.parse_obj(obj)

        _obj = V1ProhibitionRule.parse_obj({
            "severity": obj.get("severity"),
            "filter": obj.get("filter"),
            "run_overnight": obj.get("runOvernight"),
            "run_intraday": obj.get("runIntraday"),
            "manual": obj.get("manual"),
            "settled_positions_only": obj.get("settledPositionsOnly"),
            "include_non_investment_position": obj.get("includeNonInvestmentPosition"),
            "suppress_violation": obj.get("suppressViolation"),
            "disaggregate_positions": obj.get("disaggregatePositions"),
            "abacus_mode": obj.get("abacusMode"),
            "disable_directionality": obj.get("disableDirectionality")
        })
        return _obj

