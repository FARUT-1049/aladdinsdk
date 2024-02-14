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
from pydantic import BaseModel, Field, StrictBool, conlist
from aladdinsdk.api.codegen.analytics.portfolio_analytics.reporting.v1.PortfolioAnalyticsAPI.models.look_through_config_look_through_proxy_config import LookThroughConfigLookThroughProxyConfig
from aladdinsdk.api.codegen.analytics.portfolio_analytics.reporting.v1.PortfolioAnalyticsAPI.models.look_through_config_look_through_security_config import LookThroughConfigLookThroughSecurityConfig
from aladdinsdk.api.codegen.analytics.portfolio_analytics.reporting.v1.PortfolioAnalyticsAPI.models.v1_look_through_proxy_type import V1LookThroughProxyType
from aladdinsdk.api.codegen.analytics.portfolio_analytics.reporting.v1.PortfolioAnalyticsAPI.models.v1_look_through_rule import V1LookThroughRule
from aladdinsdk.api.codegen.analytics.portfolio_analytics.reporting.v1.PortfolioAnalyticsAPI.models.v1_look_through_security_type import V1LookThroughSecurityType

class V1LookThroughConfig(BaseModel):
    """
    V1LookThroughConfig
    """
    look_through_portfolio: Optional[StrictBool] = Field(None, alias="lookThroughPortfolio")
    look_through_benchmark: Optional[StrictBool] = Field(None, alias="lookThroughBenchmark")
    look_through_security_config: Optional[LookThroughConfigLookThroughSecurityConfig] = Field(None, alias="lookThroughSecurityConfig")
    look_through_security_types: Optional[conlist(V1LookThroughSecurityType)] = Field(None, alias="lookThroughSecurityTypes")
    look_through_proxy_config: Optional[LookThroughConfigLookThroughProxyConfig] = Field(None, alias="lookThroughProxyConfig")
    look_through_proxy_types: Optional[conlist(V1LookThroughProxyType)] = Field(None, alias="lookThroughProxyTypes")
    look_through_rule: Optional[V1LookThroughRule] = Field(None, alias="lookThroughRule")
    look_through_inheritance: Optional[StrictBool] = Field(None, alias="lookThroughInheritance")
    __properties = ["lookThroughPortfolio", "lookThroughBenchmark", "lookThroughSecurityConfig", "lookThroughSecurityTypes", "lookThroughProxyConfig", "lookThroughProxyTypes", "lookThroughRule", "lookThroughInheritance"]

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
    def from_json(cls, json_str: str) -> V1LookThroughConfig:
        """Create an instance of V1LookThroughConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of look_through_rule
        if self.look_through_rule:
            _dict['lookThroughRule'] = self.look_through_rule.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1LookThroughConfig:
        """Create an instance of V1LookThroughConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1LookThroughConfig.parse_obj(obj)

        _obj = V1LookThroughConfig.parse_obj({
            "look_through_portfolio": obj.get("lookThroughPortfolio"),
            "look_through_benchmark": obj.get("lookThroughBenchmark"),
            "look_through_security_config": obj.get("lookThroughSecurityConfig"),
            "look_through_security_types": obj.get("lookThroughSecurityTypes"),
            "look_through_proxy_config": obj.get("lookThroughProxyConfig"),
            "look_through_proxy_types": obj.get("lookThroughProxyTypes"),
            "look_through_rule": V1LookThroughRule.from_dict(obj.get("lookThroughRule")) if obj.get("lookThroughRule") is not None else None,
            "look_through_inheritance": obj.get("lookThroughInheritance")
        })
        return _obj

