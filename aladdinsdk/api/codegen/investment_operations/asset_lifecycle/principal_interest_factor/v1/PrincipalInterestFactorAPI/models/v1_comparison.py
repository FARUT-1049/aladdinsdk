# coding: utf-8

"""
    Principal and Interest Factor

    Principal and Interest Factors (PIFs) generally represent the amount of payment per 1000 of Original Face currency units value you currently hold in the given asset, and are used in conjunction with position data to generate cashflows. This API allows for filtering and retrieval of PIF records based on a number of criteria including assetId, dates, security groups, currency and more.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class V1Comparison(str, Enum):
    """
    Comparison operators compare two operands and yield a boolean value. Unlike in most programming languages, field names must appear on the left-hand side of a comparison operator; the right-hand side only accepts literals and logical operators.   - COMPARISON_UNSPECIFIED: Default value  - COMPARISON_LESS_EQUALS: The given `field` is less than the given `value`.  - COMPARISON_LESS_THAN: The given `field` is less than or equal to the given `value`.  - COMPARISON_GREATER_EQUALS: The given `field` is greater than or equal to the given `value`.  - COMPARISON_GREATER_THAN: The given `field` is greater than the given `value`.  - COMPARISON_NOT_EQUALS: The given `field` is not equal to the given `value`.  - COMPARISON_EQUALS: The given `field` is equal to the given `value`.
    """

    """
    allowed enum values
    """
    COMPARISON_UNSPECIFIED = 'COMPARISON_UNSPECIFIED'
    COMPARISON_LESS_EQUALS = 'COMPARISON_LESS_EQUALS'
    COMPARISON_LESS_THAN = 'COMPARISON_LESS_THAN'
    COMPARISON_GREATER_EQUALS = 'COMPARISON_GREATER_EQUALS'
    COMPARISON_GREATER_THAN = 'COMPARISON_GREATER_THAN'
    COMPARISON_NOT_EQUALS = 'COMPARISON_NOT_EQUALS'
    COMPARISON_EQUALS = 'COMPARISON_EQUALS'

    @classmethod
    def from_json(cls, json_str: str) -> V1Comparison:
        """Create an instance of V1Comparison from a JSON string"""
        return V1Comparison(json.loads(json_str))

