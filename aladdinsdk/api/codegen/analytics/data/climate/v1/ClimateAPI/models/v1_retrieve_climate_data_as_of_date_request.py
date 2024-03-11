# coding: utf-8

"""
    Climate

    The Aladdin Climate Data API exposes physical, transition, and temperature alignment analytics as of a given date. Users can retrieve data for selected entity types by specifying the desired datapoints for each climate risk type and scenario. The Aladdin Climate Meta Data API outlines the datapoints available across physical, transition, and temperature alignment analytics.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from aladdinsdk.api.codegen.analytics.data.climate.v1.ClimateAPI.models.v1_climate_risk_request import V1ClimateRiskRequest
from aladdinsdk.api.codegen.analytics.data.climate.v1.ClimateAPI.models.v1_id_type import V1IdType

class V1RetrieveClimateDataAsOfDateRequest(BaseModel):
    """
    V1RetrieveClimateDataAsOfDateRequest
    """
    id_type: V1IdType = Field(..., alias="idType")
    ids: conlist(StrictStr) = Field(...)
    as_of_date: date = Field(..., alias="asOfDate")
    climate_risk_requests: conlist(V1ClimateRiskRequest) = Field(..., alias="climateRiskRequests", description="Details needed to fetch the climate data such as scenario types, metric codes, etc.")
    page_size: Optional[StrictInt] = Field(None, alias="pageSize", description="Maximum number of ids for which data will be returned in each response. If unspecified, limit is set to the default maximum. Values above this will be coerced to this maximum.")
    page_token: Optional[StrictStr] = Field(None, alias="pageToken", description="A page token, received from a previous `RetrieveClimateDataAsOfDate` call. Provide this to retrieve the subsequent page.  When paginating, all other parameters provided to `RetrieveClimateDataAsOfDate` must match the call that provided the page token.")
    app_key: Optional[StrictStr] = Field(None, alias="appKey", description="Optional App id key used for identifying the calling application.")
    __properties = ["idType", "ids", "asOfDate", "climateRiskRequests", "pageSize", "pageToken", "appKey"]

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
    def from_json(cls, json_str: str) -> V1RetrieveClimateDataAsOfDateRequest:
        """Create an instance of V1RetrieveClimateDataAsOfDateRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in climate_risk_requests (list)
        _items = []
        if self.climate_risk_requests:
            for _item in self.climate_risk_requests:
                if _item:
                    _items.append(_item.to_dict())
            _dict['climateRiskRequests'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1RetrieveClimateDataAsOfDateRequest:
        """Create an instance of V1RetrieveClimateDataAsOfDateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1RetrieveClimateDataAsOfDateRequest.parse_obj(obj)

        _obj = V1RetrieveClimateDataAsOfDateRequest.parse_obj({
            "id_type": obj.get("idType"),
            "ids": obj.get("ids"),
            "as_of_date": obj.get("asOfDate"),
            "climate_risk_requests": [V1ClimateRiskRequest.from_dict(_item) for _item in obj.get("climateRiskRequests")] if obj.get("climateRiskRequests") is not None else None,
            "page_size": obj.get("pageSize"),
            "page_token": obj.get("pageToken"),
            "app_key": obj.get("appKey")
        })
        return _obj

