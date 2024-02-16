# coding: utf-8

"""
    Risk Governance - Rules

    Retrieve, update, and create Rules and Rule Subscriptions as surfaced in Risk Radar.  # noqa: E501

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
from aladdinsdk.api.codegen.analytics.oversight.governance.v1.RiskRuleAPI.models.oversightgovernancev1_look_through_config import Oversightgovernancev1LookThroughConfig
from aladdinsdk.api.codegen.analytics.oversight.governance.v1.RiskRuleAPI.models.v1_portfolio_analytics_benchmark_config import V1PortfolioAnalyticsBenchmarkConfig

class V1RuleSetting(BaseModel):
    """
    V1RuleSetting
    """
    benchmark_config: Optional[V1PortfolioAnalyticsBenchmarkConfig] = Field(None, alias="benchmarkConfig")
    look_through_config: Optional[Oversightgovernancev1LookThroughConfig] = Field(None, alias="lookThroughConfig")
    __properties = ["benchmarkConfig", "lookThroughConfig"]

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
    def from_json(cls, json_str: str) -> V1RuleSetting:
        """Create an instance of V1RuleSetting from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of benchmark_config
        if self.benchmark_config:
            _dict['benchmarkConfig'] = self.benchmark_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of look_through_config
        if self.look_through_config:
            _dict['lookThroughConfig'] = self.look_through_config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1RuleSetting:
        """Create an instance of V1RuleSetting from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1RuleSetting.parse_obj(obj)

        _obj = V1RuleSetting.parse_obj({
            "benchmark_config": V1PortfolioAnalyticsBenchmarkConfig.from_dict(obj.get("benchmarkConfig")) if obj.get("benchmarkConfig") is not None else None,
            "look_through_config": Oversightgovernancev1LookThroughConfig.from_dict(obj.get("lookThroughConfig")) if obj.get("lookThroughConfig") is not None else None
        })
        return _obj
