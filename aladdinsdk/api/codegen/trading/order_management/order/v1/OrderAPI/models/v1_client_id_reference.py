# coding: utf-8

"""
    Order

    Filter, post or cancel orders. An order is a directive from a portfolio manager to the trading desk to execute a particular investment decision.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class V1ClientIdReference(BaseModel):
    """
    The client ID reference used for resolving assets via a security reference type that is not in the regular types as defined in OrderAssetReference.
    """
    client_id: Optional[StrictStr] = Field(None, alias="clientId")
    alias_code: Optional[StrictStr] = Field(None, alias="aliasCode", description="Code of the organisation or account where the identifier is assigned from. Please refer to Aladdin Support for the list of valid codes.")
    alias_purpose: Optional[StrictStr] = Field(None, alias="aliasPurpose", description="The purpose field is an additional tag to the alias code for mapping this ID reference. Please refer to Aladdin Support for the list of associated values.")
    __properties = ["clientId", "aliasCode", "aliasPurpose"]

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
    def from_json(cls, json_str: str) -> V1ClientIdReference:
        """Create an instance of V1ClientIdReference from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1ClientIdReference:
        """Create an instance of V1ClientIdReference from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1ClientIdReference.parse_obj(obj)

        _obj = V1ClientIdReference.parse_obj({
            "client_id": obj.get("clientId"),
            "alias_code": obj.get("aliasCode"),
            "alias_purpose": obj.get("aliasPurpose")
        })
        return _obj
