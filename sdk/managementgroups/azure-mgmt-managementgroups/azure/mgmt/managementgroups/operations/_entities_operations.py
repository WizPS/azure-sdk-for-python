# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, Iterable, Optional, Type, TypeVar, Union
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
    *,
    skiptoken: Optional[str] = None,
    skip: Optional[int] = None,
    top: Optional[int] = None,
    select: Optional[str] = None,
    search: Optional[Union[str, _models.EntitySearchType]] = None,
    filter: Optional[str] = None,
    view: Optional[Union[str, _models.EntityViewParameterType]] = None,
    group_name: Optional[str] = None,
    cache_control: str = "no-cache",
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2021-04-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/providers/Microsoft.Management/getEntities")

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if skiptoken is not None:
        _params["$skiptoken"] = _SERIALIZER.query("skiptoken", skiptoken, "str")
    if skip is not None:
        _params["$skip"] = _SERIALIZER.query("skip", skip, "int")
    if top is not None:
        _params["$top"] = _SERIALIZER.query("top", top, "int")
    if select is not None:
        _params["$select"] = _SERIALIZER.query("select", select, "str")
    if search is not None:
        _params["$search"] = _SERIALIZER.query("search", search, "str")
    if filter is not None:
        _params["$filter"] = _SERIALIZER.query("filter", filter, "str")
    if view is not None:
        _params["$view"] = _SERIALIZER.query("view", view, "str")
    if group_name is not None:
        _params["groupName"] = _SERIALIZER.query("group_name", group_name, "str")

    # Construct headers
    if cache_control is not None:
        _headers["Cache-Control"] = _SERIALIZER.header("cache_control", cache_control, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


class EntitiesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.managementgroups.ManagementGroupsAPI`'s
        :attr:`entities` attribute.
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
        skiptoken: Optional[str] = None,
        skip: Optional[int] = None,
        top: Optional[int] = None,
        select: Optional[str] = None,
        search: Optional[Union[str, _models.EntitySearchType]] = None,
        filter: Optional[str] = None,
        view: Optional[Union[str, _models.EntityViewParameterType]] = None,
        group_name: Optional[str] = None,
        cache_control: str = "no-cache",
        **kwargs: Any
    ) -> Iterable["_models.EntityInfo"]:
        """List all entities (Management Groups, Subscriptions, etc.) for the authenticated user.

        :param skiptoken: Page continuation token is only used if a previous operation returned a
         partial result.
         If a previous response contains a nextLink element, the value of the nextLink element will
         include a token parameter that specifies a starting point to use for subsequent calls. Default
         value is None.
        :type skiptoken: str
        :param skip: Number of entities to skip over when retrieving results. Passing this in will
         override $skipToken. Default value is None.
        :type skip: int
        :param top: Number of elements to return when retrieving results. Passing this in will override
         $skipToken. Default value is None.
        :type top: int
        :param select: This parameter specifies the fields to include in the response. Can include any
         combination of Name,DisplayName,Type,ParentDisplayNameChain,ParentChain, e.g.
         '$select=Name,DisplayName,Type,ParentDisplayNameChain,ParentNameChain'. When specified the
         $select parameter can override select in $skipToken. Default value is None.
        :type select: str
        :param search: The $search parameter is used in conjunction with the $filter parameter to
         return three different outputs depending on the parameter passed in.
         With $search=AllowedParents the API will return the entity info of all groups that the
         requested entity will be able to reparent to as determined by the user's permissions.
         With $search=AllowedChildren the API will return the entity info of all entities that can be
         added as children of the requested entity.
         With $search=ParentAndFirstLevelChildren the API will return the parent and  first level of
         children that the user has either direct access to or indirect access via one of their
         descendants.
         With $search=ParentOnly the API will return only the group if the user has access to at least
         one of the descendants of the group.
         With $search=ChildrenOnly the API will return only the first level of children of the group
         entity info specified in $filter.  The user must have direct access to the children entities or
         one of it's descendants for it to show up in the results. Known values are: "AllowedParents",
         "AllowedChildren", "ParentAndFirstLevelChildren", "ParentOnly", and "ChildrenOnly". Default
         value is None.
        :type search: str or ~azure.mgmt.managementgroups.models.EntitySearchType
        :param filter: The filter parameter allows you to filter on the the name or display name
         fields. You can check for equality on the name field (e.g. name eq '{entityName}')  and you can
         check for substrings on either the name or display name fields(e.g. contains(name,
         '{substringToSearch}'), contains(displayName, '{substringToSearch')). Note that the
         '{entityName}' and '{substringToSearch}' fields are checked case insensitively. Default value
         is None.
        :type filter: str
        :param view: The view parameter allows clients to filter the type of data that is returned by
         the getEntities call. Known values are: "FullHierarchy", "GroupsOnly", "SubscriptionsOnly", and
         "Audit". Default value is None.
        :type view: str or ~azure.mgmt.managementgroups.models.EntityViewParameterType
        :param group_name: A filter which allows the get entities call to focus on a particular group
         (i.e. "$filter=name eq 'groupName'"). Default value is None.
        :type group_name: str
        :param cache_control: Indicates whether the request should utilize any caches. Populate the
         header with 'no-cache' value to bypass existing caches. Default value is "no-cache".
        :type cache_control: str
        :return: An iterator like instance of either EntityInfo or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.managementgroups.models.EntityInfo]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.EntityListResult] = kwargs.pop("cls", None)

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
                    skiptoken=skiptoken,
                    skip=skip,
                    top=top,
                    select=select,
                    search=search,
                    filter=filter,
                    view=view,
                    group_name=group_name,
                    cache_control=cache_control,
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
            deserialized = self._deserialize("EntityListResult", pipeline_response)
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
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)
