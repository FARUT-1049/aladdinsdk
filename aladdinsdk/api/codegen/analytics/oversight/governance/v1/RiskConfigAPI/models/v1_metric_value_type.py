# coding: utf-8

"""
    Risk Governance - Configuration

    Retrieve, update, and create configurations which drive Risk Governance behaviours and Risk Radar UI choices.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class V1MetricValueType(str, Enum):
    """
    - METRIC_VALUE_TYPE_UNSPECIFIED: value of custom evaluation metric type is not specefied  - METRIC_VALUE_TYPE_DOUBLE: value of custom evaluation metric type is decimal  - METRIC_VALUE_TYPE_INTEGER: value of custom evaluation metric type is whole number
    """

    """
    allowed enum values
    """
    METRIC_VALUE_TYPE_UNSPECIFIED = 'METRIC_VALUE_TYPE_UNSPECIFIED'
    METRIC_VALUE_TYPE_DOUBLE = 'METRIC_VALUE_TYPE_DOUBLE'
    METRIC_VALUE_TYPE_INTEGER = 'METRIC_VALUE_TYPE_INTEGER'

    @classmethod
    def from_json(cls, json_str: str) -> V1MetricValueType:
        """Create an instance of V1MetricValueType from a JSON string"""
        return V1MetricValueType(json.loads(json_str))

