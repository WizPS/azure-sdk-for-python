# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, cast, overload
import urllib.parse

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
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._partner_topics_operations import (
    build_activate_request,
    build_create_or_update_request,
    build_deactivate_request,
    build_delete_request,
    build_get_request,
    build_list_by_resource_group_request,
    build_list_by_subscription_request,
    build_update_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class PartnerTopicsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.eventgrid.aio.EventGridManagementClient`'s
        :attr:`partner_topics` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get(self, resource_group_name: str, partner_topic_name: str, **kwargs: Any) -> _models.PartnerTopic:
        """Get a partner topic.

        Get properties of a partner topic.

        :param resource_group_name: The name of the resource group within the user's subscription.
         Required.
        :type resource_group_name: str
        :param partner_topic_name: Name of the partner topic. Required.
        :type partner_topic_name: str
        :return: PartnerTopic or the result of cls(response)
        :rtype: ~azure.mgmt.eventgrid.models.PartnerTopic
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.PartnerTopic] = kwargs.pop("cls", None)

        _request = build_get_request(
            resource_group_name=resource_group_name,
            partner_topic_name=partner_topic_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("PartnerTopic", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        partner_topic_name: str,
        partner_topic_info: _models.PartnerTopic,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.PartnerTopic:
        """Create a partner topic.

        Asynchronously creates a new partner topic with the specified parameters.

        :param resource_group_name: The name of the resource group within the user's subscription.
         Required.
        :type resource_group_name: str
        :param partner_topic_name: Name of the partner topic. Required.
        :type partner_topic_name: str
        :param partner_topic_info: Partner Topic information. Required.
        :type partner_topic_info: ~azure.mgmt.eventgrid.models.PartnerTopic
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: PartnerTopic or the result of cls(response)
        :rtype: ~azure.mgmt.eventgrid.models.PartnerTopic
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        partner_topic_name: str,
        partner_topic_info: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.PartnerTopic:
        """Create a partner topic.

        Asynchronously creates a new partner topic with the specified parameters.

        :param resource_group_name: The name of the resource group within the user's subscription.
         Required.
        :type resource_group_name: str
        :param partner_topic_name: Name of the partner topic. Required.
        :type partner_topic_name: str
        :param partner_topic_info: Partner Topic information. Required.
        :type partner_topic_info: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: PartnerTopic or the result of cls(response)
        :rtype: ~azure.mgmt.eventgrid.models.PartnerTopic
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_or_update(
        self,
        resource_group_name: str,
        partner_topic_name: str,
        partner_topic_info: Union[_models.PartnerTopic, IO[bytes]],
        **kwargs: Any
    ) -> _models.PartnerTopic:
        """Create a partner topic.

        Asynchronously creates a new partner topic with the specified parameters.

        :param resource_group_name: The name of the resource group within the user's subscription.
         Required.
        :type resource_group_name: str
        :param partner_topic_name: Name of the partner topic. Required.
        :type partner_topic_name: str
        :param partner_topic_info: Partner Topic information. Is either a PartnerTopic type or a
         IO[bytes] type. Required.
        :type partner_topic_info: ~azure.mgmt.eventgrid.models.PartnerTopic or IO[bytes]
        :return: PartnerTopic or the result of cls(response)
        :rtype: ~azure.mgmt.eventgrid.models.PartnerTopic
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.PartnerTopic] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(partner_topic_info, (IOBase, bytes)):
            _content = partner_topic_info
        else:
            _json = self._serialize.body(partner_topic_info, "PartnerTopic")

        _request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            partner_topic_name=partner_topic_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("PartnerTopic", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("PartnerTopic", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    async def _delete_initial(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, partner_topic_name: str, **kwargs: Any
    ) -> None:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_delete_request(
            resource_group_name=resource_group_name,
            partner_topic_name=partner_topic_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 202:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        if cls:
            return cls(pipeline_response, None, response_headers)  # type: ignore

    @distributed_trace_async
    async def begin_delete(
        self, resource_group_name: str, partner_topic_name: str, **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """Delete a partner topic.

        Delete existing partner topic.

        :param resource_group_name: The name of the resource group within the user's subscription.
         Required.
        :type resource_group_name: str
        :param partner_topic_name: Name of the partner topic. Required.
        :type partner_topic_name: str
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[None] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._delete_initial(  # type: ignore
                resource_group_name=resource_group_name,
                partner_topic_name=partner_topic_name,
                api_version=api_version,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):  # pylint: disable=inconsistent-return-statements
            if cls:
                return cls(pipeline_response, None, {})  # type: ignore

        if polling is True:
            polling_method: AsyncPollingMethod = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[None].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[None](self._client, raw_result, get_long_running_output, polling_method)  # type: ignore

    @overload
    async def update(
        self,
        resource_group_name: str,
        partner_topic_name: str,
        partner_topic_update_parameters: _models.PartnerTopicUpdateParameters,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> Optional[_models.PartnerTopic]:
        """Update a partner topic.

        Asynchronously updates a partner topic with the specified parameters.

        :param resource_group_name: The name of the resource group within the user's subscription.
         Required.
        :type resource_group_name: str
        :param partner_topic_name: Name of the partner topic. Required.
        :type partner_topic_name: str
        :param partner_topic_update_parameters: PartnerTopic update information. Required.
        :type partner_topic_update_parameters:
         ~azure.mgmt.eventgrid.models.PartnerTopicUpdateParameters
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: PartnerTopic or None or the result of cls(response)
        :rtype: ~azure.mgmt.eventgrid.models.PartnerTopic or None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self,
        resource_group_name: str,
        partner_topic_name: str,
        partner_topic_update_parameters: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> Optional[_models.PartnerTopic]:
        """Update a partner topic.

        Asynchronously updates a partner topic with the specified parameters.

        :param resource_group_name: The name of the resource group within the user's subscription.
         Required.
        :type resource_group_name: str
        :param partner_topic_name: Name of the partner topic. Required.
        :type partner_topic_name: str
        :param partner_topic_update_parameters: PartnerTopic update information. Required.
        :type partner_topic_update_parameters: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: PartnerTopic or None or the result of cls(response)
        :rtype: ~azure.mgmt.eventgrid.models.PartnerTopic or None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def update(
        self,
        resource_group_name: str,
        partner_topic_name: str,
        partner_topic_update_parameters: Union[_models.PartnerTopicUpdateParameters, IO[bytes]],
        **kwargs: Any
    ) -> Optional[_models.PartnerTopic]:
        """Update a partner topic.

        Asynchronously updates a partner topic with the specified parameters.

        :param resource_group_name: The name of the resource group within the user's subscription.
         Required.
        :type resource_group_name: str
        :param partner_topic_name: Name of the partner topic. Required.
        :type partner_topic_name: str
        :param partner_topic_update_parameters: PartnerTopic update information. Is either a
         PartnerTopicUpdateParameters type or a IO[bytes] type. Required.
        :type partner_topic_update_parameters:
         ~azure.mgmt.eventgrid.models.PartnerTopicUpdateParameters or IO[bytes]
        :return: PartnerTopic or None or the result of cls(response)
        :rtype: ~azure.mgmt.eventgrid.models.PartnerTopic or None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[Optional[_models.PartnerTopic]] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(partner_topic_update_parameters, (IOBase, bytes)):
            _content = partner_topic_update_parameters
        else:
            _json = self._serialize.body(partner_topic_update_parameters, "PartnerTopicUpdateParameters")

        _request = build_update_request(
            resource_group_name=resource_group_name,
            partner_topic_name=partner_topic_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 201:
            deserialized = self._deserialize("PartnerTopic", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def list_by_subscription(
        self, filter: Optional[str] = None, top: Optional[int] = None, **kwargs: Any
    ) -> AsyncIterable["_models.PartnerTopic"]:
        """List partner topics under an Azure subscription.

        List all the partner topics under an Azure subscription.

        :param filter: The query used to filter the search results using OData syntax. Filtering is
         permitted on the 'name' property only and with limited number of OData operations. These
         operations are: the 'contains' function as well as the following logical operations: not, and,
         or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The
         following is a valid filter example: $filter=contains(namE, 'PATTERN') and name ne 'PATTERN-1'.
         The following is not a valid filter example: $filter=location eq 'westus'. Default value is
         None.
        :type filter: str
        :param top: The number of results to return per page for the list operation. Valid range for
         top parameter is 1 to 100. If not specified, the default number of results to be returned is 20
         items per page. Default value is None.
        :type top: int
        :return: An iterator like instance of either PartnerTopic or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.eventgrid.models.PartnerTopic]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.PartnerTopicsListResult] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_list_by_subscription_request(
                    subscription_id=self._config.subscription_id,
                    filter=filter,
                    top=top,
                    api_version=api_version,
                    headers=_headers,
                    params=_params,
                )
                _request = _convert_request(_request)
                _request.url = self._client.format_url(_request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                _request = _convert_request(_request)
                _request.url = self._client.format_url(_request.url)
                _request.method = "GET"
            return _request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("PartnerTopicsListResult", pipeline_response)
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
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    @distributed_trace
    def list_by_resource_group(
        self, resource_group_name: str, filter: Optional[str] = None, top: Optional[int] = None, **kwargs: Any
    ) -> AsyncIterable["_models.PartnerTopic"]:
        """List partner topics under a resource group.

        List all the partner topics under a resource group.

        :param resource_group_name: The name of the resource group within the user's subscription.
         Required.
        :type resource_group_name: str
        :param filter: The query used to filter the search results using OData syntax. Filtering is
         permitted on the 'name' property only and with limited number of OData operations. These
         operations are: the 'contains' function as well as the following logical operations: not, and,
         or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The
         following is a valid filter example: $filter=contains(namE, 'PATTERN') and name ne 'PATTERN-1'.
         The following is not a valid filter example: $filter=location eq 'westus'. Default value is
         None.
        :type filter: str
        :param top: The number of results to return per page for the list operation. Valid range for
         top parameter is 1 to 100. If not specified, the default number of results to be returned is 20
         items per page. Default value is None.
        :type top: int
        :return: An iterator like instance of either PartnerTopic or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.eventgrid.models.PartnerTopic]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.PartnerTopicsListResult] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_list_by_resource_group_request(
                    resource_group_name=resource_group_name,
                    subscription_id=self._config.subscription_id,
                    filter=filter,
                    top=top,
                    api_version=api_version,
                    headers=_headers,
                    params=_params,
                )
                _request = _convert_request(_request)
                _request.url = self._client.format_url(_request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                _request = _convert_request(_request)
                _request.url = self._client.format_url(_request.url)
                _request.method = "GET"
            return _request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("PartnerTopicsListResult", pipeline_response)
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
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    @distributed_trace_async
    async def activate(self, resource_group_name: str, partner_topic_name: str, **kwargs: Any) -> _models.PartnerTopic:
        """Activate a partner topic.

        Activate a newly created partner topic.

        :param resource_group_name: The name of the resource group within the user's subscription.
         Required.
        :type resource_group_name: str
        :param partner_topic_name: Name of the partner topic. Required.
        :type partner_topic_name: str
        :return: PartnerTopic or the result of cls(response)
        :rtype: ~azure.mgmt.eventgrid.models.PartnerTopic
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.PartnerTopic] = kwargs.pop("cls", None)

        _request = build_activate_request(
            resource_group_name=resource_group_name,
            partner_topic_name=partner_topic_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("PartnerTopic", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def deactivate(
        self, resource_group_name: str, partner_topic_name: str, **kwargs: Any
    ) -> _models.PartnerTopic:
        """Deactivate a partner topic.

        Deactivate specific partner topic.

        :param resource_group_name: The name of the resource group within the user's subscription.
         Required.
        :type resource_group_name: str
        :param partner_topic_name: Name of the partner topic. Required.
        :type partner_topic_name: str
        :return: PartnerTopic or the result of cls(response)
        :rtype: ~azure.mgmt.eventgrid.models.PartnerTopic
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.PartnerTopic] = kwargs.pop("cls", None)

        _request = build_deactivate_request(
            resource_group_name=resource_group_name,
            partner_topic_name=partner_topic_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("PartnerTopic", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
