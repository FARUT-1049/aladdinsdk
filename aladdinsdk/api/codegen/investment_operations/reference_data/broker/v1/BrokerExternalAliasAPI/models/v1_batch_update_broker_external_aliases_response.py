# coding: utf-8

"""
    Broker External Alias

    API contains operations on Broker External Alias resource.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, conlist
from aladdinsdk.api.codegen.investment_operations.reference_data.broker.v1.BrokerExternalAliasAPI.models.v1_broker_external_alias import V1BrokerExternalAlias

class V1BatchUpdateBrokerExternalAliasesResponse(BaseModel):
    """
    The response message for BrokerExternalAliasAPI.BatchUpdateBrokerExternalAliases.
    """
    broker_external_aliases: Optional[conlist(V1BrokerExternalAlias)] = Field(None, alias="brokerExternalAliases", description="Broker external aliases to be returned.")
    __properties = ["brokerExternalAliases"]

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
    def from_json(cls, json_str: str) -> V1BatchUpdateBrokerExternalAliasesResponse:
        """Create an instance of V1BatchUpdateBrokerExternalAliasesResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in broker_external_aliases (list)
        _items = []
        if self.broker_external_aliases:
            for _item in self.broker_external_aliases:
                if _item:
                    _items.append(_item.to_dict())
            _dict['brokerExternalAliases'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1BatchUpdateBrokerExternalAliasesResponse:
        """Create an instance of V1BatchUpdateBrokerExternalAliasesResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1BatchUpdateBrokerExternalAliasesResponse.parse_obj(obj)

        _obj = V1BatchUpdateBrokerExternalAliasesResponse.parse_obj({
            "broker_external_aliases": [V1BrokerExternalAlias.from_dict(_item) for _item in obj.get("brokerExternalAliases")] if obj.get("brokerExternalAliases") is not None else None
        })
        return _obj

