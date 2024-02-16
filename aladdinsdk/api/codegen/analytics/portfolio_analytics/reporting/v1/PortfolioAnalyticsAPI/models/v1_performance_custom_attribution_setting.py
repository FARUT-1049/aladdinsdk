# coding: utf-8

"""
    Portfolio Analytics

    Generate Portfolio Analytics.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, conlist
from aladdinsdk.api.codegen.analytics.portfolio_analytics.reporting.v1.PortfolioAnalyticsAPI.models.v1_performance_attribution_factors import V1PerformanceAttributionFactors
from aladdinsdk.api.codegen.analytics.portfolio_analytics.reporting.v1.PortfolioAnalyticsAPI.models.v1_performance_calculation_level import V1PerformanceCalculationLevel
from aladdinsdk.api.codegen.analytics.portfolio_analytics.reporting.v1.PortfolioAnalyticsAPI.models.v1_performance_calculation_method import V1PerformanceCalculationMethod
from aladdinsdk.api.codegen.analytics.portfolio_analytics.reporting.v1.PortfolioAnalyticsAPI.models.v1_performance_exposure_mode import V1PerformanceExposureMode
from aladdinsdk.api.codegen.analytics.portfolio_analytics.reporting.v1.PortfolioAnalyticsAPI.models.v1_performance_multi_manager_lookthrough_type import V1PerformanceMultiManagerLookthroughType
from aladdinsdk.api.codegen.analytics.portfolio_analytics.reporting.v1.PortfolioAnalyticsAPI.models.v1_performance_sector_weighting import V1PerformanceSectorWeighting

class V1PerformanceCustomAttributionSetting(BaseModel):
    """
    V1PerformanceCustomAttributionSetting
    """
    performance_attribution_factors: Optional[conlist(V1PerformanceAttributionFactors)] = Field(None, alias="performanceAttributionFactors")
    performance_sector_weighting: Optional[V1PerformanceSectorWeighting] = Field(None, alias="performanceSectorWeighting")
    performance_calculation_method: Optional[V1PerformanceCalculationMethod] = Field(None, alias="performanceCalculationMethod")
    performance_calculation_level: Optional[V1PerformanceCalculationLevel] = Field(None, alias="performanceCalculationLevel")
    performance_exposure_mode: Optional[V1PerformanceExposureMode] = Field(None, alias="performanceExposureMode")
    performance_multi_manager_lookthrough_type: Optional[V1PerformanceMultiManagerLookthroughType] = Field(None, alias="performanceMultiManagerLookthroughType")
    __properties = ["performanceAttributionFactors", "performanceSectorWeighting", "performanceCalculationMethod", "performanceCalculationLevel", "performanceExposureMode", "performanceMultiManagerLookthroughType"]

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
    def from_json(cls, json_str: str) -> V1PerformanceCustomAttributionSetting:
        """Create an instance of V1PerformanceCustomAttributionSetting from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1PerformanceCustomAttributionSetting:
        """Create an instance of V1PerformanceCustomAttributionSetting from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1PerformanceCustomAttributionSetting.parse_obj(obj)

        _obj = V1PerformanceCustomAttributionSetting.parse_obj({
            "performance_attribution_factors": obj.get("performanceAttributionFactors"),
            "performance_sector_weighting": obj.get("performanceSectorWeighting"),
            "performance_calculation_method": obj.get("performanceCalculationMethod"),
            "performance_calculation_level": obj.get("performanceCalculationLevel"),
            "performance_exposure_mode": obj.get("performanceExposureMode"),
            "performance_multi_manager_lookthrough_type": obj.get("performanceMultiManagerLookthroughType")
        })
        return _obj
