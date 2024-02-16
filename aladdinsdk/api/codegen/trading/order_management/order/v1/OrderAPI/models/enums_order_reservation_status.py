# coding: utf-8

"""
    Order

    Filter, post or cancel orders. An order is a directive from a portfolio manager to the trading desk to execute a particular investment decision.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class EnumsOrderReservationStatus(str, Enum):
    """
    - ORDER_RESERVATION_STATUS_UNSPECIFIED: Unspecified  - ORDER_RESERVATION_STATUS_PENDING: Code I  - ORDER_RESERVATION_STATUS_ACKNOWLEDGE: Code S  - ORDER_RESERVATION_STATUS_RESERVED: Code R  - ORDER_RESERVATION_STATUS_UNAVAILABLE: Code U  - ORDER_RESERVATION_STATUS_AVAILABLE: Code A  - ORDER_RESERVATION_STATUS_ERROR: Code E  - ORDER_RESERVATION_STATUS_CANCELLED: Code C  - ORDER_RESERVATION_STATUS_EXPIRED: Code X  - ORDER_RESERVATION_STATUS_PLACEHOLDER: Code P
    """

    """
    allowed enum values
    """
    ORDER_RESERVATION_STATUS_UNSPECIFIED = 'ORDER_RESERVATION_STATUS_UNSPECIFIED'
    ORDER_RESERVATION_STATUS_PENDING = 'ORDER_RESERVATION_STATUS_PENDING'
    ORDER_RESERVATION_STATUS_ACKNOWLEDGE = 'ORDER_RESERVATION_STATUS_ACKNOWLEDGE'
    ORDER_RESERVATION_STATUS_RESERVED = 'ORDER_RESERVATION_STATUS_RESERVED'
    ORDER_RESERVATION_STATUS_UNAVAILABLE = 'ORDER_RESERVATION_STATUS_UNAVAILABLE'
    ORDER_RESERVATION_STATUS_AVAILABLE = 'ORDER_RESERVATION_STATUS_AVAILABLE'
    ORDER_RESERVATION_STATUS_ERROR = 'ORDER_RESERVATION_STATUS_ERROR'
    ORDER_RESERVATION_STATUS_CANCELLED = 'ORDER_RESERVATION_STATUS_CANCELLED'
    ORDER_RESERVATION_STATUS_EXPIRED = 'ORDER_RESERVATION_STATUS_EXPIRED'
    ORDER_RESERVATION_STATUS_PLACEHOLDER = 'ORDER_RESERVATION_STATUS_PLACEHOLDER'

    @classmethod
    def from_json(cls, json_str: str) -> EnumsOrderReservationStatus:
        """Create an instance of EnumsOrderReservationStatus from a JSON string"""
        return EnumsOrderReservationStatus(json.loads(json_str))

