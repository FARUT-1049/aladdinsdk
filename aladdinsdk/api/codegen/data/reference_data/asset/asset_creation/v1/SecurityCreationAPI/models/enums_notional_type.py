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





class EnumsNotionalType(str, Enum):
    """
    enum NotionalType represents if the notional principal is fixed or varies (refixed) over the term of the swap, for example, VARIABLE OR FIXED VARIABLE: Notional principal varies (amortizing) based on the unrealized gains or losses on the reset or payment date Fixed: Notional principal remains fixed throughout the term of the swap.   - NOTIONAL_TYPE_UNSPECIFIED: UNSPECIFIED  - NOTIONAL_TYPE_VARIABLE: VARIABLE  - NOTIONAL_TYPE_FIXED: FIXED
    """

    """
    allowed enum values
    """
    NOTIONAL_TYPE_UNSPECIFIED = 'NOTIONAL_TYPE_UNSPECIFIED'
    NOTIONAL_TYPE_VARIABLE = 'NOTIONAL_TYPE_VARIABLE'
    NOTIONAL_TYPE_FIXED = 'NOTIONAL_TYPE_FIXED'

    @classmethod
    def from_json(cls, json_str: str) -> EnumsNotionalType:
        """Create an instance of EnumsNotionalType from a JSON string"""
        return EnumsNotionalType(json.loads(json_str))


