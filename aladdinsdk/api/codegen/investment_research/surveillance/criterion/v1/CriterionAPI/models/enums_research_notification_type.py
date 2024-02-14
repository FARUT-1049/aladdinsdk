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





class EnumsResearchNotificationType(str, Enum):
    """
    - RESEARCH_NOTIFICATION_TYPE_UNSPECIFIED: Unspecified  - RESEARCH_NOTIFICATION_TYPE_EMAIL: Email (-- api-linter: aladdin::9301::event-type-values=disabled  aip.dev/not-precedent: We need to do this because type specified isnt included in expected event type wordlist --)
    """

    """
    allowed enum values
    """
    RESEARCH_NOTIFICATION_TYPE_UNSPECIFIED = 'RESEARCH_NOTIFICATION_TYPE_UNSPECIFIED'
    RESEARCH_NOTIFICATION_TYPE_EMAIL = 'RESEARCH_NOTIFICATION_TYPE_EMAIL'

    @classmethod
    def from_json(cls, json_str: str) -> EnumsResearchNotificationType:
        """Create an instance of EnumsResearchNotificationType from a JSON string"""
        return EnumsResearchNotificationType(json.loads(json_str))


