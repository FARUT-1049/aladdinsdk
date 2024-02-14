# coding: utf-8

"""
    Risk Governance - Custom Evaluation Metric

    Upload or Retreive Custom Evaluation Metric to be used for Rule evaluation in Risk Radar.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date

from pydantic import BaseModel, Field, StrictStr

class V1QueryRiskCustomEvaluationMetricRequest(BaseModel):
    """
    V1QueryRiskCustomEvaluationMetricRequest
    """
    scope_id: StrictStr = Field(..., alias="scopeId")
    scope_type: StrictStr = Field(..., alias="scopeType")
    entity_id: StrictStr = Field(..., alias="entityId")
    entity_type: StrictStr = Field(..., alias="entityType")
    metric: StrictStr = Field(...)
    as_of_date: date = Field(..., alias="asOfDate", description="The effective date for the custom evaluation metric record being pulled.")
    __properties = ["scopeId", "scopeType", "entityId", "entityType", "metric", "asOfDate"]

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
    def from_json(cls, json_str: str) -> V1QueryRiskCustomEvaluationMetricRequest:
        """Create an instance of V1QueryRiskCustomEvaluationMetricRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1QueryRiskCustomEvaluationMetricRequest:
        """Create an instance of V1QueryRiskCustomEvaluationMetricRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1QueryRiskCustomEvaluationMetricRequest.parse_obj(obj)

        _obj = V1QueryRiskCustomEvaluationMetricRequest.parse_obj({
            "scope_id": obj.get("scopeId"),
            "scope_type": obj.get("scopeType"),
            "entity_id": obj.get("entityId"),
            "entity_type": obj.get("entityType"),
            "metric": obj.get("metric"),
            "as_of_date": obj.get("asOfDate")
        })
        return _obj

