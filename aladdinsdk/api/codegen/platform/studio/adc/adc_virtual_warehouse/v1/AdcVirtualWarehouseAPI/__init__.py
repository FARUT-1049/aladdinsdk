# coding: utf-8

# flake8: noqa

"""
    Adc Virtual Warehouse

    Manages Virtual Warehouses for Aladdin Data Cloud (ADC). Used by Studio's ADC Admin Center.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


__version__ = "1.0.0"

# import apis into sdk package
from aladdinsdk.api.codegen.platform.studio.adc.adc_virtual_warehouse.v1.AdcVirtualWarehouseAPI.api.default_adc_virtual_warehouse_api import DefaultAdcVirtualWarehouseAPI

# import ApiClient
from aladdinsdk.api.codegen.platform.studio.adc.adc_virtual_warehouse.v1.AdcVirtualWarehouseAPI.api_response import ApiResponse
from aladdinsdk.api.codegen.platform.studio.adc.adc_virtual_warehouse.v1.AdcVirtualWarehouseAPI.api_client import ApiClient
from aladdinsdk.api.codegen.platform.studio.adc.adc_virtual_warehouse.v1.AdcVirtualWarehouseAPI.configuration import Configuration
from aladdinsdk.api.codegen.platform.studio.adc.adc_virtual_warehouse.v1.AdcVirtualWarehouseAPI.exceptions import OpenApiException
from aladdinsdk.api.codegen.platform.studio.adc.adc_virtual_warehouse.v1.AdcVirtualWarehouseAPI.exceptions import ApiTypeError
from aladdinsdk.api.codegen.platform.studio.adc.adc_virtual_warehouse.v1.AdcVirtualWarehouseAPI.exceptions import ApiValueError
from aladdinsdk.api.codegen.platform.studio.adc.adc_virtual_warehouse.v1.AdcVirtualWarehouseAPI.exceptions import ApiKeyError
from aladdinsdk.api.codegen.platform.studio.adc.adc_virtual_warehouse.v1.AdcVirtualWarehouseAPI.exceptions import ApiAttributeError
from aladdinsdk.api.codegen.platform.studio.adc.adc_virtual_warehouse.v1.AdcVirtualWarehouseAPI.exceptions import ApiException

# import models into sdk package
from aladdinsdk.api.codegen.platform.studio.adc.adc_virtual_warehouse.v1.AdcVirtualWarehouseAPI.models.adc_virtual_warehouse_api_activate_adc_virtual_warehouse400_response import AdcVirtualWarehouseAPIActivateAdcVirtualWarehouse400Response
from aladdinsdk.api.codegen.platform.studio.adc.adc_virtual_warehouse.v1.AdcVirtualWarehouseAPI.models.any import Any
from aladdinsdk.api.codegen.platform.studio.adc.adc_virtual_warehouse.v1.AdcVirtualWarehouseAPI.models.rpc_status import RpcStatus
from aladdinsdk.api.codegen.platform.studio.adc.adc_virtual_warehouse.v1.AdcVirtualWarehouseAPI.models.v1_activate_adc_virtual_warehouse_request import V1ActivateAdcVirtualWarehouseRequest
from aladdinsdk.api.codegen.platform.studio.adc.adc_virtual_warehouse.v1.AdcVirtualWarehouseAPI.models.v1_adc_virtual_warehouse import V1AdcVirtualWarehouse
from aladdinsdk.api.codegen.platform.studio.adc.adc_virtual_warehouse.v1.AdcVirtualWarehouseAPI.models.v1_adc_virtual_warehouse_operation_response import V1AdcVirtualWarehouseOperationResponse
from aladdinsdk.api.codegen.platform.studio.adc.adc_virtual_warehouse.v1.AdcVirtualWarehouseAPI.models.v1_adc_virtual_warehouse_scaling_policy import V1AdcVirtualWarehouseScalingPolicy
from aladdinsdk.api.codegen.platform.studio.adc.adc_virtual_warehouse.v1.AdcVirtualWarehouseAPI.models.v1_adc_virtual_warehouse_size import V1AdcVirtualWarehouseSize
from aladdinsdk.api.codegen.platform.studio.adc.adc_virtual_warehouse.v1.AdcVirtualWarehouseAPI.models.v1_adc_virtual_warehouse_type import V1AdcVirtualWarehouseType
from aladdinsdk.api.codegen.platform.studio.adc.adc_virtual_warehouse.v1.AdcVirtualWarehouseAPI.models.v1_adc_virtual_warehouses import V1AdcVirtualWarehouses
from aladdinsdk.api.codegen.platform.studio.adc.adc_virtual_warehouse.v1.AdcVirtualWarehouseAPI.models.v1_adc_virtual_warehouses_against_functional_role import V1AdcVirtualWarehousesAgainstFunctionalRole
from aladdinsdk.api.codegen.platform.studio.adc.adc_virtual_warehouse.v1.AdcVirtualWarehouseAPI.models.v1_list_adc_virtual_warehouses_response import V1ListAdcVirtualWarehousesResponse
from aladdinsdk.api.codegen.platform.studio.adc.adc_virtual_warehouse.v1.AdcVirtualWarehouseAPI.models.v1_list_all_permissioned_adc_virtual_warehouse_response import V1ListAllPermissionedAdcVirtualWarehouseResponse
from aladdinsdk.api.codegen.platform.studio.adc.adc_virtual_warehouse.v1.AdcVirtualWarehouseAPI.models.v1_resume_adc_virtual_warehouse_request import V1ResumeAdcVirtualWarehouseRequest
from aladdinsdk.api.codegen.platform.studio.adc.adc_virtual_warehouse.v1.AdcVirtualWarehouseAPI.models.v1_resume_adc_virtual_warehouse_response import V1ResumeAdcVirtualWarehouseResponse
from aladdinsdk.api.codegen.platform.studio.adc.adc_virtual_warehouse.v1.AdcVirtualWarehouseAPI.models.v1_suspend_adc_virtual_warehouse_request import V1SuspendAdcVirtualWarehouseRequest
from aladdinsdk.api.codegen.platform.studio.adc.adc_virtual_warehouse.v1.AdcVirtualWarehouseAPI.models.v1_suspend_adc_virtual_warehouse_response import V1SuspendAdcVirtualWarehouseResponse