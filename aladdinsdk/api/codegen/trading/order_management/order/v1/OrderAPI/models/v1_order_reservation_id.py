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

from datetime import date
from typing import Optional
from pydantic import BaseModel, Field, StrictInt

class V1OrderReservationID(BaseModel):
    """
    V1OrderReservationID
    """
    order_detail_id: Optional[StrictInt] = Field(None, alias="orderDetailId")
    source: Optional[StrictInt] = None
    reservation_date: Optional[date] = Field(None, alias="reservationDate")
    __properties = ["orderDetailId", "source", "reservationDate"]

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
    def from_json(cls, json_str: str) -> V1OrderReservationID:
        """Create an instance of V1OrderReservationID from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1OrderReservationID:
        """Create an instance of V1OrderReservationID from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1OrderReservationID.parse_obj(obj)

        _obj = V1OrderReservationID.parse_obj({
            "order_detail_id": obj.get("orderDetailId"),
            "source": obj.get("source"),
            "reservation_date": obj.get("reservationDate")
        })
        return _obj
