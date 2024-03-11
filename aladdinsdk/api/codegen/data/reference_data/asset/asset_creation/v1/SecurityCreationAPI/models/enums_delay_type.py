# coding: utf-8

"""
    Security Creation

    This service is used to create CDS, CDX, Equity Equity, Equity Option, Futures, FX NDF, FX SPOT, FX FWRD, FX CSWAP, FX Option, Swap, Swaption, CASH/TD, CASH/REPO, ARM/TBA and MBS/TBA securities.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class EnumsDelayType(str, Enum):
    """
    - DELAY_TYPE_UNSPECIFIED: UNSPECIFIED  - DELAY_TYPE_BUSINESS: BUSINESS  - DELAY_TYPE_CALENDAR: CALENDAR
    """

    """
    allowed enum values
    """
    DELAY_TYPE_UNSPECIFIED = 'DELAY_TYPE_UNSPECIFIED'
    DELAY_TYPE_BUSINESS = 'DELAY_TYPE_BUSINESS'
    DELAY_TYPE_CALENDAR = 'DELAY_TYPE_CALENDAR'

    @classmethod
    def from_json(cls, json_str: str) -> EnumsDelayType:
        """Create an instance of EnumsDelayType from a JSON string"""
        return EnumsDelayType(json.loads(json_str))

