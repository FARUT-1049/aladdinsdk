# coding: utf-8

"""
    Portfolio Configuration Record For Accounting

    Configurations API for Aladdin Accounting allows you to access accounting configuration attributes for process types that portfolios are setup on. Data can be sourced in aggregate and filtered to improve oversight and scale of configuration monitoring. This API allows for retrieval of key data points for portfolio configurations by various parameters, including portfolio tickers, processCodes, and more.  # noqa: E501

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

from pydantic import Field, StrictStr

from aladdinsdk.api.codegen.accounting.configuration.attribute.portfolio.records.v1.PortfolioConfigurationAPI.models.v1_filter_portfolio_configuration_records_request import V1FilterPortfolioConfigurationRecordsRequest
from aladdinsdk.api.codegen.accounting.configuration.attribute.portfolio.records.v1.PortfolioConfigurationAPI.models.v1_filter_portfolio_configuration_records_response import V1FilterPortfolioConfigurationRecordsResponse
from aladdinsdk.api.codegen.accounting.configuration.attribute.portfolio.records.v1.PortfolioConfigurationAPI.models.v1_longrunning_operation import V1LongrunningOperation
from aladdinsdk.api.codegen.accounting.configuration.attribute.portfolio.records.v1.PortfolioConfigurationAPI.models.v1_portfolio_configuration_records_request import V1PortfolioConfigurationRecordsRequest

from aladdinsdk.api.codegen.accounting.configuration.attribute.portfolio.records.v1.PortfolioConfigurationAPI.api_client import ApiClient
from aladdinsdk.api.codegen.accounting.configuration.attribute.portfolio.records.v1.PortfolioConfigurationAPI.api_response import ApiResponse
from aladdinsdk.api.codegen.accounting.configuration.attribute.portfolio.records.v1.PortfolioConfigurationAPI.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class DefaultPortfolioConfigurationAPI(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def portfolio_configuration_api_filter_portfolio_configuration_records(self, vnd_com_blackrock_request_id : Annotated[StrictStr, Field(..., description="A unique identifier for this request.")], vnd_com_blackrock_origin_timestamp : Annotated[datetime, Field(..., description="Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231.")], body : V1FilterPortfolioConfigurationRecordsRequest, **kwargs) -> V1FilterPortfolioConfigurationRecordsResponse:  # noqa: E501
        """Filter Portfolio Configurations  # noqa: E501

        Filter for portfolio configuration records based on a number of parameters including tickers, processCodes, and more. For large requests that may result in timeout, it is recommended to use long running endpoint. Below are some best practices/guidelines to limit the size of the query -    a) Keep includeHistory as false    b) Restrict the number of process code in the request    c) Keep the number of portfolio tickers to 350 per process code    d) Restricting the records by the providing the attribute names (-- api-linter: aladdin::9016::rpc-name=disabled  aip.dev/not-precedent: We need to do this because keeping generic endpoint --) (-- api-linter: aladdin::9016::query-custom-method-http=disabled  aip.dev/not-precedent: We need to do this because using custom method name --)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.portfolio_configuration_api_filter_portfolio_configuration_records(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, body, async_req=True)
        >>> result = thread.get()

        :param vnd_com_blackrock_request_id: A unique identifier for this request. (required)
        :type vnd_com_blackrock_request_id: str
        :param vnd_com_blackrock_origin_timestamp: Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231. (required)
        :type vnd_com_blackrock_origin_timestamp: datetime
        :param body: (required)
        :type body: V1FilterPortfolioConfigurationRecordsRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: V1FilterPortfolioConfigurationRecordsResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the portfolio_configuration_api_filter_portfolio_configuration_records_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.portfolio_configuration_api_filter_portfolio_configuration_records_with_http_info(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, body, **kwargs)  # noqa: E501

    @validate_arguments
    def portfolio_configuration_api_filter_portfolio_configuration_records_with_http_info(self, vnd_com_blackrock_request_id : Annotated[StrictStr, Field(..., description="A unique identifier for this request.")], vnd_com_blackrock_origin_timestamp : Annotated[datetime, Field(..., description="Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231.")], body : V1FilterPortfolioConfigurationRecordsRequest, **kwargs) -> ApiResponse:  # noqa: E501
        """Filter Portfolio Configurations  # noqa: E501

        Filter for portfolio configuration records based on a number of parameters including tickers, processCodes, and more. For large requests that may result in timeout, it is recommended to use long running endpoint. Below are some best practices/guidelines to limit the size of the query -    a) Keep includeHistory as false    b) Restrict the number of process code in the request    c) Keep the number of portfolio tickers to 350 per process code    d) Restricting the records by the providing the attribute names (-- api-linter: aladdin::9016::rpc-name=disabled  aip.dev/not-precedent: We need to do this because keeping generic endpoint --) (-- api-linter: aladdin::9016::query-custom-method-http=disabled  aip.dev/not-precedent: We need to do this because using custom method name --)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.portfolio_configuration_api_filter_portfolio_configuration_records_with_http_info(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, body, async_req=True)
        >>> result = thread.get()

        :param vnd_com_blackrock_request_id: A unique identifier for this request. (required)
        :type vnd_com_blackrock_request_id: str
        :param vnd_com_blackrock_origin_timestamp: Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231. (required)
        :type vnd_com_blackrock_origin_timestamp: datetime
        :param body: (required)
        :type body: V1FilterPortfolioConfigurationRecordsRequest
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
        :rtype: tuple(V1FilterPortfolioConfigurationRecordsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'vnd_com_blackrock_request_id',
            'vnd_com_blackrock_origin_timestamp',
            'body'
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
                    " to method portfolio_configuration_api_filter_portfolio_configuration_records" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
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
        if _params['body'] is not None:
            _body_params = _params['body']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['APIKeyHeader', 'OAuth2ClientCredentials', 'basicAuth', 'OAuth2AccessCode', 'ClientKeyHeader']  # noqa: E501

        _response_types_map = {
            '200': "V1FilterPortfolioConfigurationRecordsResponse",
            '400': "PortfolioConfigurationAPIGetLongRunningPortfolioConfigurationRecordStatus400Response",
            '401': "PortfolioConfigurationAPIGetLongRunningPortfolioConfigurationRecordStatus400Response",
            '403': "PortfolioConfigurationAPIGetLongRunningPortfolioConfigurationRecordStatus400Response",
            '404': "PortfolioConfigurationAPIGetLongRunningPortfolioConfigurationRecordStatus400Response",
        }

        return self.api_client.call_api(
            '/configurations:filter', 'POST',
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

    @validate_arguments
    def portfolio_configuration_api_get_long_running_portfolio_configuration_record_status(self, vnd_com_blackrock_request_id : Annotated[StrictStr, Field(..., description="A unique identifier for this request.")], vnd_com_blackrock_origin_timestamp : Annotated[datetime, Field(..., description="Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231.")], id : Annotated[StrictStr, Field(..., description="Id of the LongrunningOperation")], **kwargs) -> V1LongrunningOperation:  # noqa: E501
        """Get Long Running Configuration Filter Status  # noqa: E501

        Retrieve the status and output from the \"Long Running Configuration Filter\" endpoint by providing a request ID. (-- api-linter: core::0131::response-message-name=disabled  aip.dev/not-precedent: We need to do this because need to consistent with backend --) (-- api-linter: aladdin::9002::wordslist-custom-method-http=disabled  aip.dev/not-precedent: We need to do this because to be consistent with api --) (-- api-linter: core::0131::request-message-name=disabled  aip.dev/not-precedent: We need to do this because using exiting long running request object --)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.portfolio_configuration_api_get_long_running_portfolio_configuration_record_status(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, id, async_req=True)
        >>> result = thread.get()

        :param vnd_com_blackrock_request_id: A unique identifier for this request. (required)
        :type vnd_com_blackrock_request_id: str
        :param vnd_com_blackrock_origin_timestamp: Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231. (required)
        :type vnd_com_blackrock_origin_timestamp: datetime
        :param id: Id of the LongrunningOperation (required)
        :type id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: V1LongrunningOperation
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the portfolio_configuration_api_get_long_running_portfolio_configuration_record_status_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.portfolio_configuration_api_get_long_running_portfolio_configuration_record_status_with_http_info(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, id, **kwargs)  # noqa: E501

    @validate_arguments
    def portfolio_configuration_api_get_long_running_portfolio_configuration_record_status_with_http_info(self, vnd_com_blackrock_request_id : Annotated[StrictStr, Field(..., description="A unique identifier for this request.")], vnd_com_blackrock_origin_timestamp : Annotated[datetime, Field(..., description="Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231.")], id : Annotated[StrictStr, Field(..., description="Id of the LongrunningOperation")], **kwargs) -> ApiResponse:  # noqa: E501
        """Get Long Running Configuration Filter Status  # noqa: E501

        Retrieve the status and output from the \"Long Running Configuration Filter\" endpoint by providing a request ID. (-- api-linter: core::0131::response-message-name=disabled  aip.dev/not-precedent: We need to do this because need to consistent with backend --) (-- api-linter: aladdin::9002::wordslist-custom-method-http=disabled  aip.dev/not-precedent: We need to do this because to be consistent with api --) (-- api-linter: core::0131::request-message-name=disabled  aip.dev/not-precedent: We need to do this because using exiting long running request object --)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.portfolio_configuration_api_get_long_running_portfolio_configuration_record_status_with_http_info(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, id, async_req=True)
        >>> result = thread.get()

        :param vnd_com_blackrock_request_id: A unique identifier for this request. (required)
        :type vnd_com_blackrock_request_id: str
        :param vnd_com_blackrock_origin_timestamp: Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231. (required)
        :type vnd_com_blackrock_origin_timestamp: datetime
        :param id: Id of the LongrunningOperation (required)
        :type id: str
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
        :rtype: tuple(V1LongrunningOperation, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'vnd_com_blackrock_request_id',
            'vnd_com_blackrock_origin_timestamp',
            'id'
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
                    " to method portfolio_configuration_api_get_long_running_portfolio_configuration_record_status" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']


        # process the query parameters
        _query_params = []
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
            '200': "V1LongrunningOperation",
            '400': "PortfolioConfigurationAPIGetLongRunningPortfolioConfigurationRecordStatus400Response",
            '401': "PortfolioConfigurationAPIGetLongRunningPortfolioConfigurationRecordStatus400Response",
            '403': "PortfolioConfigurationAPIGetLongRunningPortfolioConfigurationRecordStatus400Response",
            '404': "PortfolioConfigurationAPIGetLongRunningPortfolioConfigurationRecordStatus400Response",
        }

        return self.api_client.call_api(
            '/configurations/{id}:longRunningPortfolioConfigurationRecordStatus', 'GET',
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

    @validate_arguments
    def portfolio_configuration_api_submit_portfolio_configuration_records_request(self, vnd_com_blackrock_request_id : Annotated[StrictStr, Field(..., description="A unique identifier for this request.")], vnd_com_blackrock_origin_timestamp : Annotated[datetime, Field(..., description="Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231.")], body : V1PortfolioConfigurationRecordsRequest, **kwargs) -> V1LongrunningOperation:  # noqa: E501
        """Long Running Configuration Filter Request  # noqa: E501

        Filter for portfolio configuration records for large requests that includes a bigger set of portfolio tickers or a port group.  Option to include expansionType parameter to retrieve output for requests that specify a portfolio group. Response provided is a request ID that can be passed in the \"Get Long Running Configuation Filter Status\" endpoint to retrieve the output. If system analyzes query to be too broad, appropriate exception would be thrown. Below are some best practices/guidelines to limit the size of the query -    a) Keep includeHistory as false    b) Restrict the number of process code in the request    c) Keep the number of portfolio tickers or portfolios in a port group limited to below 7500 per process code    d) Restricting the records by the providing the attribute names (-- api-linter: aladdin::9002::wordslist-custom-method-rpc=disabled  aip.dev/not-precedent: We need to do this because customised name to be consistent with backend api's --) (-- api-linter: aladdin::9002::wordslist-custom-method-http=disabled  aip.dev/not-precedent: We need to do this because to be consistent with backend api's --)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.portfolio_configuration_api_submit_portfolio_configuration_records_request(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, body, async_req=True)
        >>> result = thread.get()

        :param vnd_com_blackrock_request_id: A unique identifier for this request. (required)
        :type vnd_com_blackrock_request_id: str
        :param vnd_com_blackrock_origin_timestamp: Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231. (required)
        :type vnd_com_blackrock_origin_timestamp: datetime
        :param body: (required)
        :type body: V1PortfolioConfigurationRecordsRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: V1LongrunningOperation
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the portfolio_configuration_api_submit_portfolio_configuration_records_request_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.portfolio_configuration_api_submit_portfolio_configuration_records_request_with_http_info(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, body, **kwargs)  # noqa: E501

    @validate_arguments
    def portfolio_configuration_api_submit_portfolio_configuration_records_request_with_http_info(self, vnd_com_blackrock_request_id : Annotated[StrictStr, Field(..., description="A unique identifier for this request.")], vnd_com_blackrock_origin_timestamp : Annotated[datetime, Field(..., description="Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231.")], body : V1PortfolioConfigurationRecordsRequest, **kwargs) -> ApiResponse:  # noqa: E501
        """Long Running Configuration Filter Request  # noqa: E501

        Filter for portfolio configuration records for large requests that includes a bigger set of portfolio tickers or a port group.  Option to include expansionType parameter to retrieve output for requests that specify a portfolio group. Response provided is a request ID that can be passed in the \"Get Long Running Configuation Filter Status\" endpoint to retrieve the output. If system analyzes query to be too broad, appropriate exception would be thrown. Below are some best practices/guidelines to limit the size of the query -    a) Keep includeHistory as false    b) Restrict the number of process code in the request    c) Keep the number of portfolio tickers or portfolios in a port group limited to below 7500 per process code    d) Restricting the records by the providing the attribute names (-- api-linter: aladdin::9002::wordslist-custom-method-rpc=disabled  aip.dev/not-precedent: We need to do this because customised name to be consistent with backend api's --) (-- api-linter: aladdin::9002::wordslist-custom-method-http=disabled  aip.dev/not-precedent: We need to do this because to be consistent with backend api's --)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.portfolio_configuration_api_submit_portfolio_configuration_records_request_with_http_info(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, body, async_req=True)
        >>> result = thread.get()

        :param vnd_com_blackrock_request_id: A unique identifier for this request. (required)
        :type vnd_com_blackrock_request_id: str
        :param vnd_com_blackrock_origin_timestamp: Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231. (required)
        :type vnd_com_blackrock_origin_timestamp: datetime
        :param body: (required)
        :type body: V1PortfolioConfigurationRecordsRequest
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
        :rtype: tuple(V1LongrunningOperation, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'vnd_com_blackrock_request_id',
            'vnd_com_blackrock_origin_timestamp',
            'body'
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
                    " to method portfolio_configuration_api_submit_portfolio_configuration_records_request" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
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
        if _params['body'] is not None:
            _body_params = _params['body']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['APIKeyHeader', 'OAuth2ClientCredentials', 'basicAuth', 'OAuth2AccessCode', 'ClientKeyHeader']  # noqa: E501

        _response_types_map = {
            '200': "V1LongrunningOperation",
            '400': "PortfolioConfigurationAPIGetLongRunningPortfolioConfigurationRecordStatus400Response",
            '401': "PortfolioConfigurationAPIGetLongRunningPortfolioConfigurationRecordStatus400Response",
            '403': "PortfolioConfigurationAPIGetLongRunningPortfolioConfigurationRecordStatus400Response",
            '404': "PortfolioConfigurationAPIGetLongRunningPortfolioConfigurationRecordStatus400Response",
        }

        return self.api_client.call_api(
            '/configurations:submitPortfolioConfigurationRecordsRequest', 'POST',
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