# coding: utf-8

"""
    Custom Investment Dataset Reader

    API for reading Dataset Definitions and Entities.  _CIDS does not transform the input data in any kind. The writer of the data owns it and is responsible for this data. CIDS provides a way to ingest the custom investment data into Aladdin for usage across Portfolio Management tools._  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class V1PermGroup(str, Enum):
    """
    Describes permission group identification for a Category, Class, Group or leaf level Dataset. Permissions can be added at Category and Class level only. And is always inherited by Group and Leaf level Dataset.   - PERM_GROUP_UNSPECIFIED: Unspecified perm group defaults to INDIVIDUAL for Category Dataset and to INHERITED for other level Datasets.  - PERM_GROUP_INDIVIDUAL: This perm group means the Dataset entry will need to be added to LIST_PERM_GROUP Decodes to add permissions on this Dataset. This value is only permitted for category and class Dataset.  - PERM_GROUP_INHERITED: This perm group means the permissions will be resolved from parents. This value is only permitted for class, group and leaf Datasets.
    """

    """
    allowed enum values
    """
    PERM_GROUP_UNSPECIFIED = 'PERM_GROUP_UNSPECIFIED'
    PERM_GROUP_INDIVIDUAL = 'PERM_GROUP_INDIVIDUAL'
    PERM_GROUP_INHERITED = 'PERM_GROUP_INHERITED'

    @classmethod
    def from_json(cls, json_str: str) -> V1PermGroup:
        """Create an instance of V1PermGroup from a JSON string"""
        return V1PermGroup(json.loads(json_str))

