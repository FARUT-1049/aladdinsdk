# coding: utf-8

"""
    Positions

    API to retrieve and monitor managed positions for Start of Day Positions. Managed positions are positions enriched with additional context such as restrictions and substitutions.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class V2CreditType(str, Enum):
    """
    - CREDIT_TYPE_UNSPECIFIED: not specified issuer type - default  - CREDIT_TYPE_GUARANTOR: credit type guarantor  - CREDIT_TYPE_UNDERLIER: credit type underlier  - CREDIT_TYPE_ENHANCER: credit type enhancer
    """

    """
    allowed enum values
    """
    CREDIT_TYPE_UNSPECIFIED = 'CREDIT_TYPE_UNSPECIFIED'
    CREDIT_TYPE_GUARANTOR = 'CREDIT_TYPE_GUARANTOR'
    CREDIT_TYPE_UNDERLIER = 'CREDIT_TYPE_UNDERLIER'
    CREDIT_TYPE_ENHANCER = 'CREDIT_TYPE_ENHANCER'

    @classmethod
    def from_json(cls, json_str: str) -> V2CreditType:
        """Create an instance of V2CreditType from a JSON string"""
        return V2CreditType(json.loads(json_str))

