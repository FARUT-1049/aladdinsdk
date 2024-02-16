# coding: utf-8

"""
    Custom Investment Dataset Writer

    API for writing Dataset Definitions and Entities.  _CIDS does not transform the input data in any kind. The writer of the data owns it and is responsible for this data. CIDS provides a way to ingest the custom investment data into Aladdin for usage across Portfolio Management tools._  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictStr, constr

class CIDWriterAPICreateCIDDatasetDefinition400Response(BaseModel):
    """
    Defines an error that occurred.
    """
    code: constr(strict=True, max_length=40) = Field(..., description="A short mnemonic reference code for the error.")
    message: StrictStr = Field(..., description="A human readable description of the error.")
    __properties = ["code", "message"]

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
    def from_json(cls, json_str: str) -> CIDWriterAPICreateCIDDatasetDefinition400Response:
        """Create an instance of CIDWriterAPICreateCIDDatasetDefinition400Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CIDWriterAPICreateCIDDatasetDefinition400Response:
        """Create an instance of CIDWriterAPICreateCIDDatasetDefinition400Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CIDWriterAPICreateCIDDatasetDefinition400Response.parse_obj(obj)

        _obj = CIDWriterAPICreateCIDDatasetDefinition400Response.parse_obj({
            "code": obj.get("code"),
            "message": obj.get("message")
        })
        return _obj
