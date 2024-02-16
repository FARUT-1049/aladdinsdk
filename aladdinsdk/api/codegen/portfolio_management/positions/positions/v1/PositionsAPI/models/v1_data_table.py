# coding: utf-8

"""
    Positions

    API to retrieve and monitor managed positions for Start of Day Positions. Managed positions are positions enriched with additional context such as restrictions and substitutions.  # noqa: E501

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
from aladdinsdk.api.codegen.portfolio_management.positions.positions.v1.PositionsAPI.models.v1_column_header import V1ColumnHeader
from aladdinsdk.api.codegen.portfolio_management.positions.positions.v1.PositionsAPI.models.v1_data_row import V1DataRow

class V1DataTable(BaseModel):
    """
    V1DataTable
    """
    column_headers: Optional[conlist(V1ColumnHeader)] = Field(None, alias="columnHeaders")
    data_rows: conlist(V1DataRow) = Field(..., alias="dataRows")
    __properties = ["columnHeaders", "dataRows"]

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
    def from_json(cls, json_str: str) -> V1DataTable:
        """Create an instance of V1DataTable from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in column_headers (list)
        _items = []
        if self.column_headers:
            for _item in self.column_headers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['columnHeaders'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in data_rows (list)
        _items = []
        if self.data_rows:
            for _item in self.data_rows:
                if _item:
                    _items.append(_item.to_dict())
            _dict['dataRows'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1DataTable:
        """Create an instance of V1DataTable from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1DataTable.parse_obj(obj)

        _obj = V1DataTable.parse_obj({
            "column_headers": [V1ColumnHeader.from_dict(_item) for _item in obj.get("columnHeaders")] if obj.get("columnHeaders") is not None else None,
            "data_rows": [V1DataRow.from_dict(_item) for _item in obj.get("dataRows")] if obj.get("dataRows") is not None else None
        })
        return _obj
