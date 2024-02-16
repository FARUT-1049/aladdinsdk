# coding: utf-8

"""
    Risk Governance - Rule Evaluation

    Trigger Rule evaluations for Rules created and subscribed to within Risk Radar.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictInt, conlist
from aladdinsdk.api.codegen.analytics.oversight.governance.v1.EvaluatorAnalyticsAPI.models.v1_risk_facet_search_list import V1RiskFacetSearchList
from aladdinsdk.api.codegen.analytics.oversight.governance.v1.EvaluatorAnalyticsAPI.models.v1_risk_navigation_links import V1RiskNavigationLinks
from aladdinsdk.api.codegen.analytics.oversight.governance.v1.EvaluatorAnalyticsAPI.models.v1_rule_evaluation import V1RuleEvaluation

class V1ListRuleEvaluationsResponse(BaseModel):
    """
    V1ListRuleEvaluationsResponse
    """
    navigation: Optional[V1RiskNavigationLinks] = None
    count: StrictInt = Field(...)
    total: StrictInt = Field(...)
    search_facets: Optional[Dict[str, V1RiskFacetSearchList]] = Field(None, alias="searchFacets")
    rule_evaluations: Optional[conlist(V1RuleEvaluation)] = Field(None, alias="ruleEvaluations")
    __properties = ["navigation", "count", "total", "searchFacets", "ruleEvaluations"]

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
    def from_json(cls, json_str: str) -> V1ListRuleEvaluationsResponse:
        """Create an instance of V1ListRuleEvaluationsResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of navigation
        if self.navigation:
            _dict['navigation'] = self.navigation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in search_facets (dict)
        _field_dict = {}
        if self.search_facets:
            for _key in self.search_facets:
                if self.search_facets[_key]:
                    _field_dict[_key] = self.search_facets[_key].to_dict()
            _dict['searchFacets'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each item in rule_evaluations (list)
        _items = []
        if self.rule_evaluations:
            for _item in self.rule_evaluations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ruleEvaluations'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1ListRuleEvaluationsResponse:
        """Create an instance of V1ListRuleEvaluationsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1ListRuleEvaluationsResponse.parse_obj(obj)

        _obj = V1ListRuleEvaluationsResponse.parse_obj({
            "navigation": V1RiskNavigationLinks.from_dict(obj.get("navigation")) if obj.get("navigation") is not None else None,
            "count": obj.get("count"),
            "total": obj.get("total"),
            "search_facets": dict(
                (_k, V1RiskFacetSearchList.from_dict(_v))
                for _k, _v in obj.get("searchFacets").items()
            )
            if obj.get("searchFacets") is not None
            else None,
            "rule_evaluations": [V1RuleEvaluation.from_dict(_item) for _item in obj.get("ruleEvaluations")] if obj.get("ruleEvaluations") is not None else None
        })
        return _obj
