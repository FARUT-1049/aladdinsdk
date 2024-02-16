# coding: utf-8

"""
    Account Info

    API contains operations on Account Info resource.  # noqa: E501

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
from aladdinsdk.api.codegen.investment_operations.reference_data.account_info.v1.AccountInfoAPI.models.v1_account_info import V1AccountInfo

class V1SearchAccountInfosResponse(BaseModel):
    """
    The response message for AccountInfoAPI.SearchAccountInfos.
    """
    account_infos: Optional[conlist(V1AccountInfo)] = Field(None, alias="accountInfos", description="Account Infos to be returned.")
    next_page_token: Optional[StrictStr] = Field(None, alias="nextPageToken", description="A token, which can be sent as 'page_token' to retrieve the next page(Pagination is not supported currently).")
    __properties = ["accountInfos", "nextPageToken"]

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
    def from_json(cls, json_str: str) -> V1SearchAccountInfosResponse:
        """Create an instance of V1SearchAccountInfosResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in account_infos (list)
        _items = []
        if self.account_infos:
            for _item in self.account_infos:
                if _item:
                    _items.append(_item.to_dict())
            _dict['accountInfos'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1SearchAccountInfosResponse:
        """Create an instance of V1SearchAccountInfosResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1SearchAccountInfosResponse.parse_obj(obj)

        _obj = V1SearchAccountInfosResponse.parse_obj({
            "account_infos": [V1AccountInfo.from_dict(_item) for _item in obj.get("accountInfos")] if obj.get("accountInfos") is not None else None,
            "next_page_token": obj.get("nextPageToken")
        })
        return _obj
