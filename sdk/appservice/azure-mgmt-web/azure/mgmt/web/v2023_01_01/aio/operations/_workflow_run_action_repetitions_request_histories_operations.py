# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, AsyncIterable, Callable, Dict, Optional, TypeVar
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
from ...operations._workflow_run_action_repetitions_request_histories_operations import (
    build_get_request,
    build_list_request,
)

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class WorkflowRunActionRepetitionsRequestHistoriesOperations:  # pylint: disable=name-too-long
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.web.v2023_01_01.aio.WebSiteManagementClient`'s
        :attr:`workflow_run_action_repetitions_request_histories` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")
        self._api_version = input_args.pop(0) if input_args else kwargs.pop("api_version")

    @distributed_trace
    def list(
        self,
        resource_group_name: str,
        name: str,
        workflow_name: str,
        run_name: str,
        action_name: str,
        repetition_name: str,
        **kwargs: Any
    ) -> AsyncIterable["_models.RequestHistory"]:
        """List a workflow run repetition request history.

        :param resource_group_name: Name of the resource group to which the resource belongs. Required.
        :type resource_group_name: str
        :param name: Site name. Required.
        :type name: str
        :param workflow_name: The workflow name. Required.
        :type workflow_name: str
        :param run_name: The workflow run name. Required.
        :type run_name: str
        :param action_name: The workflow action name. Required.
        :type action_name: str
        :param repetition_name: The workflow repetition. Required.
        :type repetition_name: str
        :return: An iterator like instance of either RequestHistory or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.web.v2023_01_01.models.RequestHistory]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2023-01-01"))
        cls: ClsType[_models.RequestHistoryListResult] = kwargs.pop("cls", None)

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
                    name=name,
                    workflow_name=workflow_name,
                    run_name=run_name,
                    action_name=action_name,
                    repetition_name=repetition_name,
                    subscription_id=self._config.subscription_id,
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
            deserialized = self._deserialize("RequestHistoryListResult", pipeline_response)
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
        self,
        resource_group_name: str,
        name: str,
        workflow_name: str,
        run_name: str,
        action_name: str,
        repetition_name: str,
        request_history_name: str,
        **kwargs: Any
    ) -> _models.RequestHistory:
        """Gets a workflow run repetition request history.

        :param resource_group_name: Name of the resource group to which the resource belongs. Required.
        :type resource_group_name: str
        :param name: Site name. Required.
        :type name: str
        :param workflow_name: The workflow name. Required.
        :type workflow_name: str
        :param run_name: The workflow run name. Required.
        :type run_name: str
        :param action_name: The workflow action name. Required.
        :type action_name: str
        :param repetition_name: The workflow repetition. Required.
        :type repetition_name: str
        :param request_history_name: The request history name. Required.
        :type request_history_name: str
        :return: RequestHistory or the result of cls(response)
        :rtype: ~azure.mgmt.web.v2023_01_01.models.RequestHistory
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2023-01-01"))
        cls: ClsType[_models.RequestHistory] = kwargs.pop("cls", None)

        _request = build_get_request(
            resource_group_name=resource_group_name,
            name=name,
            workflow_name=workflow_name,
            run_name=run_name,
            action_name=action_name,
            repetition_name=repetition_name,
            request_history_name=request_history_name,
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

        deserialized = self._deserialize("RequestHistory", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
