# coding: utf-8

"""
    Portfolio Configuration Record For Accounting

    Configurations API for Aladdin Accounting allows you to access accounting configuration attributes for process types that portfolios are setup on. Data can be sourced in aggregate and filtered to improve oversight and scale of configuration monitoring. This API allows for retrieval of key data points for portfolio configurations by various parameters, including portfolio tickers, processCodes, and more.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class EnumsTickerExpansionType(str, Enum):
    """
    - TICKER_EXPANSION_TYPE_UNSPECIFIED: Default value  - TICKER_EXPANSION_TYPE_PORT_GROUP: The port group ticker  - TICKER_EXPANSION_TYPE_REPORTING_GROUP: The reporting group ticker
    """

    """
    allowed enum values
    """
    TICKER_EXPANSION_TYPE_UNSPECIFIED = 'TICKER_EXPANSION_TYPE_UNSPECIFIED'
    TICKER_EXPANSION_TYPE_PORT_GROUP = 'TICKER_EXPANSION_TYPE_PORT_GROUP'
    TICKER_EXPANSION_TYPE_REPORTING_GROUP = 'TICKER_EXPANSION_TYPE_REPORTING_GROUP'

    @classmethod
    def from_json(cls, json_str: str) -> EnumsTickerExpansionType:
        """Create an instance of EnumsTickerExpansionType from a JSON string"""
        return EnumsTickerExpansionType(json.loads(json_str))

