# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import sys
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, overload
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
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ...operations._encryption_scopes_operations import (
    build_get_request,
    build_list_request,
    build_patch_request,
    build_put_request,
)

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class EncryptionScopesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.storage.v2023_05_01.aio.StorageManagementClient`'s
        :attr:`encryption_scopes` attribute.
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
    async def put(
        self,
        resource_group_name: str,
        account_name: str,
        encryption_scope_name: str,
        encryption_scope: _models.EncryptionScope,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.EncryptionScope:
        """Synchronously creates or updates an encryption scope under the specified storage account. If an
        encryption scope is already created and a subsequent request is issued with different
        properties, the encryption scope properties will be updated per the specified request.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :param encryption_scope_name: The name of the encryption scope within the specified storage
         account. Encryption scope names must be between 3 and 63 characters in length and use numbers,
         lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and
         followed by a letter or number. Required.
        :type encryption_scope_name: str
        :param encryption_scope: Encryption scope properties to be used for the create or update.
         Required.
        :type encryption_scope: ~azure.mgmt.storage.v2023_05_01.models.EncryptionScope
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: EncryptionScope or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2023_05_01.models.EncryptionScope
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def put(
        self,
        resource_group_name: str,
        account_name: str,
        encryption_scope_name: str,
        encryption_scope: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.EncryptionScope:
        """Synchronously creates or updates an encryption scope under the specified storage account. If an
        encryption scope is already created and a subsequent request is issued with different
        properties, the encryption scope properties will be updated per the specified request.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :param encryption_scope_name: The name of the encryption scope within the specified storage
         account. Encryption scope names must be between 3 and 63 characters in length and use numbers,
         lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and
         followed by a letter or number. Required.
        :type encryption_scope_name: str
        :param encryption_scope: Encryption scope properties to be used for the create or update.
         Required.
        :type encryption_scope: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: EncryptionScope or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2023_05_01.models.EncryptionScope
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def put(
        self,
        resource_group_name: str,
        account_name: str,
        encryption_scope_name: str,
        encryption_scope: Union[_models.EncryptionScope, IO[bytes]],
        **kwargs: Any
    ) -> _models.EncryptionScope:
        """Synchronously creates or updates an encryption scope under the specified storage account. If an
        encryption scope is already created and a subsequent request is issued with different
        properties, the encryption scope properties will be updated per the specified request.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :param encryption_scope_name: The name of the encryption scope within the specified storage
         account. Encryption scope names must be between 3 and 63 characters in length and use numbers,
         lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and
         followed by a letter or number. Required.
        :type encryption_scope_name: str
        :param encryption_scope: Encryption scope properties to be used for the create or update. Is
         either a EncryptionScope type or a IO[bytes] type. Required.
        :type encryption_scope: ~azure.mgmt.storage.v2023_05_01.models.EncryptionScope or IO[bytes]
        :return: EncryptionScope or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2023_05_01.models.EncryptionScope
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2023-05-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.EncryptionScope] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(encryption_scope, (IOBase, bytes)):
            _content = encryption_scope
        else:
            _json = self._serialize.body(encryption_scope, "EncryptionScope")

        _request = build_put_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            encryption_scope_name=encryption_scope_name,
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

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("EncryptionScope", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def patch(
        self,
        resource_group_name: str,
        account_name: str,
        encryption_scope_name: str,
        encryption_scope: _models.EncryptionScope,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.EncryptionScope:
        """Update encryption scope properties as specified in the request body. Update fails if the
        specified encryption scope does not already exist.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :param encryption_scope_name: The name of the encryption scope within the specified storage
         account. Encryption scope names must be between 3 and 63 characters in length and use numbers,
         lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and
         followed by a letter or number. Required.
        :type encryption_scope_name: str
        :param encryption_scope: Encryption scope properties to be used for the update. Required.
        :type encryption_scope: ~azure.mgmt.storage.v2023_05_01.models.EncryptionScope
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: EncryptionScope or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2023_05_01.models.EncryptionScope
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def patch(
        self,
        resource_group_name: str,
        account_name: str,
        encryption_scope_name: str,
        encryption_scope: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.EncryptionScope:
        """Update encryption scope properties as specified in the request body. Update fails if the
        specified encryption scope does not already exist.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :param encryption_scope_name: The name of the encryption scope within the specified storage
         account. Encryption scope names must be between 3 and 63 characters in length and use numbers,
         lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and
         followed by a letter or number. Required.
        :type encryption_scope_name: str
        :param encryption_scope: Encryption scope properties to be used for the update. Required.
        :type encryption_scope: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: EncryptionScope or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2023_05_01.models.EncryptionScope
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def patch(
        self,
        resource_group_name: str,
        account_name: str,
        encryption_scope_name: str,
        encryption_scope: Union[_models.EncryptionScope, IO[bytes]],
        **kwargs: Any
    ) -> _models.EncryptionScope:
        """Update encryption scope properties as specified in the request body. Update fails if the
        specified encryption scope does not already exist.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :param encryption_scope_name: The name of the encryption scope within the specified storage
         account. Encryption scope names must be between 3 and 63 characters in length and use numbers,
         lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and
         followed by a letter or number. Required.
        :type encryption_scope_name: str
        :param encryption_scope: Encryption scope properties to be used for the update. Is either a
         EncryptionScope type or a IO[bytes] type. Required.
        :type encryption_scope: ~azure.mgmt.storage.v2023_05_01.models.EncryptionScope or IO[bytes]
        :return: EncryptionScope or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2023_05_01.models.EncryptionScope
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2023-05-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.EncryptionScope] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(encryption_scope, (IOBase, bytes)):
            _content = encryption_scope
        else:
            _json = self._serialize.body(encryption_scope, "EncryptionScope")

        _request = build_patch_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            encryption_scope_name=encryption_scope_name,
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

        deserialized = self._deserialize("EncryptionScope", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def get(
        self, resource_group_name: str, account_name: str, encryption_scope_name: str, **kwargs: Any
    ) -> _models.EncryptionScope:
        """Returns the properties for the specified encryption scope.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :param encryption_scope_name: The name of the encryption scope within the specified storage
         account. Encryption scope names must be between 3 and 63 characters in length and use numbers,
         lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and
         followed by a letter or number. Required.
        :type encryption_scope_name: str
        :return: EncryptionScope or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2023_05_01.models.EncryptionScope
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2023-05-01"))
        cls: ClsType[_models.EncryptionScope] = kwargs.pop("cls", None)

        _request = build_get_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            encryption_scope_name=encryption_scope_name,
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

        deserialized = self._deserialize("EncryptionScope", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def list(
        self,
        resource_group_name: str,
        account_name: str,
        maxpagesize: Optional[int] = None,
        filter: Optional[str] = None,
        include: Optional[Union[str, _models.ListEncryptionScopesInclude]] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.EncryptionScope"]:
        """Lists all the encryption scopes available under the specified storage account.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :param maxpagesize: Optional, specifies the maximum number of encryption scopes that will be
         included in the list response. Default value is None.
        :type maxpagesize: int
        :param filter: Optional. When specified, only encryption scope names starting with the filter
         will be listed. Default value is None.
        :type filter: str
        :param include: Optional, when specified, will list encryption scopes with the specific state.
         Defaults to All. Known values are: "All", "Enabled", and "Disabled". Default value is None.
        :type include: str or ~azure.mgmt.storage.v2023_05_01.models.ListEncryptionScopesInclude
        :return: An iterator like instance of either EncryptionScope or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.storage.v2023_05_01.models.EncryptionScope]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2023-05-01"))
        cls: ClsType[_models.EncryptionScopeListResult] = kwargs.pop("cls", None)

        error_map: MutableMapping = {
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
                    account_name=account_name,
                    subscription_id=self._config.subscription_id,
                    maxpagesize=maxpagesize,
                    filter=filter,
                    include=include,
                    api_version=api_version,
                    headers=_headers,
                    params=_params,
                )
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
                _next_request_params["api-version"] = self._api_version
                _request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                _request.url = self._client.format_url(_request.url)
                _request.method = "GET"
            return _request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("EncryptionScopeListResult", pipeline_response)
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
