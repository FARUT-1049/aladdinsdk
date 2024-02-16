# coding: utf-8

"""
    Cashflows

    This API allows users to create, update and cancel miscellaneous cashflows. There are three endpoints to create, update, and cancel cashflows with SSI, and three other endpoints to create, update, and cancel cashflows without SSI. For full details on this API including permissions required and sample calls, please check out the Cashflows API Release Note available in the Release Note section on Studio or on your client site homepage.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class V1TransactionType(str, Enum):
    """
    - TRANSACTION_TYPE_UNSPECIFIED: unspecified  - TRANSACTION_TYPE_MISC: Miscellaneous
    """

    """
    allowed enum values
    """
    TRANSACTION_TYPE_UNSPECIFIED = 'TRANSACTION_TYPE_UNSPECIFIED'
    TRANSACTION_TYPE_MISC = 'TRANSACTION_TYPE_MISC'

    @classmethod
    def from_json(cls, json_str: str) -> V1TransactionType:
        """Create an instance of V1TransactionType from a JSON string"""
        return V1TransactionType(json.loads(json_str))

