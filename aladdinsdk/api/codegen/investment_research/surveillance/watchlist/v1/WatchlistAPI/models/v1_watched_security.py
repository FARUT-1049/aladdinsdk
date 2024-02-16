# coding: utf-8

"""
    Investment Watchlist

    Create, modify, delete, and retrieve watchlists; Add and remove securities from watchlist.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from aladdinsdk.api.codegen.investment_research.surveillance.watchlist.v1.WatchlistAPI.models.enums_research_asset_type import EnumsResearchAssetType

class V1WatchedSecurity(BaseModel):
    """
    V1WatchedSecurity
    """
    asset_id: Optional[StrictStr] = Field(None, alias="assetId")
    added_date: Optional[date] = Field(None, alias="addedDate")
    expiry_date: Optional[date] = Field(None, alias="expiryDate")
    pre_trade_note: Optional[StrictStr] = Field(None, alias="preTradeNote")
    asset_type: Optional[EnumsResearchAssetType] = Field(None, alias="assetType")
    __properties = ["assetId", "addedDate", "expiryDate", "preTradeNote", "assetType"]

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
    def from_json(cls, json_str: str) -> V1WatchedSecurity:
        """Create an instance of V1WatchedSecurity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1WatchedSecurity:
        """Create an instance of V1WatchedSecurity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1WatchedSecurity.parse_obj(obj)

        _obj = V1WatchedSecurity.parse_obj({
            "asset_id": obj.get("assetId"),
            "added_date": obj.get("addedDate"),
            "expiry_date": obj.get("expiryDate"),
            "pre_trade_note": obj.get("preTradeNote"),
            "asset_type": obj.get("assetType")
        })
        return _obj
