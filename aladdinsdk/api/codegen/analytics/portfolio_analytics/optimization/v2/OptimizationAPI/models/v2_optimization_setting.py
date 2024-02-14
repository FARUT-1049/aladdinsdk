# coding: utf-8

"""
    Portfolio Optimization 2.0

    Optimize portfolio positions to maximize expected returns and minimize risk and transaction costs.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_blk_ops_entry import V2BlkOpsEntry
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_optimizer_control_parameter import V2OptimizerControlParameter
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_report_request_entry import V2ReportRequestEntry

class V2OptimizationSetting(BaseModel):
    """
    V2OptimizationSetting
    """
    optimizer_parameter: Optional[V2OptimizerControlParameter] = Field(None, alias="optimizerParameter")
    requested_reports: conlist(V2ReportRequestEntry) = Field(..., alias="requestedReports")
    blkops_path_throughs: Optional[conlist(V2BlkOpsEntry)] = Field(None, alias="blkopsPathThroughs")
    custom_component: Optional[StrictStr] = Field(None, alias="customComponent")
    debug_settings: Optional[Dict[str, StrictStr]] = Field(None, alias="debugSettings", description="Additional settings to test temporary features. For developers only.")
    blkops_pass_throughs: Optional[conlist(V2BlkOpsEntry)] = Field(None, alias="blkopsPassThroughs")
    __properties = ["optimizerParameter", "requestedReports", "blkopsPathThroughs", "customComponent", "debugSettings", "blkopsPassThroughs"]

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
    def from_json(cls, json_str: str) -> V2OptimizationSetting:
        """Create an instance of V2OptimizationSetting from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of optimizer_parameter
        if self.optimizer_parameter:
            _dict['optimizerParameter'] = self.optimizer_parameter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in requested_reports (list)
        _items = []
        if self.requested_reports:
            for _item in self.requested_reports:
                if _item:
                    _items.append(_item.to_dict())
            _dict['requestedReports'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in blkops_path_throughs (list)
        _items = []
        if self.blkops_path_throughs:
            for _item in self.blkops_path_throughs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['blkopsPathThroughs'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in blkops_pass_throughs (list)
        _items = []
        if self.blkops_pass_throughs:
            for _item in self.blkops_pass_throughs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['blkopsPassThroughs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V2OptimizationSetting:
        """Create an instance of V2OptimizationSetting from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V2OptimizationSetting.parse_obj(obj)

        _obj = V2OptimizationSetting.parse_obj({
            "optimizer_parameter": V2OptimizerControlParameter.from_dict(obj.get("optimizerParameter")) if obj.get("optimizerParameter") is not None else None,
            "requested_reports": [V2ReportRequestEntry.from_dict(_item) for _item in obj.get("requestedReports")] if obj.get("requestedReports") is not None else None,
            "blkops_path_throughs": [V2BlkOpsEntry.from_dict(_item) for _item in obj.get("blkopsPathThroughs")] if obj.get("blkopsPathThroughs") is not None else None,
            "custom_component": obj.get("customComponent"),
            "debug_settings": obj.get("debugSettings"),
            "blkops_pass_throughs": [V2BlkOpsEntry.from_dict(_item) for _item in obj.get("blkopsPassThroughs")] if obj.get("blkopsPassThroughs") is not None else None
        })
        return _obj

