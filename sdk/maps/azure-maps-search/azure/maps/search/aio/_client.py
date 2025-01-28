# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, Optional, TYPE_CHECKING

from azure.core import AsyncPipelineClient
from azure.core.pipeline import policies
from azure.core.rest import AsyncHttpResponse, HttpRequest

from .._serialization import Deserializer, Serializer
from ._configuration import MapsSearchClientConfiguration
from .operations import SearchOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential


class MapsSearchClient(SearchOperations):  # pylint: disable=client-accepts-api-version-keyword
    """Azure Maps Search REST APIs.

    :ivar search: SearchOperations operations
    :vartype search: azure.maps.search.aio.operations.SearchOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param accept_language: Language in which search results should be returned.

     Please refer to `Supported Languages </azure/azure-maps/supported-languages>`_ for details.
     Default value is None.
    :type accept_language: str
    :param client_id: Specifies which account is intended for usage in conjunction with the Azure
     AD security model.  It represents a unique ID for the Azure Maps account and can be retrieved
     from the Azure Maps management  plane Account API. To use Azure AD security in Azure Maps see
     the following `articles <https://aka.ms/amauthdetails>`_ for guidance. Default value is None.
    :type client_id: str
    :keyword endpoint: Service URL. Default value is "https://atlas.microsoft.com".
    :paramtype endpoint: str
    :keyword api_version: Api Version. Default value is "2023-06-01". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        accept_language: Optional[str] = None,
        client_id: Optional[str] = None,
        *,
        endpoint: str = "https://atlas.microsoft.com",
        **kwargs: Any
    ) -> None:
        self._config = MapsSearchClientConfiguration(
            credential=credential, accept_language=accept_language, client_id=client_id, **kwargs
        )
        _policies = kwargs.pop("policies", None)
        if _policies is None:
            _policies = [
                policies.RequestIdPolicy(**kwargs),
                self._config.headers_policy,
                self._config.user_agent_policy,
                self._config.proxy_policy,
                policies.ContentDecodePolicy(**kwargs),
                self._config.redirect_policy,
                self._config.retry_policy,
                self._config.authentication_policy,
                self._config.custom_hook_policy,
                self._config.logging_policy,
                policies.DistributedTracingPolicy(**kwargs),
                policies.SensitiveHeaderCleanupPolicy(**kwargs) if self._config.redirect_policy else None,
                self._config.http_logging_policy,
            ]
        self._client: AsyncPipelineClient = AsyncPipelineClient(base_url=endpoint, policies=_policies, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False

        # Initialize the base SearchOperations
        super().__init__(
            client=self._client, config=self._config, serializer=self._serialize, deserializer=self._deserialize
        )

    def send_request(
        self, request: HttpRequest, *, stream: bool = False, **kwargs: Any
    ) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client.send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, stream=stream, **kwargs)  # type: ignore

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "MapsSearchClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details: Any) -> None:
        await self._client.__aexit__(*exc_details)
