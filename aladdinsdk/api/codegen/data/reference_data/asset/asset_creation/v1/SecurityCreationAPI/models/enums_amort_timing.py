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





class EnumsAmortTiming(str, Enum):
    """
    - AMORT_TIMING_UNSPECIFIED: UNSPECIFIED  - AMORT_TIMING_AT_FIXING: AT_FIXING  - AMORT_TIMING_AT_PAYMENT: AT_PAYMENT
    """

    """
    allowed enum values
    """
    AMORT_TIMING_UNSPECIFIED = 'AMORT_TIMING_UNSPECIFIED'
    AMORT_TIMING_AT_FIXING = 'AMORT_TIMING_AT_FIXING'
    AMORT_TIMING_AT_PAYMENT = 'AMORT_TIMING_AT_PAYMENT'

    @classmethod
    def from_json(cls, json_str: str) -> EnumsAmortTiming:
        """Create an instance of EnumsAmortTiming from a JSON string"""
        return EnumsAmortTiming(json.loads(json_str))


