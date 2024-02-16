# coding: utf-8

"""
    Order

    Filter, post or cancel orders. An order is a directive from a portfolio manager to the trading desk to execute a particular investment decision.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class EnumsCompliancePositionSource(str, Enum):
    """
    - COMPLIANCE_POSITION_SOURCE_UNSPECIFIED: Unspecified position source  - COMPLIANCE_POSITION_SOURCE_ORDER: The position source is order  - COMPLIANCE_POSITION_SOURCE_TRADE: The position source is trade  - COMPLIANCE_POSITION_SOURCE_POSITION: The position source is position  - COMPLIANCE_POSITION_SOURCE_NEW_CASH: The position source is new cash  - COMPLIANCE_POSITION_SOURCE_MISC_CASH: The position source is misc cash  - COMPLIANCE_POSITION_SOURCE_COMMITTED_CASH: The position source is committed cash
    """

    """
    allowed enum values
    """
    COMPLIANCE_POSITION_SOURCE_UNSPECIFIED = 'COMPLIANCE_POSITION_SOURCE_UNSPECIFIED'
    COMPLIANCE_POSITION_SOURCE_ORDER = 'COMPLIANCE_POSITION_SOURCE_ORDER'
    COMPLIANCE_POSITION_SOURCE_TRADE = 'COMPLIANCE_POSITION_SOURCE_TRADE'
    COMPLIANCE_POSITION_SOURCE_POSITION = 'COMPLIANCE_POSITION_SOURCE_POSITION'
    COMPLIANCE_POSITION_SOURCE_NEW_CASH = 'COMPLIANCE_POSITION_SOURCE_NEW_CASH'
    COMPLIANCE_POSITION_SOURCE_MISC_CASH = 'COMPLIANCE_POSITION_SOURCE_MISC_CASH'
    COMPLIANCE_POSITION_SOURCE_COMMITTED_CASH = 'COMPLIANCE_POSITION_SOURCE_COMMITTED_CASH'

    @classmethod
    def from_json(cls, json_str: str) -> EnumsCompliancePositionSource:
        """Create an instance of EnumsCompliancePositionSource from a JSON string"""
        return EnumsCompliancePositionSource(json.loads(json_str))

