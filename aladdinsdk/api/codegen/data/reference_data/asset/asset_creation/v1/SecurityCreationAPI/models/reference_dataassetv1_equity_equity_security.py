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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from aladdinsdk.api.codegen.data.reference_data.asset.asset_creation.v1.SecurityCreationAPI.models.enums_registration import EnumsRegistration
from aladdinsdk.api.codegen.data.reference_data.asset.asset_creation.v1.SecurityCreationAPI.models.v1_offering_data import V1OfferingData

class ReferenceDataassetv1EquityEquitySecurity(BaseModel):
    """
    ReferenceDataassetv1EquityEquitySecurity
    """
    ticker: StrictStr = Field(..., description="Ticker - An acronmyn for the security. It is often used to aid in the identification of a security.")
    name: StrictStr = Field(..., description="Name - This is a security descriptive field. It briefly describes the equity security.")
    currency_code: StrictStr = Field(..., alias="currencyCode", description="Currency - Represents USD, GBP etc.")
    country_code: StrictStr = Field(..., alias="countryCode", description="Country Code - Represents US, UK etc.")
    exchange: Optional[StrictStr] = Field(None, description="Equity Data - Primary Security Exchange code.")
    registration_flag: Optional[EnumsRegistration] = Field(None, alias="registrationFlag")
    lot_size: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="lotSize")
    asset_id: Optional[StrictStr] = Field(None, alias="assetId", description="Identifier corresponds to Aladdin identifier.")
    sedol: Optional[StrictStr] = Field(None, description="Public Identifier - The alternate identifier.")
    offering_info: Optional[V1OfferingData] = Field(None, alias="offeringInfo")
    counterparty: Optional[StrictStr] = None
    __properties = ["ticker", "name", "currencyCode", "countryCode", "exchange", "registrationFlag", "lotSize", "assetId", "sedol", "offeringInfo", "counterparty"]

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
    def from_json(cls, json_str: str) -> ReferenceDataassetv1EquityEquitySecurity:
        """Create an instance of ReferenceDataassetv1EquityEquitySecurity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of offering_info
        if self.offering_info:
            _dict['offeringInfo'] = self.offering_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReferenceDataassetv1EquityEquitySecurity:
        """Create an instance of ReferenceDataassetv1EquityEquitySecurity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ReferenceDataassetv1EquityEquitySecurity.parse_obj(obj)

        _obj = ReferenceDataassetv1EquityEquitySecurity.parse_obj({
            "ticker": obj.get("ticker"),
            "name": obj.get("name"),
            "currency_code": obj.get("currencyCode"),
            "country_code": obj.get("countryCode"),
            "exchange": obj.get("exchange"),
            "registration_flag": obj.get("registrationFlag"),
            "lot_size": obj.get("lotSize"),
            "asset_id": obj.get("assetId"),
            "sedol": obj.get("sedol"),
            "offering_info": V1OfferingData.from_dict(obj.get("offeringInfo")) if obj.get("offeringInfo") is not None else None,
            "counterparty": obj.get("counterparty")
        })
        return _obj

