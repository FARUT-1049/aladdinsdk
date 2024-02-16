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





class V1NamedTimePeriod(str, Enum):
    """
    Enum for the supported named periods.  The time period will be calculated automattically given the date in the request.   - NAMED_TIME_PERIOD_UNSPECIFIED: If the unspecified is used the default of business day will be used.  - NAMED_TIME_PERIOD_BUSINESS_DAY: Time period for one business day.  This will incude weekend or holidays.  - NAMED_TIME_PERIOD_PREVIOUS_MONTH: The previous month for the given date in the request.  - NAMED_TIME_PERIOD_PREVIOUS_QUARTER: The previous quarter for the given date in the request.  - NAMED_TIME_PERIOD_FISCAL_YEAR: Depending on the fiscal year settings for the portfolio.
    """

    """
    allowed enum values
    """
    NAMED_TIME_PERIOD_UNSPECIFIED = 'NAMED_TIME_PERIOD_UNSPECIFIED'
    NAMED_TIME_PERIOD_BUSINESS_DAY = 'NAMED_TIME_PERIOD_BUSINESS_DAY'
    NAMED_TIME_PERIOD_PREVIOUS_MONTH = 'NAMED_TIME_PERIOD_PREVIOUS_MONTH'
    NAMED_TIME_PERIOD_PREVIOUS_QUARTER = 'NAMED_TIME_PERIOD_PREVIOUS_QUARTER'
    NAMED_TIME_PERIOD_FISCAL_YEAR = 'NAMED_TIME_PERIOD_FISCAL_YEAR'

    @classmethod
    def from_json(cls, json_str: str) -> V1NamedTimePeriod:
        """Create an instance of V1NamedTimePeriod from a JSON string"""
        return V1NamedTimePeriod(json.loads(json_str))

