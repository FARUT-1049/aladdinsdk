# coding: utf-8

"""
    Risk Governance - Tasks

    Retrieve Tasks, as surfaced in Risk Radar, which are aggregates that comprise of related Exceptions, Rules, and Workflow items.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date, datetime
from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist
from aladdinsdk.api.codegen.analytics.oversight.governance.v1.RiskTaskAPI.models.v1_condition_definition import V1ConditionDefinition
from aladdinsdk.api.codegen.analytics.oversight.governance.v1.RiskTaskAPI.models.v1_evaluator import V1Evaluator
from aladdinsdk.api.codegen.analytics.oversight.governance.v1.RiskTaskAPI.models.v1_risk_rule_state import V1RiskRuleState
from aladdinsdk.api.codegen.analytics.oversight.governance.v1.RiskTaskAPI.models.v1_rule_setting import V1RuleSetting

class V1RiskRule(BaseModel):
    """
    V1RiskRule
    """
    id: Optional[StrictStr] = None
    evaluator: Optional[V1Evaluator] = None
    name: StrictStr = Field(...)
    tier_key: StrictStr = Field(..., alias="tierKey")
    conditions: Optional[conlist(V1ConditionDefinition)] = None
    split_exceptions: StrictBool = Field(..., alias="splitExceptions")
    priority: StrictInt = Field(...)
    rule_state: Optional[V1RiskRuleState] = Field(None, alias="ruleState")
    final_sign_off_author: Optional[StrictStr] = Field(None, alias="finalSignOffAuthor")
    final_sign_off_time: Optional[datetime] = Field(None, alias="finalSignOffTime")
    modifier: Optional[StrictStr] = None
    modify_time: Optional[datetime] = Field(None, alias="modifyTime")
    version: Optional[StrictStr] = None
    effective_date: Optional[date] = Field(None, alias="effectiveDate")
    category_key: Optional[StrictStr] = Field(None, alias="categoryKey")
    version_time: Optional[datetime] = Field(None, alias="versionTime")
    sub_category_key: Optional[StrictStr] = Field(None, alias="subCategoryKey")
    permission_scopes: Optional[conlist(StrictStr)] = Field(None, alias="permissionScopes")
    rule_setting: Optional[V1RuleSetting] = Field(None, alias="ruleSetting")
    __properties = ["id", "evaluator", "name", "tierKey", "conditions", "splitExceptions", "priority", "ruleState", "finalSignOffAuthor", "finalSignOffTime", "modifier", "modifyTime", "version", "effectiveDate", "categoryKey", "versionTime", "subCategoryKey", "permissionScopes", "ruleSetting"]

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
    def from_json(cls, json_str: str) -> V1RiskRule:
        """Create an instance of V1RiskRule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "version_time",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in conditions (list)
        _items = []
        if self.conditions:
            for _item in self.conditions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['conditions'] = _items
        # override the default output from pydantic by calling `to_dict()` of rule_setting
        if self.rule_setting:
            _dict['ruleSetting'] = self.rule_setting.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1RiskRule:
        """Create an instance of V1RiskRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1RiskRule.parse_obj(obj)

        _obj = V1RiskRule.parse_obj({
            "id": obj.get("id"),
            "evaluator": obj.get("evaluator"),
            "name": obj.get("name"),
            "tier_key": obj.get("tierKey"),
            "conditions": [V1ConditionDefinition.from_dict(_item) for _item in obj.get("conditions")] if obj.get("conditions") is not None else None,
            "split_exceptions": obj.get("splitExceptions"),
            "priority": obj.get("priority"),
            "rule_state": obj.get("ruleState"),
            "final_sign_off_author": obj.get("finalSignOffAuthor"),
            "final_sign_off_time": obj.get("finalSignOffTime"),
            "modifier": obj.get("modifier"),
            "modify_time": obj.get("modifyTime"),
            "version": obj.get("version"),
            "effective_date": obj.get("effectiveDate"),
            "category_key": obj.get("categoryKey"),
            "version_time": obj.get("versionTime"),
            "sub_category_key": obj.get("subCategoryKey"),
            "permission_scopes": obj.get("permissionScopes"),
            "rule_setting": V1RuleSetting.from_dict(obj.get("ruleSetting")) if obj.get("ruleSetting") is not None else None
        })
        return _obj

