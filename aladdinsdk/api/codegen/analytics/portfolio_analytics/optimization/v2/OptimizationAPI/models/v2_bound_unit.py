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





class V2BoundUnit(str, Enum):
    """
    - BOUND_UNIT_UNSPECIFIED: value if bound_unit is not specified. The default behavior depends on constraint; currently trade increment defaults to shares but all other per-asset bounds default to portfolio fraction  - BOUND_UNIT_PORTFOLIO_FRACTION: portfolio fraction  - BOUND_UNIT_SHARE: number of shares  - BOUND_UNIT_MONETARY_VALUE: monetary value
    """

    """
    allowed enum values
    """
    BOUND_UNIT_UNSPECIFIED = 'BOUND_UNIT_UNSPECIFIED'
    BOUND_UNIT_PORTFOLIO_FRACTION = 'BOUND_UNIT_PORTFOLIO_FRACTION'
    BOUND_UNIT_SHARE = 'BOUND_UNIT_SHARE'
    BOUND_UNIT_MONETARY_VALUE = 'BOUND_UNIT_MONETARY_VALUE'

    @classmethod
    def from_json(cls, json_str: str) -> V2BoundUnit:
        """Create an instance of V2BoundUnit from a JSON string"""
        return V2BoundUnit(json.loads(json_str))

