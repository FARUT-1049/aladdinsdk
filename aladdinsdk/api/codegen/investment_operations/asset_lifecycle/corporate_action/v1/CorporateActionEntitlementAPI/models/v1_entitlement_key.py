# coding: utf-8

"""
    Aladdin Corporate Action Entitlement

    API contains operations on Aladdin Corporate Action Entitlement resource.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictInt, StrictStr

class V1EntitlementKey(BaseModel):
    """
    Entitlement key uniquely identifies an entitlement. It is a combination of corporate action id, entitlement id and entitlement touch count.
    """
    entitlement_id: StrictStr = Field(..., alias="entitlementId", description="Entitlement Id.")
    corporate_action_id: StrictStr = Field(..., alias="corporateActionId", description="Corporate Action Id.")
    entitlement_touch_count: StrictInt = Field(..., alias="entitlementTouchCount", description="Entitlement touch count.")
    __properties = ["entitlementId", "corporateActionId", "entitlementTouchCount"]

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
    def from_json(cls, json_str: str) -> V1EntitlementKey:
        """Create an instance of V1EntitlementKey from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1EntitlementKey:
        """Create an instance of V1EntitlementKey from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1EntitlementKey.parse_obj(obj)

        _obj = V1EntitlementKey.parse_obj({
            "entitlement_id": obj.get("entitlementId"),
            "corporate_action_id": obj.get("corporateActionId"),
            "entitlement_touch_count": obj.get("entitlementTouchCount")
        })
        return _obj
