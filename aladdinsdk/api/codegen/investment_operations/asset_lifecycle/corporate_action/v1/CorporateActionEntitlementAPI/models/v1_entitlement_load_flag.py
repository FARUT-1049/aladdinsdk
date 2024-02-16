# coding: utf-8

"""
    Aladdin Corporate Action Entitlement

    API contains operations on Aladdin Corporate Action Entitlement resource.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class V1EntitlementLoadFlag(str, Enum):
    """
    Enumeration of corporate action entitlement load flag.   - ENTITLEMENT_LOAD_FLAG_UNSPECIFIED: The reserved value.  - ENTITLEMENT_LOAD_FLAG_DETAILS: DETAILS.  - ENTITLEMENT_LOAD_FLAG_EVENT: EVENT.  - ENTITLEMENT_LOAD_FLAG_ACCT_RESP: ACCT_RESP.  - ENTITLEMENT_LOAD_FLAG_INSTRUCTION: INSTRUCTION.  - ENTITLEMENT_LOAD_FLAG_EXT_CA_ID: EXT CA ID.  - ENTITLEMENT_LOAD_FLAG_SETTLEMENT: SETTLEMENT.  - ENTITLEMENT_LOAD_FLAG_RELATED_ENTITLEMENTS: RELATED ENTITLEMENTS.  - ENTITLEMENT_LOAD_FLAG_ADJUSTMENT: ADJUSTMENT.  - ENTITLEMENT_LOAD_FLAG_CUSTODIAN_ENTITLEMENTS: CUSTODIAN ENTITLEMENTS.  - ENTITLEMENT_LOAD_FLAG_RELATED_PORTFOLIO_ENTITLEMENTS: RELATED PORTFOLIO ENTITLEMENTS.
    """

    """
    allowed enum values
    """
    ENTITLEMENT_LOAD_FLAG_UNSPECIFIED = 'ENTITLEMENT_LOAD_FLAG_UNSPECIFIED'
    ENTITLEMENT_LOAD_FLAG_DETAILS = 'ENTITLEMENT_LOAD_FLAG_DETAILS'
    ENTITLEMENT_LOAD_FLAG_EVENT = 'ENTITLEMENT_LOAD_FLAG_EVENT'
    ENTITLEMENT_LOAD_FLAG_ACCT_RESP = 'ENTITLEMENT_LOAD_FLAG_ACCT_RESP'
    ENTITLEMENT_LOAD_FLAG_INSTRUCTION = 'ENTITLEMENT_LOAD_FLAG_INSTRUCTION'
    ENTITLEMENT_LOAD_FLAG_EXT_CA_ID = 'ENTITLEMENT_LOAD_FLAG_EXT_CA_ID'
    ENTITLEMENT_LOAD_FLAG_SETTLEMENT = 'ENTITLEMENT_LOAD_FLAG_SETTLEMENT'
    ENTITLEMENT_LOAD_FLAG_RELATED_ENTITLEMENTS = 'ENTITLEMENT_LOAD_FLAG_RELATED_ENTITLEMENTS'
    ENTITLEMENT_LOAD_FLAG_ADJUSTMENT = 'ENTITLEMENT_LOAD_FLAG_ADJUSTMENT'
    ENTITLEMENT_LOAD_FLAG_CUSTODIAN_ENTITLEMENTS = 'ENTITLEMENT_LOAD_FLAG_CUSTODIAN_ENTITLEMENTS'
    ENTITLEMENT_LOAD_FLAG_RELATED_PORTFOLIO_ENTITLEMENTS = 'ENTITLEMENT_LOAD_FLAG_RELATED_PORTFOLIO_ENTITLEMENTS'

    @classmethod
    def from_json(cls, json_str: str) -> V1EntitlementLoadFlag:
        """Create an instance of V1EntitlementLoadFlag from a JSON string"""
        return V1EntitlementLoadFlag(json.loads(json_str))

