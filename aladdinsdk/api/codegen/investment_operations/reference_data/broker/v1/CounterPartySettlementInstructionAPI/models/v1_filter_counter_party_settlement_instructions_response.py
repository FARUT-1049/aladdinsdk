# coding: utf-8

"""
    Counter Party Settlement Instruction

    API contains operations on Counter Party Settlement Instruction resource.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from aladdinsdk.api.codegen.investment_operations.reference_data.broker.v1.CounterPartySettlementInstructionAPI.models.v1_counter_party_settlement_instruction import V1CounterPartySettlementInstruction

class V1FilterCounterPartySettlementInstructionsResponse(BaseModel):
    """
    The response message for CounterPartySettlementInstructionAPI.FilterCounterPartySettlementInstructions.
    """
    counterparty_settlement_instructions: Optional[conlist(V1CounterPartySettlementInstruction)] = Field(None, alias="counterpartySettlementInstructions", description="Counterparty settlement instructions to be returned.")
    next_page_token: Optional[StrictStr] = Field(None, alias="nextPageToken", description="A token, which can be sent as 'page_token' to retrieve the next page. If this field is omitted, there are no subsequent pages.")
    __properties = ["counterpartySettlementInstructions", "nextPageToken"]

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
    def from_json(cls, json_str: str) -> V1FilterCounterPartySettlementInstructionsResponse:
        """Create an instance of V1FilterCounterPartySettlementInstructionsResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in counterparty_settlement_instructions (list)
        _items = []
        if self.counterparty_settlement_instructions:
            for _item in self.counterparty_settlement_instructions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['counterpartySettlementInstructions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1FilterCounterPartySettlementInstructionsResponse:
        """Create an instance of V1FilterCounterPartySettlementInstructionsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1FilterCounterPartySettlementInstructionsResponse.parse_obj(obj)

        _obj = V1FilterCounterPartySettlementInstructionsResponse.parse_obj({
            "counterparty_settlement_instructions": [V1CounterPartySettlementInstruction.from_dict(_item) for _item in obj.get("counterpartySettlementInstructions")] if obj.get("counterpartySettlementInstructions") is not None else None,
            "next_page_token": obj.get("nextPageToken")
        })
        return _obj

