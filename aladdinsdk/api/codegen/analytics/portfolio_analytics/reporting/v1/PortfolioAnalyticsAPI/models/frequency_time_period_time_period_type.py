# coding: utf-8

"""
    Portfolio Analytics

    Generate Portfolio Analytics.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class FrequencyTimePeriodTimePeriodType(str, Enum):
    """
    The type of period the time period is for.   - TIME_PERIOD_TYPE_UNSPECIFIED: If unspecidied is used the default of fixed will be used.  - TIME_PERIOD_TYPE_FIXED: Fixed will use the start of the period.  For example a monthly fixed period will be for the month to date period.  - TIME_PERIOD_TYPE_ROLLING: Rolling will go back the number of whole periods.  For example a monthly rolling period will start from the same day in the previous month.
    """

    """
    allowed enum values
    """
    TIME_PERIOD_TYPE_UNSPECIFIED = 'TIME_PERIOD_TYPE_UNSPECIFIED'
    TIME_PERIOD_TYPE_FIXED = 'TIME_PERIOD_TYPE_FIXED'
    TIME_PERIOD_TYPE_ROLLING = 'TIME_PERIOD_TYPE_ROLLING'

    @classmethod
    def from_json(cls, json_str: str) -> FrequencyTimePeriodTimePeriodType:
        """Create an instance of FrequencyTimePeriodTimePeriodType from a JSON string"""
        return FrequencyTimePeriodTimePeriodType(json.loads(json_str))

