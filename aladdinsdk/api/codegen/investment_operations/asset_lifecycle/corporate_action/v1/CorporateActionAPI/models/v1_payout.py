# coding: utf-8

"""
    Aladdin Corporate Action

    A corporate action is an event triggered by a public company that changes an equity or fixed income security issued by the company. There are two main categories - Mandatory and Voluntary.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.CorporateActionAPI.models.v1_payout_type import V1PayoutType

class V1Payout(BaseModel):
    """
    V1Payout
    """
    asset_id: Optional[StrictStr] = Field(None, alias="assetId")
    payout_amount: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="payoutAmount", description="Cash amount paid out.")
    payout_amount_currency_code: Optional[StrictStr] = Field(None, alias="payoutAmountCurrencyCode", description="Currency of the amount paid out.")
    payout_price: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="payoutPrice", description="Amount to participate in a corporate action.")
    payout_price_currency_code: Optional[StrictStr] = Field(None, alias="payoutPriceCurrencyCode", description="Currency of the amount needed to participate in a corporate action.")
    payout_rate: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="payoutRate", description="Ratio of security payout based on shares owned.")
    payout_type: Optional[V1PayoutType] = Field(None, alias="payoutType")
    __properties = ["assetId", "payoutAmount", "payoutAmountCurrencyCode", "payoutPrice", "payoutPriceCurrencyCode", "payoutRate", "payoutType"]

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
    def from_json(cls, json_str: str) -> V1Payout:
        """Create an instance of V1Payout from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1Payout:
        """Create an instance of V1Payout from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1Payout.parse_obj(obj)

        _obj = V1Payout.parse_obj({
            "asset_id": obj.get("assetId"),
            "payout_amount": obj.get("payoutAmount"),
            "payout_amount_currency_code": obj.get("payoutAmountCurrencyCode"),
            "payout_price": obj.get("payoutPrice"),
            "payout_price_currency_code": obj.get("payoutPriceCurrencyCode"),
            "payout_rate": obj.get("payoutRate"),
            "payout_type": obj.get("payoutType")
        })
        return _obj

