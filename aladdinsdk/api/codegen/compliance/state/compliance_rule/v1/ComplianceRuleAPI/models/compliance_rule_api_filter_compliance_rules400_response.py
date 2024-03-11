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



from pydantic import BaseModel, Field, StrictStr, constr

class ComplianceRuleAPIFilterComplianceRules400Response(BaseModel):
    """
    Defines an error that occurred.
    """
    code: constr(strict=True, max_length=40) = Field(..., description="A short mnemonic reference code for the error.")
    message: StrictStr = Field(..., description="A human readable description of the error.")
    __properties = ["code", "message"]

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
    def from_json(cls, json_str: str) -> ComplianceRuleAPIFilterComplianceRules400Response:
        """Create an instance of ComplianceRuleAPIFilterComplianceRules400Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ComplianceRuleAPIFilterComplianceRules400Response:
        """Create an instance of ComplianceRuleAPIFilterComplianceRules400Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ComplianceRuleAPIFilterComplianceRules400Response.parse_obj(obj)

        _obj = ComplianceRuleAPIFilterComplianceRules400Response.parse_obj({
            "code": obj.get("code"),
            "message": obj.get("message")
        })
        return _obj

