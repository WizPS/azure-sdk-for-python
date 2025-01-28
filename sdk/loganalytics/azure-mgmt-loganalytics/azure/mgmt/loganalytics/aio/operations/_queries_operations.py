# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import sys
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, Type, TypeVar, Union, overload

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ...operations._queries_operations import (
    build_delete_request,
    build_get_request,
    build_list_request,
    build_put_request,
    build_search_request,
    build_update_request,
)

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class QueriesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.loganalytics.aio.LogAnalyticsManagementClient`'s
        :attr:`queries` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list(
        self,
        resource_group_name: str,
        query_pack_name: str,
        top: Optional[int] = None,
        include_body: Optional[bool] = None,
        skip_token: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.LogAnalyticsQueryPackQuery"]:
        """Gets a list of Queries defined within a Log Analytics QueryPack.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param query_pack_name: The name of the Log Analytics QueryPack resource. Required.
        :type query_pack_name: str
        :param top: Maximum items returned in page. Default value is None.
        :type top: int
        :param include_body: Flag indicating whether or not to return the body of each applicable
         query. If false, only return the query information. Default value is None.
        :type include_body: bool
        :param skip_token: Base64 encoded token used to fetch the next page of items. Default is null.
         Default value is None.
        :type skip_token: str
        :return: An iterator like instance of either LogAnalyticsQueryPackQuery or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.loganalytics.models.LogAnalyticsQueryPackQuery]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2019-09-01"))
        cls: ClsType[_models.LogAnalyticsQueryPackQueryListResult] = kwargs.pop("cls", None)

        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_list_request(
                    resource_group_name=resource_group_name,
                    query_pack_name=query_pack_name,
                    subscription_id=self._config.subscription_id,
                    top=top,
                    include_body=include_body,
                    skip_token=skip_token,
                    api_version=api_version,
                    headers=_headers,
                    params=_params,
                )
                _request.url = self._client.format_url(_request.url)

            else:
                _request = HttpRequest("GET", next_link)
                _request.url = self._client.format_url(_request.url)
                _request.method = "GET"
            return _request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("LogAnalyticsQueryPackQueryListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                _request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    @overload
    def search(
        self,
        resource_group_name: str,
        query_pack_name: str,
        query_search_properties: _models.LogAnalyticsQueryPackQuerySearchProperties,
        top: Optional[int] = None,
        include_body: Optional[bool] = None,
        skip_token: Optional[str] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncIterable["_models.LogAnalyticsQueryPackQuery"]:
        """Search a list of Queries defined within a Log Analytics QueryPack according to given search
        properties.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param query_pack_name: The name of the Log Analytics QueryPack resource. Required.
        :type query_pack_name: str
        :param query_search_properties: Properties by which to search queries in the given Log
         Analytics QueryPack. Required.
        :type query_search_properties:
         ~azure.mgmt.loganalytics.models.LogAnalyticsQueryPackQuerySearchProperties
        :param top: Maximum items returned in page. Default value is None.
        :type top: int
        :param include_body: Flag indicating whether or not to return the body of each applicable
         query. If false, only return the query information. Default value is None.
        :type include_body: bool
        :param skip_token: Base64 encoded token used to fetch the next page of items. Default is null.
         Default value is None.
        :type skip_token: str
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An iterator like instance of either LogAnalyticsQueryPackQuery or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.loganalytics.models.LogAnalyticsQueryPackQuery]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def search(
        self,
        resource_group_name: str,
        query_pack_name: str,
        query_search_properties: IO[bytes],
        top: Optional[int] = None,
        include_body: Optional[bool] = None,
        skip_token: Optional[str] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncIterable["_models.LogAnalyticsQueryPackQuery"]:
        """Search a list of Queries defined within a Log Analytics QueryPack according to given search
        properties.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param query_pack_name: The name of the Log Analytics QueryPack resource. Required.
        :type query_pack_name: str
        :param query_search_properties: Properties by which to search queries in the given Log
         Analytics QueryPack. Required.
        :type query_search_properties: IO[bytes]
        :param top: Maximum items returned in page. Default value is None.
        :type top: int
        :param include_body: Flag indicating whether or not to return the body of each applicable
         query. If false, only return the query information. Default value is None.
        :type include_body: bool
        :param skip_token: Base64 encoded token used to fetch the next page of items. Default is null.
         Default value is None.
        :type skip_token: str
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An iterator like instance of either LogAnalyticsQueryPackQuery or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.loganalytics.models.LogAnalyticsQueryPackQuery]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def search(
        self,
        resource_group_name: str,
        query_pack_name: str,
        query_search_properties: Union[_models.LogAnalyticsQueryPackQuerySearchProperties, IO[bytes]],
        top: Optional[int] = None,
        include_body: Optional[bool] = None,
        skip_token: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.LogAnalyticsQueryPackQuery"]:
        """Search a list of Queries defined within a Log Analytics QueryPack according to given search
        properties.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param query_pack_name: The name of the Log Analytics QueryPack resource. Required.
        :type query_pack_name: str
        :param query_search_properties: Properties by which to search queries in the given Log
         Analytics QueryPack. Is either a LogAnalyticsQueryPackQuerySearchProperties type or a IO[bytes]
         type. Required.
        :type query_search_properties:
         ~azure.mgmt.loganalytics.models.LogAnalyticsQueryPackQuerySearchProperties or IO[bytes]
        :param top: Maximum items returned in page. Default value is None.
        :type top: int
        :param include_body: Flag indicating whether or not to return the body of each applicable
         query. If false, only return the query information. Default value is None.
        :type include_body: bool
        :param skip_token: Base64 encoded token used to fetch the next page of items. Default is null.
         Default value is None.
        :type skip_token: str
        :return: An iterator like instance of either LogAnalyticsQueryPackQuery or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.loganalytics.models.LogAnalyticsQueryPackQuery]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2019-09-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.LogAnalyticsQueryPackQueryListResult] = kwargs.pop("cls", None)

        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})
        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(query_search_properties, (IOBase, bytes)):
            _content = query_search_properties
        else:
            _json = self._serialize.body(query_search_properties, "LogAnalyticsQueryPackQuerySearchProperties")

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_search_request(
                    resource_group_name=resource_group_name,
                    query_pack_name=query_pack_name,
                    subscription_id=self._config.subscription_id,
                    top=top,
                    include_body=include_body,
                    skip_token=skip_token,
                    api_version=api_version,
                    content_type=content_type,
                    json=_json,
                    content=_content,
                    headers=_headers,
                    params=_params,
                )
                _request.url = self._client.format_url(_request.url)

            else:
                _request = HttpRequest("GET", next_link)
                _request.url = self._client.format_url(_request.url)
                _request.method = "GET"
            return _request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("LogAnalyticsQueryPackQueryListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                _request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    @distributed_trace_async
    async def get(
        self, resource_group_name: str, query_pack_name: str, id: str, **kwargs: Any
    ) -> _models.LogAnalyticsQueryPackQuery:
        """Gets a specific Log Analytics Query defined within a Log Analytics QueryPack.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param query_pack_name: The name of the Log Analytics QueryPack resource. Required.
        :type query_pack_name: str
        :param id: The id of a specific query defined in the Log Analytics QueryPack. Required.
        :type id: str
        :return: LogAnalyticsQueryPackQuery or the result of cls(response)
        :rtype: ~azure.mgmt.loganalytics.models.LogAnalyticsQueryPackQuery
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2019-09-01"))
        cls: ClsType[_models.LogAnalyticsQueryPackQuery] = kwargs.pop("cls", None)

        _request = build_get_request(
            resource_group_name=resource_group_name,
            query_pack_name=query_pack_name,
            id=id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("LogAnalyticsQueryPackQuery", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def put(
        self,
        resource_group_name: str,
        query_pack_name: str,
        id: str,
        query_payload: _models.LogAnalyticsQueryPackQuery,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.LogAnalyticsQueryPackQuery:
        """Adds or Updates a specific Query within a Log Analytics QueryPack.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param query_pack_name: The name of the Log Analytics QueryPack resource. Required.
        :type query_pack_name: str
        :param id: The id of a specific query defined in the Log Analytics QueryPack. Required.
        :type id: str
        :param query_payload: Properties that need to be specified to create a new query and add it to
         a Log Analytics QueryPack. Required.
        :type query_payload: ~azure.mgmt.loganalytics.models.LogAnalyticsQueryPackQuery
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: LogAnalyticsQueryPackQuery or the result of cls(response)
        :rtype: ~azure.mgmt.loganalytics.models.LogAnalyticsQueryPackQuery
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def put(
        self,
        resource_group_name: str,
        query_pack_name: str,
        id: str,
        query_payload: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.LogAnalyticsQueryPackQuery:
        """Adds or Updates a specific Query within a Log Analytics QueryPack.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param query_pack_name: The name of the Log Analytics QueryPack resource. Required.
        :type query_pack_name: str
        :param id: The id of a specific query defined in the Log Analytics QueryPack. Required.
        :type id: str
        :param query_payload: Properties that need to be specified to create a new query and add it to
         a Log Analytics QueryPack. Required.
        :type query_payload: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: LogAnalyticsQueryPackQuery or the result of cls(response)
        :rtype: ~azure.mgmt.loganalytics.models.LogAnalyticsQueryPackQuery
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def put(
        self,
        resource_group_name: str,
        query_pack_name: str,
        id: str,
        query_payload: Union[_models.LogAnalyticsQueryPackQuery, IO[bytes]],
        **kwargs: Any
    ) -> _models.LogAnalyticsQueryPackQuery:
        """Adds or Updates a specific Query within a Log Analytics QueryPack.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param query_pack_name: The name of the Log Analytics QueryPack resource. Required.
        :type query_pack_name: str
        :param id: The id of a specific query defined in the Log Analytics QueryPack. Required.
        :type id: str
        :param query_payload: Properties that need to be specified to create a new query and add it to
         a Log Analytics QueryPack. Is either a LogAnalyticsQueryPackQuery type or a IO[bytes] type.
         Required.
        :type query_payload: ~azure.mgmt.loganalytics.models.LogAnalyticsQueryPackQuery or IO[bytes]
        :return: LogAnalyticsQueryPackQuery or the result of cls(response)
        :rtype: ~azure.mgmt.loganalytics.models.LogAnalyticsQueryPackQuery
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2019-09-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.LogAnalyticsQueryPackQuery] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(query_payload, (IOBase, bytes)):
            _content = query_payload
        else:
            _json = self._serialize.body(query_payload, "LogAnalyticsQueryPackQuery")

        _request = build_put_request(
            resource_group_name=resource_group_name,
            query_pack_name=query_pack_name,
            id=id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("LogAnalyticsQueryPackQuery", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def update(
        self,
        resource_group_name: str,
        query_pack_name: str,
        id: str,
        query_payload: _models.LogAnalyticsQueryPackQuery,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.LogAnalyticsQueryPackQuery:
        """Adds or Updates a specific Query within a Log Analytics QueryPack.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param query_pack_name: The name of the Log Analytics QueryPack resource. Required.
        :type query_pack_name: str
        :param id: The id of a specific query defined in the Log Analytics QueryPack. Required.
        :type id: str
        :param query_payload: Properties that need to be specified to create a new query and add it to
         a Log Analytics QueryPack. Required.
        :type query_payload: ~azure.mgmt.loganalytics.models.LogAnalyticsQueryPackQuery
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: LogAnalyticsQueryPackQuery or the result of cls(response)
        :rtype: ~azure.mgmt.loganalytics.models.LogAnalyticsQueryPackQuery
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self,
        resource_group_name: str,
        query_pack_name: str,
        id: str,
        query_payload: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.LogAnalyticsQueryPackQuery:
        """Adds or Updates a specific Query within a Log Analytics QueryPack.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param query_pack_name: The name of the Log Analytics QueryPack resource. Required.
        :type query_pack_name: str
        :param id: The id of a specific query defined in the Log Analytics QueryPack. Required.
        :type id: str
        :param query_payload: Properties that need to be specified to create a new query and add it to
         a Log Analytics QueryPack. Required.
        :type query_payload: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: LogAnalyticsQueryPackQuery or the result of cls(response)
        :rtype: ~azure.mgmt.loganalytics.models.LogAnalyticsQueryPackQuery
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def update(
        self,
        resource_group_name: str,
        query_pack_name: str,
        id: str,
        query_payload: Union[_models.LogAnalyticsQueryPackQuery, IO[bytes]],
        **kwargs: Any
    ) -> _models.LogAnalyticsQueryPackQuery:
        """Adds or Updates a specific Query within a Log Analytics QueryPack.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param query_pack_name: The name of the Log Analytics QueryPack resource. Required.
        :type query_pack_name: str
        :param id: The id of a specific query defined in the Log Analytics QueryPack. Required.
        :type id: str
        :param query_payload: Properties that need to be specified to create a new query and add it to
         a Log Analytics QueryPack. Is either a LogAnalyticsQueryPackQuery type or a IO[bytes] type.
         Required.
        :type query_payload: ~azure.mgmt.loganalytics.models.LogAnalyticsQueryPackQuery or IO[bytes]
        :return: LogAnalyticsQueryPackQuery or the result of cls(response)
        :rtype: ~azure.mgmt.loganalytics.models.LogAnalyticsQueryPackQuery
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2019-09-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.LogAnalyticsQueryPackQuery] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(query_payload, (IOBase, bytes)):
            _content = query_payload
        else:
            _json = self._serialize.body(query_payload, "LogAnalyticsQueryPackQuery")

        _request = build_update_request(
            resource_group_name=resource_group_name,
            query_pack_name=query_pack_name,
            id=id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("LogAnalyticsQueryPackQuery", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, query_pack_name: str, id: str, **kwargs: Any
    ) -> None:
        """Deletes a specific Query defined within an Log Analytics QueryPack.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param query_pack_name: The name of the Log Analytics QueryPack resource. Required.
        :type query_pack_name: str
        :param id: The id of a specific query defined in the Log Analytics QueryPack. Required.
        :type id: str
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2019-09-01"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_delete_request(
            resource_group_name=resource_group_name,
            query_pack_name=query_pack_name,
            id=id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
