# coding: utf-8

"""
    ESG Data

    The ESG Data API offers a centralized source of ESG data and meta data across multiple vendors. The API retrieves ESG data by asset and issuer from multiple vendors, providing the data in one digestible schema. Retrieve ESG data for selected assets and issuers by providing entity id, provider id, date(s) and measure name. Meta data on ESG data measures can be retrieved by selecting a provider, provider category and unique measure names. Time Series API in alpha version, changes may be made at any time.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Dict, Optional
from pydantic import BaseModel, Field, StrictStr
from aladdinsdk.api.codegen.analytics.data.esg.v1.EsgDataAPI.models.types_analytic_data_value import TypesAnalyticDataValue

class V1ProviderMeasureMetadataExt(BaseModel):
    """
    V1ProviderMeasureMetadataExt
    """
    source_name: Optional[StrictStr] = Field(None, alias="sourceName")
    metadata: Optional[Dict[str, TypesAnalyticDataValue]] = Field(None, description="Provider specific metadata.")
    __properties = ["sourceName", "metadata"]

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
    def from_json(cls, json_str: str) -> V1ProviderMeasureMetadataExt:
        """Create an instance of V1ProviderMeasureMetadataExt from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in metadata (dict)
        _field_dict = {}
        if self.metadata:
            for _key in self.metadata:
                if self.metadata[_key]:
                    _field_dict[_key] = self.metadata[_key].to_dict()
            _dict['metadata'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1ProviderMeasureMetadataExt:
        """Create an instance of V1ProviderMeasureMetadataExt from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1ProviderMeasureMetadataExt.parse_obj(obj)

        _obj = V1ProviderMeasureMetadataExt.parse_obj({
            "source_name": obj.get("sourceName"),
            "metadata": dict(
                (_k, TypesAnalyticDataValue.from_dict(_v))
                for _k, _v in obj.get("metadata").items()
            )
            if obj.get("metadata") is not None
            else None
        })
        return _obj

