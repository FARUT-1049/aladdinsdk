# coding: utf-8

"""
    Risk Governance - Tasks

    Retrieve Tasks, as surfaced in Risk Radar, which are aggregates that comprise of related Exceptions, Rules, and Workflow items.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from datetime import datetime

from pydantic import Field, StrictStr, conlist

from typing import Optional

from aladdinsdk.api.codegen.analytics.oversight.governance.v1.RiskTaskAPI.models.v1_list_risk_tasks_response import V1ListRiskTasksResponse

from aladdinsdk.api.codegen.analytics.oversight.governance.v1.RiskTaskAPI.api_client import ApiClient
from aladdinsdk.api.codegen.analytics.oversight.governance.v1.RiskTaskAPI.api_response import ApiResponse
from aladdinsdk.api.codegen.analytics.oversight.governance.v1.RiskTaskAPI.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class DefaultRiskTaskAPI(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def risk_task_api_list_risk_tasks(self, vnd_com_blackrock_request_id : Annotated[StrictStr, Field(..., description="A unique identifier for this request.")], vnd_com_blackrock_origin_timestamp : Annotated[datetime, Field(..., description="Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231.")], workflow_states : Annotated[Optional[conlist(StrictStr)], Field(description="A list of workflow states used to filter returned tasks. If parameter value is not provided, only tasks with workflow items with non-terminal states will be returned. If terminal states are provided and the begin range time is not provided, the workflow  items returned for these states will be restricted to a lookback period of 45 days.")] = None, workflow_begin_range_time : Annotated[Optional[datetime], Field(description="The workflow start date and time from which to apply the provided search parameters.")] = None, workflow_end_range_time : Annotated[Optional[datetime], Field(description="The workflow end date and time to which to apply the provided search parameters.")] = None, **kwargs) -> V1ListRiskTasksResponse:  # noqa: E501
        """Retrieve list of Tasks  # noqa: E501

        Provides list of tasks (workflow, exceptions and rule combined) matching to search parameters provided.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.risk_task_api_list_risk_tasks(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, workflow_states, workflow_begin_range_time, workflow_end_range_time, async_req=True)
        >>> result = thread.get()

        :param vnd_com_blackrock_request_id: A unique identifier for this request. (required)
        :type vnd_com_blackrock_request_id: str
        :param vnd_com_blackrock_origin_timestamp: Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231. (required)
        :type vnd_com_blackrock_origin_timestamp: datetime
        :param workflow_states: A list of workflow states used to filter returned tasks. If parameter value is not provided, only tasks with workflow items with non-terminal states will be returned. If terminal states are provided and the begin range time is not provided, the workflow  items returned for these states will be restricted to a lookback period of 45 days.
        :type workflow_states: List[str]
        :param workflow_begin_range_time: The workflow start date and time from which to apply the provided search parameters.
        :type workflow_begin_range_time: datetime
        :param workflow_end_range_time: The workflow end date and time to which to apply the provided search parameters.
        :type workflow_end_range_time: datetime
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: V1ListRiskTasksResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the risk_task_api_list_risk_tasks_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.risk_task_api_list_risk_tasks_with_http_info(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, workflow_states, workflow_begin_range_time, workflow_end_range_time, **kwargs)  # noqa: E501

    @validate_arguments
    def risk_task_api_list_risk_tasks_with_http_info(self, vnd_com_blackrock_request_id : Annotated[StrictStr, Field(..., description="A unique identifier for this request.")], vnd_com_blackrock_origin_timestamp : Annotated[datetime, Field(..., description="Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231.")], workflow_states : Annotated[Optional[conlist(StrictStr)], Field(description="A list of workflow states used to filter returned tasks. If parameter value is not provided, only tasks with workflow items with non-terminal states will be returned. If terminal states are provided and the begin range time is not provided, the workflow  items returned for these states will be restricted to a lookback period of 45 days.")] = None, workflow_begin_range_time : Annotated[Optional[datetime], Field(description="The workflow start date and time from which to apply the provided search parameters.")] = None, workflow_end_range_time : Annotated[Optional[datetime], Field(description="The workflow end date and time to which to apply the provided search parameters.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve list of Tasks  # noqa: E501

        Provides list of tasks (workflow, exceptions and rule combined) matching to search parameters provided.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.risk_task_api_list_risk_tasks_with_http_info(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, workflow_states, workflow_begin_range_time, workflow_end_range_time, async_req=True)
        >>> result = thread.get()

        :param vnd_com_blackrock_request_id: A unique identifier for this request. (required)
        :type vnd_com_blackrock_request_id: str
        :param vnd_com_blackrock_origin_timestamp: Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231. (required)
        :type vnd_com_blackrock_origin_timestamp: datetime
        :param workflow_states: A list of workflow states used to filter returned tasks. If parameter value is not provided, only tasks with workflow items with non-terminal states will be returned. If terminal states are provided and the begin range time is not provided, the workflow  items returned for these states will be restricted to a lookback period of 45 days.
        :type workflow_states: List[str]
        :param workflow_begin_range_time: The workflow start date and time from which to apply the provided search parameters.
        :type workflow_begin_range_time: datetime
        :param workflow_end_range_time: The workflow end date and time to which to apply the provided search parameters.
        :type workflow_end_range_time: datetime
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(V1ListRiskTasksResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'vnd_com_blackrock_request_id',
            'vnd_com_blackrock_origin_timestamp',
            'workflow_states',
            'workflow_begin_range_time',
            'workflow_end_range_time'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method risk_task_api_list_risk_tasks" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('workflow_states') is not None:  # noqa: E501
            _query_params.append(('workflowStates', _params['workflow_states']))
            _collection_formats['workflowStates'] = 'multi'

        if _params.get('workflow_begin_range_time') is not None:  # noqa: E501
            if isinstance(_params['workflow_begin_range_time'], datetime):
                _query_params.append(('workflowBeginRangeTime', _params['workflow_begin_range_time'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('workflowBeginRangeTime', _params['workflow_begin_range_time']))

        if _params.get('workflow_end_range_time') is not None:  # noqa: E501
            if isinstance(_params['workflow_end_range_time'], datetime):
                _query_params.append(('workflowEndRangeTime', _params['workflow_end_range_time'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('workflowEndRangeTime', _params['workflow_end_range_time']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['vnd_com_blackrock_request_id']:
            _header_params['VND.com.blackrock.Request-ID'] = _params['vnd_com_blackrock_request_id']

        if _params['vnd_com_blackrock_origin_timestamp']:
            _header_params['VND.com.blackrock.Origin-Timestamp'] = _params['vnd_com_blackrock_origin_timestamp']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['APIKeyHeader', 'OAuth2ClientCredentials', 'basicAuth', 'OAuth2AccessCode', 'ClientKeyHeader']  # noqa: E501

        _response_types_map = {
            '200': "V1ListRiskTasksResponse",
            '400': "RiskTaskAPIListRiskTasks400Response",
            '401': "RiskTaskAPIListRiskTasks400Response",
            '403': "RiskTaskAPIListRiskTasks400Response",
            '404': "RiskTaskAPIListRiskTasks400Response",
        }

        return self.api_client.call_api(
            '/tasks', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
