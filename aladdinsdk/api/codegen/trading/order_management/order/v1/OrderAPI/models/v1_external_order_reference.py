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

class V1ExternalOrderReference(BaseModel):
    """
    V1ExternalOrderReference
    """
    external_id1: Optional[StrictStr] = Field(None, alias="externalId1", description="First external order number. A limit of 64 characters is applied.")
    external_id2: Optional[StrictStr] = Field(None, alias="externalId2", description="Second external order number. A limit of 64 characters is applied.")
    account_code: Optional[StrictStr] = Field(None, alias="accountCode", description="Aladdin's unique account code/ID for an organization or system (e.g. an external broker or counterparty). Also known as \"org_id\" to some legacy systems.")
    __properties = ["externalId1", "externalId2", "accountCode"]

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
    def from_json(cls, json_str: str) -> V1ExternalOrderReference:
        """Create an instance of V1ExternalOrderReference from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1ExternalOrderReference:
        """Create an instance of V1ExternalOrderReference from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1ExternalOrderReference.parse_obj(obj)

        _obj = V1ExternalOrderReference.parse_obj({
            "external_id1": obj.get("externalId1"),
            "external_id2": obj.get("externalId2"),
            "account_code": obj.get("accountCode")
        })
        return _obj

