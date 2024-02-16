# coding: utf-8

"""
    Portfolio Analytics

    Generate Portfolio Analytics.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class V1IlliquidType(str, Enum):
    """
    - ILLIQUID_TYPE_UNSPECIFIED: unspecified  - ILLIQUID_TYPE_ABSOLUTE: Absolute value  - ILLIQUID_TYPE_RELATIVE: Relative
    """

    """
    allowed enum values
    """
    ILLIQUID_TYPE_UNSPECIFIED = 'ILLIQUID_TYPE_UNSPECIFIED'
    ILLIQUID_TYPE_ABSOLUTE = 'ILLIQUID_TYPE_ABSOLUTE'
    ILLIQUID_TYPE_RELATIVE = 'ILLIQUID_TYPE_RELATIVE'

    @classmethod
    def from_json(cls, json_str: str) -> V1IlliquidType:
        """Create an instance of V1IlliquidType from a JSON string"""
        return V1IlliquidType(json.loads(json_str))

