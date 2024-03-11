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





class EnumsIndexGroup(str, Enum):
    """
    enum IndexGroup represents the index, for example, CDX, CMBX, ABX etc.   - INDEX_GROUP_UNSPECIFIED: UNSPECIFIED  - INDEX_GROUP_ABX: ABX  - INDEX_GROUP_CDX: CDX  - INDEX_GROUP_CMBX: CMBX  - INDEX_GROUP_ITRAXX: ITRAXX  - INDEX_GROUP_LCDX: LCDX  - INDEX_GROUP_MCDX: MCDX  - INDEX_GROUP_PRIMEX: PRIMEX
    """

    """
    allowed enum values
    """
    INDEX_GROUP_UNSPECIFIED = 'INDEX_GROUP_UNSPECIFIED'
    INDEX_GROUP_ABX = 'INDEX_GROUP_ABX'
    INDEX_GROUP_CDX = 'INDEX_GROUP_CDX'
    INDEX_GROUP_CMBX = 'INDEX_GROUP_CMBX'
    INDEX_GROUP_ITRAXX = 'INDEX_GROUP_ITRAXX'
    INDEX_GROUP_LCDX = 'INDEX_GROUP_LCDX'
    INDEX_GROUP_MCDX = 'INDEX_GROUP_MCDX'
    INDEX_GROUP_PRIMEX = 'INDEX_GROUP_PRIMEX'

    @classmethod
    def from_json(cls, json_str: str) -> EnumsIndexGroup:
        """Create an instance of EnumsIndexGroup from a JSON string"""
        return EnumsIndexGroup(json.loads(json_str))


