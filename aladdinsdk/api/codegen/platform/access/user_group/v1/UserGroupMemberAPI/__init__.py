# coding: utf-8

# flake8: noqa

"""
    Aladdin User Group Member

    API contains operations on Aladdin User Group Member resource. Note: This is not intended to be used for Authorization.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


__version__ = "1.0.0"

# import apis into sdk package
from aladdinsdk.api.codegen.platform.access.user_group.v1.UserGroupMemberAPI.api.default_user_group_member_api import DefaultUserGroupMemberAPI

# import ApiClient
from aladdinsdk.api.codegen.platform.access.user_group.v1.UserGroupMemberAPI.api_response import ApiResponse
from aladdinsdk.api.codegen.platform.access.user_group.v1.UserGroupMemberAPI.api_client import ApiClient
from aladdinsdk.api.codegen.platform.access.user_group.v1.UserGroupMemberAPI.configuration import Configuration
from aladdinsdk.api.codegen.platform.access.user_group.v1.UserGroupMemberAPI.exceptions import OpenApiException
from aladdinsdk.api.codegen.platform.access.user_group.v1.UserGroupMemberAPI.exceptions import ApiTypeError
from aladdinsdk.api.codegen.platform.access.user_group.v1.UserGroupMemberAPI.exceptions import ApiValueError
from aladdinsdk.api.codegen.platform.access.user_group.v1.UserGroupMemberAPI.exceptions import ApiKeyError
from aladdinsdk.api.codegen.platform.access.user_group.v1.UserGroupMemberAPI.exceptions import ApiAttributeError
from aladdinsdk.api.codegen.platform.access.user_group.v1.UserGroupMemberAPI.exceptions import ApiException

# import models into sdk package
from aladdinsdk.api.codegen.platform.access.user_group.v1.UserGroupMemberAPI.models.any import Any
from aladdinsdk.api.codegen.platform.access.user_group.v1.UserGroupMemberAPI.models.rpc_status import RpcStatus
from aladdinsdk.api.codegen.platform.access.user_group.v1.UserGroupMemberAPI.models.the_request_message_for_user_group_member_api_batch_create_user_group_members_api_linter_core0233_request_requests_field_disabled_aip_dev_not_precedent_we_need_to_do_this_because_we_have_renamed_the_field_name_to_create_requests_for_clarity import TheRequestMessageForUserGroupMemberAPIBatchCreateUserGroupMembersApiLinterCore0233RequestRequestsFieldDisabledAipDevNotPrecedentWeNeedToDoThisBecauseWeHaveRenamedTheFieldNameToCreateRequestsForClarity
from aladdinsdk.api.codegen.platform.access.user_group.v1.UserGroupMemberAPI.models.user_group_member_api_batch_delete_user_group_members_request import UserGroupMemberAPIBatchDeleteUserGroupMembersRequest
from aladdinsdk.api.codegen.platform.access.user_group.v1.UserGroupMemberAPI.models.user_group_member_api_list_user_group_members400_response import UserGroupMemberAPIListUserGroupMembers400Response
from aladdinsdk.api.codegen.platform.access.user_group.v1.UserGroupMemberAPI.models.v1_batch_create_user_group_members_response import V1BatchCreateUserGroupMembersResponse
from aladdinsdk.api.codegen.platform.access.user_group.v1.UserGroupMemberAPI.models.v1_create_user_group_member_request import V1CreateUserGroupMemberRequest
from aladdinsdk.api.codegen.platform.access.user_group.v1.UserGroupMemberAPI.models.v1_list_user_group_members_response import V1ListUserGroupMembersResponse
from aladdinsdk.api.codegen.platform.access.user_group.v1.UserGroupMemberAPI.models.v1_user_group_member import V1UserGroupMember
