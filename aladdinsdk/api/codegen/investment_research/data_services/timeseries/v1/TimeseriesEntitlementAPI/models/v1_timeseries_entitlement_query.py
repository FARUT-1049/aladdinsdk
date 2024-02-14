# coding: utf-8

"""
    Timeseries Entitlement

    Timeseries entitlement offers the capability to assign, remove and lookup entitlements for each timeseries data.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from aladdinsdk.api.codegen.investment_research.data_services.timeseries.v1.TimeseriesEntitlementAPI.models.timeseriesv1_access_type import Timeseriesv1AccessType

class V1TimeseriesEntitlementQuery(BaseModel):
    """
    The query required to perform a search query.
    """
    timeseries_ids: Optional[conlist(StrictStr)] = Field(None, alias="timeseriesIds")
    entitlements: Optional[conlist(StrictStr)] = None
    access_type: Optional[Timeseriesv1AccessType] = Field(None, alias="accessType")
    __properties = ["timeseriesIds", "entitlements", "accessType"]

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
    def from_json(cls, json_str: str) -> V1TimeseriesEntitlementQuery:
        """Create an instance of V1TimeseriesEntitlementQuery from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1TimeseriesEntitlementQuery:
        """Create an instance of V1TimeseriesEntitlementQuery from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1TimeseriesEntitlementQuery.parse_obj(obj)

        _obj = V1TimeseriesEntitlementQuery.parse_obj({
            "timeseries_ids": obj.get("timeseriesIds"),
            "entitlements": obj.get("entitlements"),
            "access_type": obj.get("accessType")
        })
        return _obj

