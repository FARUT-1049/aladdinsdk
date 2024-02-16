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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, conlist
from aladdinsdk.api.codegen.analytics.portfolio_analytics.reporting.v1.PortfolioAnalyticsAPI.models.tree_table_data_tree_table_generic_data import TreeTableDataTreeTableGenericData

class TreeTableDataTreeTableDataNode(BaseModel):
    """
    TreeTableDataTreeTableDataNode
    """
    cell_values: Optional[conlist(Dict[str, Any])] = Field(None, alias="cellValues")
    child_nodes: Optional[conlist(TreeTableDataTreeTableDataNode)] = Field(None, alias="childNodes")
    extension_data_object: Optional[TreeTableDataTreeTableGenericData] = Field(None, alias="extensionDataObject")
    __properties = ["cellValues", "childNodes", "extensionDataObject"]

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
    def from_json(cls, json_str: str) -> TreeTableDataTreeTableDataNode:
        """Create an instance of TreeTableDataTreeTableDataNode from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in child_nodes (list)
        _items = []
        if self.child_nodes:
            for _item in self.child_nodes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['childNodes'] = _items
        # override the default output from pydantic by calling `to_dict()` of extension_data_object
        if self.extension_data_object:
            _dict['extensionDataObject'] = self.extension_data_object.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TreeTableDataTreeTableDataNode:
        """Create an instance of TreeTableDataTreeTableDataNode from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TreeTableDataTreeTableDataNode.parse_obj(obj)

        _obj = TreeTableDataTreeTableDataNode.parse_obj({
            "cell_values": obj.get("cellValues"),
            "child_nodes": [TreeTableDataTreeTableDataNode.from_dict(_item) for _item in obj.get("childNodes")] if obj.get("childNodes") is not None else None,
            "extension_data_object": TreeTableDataTreeTableGenericData.from_dict(obj.get("extensionDataObject")) if obj.get("extensionDataObject") is not None else None
        })
        return _obj
