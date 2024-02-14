# coding: utf-8

"""
    Risk Governance - Tasks

    Retrieve Tasks, as surfaced in Risk Radar, which are aggregates that comprise of related Exceptions, Rules, and Workflow items.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class V1PortfolioAnalyticsBenchmarkOrder(str, Enum):
    """
    - PORTFOLIO_ANALYTICS_BENCHMARK_ORDER_UNSPECIFIED: Unspecfied value  - PORTFOLIO_ANALYTICS_BENCHMARK_ORDER_PRIMARY: Represents the primary order benchmark  - PORTFOLIO_ANALYTICS_BENCHMARK_ORDER_SECONDARY: Represents the secondary order benchmark
    """

    """
    allowed enum values
    """
    PORTFOLIO_ANALYTICS_BENCHMARK_ORDER_UNSPECIFIED = 'PORTFOLIO_ANALYTICS_BENCHMARK_ORDER_UNSPECIFIED'
    PORTFOLIO_ANALYTICS_BENCHMARK_ORDER_PRIMARY = 'PORTFOLIO_ANALYTICS_BENCHMARK_ORDER_PRIMARY'
    PORTFOLIO_ANALYTICS_BENCHMARK_ORDER_SECONDARY = 'PORTFOLIO_ANALYTICS_BENCHMARK_ORDER_SECONDARY'

    @classmethod
    def from_json(cls, json_str: str) -> V1PortfolioAnalyticsBenchmarkOrder:
        """Create an instance of V1PortfolioAnalyticsBenchmarkOrder from a JSON string"""
        return V1PortfolioAnalyticsBenchmarkOrder(json.loads(json_str))


