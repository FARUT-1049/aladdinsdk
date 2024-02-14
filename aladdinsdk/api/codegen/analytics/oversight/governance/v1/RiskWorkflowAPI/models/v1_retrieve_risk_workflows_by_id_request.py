# coding: utf-8

"""
    Risk Governance - Workflows

    Retrieve, update, and transition Workflow items as surfaced in Risk Radar.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, StrictStr, conlist

class V1RetrieveRiskWorkflowsByIdRequest(BaseModel):
    """
    V1RetrieveRiskWorkflowsByIdRequest
    """
    workflow_ids: conlist(StrictStr) = Field(..., alias="workflowIds")
    __properties = ["workflowIds"]

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
    def from_json(cls, json_str: str) -> V1RetrieveRiskWorkflowsByIdRequest:
        """Create an instance of V1RetrieveRiskWorkflowsByIdRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1RetrieveRiskWorkflowsByIdRequest:
        """Create an instance of V1RetrieveRiskWorkflowsByIdRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1RetrieveRiskWorkflowsByIdRequest.parse_obj(obj)

        _obj = V1RetrieveRiskWorkflowsByIdRequest.parse_obj({
            "workflow_ids": obj.get("workflowIds")
        })
        return _obj

