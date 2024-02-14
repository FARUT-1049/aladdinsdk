# coding: utf-8

"""
    Security Analytics Compute

    Compute security level analytics, cash flows and scenario analytics with custom valuation settings.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class V1CashFlowsResultType(str, Enum):
    """
    - CASH_FLOWS_RESULT_TYPE_UNSPECIFIED: No cashflow response data type specified  - CASH_FLOWS_RESULT_TYPE_DEFAULT: Default cashflow response data type
    """

    """
    allowed enum values
    """
    CASH_FLOWS_RESULT_TYPE_UNSPECIFIED = 'CASH_FLOWS_RESULT_TYPE_UNSPECIFIED'
    CASH_FLOWS_RESULT_TYPE_DEFAULT = 'CASH_FLOWS_RESULT_TYPE_DEFAULT'

    @classmethod
    def from_json(cls, json_str: str) -> V1CashFlowsResultType:
        """Create an instance of V1CashFlowsResultType from a JSON string"""
        return V1CashFlowsResultType(json.loads(json_str))


