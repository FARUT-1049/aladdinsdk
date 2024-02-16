# coding: utf-8

"""
    Custom Investment Dataset Reader

    API for reading Dataset Definitions and Entities.  _CIDS does not transform the input data in any kind. The writer of the data owns it and is responsible for this data. CIDS provides a way to ingest the custom investment data into Aladdin for usage across Portfolio Management tools._  # noqa: E501

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
from aladdinsdk.api.codegen.portfolio_management.setup.cids.v1.CIDReaderAPI.models.v1_date_time_range import V1DateTimeRange
from aladdinsdk.api.codegen.portfolio_management.setup.cids.v1.CIDReaderAPI.models.v1_state import V1State

class V1CIDEntity(BaseModel):
    """
    Custom Investment Dataset Entity.
    """
    id: Optional[StrictStr] = Field(None, description="unique identifier for the entity; of the format : entity_name/{entity_name}/dataset_name/{dataset_name}/start_time/{start_time}/revision_id/{revision_id} ID is automated from the server and the client does not need to pass value in it.")
    entity_name: StrictStr = Field(..., alias="entityName", description="Name of the Entity. Entity name should not contain | (pipe character) in it Character Limit: 32.")
    dataset_name: StrictStr = Field(..., alias="datasetName", description="Dataset name of the Entity. This cannot be Category, Class or Group. Only leaf level Dataset can have Entities. Character Limit: 15.")
    entity_type: Optional[StrictStr] = Field(None, alias="entityType", description="Type of an entity such as isin, cusip, broker etc. Possible values of entity type while creation will eventually be driven from the CIDS_ENT_TYPE decode. While updating an existing entity, entity type can not be changed and will be defaulted to previous value if no value is provided in current request. Character Limit: 15.")
    time_range: Optional[V1DateTimeRange] = Field(None, alias="timeRange")
    revision_id: Optional[StrictStr] = Field(None, alias="revisionId", description="Current Version of the Entity.")
    revision_create_time: Optional[datetime] = Field(None, alias="revisionCreateTime", description="Revision create time (in UTC) of the Entity describes when this version of Entity is created.")
    state: Optional[V1State] = None
    data: Optional[StrictStr] = None
    author: StrictStr = Field(..., description="Login ID of the person or program that created or last modified the Entity. Character Limit: 8.")
    portfolio_name: Optional[StrictStr] = Field(None, alias="portfolioName", description="Portfolio Name - should only be present for Portfolio datasets. Portfolio name should not contain | (pipe character) in it Character Limit: 10.")
    __properties = ["id", "entityName", "datasetName", "entityType", "timeRange", "revisionId", "revisionCreateTime", "state", "data", "author", "portfolioName"]

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
    def from_json(cls, json_str: str) -> V1CIDEntity:
        """Create an instance of V1CIDEntity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "revision_id",
                            "revision_create_time",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of time_range
        if self.time_range:
            _dict['timeRange'] = self.time_range.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1CIDEntity:
        """Create an instance of V1CIDEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1CIDEntity.parse_obj(obj)

        _obj = V1CIDEntity.parse_obj({
            "id": obj.get("id"),
            "entity_name": obj.get("entityName"),
            "dataset_name": obj.get("datasetName"),
            "entity_type": obj.get("entityType"),
            "time_range": V1DateTimeRange.from_dict(obj.get("timeRange")) if obj.get("timeRange") is not None else None,
            "revision_id": obj.get("revisionId"),
            "revision_create_time": obj.get("revisionCreateTime"),
            "state": obj.get("state"),
            "data": obj.get("data"),
            "author": obj.get("author"),
            "portfolio_name": obj.get("portfolioName")
        })
        return _obj
