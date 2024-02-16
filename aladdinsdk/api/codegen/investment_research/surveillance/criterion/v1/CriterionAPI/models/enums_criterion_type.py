# coding: utf-8

"""
    Criterion

    Create, modify, delete, search and evaluate criteria.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class EnumsCriterionType(str, Enum):
    """
    - CRITERION_TYPE_UNSPECIFIED: Unspecified criteria type  - CRITERION_TYPE_WATCHLIST: Watchlist criteria type  - CRITERION_TYPE_RESEARCH_NOTE: Research note criteria type  - CRITERION_TYPE_INVESTMENT_OPINION: Investment opinion value criteria type  - CRITERION_TYPE_CREDIT_APPROVAL: Credit approval criteria type  - CRITERION_TYPE_ESG: ESG criteria type  - CRITERION_TYPE_INVESTMENT_OPINION_UPDATE: Investment opinion update criteria type
    """

    """
    allowed enum values
    """
    CRITERION_TYPE_UNSPECIFIED = 'CRITERION_TYPE_UNSPECIFIED'
    CRITERION_TYPE_WATCHLIST = 'CRITERION_TYPE_WATCHLIST'
    CRITERION_TYPE_RESEARCH_NOTE = 'CRITERION_TYPE_RESEARCH_NOTE'
    CRITERION_TYPE_INVESTMENT_OPINION = 'CRITERION_TYPE_INVESTMENT_OPINION'
    CRITERION_TYPE_CREDIT_APPROVAL = 'CRITERION_TYPE_CREDIT_APPROVAL'
    CRITERION_TYPE_ESG = 'CRITERION_TYPE_ESG'
    CRITERION_TYPE_INVESTMENT_OPINION_UPDATE = 'CRITERION_TYPE_INVESTMENT_OPINION_UPDATE'

    @classmethod
    def from_json(cls, json_str: str) -> EnumsCriterionType:
        """Create an instance of EnumsCriterionType from a JSON string"""
        return EnumsCriterionType(json.loads(json_str))

