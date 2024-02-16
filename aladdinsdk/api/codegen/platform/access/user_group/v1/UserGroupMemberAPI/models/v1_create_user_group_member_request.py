# coding: utf-8

"""
    Aladdin User Group Member

    API contains operations on Aladdin User Group Member resource. Note: This is not intended to be used for Authorization.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field
from aladdinsdk.api.codegen.platform.access.user_group.v1.UserGroupMemberAPI.models.v1_user_group_member import V1UserGroupMember

class V1CreateUserGroupMemberRequest(BaseModel):
    """
    V1CreateUserGroupMemberRequest
    """
    user_group_member: Optional[V1UserGroupMember] = Field(None, alias="userGroupMember")
    __properties = ["userGroupMember"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> V1CreateUserGroupMemberRequest:
        """Create an instance of V1CreateUserGroupMemberRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of user_group_member
        if self.user_group_member:
            _dict['userGroupMember'] = self.user_group_member.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1CreateUserGroupMemberRequest:
        """Create an instance of V1CreateUserGroupMemberRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1CreateUserGroupMemberRequest.parse_obj(obj)

        _obj = V1CreateUserGroupMemberRequest.parse_obj({
            "user_group_member": V1UserGroupMember.from_dict(obj.get("userGroupMember")) if obj.get("userGroupMember") is not None else None
        })
        return _obj
