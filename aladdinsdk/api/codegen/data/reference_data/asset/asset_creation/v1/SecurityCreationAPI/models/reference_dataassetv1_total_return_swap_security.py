# coding: utf-8

"""
    Security Creation

    This service is used to create CDS, CDX, Equity Equity, Equity Option, Futures, FX NDF, FX SPOT, FX FWRD, FX CSWAP, FX Option, Swap, Swaption, CASH/TD, CASH/REPO, ARM/TBA and MBS/TBA securities.  # noqa: E501

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
from aladdinsdk.api.codegen.data.reference_data.asset.asset_creation.v1.SecurityCreationAPI.models.v1_custom_schedule import V1CustomSchedule
from aladdinsdk.api.codegen.data.reference_data.asset.asset_creation.v1.SecurityCreationAPI.models.v1_income_fee import V1IncomeFee
from aladdinsdk.api.codegen.data.reference_data.asset.asset_creation.v1.SecurityCreationAPI.models.v1_swap_data import V1SwapData

class ReferenceDataassetv1TotalReturnSwapSecurity(BaseModel):
    """
    ReferenceDataassetv1TotalReturnSwapSecurity
    """
    swap_info: Optional[V1SwapData] = Field(None, alias="swapInfo")
    rec_leg_income_fee: Optional[V1IncomeFee] = Field(None, alias="recLegIncomeFee")
    rec_leg_custom_schedules: Optional[conlist(V1CustomSchedule)] = Field(None, alias="recLegCustomSchedules")
    pay_leg_custom_schedules: Optional[conlist(V1CustomSchedule)] = Field(None, alias="payLegCustomSchedules")
    counterparty: Optional[StrictStr] = None
    __properties = ["swapInfo", "recLegIncomeFee", "recLegCustomSchedules", "payLegCustomSchedules", "counterparty"]

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
    def from_json(cls, json_str: str) -> ReferenceDataassetv1TotalReturnSwapSecurity:
        """Create an instance of ReferenceDataassetv1TotalReturnSwapSecurity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of swap_info
        if self.swap_info:
            _dict['swapInfo'] = self.swap_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rec_leg_income_fee
        if self.rec_leg_income_fee:
            _dict['recLegIncomeFee'] = self.rec_leg_income_fee.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in rec_leg_custom_schedules (list)
        _items = []
        if self.rec_leg_custom_schedules:
            for _item in self.rec_leg_custom_schedules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['recLegCustomSchedules'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in pay_leg_custom_schedules (list)
        _items = []
        if self.pay_leg_custom_schedules:
            for _item in self.pay_leg_custom_schedules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['payLegCustomSchedules'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReferenceDataassetv1TotalReturnSwapSecurity:
        """Create an instance of ReferenceDataassetv1TotalReturnSwapSecurity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ReferenceDataassetv1TotalReturnSwapSecurity.parse_obj(obj)

        _obj = ReferenceDataassetv1TotalReturnSwapSecurity.parse_obj({
            "swap_info": V1SwapData.from_dict(obj.get("swapInfo")) if obj.get("swapInfo") is not None else None,
            "rec_leg_income_fee": V1IncomeFee.from_dict(obj.get("recLegIncomeFee")) if obj.get("recLegIncomeFee") is not None else None,
            "rec_leg_custom_schedules": [V1CustomSchedule.from_dict(_item) for _item in obj.get("recLegCustomSchedules")] if obj.get("recLegCustomSchedules") is not None else None,
            "pay_leg_custom_schedules": [V1CustomSchedule.from_dict(_item) for _item in obj.get("payLegCustomSchedules")] if obj.get("payLegCustomSchedules") is not None else None,
            "counterparty": obj.get("counterparty")
        })
        return _obj
