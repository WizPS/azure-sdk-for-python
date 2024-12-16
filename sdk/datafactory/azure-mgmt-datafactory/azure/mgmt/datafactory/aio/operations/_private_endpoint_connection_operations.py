# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

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
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ...operations._private_endpoint_connection_operations import (
    build_create_or_update_request,
    build_delete_request,
    build_get_request,
)

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class PrivateEndpointConnectionOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.datafactory.aio.DataFactoryManagementClient`'s
        :attr:`private_endpoint_connection` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        factory_name: str,
        private_endpoint_connection_name: str,
        private_endpoint_wrapper: _models.PrivateLinkConnectionApprovalRequestResource,
        if_match: Optional[str] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.PrivateEndpointConnectionResource:
        """Approves or rejects a private endpoint connection.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param factory_name: The factory name. Required.
        :type factory_name: str
        :param private_endpoint_connection_name: The private endpoint connection name. Required.
        :type private_endpoint_connection_name: str
        :param private_endpoint_wrapper: Required.
        :type private_endpoint_wrapper:
         ~azure.mgmt.datafactory.models.PrivateLinkConnectionApprovalRequestResource
        :param if_match: ETag of the private endpoint connection entity.  Should only be specified for
         update, for which it should match existing entity or can be * for unconditional update. Default
         value is None.
        :type if_match: str
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: PrivateEndpointConnectionResource or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.PrivateEndpointConnectionResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        factory_name: str,
        private_endpoint_connection_name: str,
        private_endpoint_wrapper: IO[bytes],
        if_match: Optional[str] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.PrivateEndpointConnectionResource:
        """Approves or rejects a private endpoint connection.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param factory_name: The factory name. Required.
        :type factory_name: str
        :param private_endpoint_connection_name: The private endpoint connection name. Required.
        :type private_endpoint_connection_name: str
        :param private_endpoint_wrapper: Required.
        :type private_endpoint_wrapper: IO[bytes]
        :param if_match: ETag of the private endpoint connection entity.  Should only be specified for
         update, for which it should match existing entity or can be * for unconditional update. Default
         value is None.
        :type if_match: str
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: PrivateEndpointConnectionResource or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.PrivateEndpointConnectionResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_or_update(
        self,
        resource_group_name: str,
        factory_name: str,
        private_endpoint_connection_name: str,
        private_endpoint_wrapper: Union[_models.PrivateLinkConnectionApprovalRequestResource, IO[bytes]],
        if_match: Optional[str] = None,
        **kwargs: Any
    ) -> _models.PrivateEndpointConnectionResource:
        """Approves or rejects a private endpoint connection.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param factory_name: The factory name. Required.
        :type factory_name: str
        :param private_endpoint_connection_name: The private endpoint connection name. Required.
        :type private_endpoint_connection_name: str
        :param private_endpoint_wrapper: Is either a PrivateLinkConnectionApprovalRequestResource type
         or a IO[bytes] type. Required.
        :type private_endpoint_wrapper:
         ~azure.mgmt.datafactory.models.PrivateLinkConnectionApprovalRequestResource or IO[bytes]
        :param if_match: ETag of the private endpoint connection entity.  Should only be specified for
         update, for which it should match existing entity or can be * for unconditional update. Default
         value is None.
        :type if_match: str
        :return: PrivateEndpointConnectionResource or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.PrivateEndpointConnectionResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
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
        cls: ClsType[_models.PrivateEndpointConnectionResource] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(private_endpoint_wrapper, (IOBase, bytes)):
            _content = private_endpoint_wrapper
        else:
            _json = self._serialize.body(private_endpoint_wrapper, "PrivateLinkConnectionApprovalRequestResource")

        _request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            factory_name=factory_name,
            private_endpoint_connection_name=private_endpoint_connection_name,
            subscription_id=self._config.subscription_id,
            if_match=if_match,
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
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("PrivateEndpointConnectionResource", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        factory_name: str,
        private_endpoint_connection_name: str,
        if_none_match: Optional[str] = None,
        **kwargs: Any
    ) -> _models.PrivateEndpointConnectionResource:
        """Gets a private endpoint connection.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param factory_name: The factory name. Required.
        :type factory_name: str
        :param private_endpoint_connection_name: The private endpoint connection name. Required.
        :type private_endpoint_connection_name: str
        :param if_none_match: ETag of the private endpoint connection entity. Should only be specified
         for get. If the ETag matches the existing entity tag, or if * was provided, then no content
         will be returned. Default value is None.
        :type if_none_match: str
        :return: PrivateEndpointConnectionResource or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.PrivateEndpointConnectionResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.PrivateEndpointConnectionResource] = kwargs.pop("cls", None)

        _request = build_get_request(
            resource_group_name=resource_group_name,
            factory_name=factory_name,
            private_endpoint_connection_name=private_endpoint_connection_name,
            subscription_id=self._config.subscription_id,
            if_none_match=if_none_match,
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
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("PrivateEndpointConnectionResource", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def delete(
        self, resource_group_name: str, factory_name: str, private_endpoint_connection_name: str, **kwargs: Any
    ) -> None:
        """Deletes a private endpoint connection.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param factory_name: The factory name. Required.
        :type factory_name: str
        :param private_endpoint_connection_name: The private endpoint connection name. Required.
        :type private_endpoint_connection_name: str
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
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
            factory_name=factory_name,
            private_endpoint_connection_name=private_endpoint_connection_name,
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
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
