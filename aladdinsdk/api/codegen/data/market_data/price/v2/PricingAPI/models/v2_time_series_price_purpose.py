# coding: utf-8

"""
    Price

    This service offers the ability to retrieve security prices via specifying a price hierarchy or price purpose. This can be used to retrieve a single price for a specific date, time series of prices for a date range, or month-end prices for a date range.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from aladdinsdk.api.codegen.data.market_data.price.v2.PricingAPI.models.v2_time_series_price_request import V2TimeSeriesPriceRequest

class V2TimeSeriesPricePurpose(BaseModel):
    """
    V2TimeSeriesPricePurpose
    """
    time_series_asset_price: Optional[V2TimeSeriesPriceRequest] = Field(None, alias="timeSeriesAssetPrice")
    purpose: Optional[StrictStr] = None
    __properties = ["timeSeriesAssetPrice", "purpose"]

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
    def from_json(cls, json_str: str) -> V2TimeSeriesPricePurpose:
        """Create an instance of V2TimeSeriesPricePurpose from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of time_series_asset_price
        if self.time_series_asset_price:
            _dict['timeSeriesAssetPrice'] = self.time_series_asset_price.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V2TimeSeriesPricePurpose:
        """Create an instance of V2TimeSeriesPricePurpose from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V2TimeSeriesPricePurpose.parse_obj(obj)

        _obj = V2TimeSeriesPricePurpose.parse_obj({
            "time_series_asset_price": V2TimeSeriesPriceRequest.from_dict(obj.get("timeSeriesAssetPrice")) if obj.get("timeSeriesAssetPrice") is not None else None,
            "purpose": obj.get("purpose")
        })
        return _obj
