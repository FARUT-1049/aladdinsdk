# coding: utf-8

"""
    Portfolio Optimization 2.0

    Optimize portfolio positions to maximize expected returns and minimize risk and transaction costs.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class BoundBoundStyle(str, Enum):
    """
    - BOUND_STYLE_UNSPECIFIED: value if bound_style is not specified. Will default to hard bound  - BOUND_STYLE_HARD: hard bound  - BOUND_STYLE_SOFT: soft bounds  - BOUND_STYLE_RELAXABLE: relaxable bounds
    """

    """
    allowed enum values
    """
    BOUND_STYLE_UNSPECIFIED = 'BOUND_STYLE_UNSPECIFIED'
    BOUND_STYLE_HARD = 'BOUND_STYLE_HARD'
    BOUND_STYLE_SOFT = 'BOUND_STYLE_SOFT'
    BOUND_STYLE_RELAXABLE = 'BOUND_STYLE_RELAXABLE'

    @classmethod
    def from_json(cls, json_str: str) -> BoundBoundStyle:
        """Create an instance of BoundBoundStyle from a JSON string"""
        return BoundBoundStyle(json.loads(json_str))

