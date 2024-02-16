# coding: utf-8

# flake8: noqa

"""
    Research Note

    Create, modify, delete and retrieve research notes.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


__version__ = "1.0.0"

# import apis into sdk package
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.api.default_research_note_api import DefaultResearchNoteAPI

# import ApiClient
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.api_response import ApiResponse
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.api_client import ApiClient
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.configuration import Configuration
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.exceptions import OpenApiException
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.exceptions import ApiTypeError
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.exceptions import ApiValueError
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.exceptions import ApiKeyError
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.exceptions import ApiAttributeError
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.exceptions import ApiException

# import models into sdk package
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.models.any import Any
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.models.research_note_api_create_research_note400_response import ResearchNoteAPICreateResearchNote400Response
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.models.rpc_status import RpcStatus
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.models.types_entity_id import TypesEntityId
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.models.v1_expiring_permission_group import V1ExpiringPermissionGroup
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.models.v1_expiring_permission_time_unit import V1ExpiringPermissionTimeUnit
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.models.v1_investment_stewardship_assessment import V1InvestmentStewardshipAssessment
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.models.v1_investment_stewardship_detail import V1InvestmentStewardshipDetail
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.models.v1_investment_stewardship_engagement import V1InvestmentStewardshipEngagement
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.models.v1_investment_stewardship_fixed_keyword import V1InvestmentStewardshipFixedKeyword
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.models.v1_investment_stewardship_format import V1InvestmentStewardshipFormat
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.models.v1_investment_stewardship_initiator import V1InvestmentStewardshipInitiator
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.models.v1_investment_stewardship_outcome import V1InvestmentStewardshipOutcome
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.models.v1_investment_stewardship_score import V1InvestmentStewardshipScore
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.models.v1_investment_stewardship_time_frame import V1InvestmentStewardshipTimeFrame
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.models.v1_investment_stewardship_topic import V1InvestmentStewardshipTopic
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.models.v1_investment_stewardship_topic_details import V1InvestmentStewardshipTopicDetails
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.models.v1_note_state import V1NoteState
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.models.v1_publish_preference import V1PublishPreference
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.models.v1_research_note import V1ResearchNote
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.models.v1_research_strategy_detail import V1ResearchStrategyDetail
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.models.v1_search_preference import V1SearchPreference
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.models.v1_search_research_notes_response import V1SearchResearchNotesResponse
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.models.v1_user_preferences import V1UserPreferences