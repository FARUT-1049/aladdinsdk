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





class V1CorporateActionValidationSeverity(str, Enum):
    """
    Severity describes whether the validation is a warning or an error.   - CORPORATE_ACTION_VALIDATION_SEVERITY_UNSPECIFIED: Default value.  - CORPORATE_ACTION_VALIDATION_SEVERITY_WARNING: Warning.  - CORPORATE_ACTION_VALIDATION_SEVERITY_ERROR: Error.
    """

    """
    allowed enum values
    """
    CORPORATE_ACTION_VALIDATION_SEVERITY_UNSPECIFIED = 'CORPORATE_ACTION_VALIDATION_SEVERITY_UNSPECIFIED'
    CORPORATE_ACTION_VALIDATION_SEVERITY_WARNING = 'CORPORATE_ACTION_VALIDATION_SEVERITY_WARNING'
    CORPORATE_ACTION_VALIDATION_SEVERITY_ERROR = 'CORPORATE_ACTION_VALIDATION_SEVERITY_ERROR'

    @classmethod
    def from_json(cls, json_str: str) -> V1CorporateActionValidationSeverity:
        """Create an instance of V1CorporateActionValidationSeverity from a JSON string"""
        return V1CorporateActionValidationSeverity(json.loads(json_str))

