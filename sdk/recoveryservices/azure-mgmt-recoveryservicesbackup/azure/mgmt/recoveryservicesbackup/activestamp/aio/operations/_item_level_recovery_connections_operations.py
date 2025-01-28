# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
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
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._item_level_recovery_connections_operations import build_provision_request, build_revoke_request
from .._vendor import RecoveryServicesBackupClientMixinABC

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ItemLevelRecoveryConnectionsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.recoveryservicesbackup.activestamp.aio.RecoveryServicesBackupClient`'s
        :attr:`item_level_recovery_connections` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def provision(  # pylint: disable=inconsistent-return-statements
        self,
        vault_name: str,
        resource_group_name: str,
        fabric_name: str,
        container_name: str,
        protected_item_name: str,
        recovery_point_id: str,
        parameters: _models.ILRRequestResource,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> None:
        """Provisions a script which invokes an iSCSI connection to the backup data. Executing this script
        opens a file
        explorer displaying all the recoverable files and folders. This is an asynchronous operation.
        To know the status of
        provisioning, call GetProtectedItemOperationResult API.

        :param vault_name: The name of the recovery services vault. Required.
        :type vault_name: str
        :param resource_group_name: The name of the resource group where the recovery services vault is
         present. Required.
        :type resource_group_name: str
        :param fabric_name: Fabric name associated with the backed up items. Required.
        :type fabric_name: str
        :param container_name: Container name associated with the backed up items. Required.
        :type container_name: str
        :param protected_item_name: Backed up item name whose files/folders are to be restored.
         Required.
        :type protected_item_name: str
        :param recovery_point_id: Recovery point ID which represents backed up data. iSCSI connection
         will be provisioned
         for this backed up data. Required.
        :type recovery_point_id: str
        :param parameters: resource ILR request. Required.
        :type parameters: ~azure.mgmt.recoveryservicesbackup.activestamp.models.ILRRequestResource
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def provision(  # pylint: disable=inconsistent-return-statements
        self,
        vault_name: str,
        resource_group_name: str,
        fabric_name: str,
        container_name: str,
        protected_item_name: str,
        recovery_point_id: str,
        parameters: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> None:
        """Provisions a script which invokes an iSCSI connection to the backup data. Executing this script
        opens a file
        explorer displaying all the recoverable files and folders. This is an asynchronous operation.
        To know the status of
        provisioning, call GetProtectedItemOperationResult API.

        :param vault_name: The name of the recovery services vault. Required.
        :type vault_name: str
        :param resource_group_name: The name of the resource group where the recovery services vault is
         present. Required.
        :type resource_group_name: str
        :param fabric_name: Fabric name associated with the backed up items. Required.
        :type fabric_name: str
        :param container_name: Container name associated with the backed up items. Required.
        :type container_name: str
        :param protected_item_name: Backed up item name whose files/folders are to be restored.
         Required.
        :type protected_item_name: str
        :param recovery_point_id: Recovery point ID which represents backed up data. iSCSI connection
         will be provisioned
         for this backed up data. Required.
        :type recovery_point_id: str
        :param parameters: resource ILR request. Required.
        :type parameters: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def provision(  # pylint: disable=inconsistent-return-statements
        self,
        vault_name: str,
        resource_group_name: str,
        fabric_name: str,
        container_name: str,
        protected_item_name: str,
        recovery_point_id: str,
        parameters: Union[_models.ILRRequestResource, IO[bytes]],
        **kwargs: Any
    ) -> None:
        """Provisions a script which invokes an iSCSI connection to the backup data. Executing this script
        opens a file
        explorer displaying all the recoverable files and folders. This is an asynchronous operation.
        To know the status of
        provisioning, call GetProtectedItemOperationResult API.

        :param vault_name: The name of the recovery services vault. Required.
        :type vault_name: str
        :param resource_group_name: The name of the resource group where the recovery services vault is
         present. Required.
        :type resource_group_name: str
        :param fabric_name: Fabric name associated with the backed up items. Required.
        :type fabric_name: str
        :param container_name: Container name associated with the backed up items. Required.
        :type container_name: str
        :param protected_item_name: Backed up item name whose files/folders are to be restored.
         Required.
        :type protected_item_name: str
        :param recovery_point_id: Recovery point ID which represents backed up data. iSCSI connection
         will be provisioned
         for this backed up data. Required.
        :type recovery_point_id: str
        :param parameters: resource ILR request. Is either a ILRRequestResource type or a IO[bytes]
         type. Required.
        :type parameters: ~azure.mgmt.recoveryservicesbackup.activestamp.models.ILRRequestResource or
         IO[bytes]
        :return: None or the result of cls(response)
        :rtype: None
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
        cls: ClsType[None] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IOBase, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "ILRRequestResource")

        _request = build_provision_request(
            vault_name=vault_name,
            resource_group_name=resource_group_name,
            fabric_name=fabric_name,
            container_name=container_name,
            protected_item_name=protected_item_name,
            recovery_point_id=recovery_point_id,
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

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def revoke(  # pylint: disable=inconsistent-return-statements
        self,
        vault_name: str,
        resource_group_name: str,
        fabric_name: str,
        container_name: str,
        protected_item_name: str,
        recovery_point_id: str,
        **kwargs: Any
    ) -> None:
        """Revokes an iSCSI connection which can be used to download a script. Executing this script opens
        a file explorer
        displaying all recoverable files and folders. This is an asynchronous operation.

        :param vault_name: The name of the recovery services vault. Required.
        :type vault_name: str
        :param resource_group_name: The name of the resource group where the recovery services vault is
         present. Required.
        :type resource_group_name: str
        :param fabric_name: Fabric name associated with the backed up items. Required.
        :type fabric_name: str
        :param container_name: Container name associated with the backed up items. Required.
        :type container_name: str
        :param protected_item_name: Backed up item name whose files/folders are to be restored.
         Required.
        :type protected_item_name: str
        :param recovery_point_id: Recovery point ID which represents backed up data. iSCSI connection
         will be revoked for
         this backed up data. Required.
        :type recovery_point_id: str
        :return: None or the result of cls(response)
        :rtype: None
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
        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_revoke_request(
            vault_name=vault_name,
            resource_group_name=resource_group_name,
            fabric_name=fabric_name,
            container_name=container_name,
            protected_item_name=protected_item_name,
            recovery_point_id=recovery_point_id,
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

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
