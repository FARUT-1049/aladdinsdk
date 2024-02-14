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





class V1EvaluationState(str, Enum):
    """
    - EVALUATION_STATE_UNSPECIFIED: No definition present (not a valid input value)  - EVALUATION_STATE_BREACH: High severity state signalling that the evaluation has identified a BREACH  - EVALUATION_STATE_WARNING: Lower severity state signalling that the valuation has identified a WARNING  - EVALUATION_STATE_OK: OK state signalling that a prior exception is no longer an exception and is to be closed out by the system
    """

    """
    allowed enum values
    """
    EVALUATION_STATE_UNSPECIFIED = 'EVALUATION_STATE_UNSPECIFIED'
    EVALUATION_STATE_BREACH = 'EVALUATION_STATE_BREACH'
    EVALUATION_STATE_WARNING = 'EVALUATION_STATE_WARNING'
    EVALUATION_STATE_OK = 'EVALUATION_STATE_OK'

    @classmethod
    def from_json(cls, json_str: str) -> V1EvaluationState:
        """Create an instance of V1EvaluationState from a JSON string"""
        return V1EvaluationState(json.loads(json_str))


