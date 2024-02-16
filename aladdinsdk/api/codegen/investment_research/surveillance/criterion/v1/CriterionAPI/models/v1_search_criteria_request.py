# coding: utf-8

"""
    Criterion

    Create, modify, delete, search and evaluate criteria.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist

class V1SearchCriteriaRequest(BaseModel):
    """
    V1SearchCriteriaRequest
    """
    filter_criteria: Optional[conlist(StrictStr)] = Field(None, alias="filterCriteria", description="Multiple criteria can also be joined by AND and OR logic operator Other supported logic operator includes ! means not equal, IN for a list of value terms, etc. e.g. criterion.owner:\"user\" AND (criterion.entity_id.asset_id:\"123456789\" OR criterion.entity_id.issuer:\"*ABC*\") , etc. (-- api-linter: core::0132::request-unknown-fields=disabled aip.dev/not-precedent: We really need this field because it is already implemented in prod --)")
    order_by: Optional[StrictStr] = Field(None, alias="orderBy", description="Sorts the response with ascending or descending order based on specific field. Default as asc.")
    page_size: Optional[StrictInt] = Field(None, alias="pageSize", description="The maximum number of research notes to return. The service may return fewer than this value. If unspecified, at most 10 note will be returned.")
    page_number: Optional[StrictInt] = Field(None, alias="pageNumber", description="When paginating, all other parameters provided to 'SearchCriteria' must match the call that provided the page number.")
    __properties = ["filterCriteria", "orderBy", "pageSize", "pageNumber"]

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
    def from_json(cls, json_str: str) -> V1SearchCriteriaRequest:
        """Create an instance of V1SearchCriteriaRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1SearchCriteriaRequest:
        """Create an instance of V1SearchCriteriaRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1SearchCriteriaRequest.parse_obj(obj)

        _obj = V1SearchCriteriaRequest.parse_obj({
            "filter_criteria": obj.get("filterCriteria"),
            "order_by": obj.get("orderBy"),
            "page_size": obj.get("pageSize"),
            "page_number": obj.get("pageNumber")
        })
        return _obj
