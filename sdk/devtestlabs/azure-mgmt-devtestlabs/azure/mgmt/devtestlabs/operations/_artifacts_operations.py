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
from typing import Any, Callable, Dict, IO, Iterable, Optional, Type, TypeVar, Union, overload
import urllib.parse

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.rest import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._serialization import Serializer

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_list_request(
    resource_group_name: str,
    lab_name: str,
    artifact_source_name: str,
    subscription_id: str,
    *,
    expand: Optional[str] = None,
    filter: Optional[str] = None,
    top: Optional[int] = None,
    orderby: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2018-09-15"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/artifactsources/{artifactSourceName}/artifacts",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "labName": _SERIALIZER.url("lab_name", lab_name, "str"),
        "artifactSourceName": _SERIALIZER.url("artifact_source_name", artifact_source_name, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    if expand is not None:
        _params["$expand"] = _SERIALIZER.query("expand", expand, "str")
    if filter is not None:
        _params["$filter"] = _SERIALIZER.query("filter", filter, "str")
    if top is not None:
        _params["$top"] = _SERIALIZER.query("top", top, "int")
    if orderby is not None:
        _params["$orderby"] = _SERIALIZER.query("orderby", orderby, "str")
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_request(
    resource_group_name: str,
    lab_name: str,
    artifact_source_name: str,
    name: str,
    subscription_id: str,
    *,
    expand: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2018-09-15"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/artifactsources/{artifactSourceName}/artifacts/{name}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "labName": _SERIALIZER.url("lab_name", lab_name, "str"),
        "artifactSourceName": _SERIALIZER.url("artifact_source_name", artifact_source_name, "str"),
        "name": _SERIALIZER.url("name", name, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    if expand is not None:
        _params["$expand"] = _SERIALIZER.query("expand", expand, "str")
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_generate_arm_template_request(
    resource_group_name: str, lab_name: str, artifact_source_name: str, name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2018-09-15"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/artifactsources/{artifactSourceName}/artifacts/{name}/generateArmTemplate",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "labName": _SERIALIZER.url("lab_name", lab_name, "str"),
        "artifactSourceName": _SERIALIZER.url("artifact_source_name", artifact_source_name, "str"),
        "name": _SERIALIZER.url("name", name, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


class ArtifactsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.devtestlabs.DevTestLabsClient`'s
        :attr:`artifacts` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list(
        self,
        resource_group_name: str,
        lab_name: str,
        artifact_source_name: str,
        expand: Optional[str] = None,
        filter: Optional[str] = None,
        top: Optional[int] = None,
        orderby: Optional[str] = None,
        **kwargs: Any
    ) -> Iterable["_models.Artifact"]:
        """List artifacts in a given artifact source.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param lab_name: The name of the lab. Required.
        :type lab_name: str
        :param artifact_source_name: The name of the artifact source. Required.
        :type artifact_source_name: str
        :param expand: Specify the $expand query. Example: 'properties($select=title)'. Default value
         is None.
        :type expand: str
        :param filter: The filter to apply to the operation. Example: '$filter=contains(name,'myName').
         Default value is None.
        :type filter: str
        :param top: The maximum number of resources to return from the operation. Example: '$top=10'.
         Default value is None.
        :type top: int
        :param orderby: The ordering expression for the results, using OData notation. Example:
         '$orderby=name desc'. Default value is None.
        :type orderby: str
        :return: An iterator like instance of either Artifact or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.devtestlabs.models.Artifact]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.ArtifactList] = kwargs.pop("cls", None)

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
                    lab_name=lab_name,
                    artifact_source_name=artifact_source_name,
                    subscription_id=self._config.subscription_id,
                    expand=expand,
                    filter=filter,
                    top=top,
                    orderby=orderby,
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
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                _request.url = self._client.format_url(_request.url)
                _request.method = "GET"
            return _request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("ArtifactList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
                _request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    @distributed_trace
    def get(
        self,
        resource_group_name: str,
        lab_name: str,
        artifact_source_name: str,
        name: str,
        expand: Optional[str] = None,
        **kwargs: Any
    ) -> _models.Artifact:
        """Get artifact.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param lab_name: The name of the lab. Required.
        :type lab_name: str
        :param artifact_source_name: The name of the artifact source. Required.
        :type artifact_source_name: str
        :param name: The name of the artifact. Required.
        :type name: str
        :param expand: Specify the $expand query. Example: 'properties($select=title)'. Default value
         is None.
        :type expand: str
        :return: Artifact or the result of cls(response)
        :rtype: ~azure.mgmt.devtestlabs.models.Artifact
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.Artifact] = kwargs.pop("cls", None)

        _request = build_get_request(
            resource_group_name=resource_group_name,
            lab_name=lab_name,
            artifact_source_name=artifact_source_name,
            name=name,
            subscription_id=self._config.subscription_id,
            expand=expand,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("Artifact", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def generate_arm_template(
        self,
        resource_group_name: str,
        lab_name: str,
        artifact_source_name: str,
        name: str,
        generate_arm_template_request: _models.GenerateArmTemplateRequest,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ArmTemplateInfo:
        """Generates an ARM template for the given artifact, uploads the required files to a storage
        account, and validates the generated artifact.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param lab_name: The name of the lab. Required.
        :type lab_name: str
        :param artifact_source_name: The name of the artifact source. Required.
        :type artifact_source_name: str
        :param name: The name of the artifact. Required.
        :type name: str
        :param generate_arm_template_request: Parameters for generating an ARM template for deploying
         artifacts. Required.
        :type generate_arm_template_request: ~azure.mgmt.devtestlabs.models.GenerateArmTemplateRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ArmTemplateInfo or the result of cls(response)
        :rtype: ~azure.mgmt.devtestlabs.models.ArmTemplateInfo
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def generate_arm_template(
        self,
        resource_group_name: str,
        lab_name: str,
        artifact_source_name: str,
        name: str,
        generate_arm_template_request: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ArmTemplateInfo:
        """Generates an ARM template for the given artifact, uploads the required files to a storage
        account, and validates the generated artifact.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param lab_name: The name of the lab. Required.
        :type lab_name: str
        :param artifact_source_name: The name of the artifact source. Required.
        :type artifact_source_name: str
        :param name: The name of the artifact. Required.
        :type name: str
        :param generate_arm_template_request: Parameters for generating an ARM template for deploying
         artifacts. Required.
        :type generate_arm_template_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ArmTemplateInfo or the result of cls(response)
        :rtype: ~azure.mgmt.devtestlabs.models.ArmTemplateInfo
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def generate_arm_template(
        self,
        resource_group_name: str,
        lab_name: str,
        artifact_source_name: str,
        name: str,
        generate_arm_template_request: Union[_models.GenerateArmTemplateRequest, IO[bytes]],
        **kwargs: Any
    ) -> _models.ArmTemplateInfo:
        """Generates an ARM template for the given artifact, uploads the required files to a storage
        account, and validates the generated artifact.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param lab_name: The name of the lab. Required.
        :type lab_name: str
        :param artifact_source_name: The name of the artifact source. Required.
        :type artifact_source_name: str
        :param name: The name of the artifact. Required.
        :type name: str
        :param generate_arm_template_request: Parameters for generating an ARM template for deploying
         artifacts. Is either a GenerateArmTemplateRequest type or a IO[bytes] type. Required.
        :type generate_arm_template_request: ~azure.mgmt.devtestlabs.models.GenerateArmTemplateRequest
         or IO[bytes]
        :return: ArmTemplateInfo or the result of cls(response)
        :rtype: ~azure.mgmt.devtestlabs.models.ArmTemplateInfo
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ArmTemplateInfo] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(generate_arm_template_request, (IOBase, bytes)):
            _content = generate_arm_template_request
        else:
            _json = self._serialize.body(generate_arm_template_request, "GenerateArmTemplateRequest")

        _request = build_generate_arm_template_request(
            resource_group_name=resource_group_name,
            lab_name=lab_name,
            artifact_source_name=artifact_source_name,
            name=name,
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
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ArmTemplateInfo", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
