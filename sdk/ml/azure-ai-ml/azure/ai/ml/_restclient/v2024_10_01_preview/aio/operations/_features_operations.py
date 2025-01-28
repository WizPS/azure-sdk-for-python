# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Optional, TypeVar, Union

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._features_operations import build_get_request, build_list_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class FeaturesOperations:
    """FeaturesOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.machinelearningservices.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def list(
        self,
        resource_group_name: str,
        workspace_name: str,
        featureset_name: str,
        featureset_version: str,
        skip: Optional[str] = None,
        tags: Optional[str] = None,
        feature_name: Optional[str] = None,
        description: Optional[str] = None,
        list_view_type: Optional[Union[str, "_models.ListViewType"]] = None,
        page_size: Optional[int] = 1000,
        **kwargs: Any
    ) -> AsyncIterable["_models.FeatureResourceArmPaginatedResult"]:
        """List Features.

        List Features.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param workspace_name: Name of Azure Machine Learning workspace.
        :type workspace_name: str
        :param featureset_name: Featureset name. This is case-sensitive.
        :type featureset_name: str
        :param featureset_version: Featureset Version identifier. This is case-sensitive.
        :type featureset_version: str
        :param skip: Continuation token for pagination.
        :type skip: str
        :param tags: Comma-separated list of tag names (and optionally values). Example:
         tag1,tag2=value2.
        :type tags: str
        :param feature_name: feature name.
        :type feature_name: str
        :param description: Description of the featureset.
        :type description: str
        :param list_view_type: [ListViewType.ActiveOnly, ListViewType.ArchivedOnly,
         ListViewType.All]View type for including/excluding (for example) archived entities.
        :type list_view_type: str or ~azure.mgmt.machinelearningservices.models.ListViewType
        :param page_size: Page size.
        :type page_size: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either FeatureResourceArmPaginatedResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.machinelearningservices.models.FeatureResourceArmPaginatedResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2024-10-01-preview")  # type: str

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.FeatureResourceArmPaginatedResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    workspace_name=workspace_name,
                    featureset_name=featureset_name,
                    featureset_version=featureset_version,
                    api_version=api_version,
                    skip=skip,
                    tags=tags,
                    feature_name=feature_name,
                    description=description,
                    list_view_type=list_view_type,
                    page_size=page_size,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    workspace_name=workspace_name,
                    featureset_name=featureset_name,
                    featureset_version=featureset_version,
                    api_version=api_version,
                    skip=skip,
                    tags=tags,
                    feature_name=feature_name,
                    description=description,
                    list_view_type=list_view_type,
                    page_size=page_size,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("FeatureResourceArmPaginatedResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/featuresets/{featuresetName}/versions/{featuresetVersion}/features"}  # type: ignore

    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        workspace_name: str,
        featureset_name: str,
        featureset_version: str,
        feature_name: str,
        **kwargs: Any
    ) -> "_models.Feature":
        """Get feature.

        Get feature.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param workspace_name: Name of Azure Machine Learning workspace.
        :type workspace_name: str
        :param featureset_name: Feature set name. This is case-sensitive.
        :type featureset_name: str
        :param featureset_version: Feature set version identifier. This is case-sensitive.
        :type featureset_version: str
        :param feature_name: Feature Name. This is case-sensitive.
        :type feature_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Feature, or the result of cls(response)
        :rtype: ~azure.mgmt.machinelearningservices.models.Feature
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Feature"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2024-10-01-preview")  # type: str

        
        request = build_get_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            featureset_name=featureset_name,
            featureset_version=featureset_version,
            feature_name=feature_name,
            api_version=api_version,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Feature', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/featuresets/{featuresetName}/versions/{featuresetVersion}/features/{featureName}"}  # type: ignore

