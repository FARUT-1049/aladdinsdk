# coding: utf-8

"""
    Custom Investment Dataset Writer

    API for writing Dataset Definitions and Entities.  _CIDS does not transform the input data in any kind. The writer of the data owns it and is responsible for this data. CIDS provides a way to ingest the custom investment data into Aladdin for usage across Portfolio Management tools._  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from aladdinsdk.api.codegen.portfolio_management.setup.cids.v1.CIDWriterAPI.models.v1_dataset_type import V1DatasetType
from aladdinsdk.api.codegen.portfolio_management.setup.cids.v1.CIDWriterAPI.models.v1_perm_group import V1PermGroup
from aladdinsdk.api.codegen.portfolio_management.setup.cids.v1.CIDWriterAPI.models.v1_purpose import V1Purpose
from aladdinsdk.api.codegen.portfolio_management.setup.cids.v1.CIDWriterAPI.models.v1_state import V1State

class V1CIDDatasetDefinition(BaseModel):
    """
    Dataset Definition is a metadata of the Dataset.
    """
    id: StrictStr = Field(..., description="Definition Id as Identifier. ID is automated from the server and the client does not need to pass value in it.")
    dataset_name: StrictStr = Field(..., alias="datasetName", description="Describes name of the Category, Class, Group or Leaf Level Dataset. Character Limit: 15.")
    dataset_type: Optional[V1DatasetType] = Field(None, alias="datasetType")
    author: StrictStr = Field(..., description="Login ID of the person or program that created or last modified the Dataset Definition. Character Limit: 8.")
    retention_policy_period: Optional[StrictStr] = Field(None, alias="retentionPolicyPeriod")
    revision_id: Optional[StrictStr] = Field(None, alias="revisionId", description="Current Version of the Dataset.")
    revision_create_time: Optional[datetime] = Field(None, alias="revisionCreateTime", description="Revision create time (in UTC) of the Dataset describes when this version of definition is created.")
    state: Optional[V1State] = None
    description: Optional[StrictStr] = None
    schema_name: Optional[StrictStr] = Field(None, alias="schemaName", description="Name of the schema in case of DATASET_TYPE_SCHEMA. Character Limit: 25.")
    repo_name: Optional[StrictStr] = Field(None, alias="repoName", description="Repo name of the Dataset is type of data will be written in this datasets. This should be cde value from CIDS_REPO decode. This can only be used by ADMIN users while creating Dataset Category and is inherited by other level datasets from its parent category. Character Limit: 15.")
    element_path: StrictStr = Field(..., alias="elementPath", description="Describes Dataset Hierarchy definition.  Represented through a list of strings separated by a '.' (CATEGORY.CLASS.GROUP.DATASET).  Example: When creating CLASS Dataset TEST_CLASS under TEST_CATEGORY, then elementPath should be 'TEST_CATEGORY.TEST_CLASS'.  all parents should be active Character Limit: 64. (-- api-linter: core::0203::optional=disabled  aip.dev/not-precedent: We need to do this because this is required field --)")
    perm_group: Optional[V1PermGroup] = Field(None, alias="permGroup")
    meta_info: Optional[StrictStr] = Field(None, alias="metaInfo", description="Additional information to assign to the Dataset.  should be in key=value format Example: \"test=123\" To enable support for adding historical start date entities in dataset -> Key: 'backDatedStartDateSupport' and Value: TRUE/FALSE Note: you cannot use or update \"maxNoOfAttributes\" in metaInfo as it is used for internal purpose Character Limit: 255.")
    team: Optional[StrictStr] = Field(None, description="Team that owns the Dataset.  Character Limit: 15.")
    purpose: V1Purpose = Field(...)
    dataset_full_name: StrictStr = Field(..., alias="datasetFullName", description="Describes full name of the Category, Class, Group or Leaf Level Dataset. Character Limit: 75.")
    __properties = ["id", "datasetName", "datasetType", "author", "retentionPolicyPeriod", "revisionId", "revisionCreateTime", "state", "description", "schemaName", "repoName", "elementPath", "permGroup", "metaInfo", "team", "purpose", "datasetFullName"]

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
    def from_json(cls, json_str: str) -> V1CIDDatasetDefinition:
        """Create an instance of V1CIDDatasetDefinition from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "revision_id",
                            "revision_create_time",
                            "repo_name",
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1CIDDatasetDefinition:
        """Create an instance of V1CIDDatasetDefinition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1CIDDatasetDefinition.parse_obj(obj)

        _obj = V1CIDDatasetDefinition.parse_obj({
            "id": obj.get("id"),
            "dataset_name": obj.get("datasetName"),
            "dataset_type": obj.get("datasetType"),
            "author": obj.get("author"),
            "retention_policy_period": obj.get("retentionPolicyPeriod"),
            "revision_id": obj.get("revisionId"),
            "revision_create_time": obj.get("revisionCreateTime"),
            "state": obj.get("state"),
            "description": obj.get("description"),
            "schema_name": obj.get("schemaName"),
            "repo_name": obj.get("repoName"),
            "element_path": obj.get("elementPath"),
            "perm_group": obj.get("permGroup"),
            "meta_info": obj.get("metaInfo"),
            "team": obj.get("team"),
            "purpose": obj.get("purpose"),
            "dataset_full_name": obj.get("datasetFullName")
        })
        return _obj
