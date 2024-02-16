# coding: utf-8

"""
    Aladdin Permission

    API contains operations on Aladdin Permission resource. Permissions cannot be applied directly to a user, they must be applied to a User Group first, then the user is added to a User Group. Note: This is not intended to be used for Authorization.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from aladdinsdk.api.codegen.platform.access.permission.v1.PermissionAPI.models.v1_permission_sensitivity_grade import V1PermissionSensitivityGrade

class V1Permission(BaseModel):
    """
    Permission describes Permission resource in Aladdin.
    """
    id: StrictStr = Field(...)
    description: StrictStr = Field(..., description="Describes what the permission controls.")
    functional_area: StrictStr = Field(..., alias="functionalArea", description="Used to link together groups of permission types. Applications may use this field so they only need to load permission information that is associated with a specific functional area.")
    action: Optional[StrictStr] = Field(None, description="Identifies the type of action that this permission controls i.e. View, Modify, Delete.")
    perm_group: StrictStr = Field(..., alias="permGroup", description="Identifies the grouping that is used by this permission type to define the scope: - PORTFOLIO - The permission grants access to portfolios. The portfolios are identified by either a portfolio_name from the portfolios table or a portfolio_group from the port_group table. If a portfolio_group is specified then that group is automatically expanded out to all of the portfolios that are contained within that group. - PORTGROUP - The permission grants access to a portfolio group defined in the port_group table. The specified portfolio group is not expanded out to its individual portfolios for this type of permission. - NONE - The permission must be added with * tbl_desc This permission group type identifies a list of items from the decodes table identified by the specified tbl_desc. Permissions may be granted for any item in that decodes entry. If permissions are granted for the perm_group \"*\" then the permission is granted for every item in the decodes entry.")
    sensitivity_grade: Optional[V1PermissionSensitivityGrade] = Field(None, alias="sensitivityGrade")
    __properties = ["id", "description", "functionalArea", "action", "permGroup", "sensitivityGrade"]

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
    def from_json(cls, json_str: str) -> V1Permission:
        """Create an instance of V1Permission from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1Permission:
        """Create an instance of V1Permission from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1Permission.parse_obj(obj)

        _obj = V1Permission.parse_obj({
            "id": obj.get("id"),
            "description": obj.get("description"),
            "functional_area": obj.get("functionalArea"),
            "action": obj.get("action"),
            "perm_group": obj.get("permGroup"),
            "sensitivity_grade": obj.get("sensitivityGrade")
        })
        return _obj
