# coding: utf-8

"""
    Order

    Filter, post or cancel orders. An order is a directive from a portfolio manager to the trading desk to execute a particular investment decision.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool
from aladdinsdk.api.codegen.trading.order_management.order.v1.OrderAPI.models.v1_basket_id_criterion import V1BasketIdCriterion
from aladdinsdk.api.codegen.trading.order_management.order.v1.OrderAPI.models.v1_external_id_criterion import V1ExternalIdCriterion
from aladdinsdk.api.codegen.trading.order_management.order.v1.OrderAPI.models.v1_external_id_list_criterion import V1ExternalIdListCriterion
from aladdinsdk.api.codegen.trading.order_management.order.v1.OrderAPI.models.v1_order_ids_criterion import V1OrderIdsCriterion
from aladdinsdk.api.codegen.trading.order_management.order.v1.OrderAPI.models.v1_portfolio_group_criterion import V1PortfolioGroupCriterion

class V1OrderQuery(BaseModel):
    """
    V1OrderQuery
    """
    retrieve_order_reservations: Optional[StrictBool] = Field(None, alias="retrieveOrderReservations")
    order_id_criterion: Optional[V1OrderIdsCriterion] = Field(None, alias="orderIdCriterion")
    external_id_criterion: Optional[V1ExternalIdCriterion] = Field(None, alias="externalIdCriterion")
    external_id_list_criterion: Optional[V1ExternalIdListCriterion] = Field(None, alias="externalIdListCriterion")
    portfolio_group_criterion: Optional[V1PortfolioGroupCriterion] = Field(None, alias="portfolioGroupCriterion")
    basket_id_criterion: Optional[V1BasketIdCriterion] = Field(None, alias="basketIdCriterion")
    __properties = ["retrieveOrderReservations", "orderIdCriterion", "externalIdCriterion", "externalIdListCriterion", "portfolioGroupCriterion", "basketIdCriterion"]

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
    def from_json(cls, json_str: str) -> V1OrderQuery:
        """Create an instance of V1OrderQuery from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of order_id_criterion
        if self.order_id_criterion:
            _dict['orderIdCriterion'] = self.order_id_criterion.to_dict()
        # override the default output from pydantic by calling `to_dict()` of external_id_criterion
        if self.external_id_criterion:
            _dict['externalIdCriterion'] = self.external_id_criterion.to_dict()
        # override the default output from pydantic by calling `to_dict()` of external_id_list_criterion
        if self.external_id_list_criterion:
            _dict['externalIdListCriterion'] = self.external_id_list_criterion.to_dict()
        # override the default output from pydantic by calling `to_dict()` of portfolio_group_criterion
        if self.portfolio_group_criterion:
            _dict['portfolioGroupCriterion'] = self.portfolio_group_criterion.to_dict()
        # override the default output from pydantic by calling `to_dict()` of basket_id_criterion
        if self.basket_id_criterion:
            _dict['basketIdCriterion'] = self.basket_id_criterion.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1OrderQuery:
        """Create an instance of V1OrderQuery from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1OrderQuery.parse_obj(obj)

        _obj = V1OrderQuery.parse_obj({
            "retrieve_order_reservations": obj.get("retrieveOrderReservations"),
            "order_id_criterion": V1OrderIdsCriterion.from_dict(obj.get("orderIdCriterion")) if obj.get("orderIdCriterion") is not None else None,
            "external_id_criterion": V1ExternalIdCriterion.from_dict(obj.get("externalIdCriterion")) if obj.get("externalIdCriterion") is not None else None,
            "external_id_list_criterion": V1ExternalIdListCriterion.from_dict(obj.get("externalIdListCriterion")) if obj.get("externalIdListCriterion") is not None else None,
            "portfolio_group_criterion": V1PortfolioGroupCriterion.from_dict(obj.get("portfolioGroupCriterion")) if obj.get("portfolioGroupCriterion") is not None else None,
            "basket_id_criterion": V1BasketIdCriterion.from_dict(obj.get("basketIdCriterion")) if obj.get("basketIdCriterion") is not None else None
        })
        return _obj
