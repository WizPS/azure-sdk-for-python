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
from ...operations._configuration_operations import build_get_request, build_patch_request

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ConfigurationOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.eventhub.v2021_11_01.aio.EventHubManagementClient`'s
        :attr:`configuration` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")
        self._api_version = input_args.pop(0) if input_args else kwargs.pop("api_version")

    @overload
    async def patch(
        self,
        resource_group_name: str,
        cluster_name: str,
        parameters: _models.ClusterQuotaConfigurationProperties,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> Optional[_models.ClusterQuotaConfigurationProperties]:
        """Replace all specified Event Hubs Cluster settings with those contained in the request body.
        Leaves the settings not specified in the request body unmodified.

        :param resource_group_name: Name of the resource group within the azure subscription. Required.
        :type resource_group_name: str
        :param cluster_name: The name of the Event Hubs Cluster. Required.
        :type cluster_name: str
        :param parameters: Parameters for creating an Event Hubs Cluster resource. Required.
        :type parameters: ~azure.mgmt.eventhub.v2021_11_01.models.ClusterQuotaConfigurationProperties
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ClusterQuotaConfigurationProperties or None or the result of cls(response)
        :rtype: ~azure.mgmt.eventhub.v2021_11_01.models.ClusterQuotaConfigurationProperties or None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def patch(
        self,
        resource_group_name: str,
        cluster_name: str,
        parameters: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> Optional[_models.ClusterQuotaConfigurationProperties]:
        """Replace all specified Event Hubs Cluster settings with those contained in the request body.
        Leaves the settings not specified in the request body unmodified.

        :param resource_group_name: Name of the resource group within the azure subscription. Required.
        :type resource_group_name: str
        :param cluster_name: The name of the Event Hubs Cluster. Required.
        :type cluster_name: str
        :param parameters: Parameters for creating an Event Hubs Cluster resource. Required.
        :type parameters: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ClusterQuotaConfigurationProperties or None or the result of cls(response)
        :rtype: ~azure.mgmt.eventhub.v2021_11_01.models.ClusterQuotaConfigurationProperties or None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def patch(
        self,
        resource_group_name: str,
        cluster_name: str,
        parameters: Union[_models.ClusterQuotaConfigurationProperties, IO[bytes]],
        **kwargs: Any
    ) -> Optional[_models.ClusterQuotaConfigurationProperties]:
        """Replace all specified Event Hubs Cluster settings with those contained in the request body.
        Leaves the settings not specified in the request body unmodified.

        :param resource_group_name: Name of the resource group within the azure subscription. Required.
        :type resource_group_name: str
        :param cluster_name: The name of the Event Hubs Cluster. Required.
        :type cluster_name: str
        :param parameters: Parameters for creating an Event Hubs Cluster resource. Is either a
         ClusterQuotaConfigurationProperties type or a IO[bytes] type. Required.
        :type parameters: ~azure.mgmt.eventhub.v2021_11_01.models.ClusterQuotaConfigurationProperties
         or IO[bytes]
        :return: ClusterQuotaConfigurationProperties or None or the result of cls(response)
        :rtype: ~azure.mgmt.eventhub.v2021_11_01.models.ClusterQuotaConfigurationProperties or None
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2021-11-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[Optional[_models.ClusterQuotaConfigurationProperties]] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IOBase, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "ClusterQuotaConfigurationProperties")

        _request = build_patch_request(
            resource_group_name=resource_group_name,
            cluster_name=cluster_name,
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

        if response.status_code not in [200, 201, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = None
        deserialized = self._deserialize("ClusterQuotaConfigurationProperties", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def get(
        self, resource_group_name: str, cluster_name: str, **kwargs: Any
    ) -> _models.ClusterQuotaConfigurationProperties:
        """Get all Event Hubs Cluster settings - a collection of key/value pairs which represent the
        quotas and settings imposed on the cluster.

        :param resource_group_name: Name of the resource group within the azure subscription. Required.
        :type resource_group_name: str
        :param cluster_name: The name of the Event Hubs Cluster. Required.
        :type cluster_name: str
        :return: ClusterQuotaConfigurationProperties or the result of cls(response)
        :rtype: ~azure.mgmt.eventhub.v2021_11_01.models.ClusterQuotaConfigurationProperties
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2021-11-01"))
        cls: ClsType[_models.ClusterQuotaConfigurationProperties] = kwargs.pop("cls", None)

        _request = build_get_request(
            resource_group_name=resource_group_name,
            cluster_name=cluster_name,
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

        deserialized = self._deserialize("ClusterQuotaConfigurationProperties", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
