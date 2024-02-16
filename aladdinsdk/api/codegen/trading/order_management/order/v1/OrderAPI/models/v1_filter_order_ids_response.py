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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist

class V1FilterOrderIdsResponse(BaseModel):
    """
    V1FilterOrderIdsResponse
    """
    order_ids: Optional[conlist(StrictStr)] = Field(None, alias="orderIds")
    next_page_token: Optional[StrictStr] = Field(None, alias="nextPageToken", description="A token, which can be sent as 'pageToken' to retrieve the next page. If this field is omitted, there are no subsequent pages.")
    status: Optional[StrictStr] = None
    __properties = ["orderIds", "nextPageToken", "status"]

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
    def from_json(cls, json_str: str) -> V1FilterOrderIdsResponse:
        """Create an instance of V1FilterOrderIdsResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1FilterOrderIdsResponse:
        """Create an instance of V1FilterOrderIdsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1FilterOrderIdsResponse.parse_obj(obj)

        _obj = V1FilterOrderIdsResponse.parse_obj({
            "order_ids": obj.get("orderIds"),
            "next_page_token": obj.get("nextPageToken"),
            "status": obj.get("status")
        })
        return _obj
