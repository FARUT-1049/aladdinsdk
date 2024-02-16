# coding: utf-8

"""
    ESG Data

    The ESG Data API offers a centralized source of ESG data and meta data across multiple vendors. The API retrieves ESG data by asset and issuer from multiple vendors, providing the data in one digestible schema. Retrieve ESG data for selected assets and issuers by providing entity id, provider id, date(s) and measure name. Meta data on ESG data measures can be retrieved by selecting a provider, provider category and unique measure names. Time Series API in alpha version, changes may be made at any time.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class V1ReportFrequency(str, Enum):
    """
    - REPORT_FREQUENCY_UNSPECIFIED: Default Value - will return any data available in time range without any modifications  - REPORT_FREQUENCY_WEEKLY: Weekly - return data split into weeks based on the time range  - REPORT_FREQUENCY_MONTHLY: Monthly - return data split into months based on the time range  - REPORT_FREQUENCY_QUARTERLY: Quarterly - return data split into quarters based on the time range  - REPORT_FREQUENCY_ANNUALLY: Annually - return data split into years based on the time range
    """

    """
    allowed enum values
    """
    REPORT_FREQUENCY_UNSPECIFIED = 'REPORT_FREQUENCY_UNSPECIFIED'
    REPORT_FREQUENCY_WEEKLY = 'REPORT_FREQUENCY_WEEKLY'
    REPORT_FREQUENCY_MONTHLY = 'REPORT_FREQUENCY_MONTHLY'
    REPORT_FREQUENCY_QUARTERLY = 'REPORT_FREQUENCY_QUARTERLY'
    REPORT_FREQUENCY_ANNUALLY = 'REPORT_FREQUENCY_ANNUALLY'

    @classmethod
    def from_json(cls, json_str: str) -> V1ReportFrequency:
        """Create an instance of V1ReportFrequency from a JSON string"""
        return V1ReportFrequency(json.loads(json_str))

