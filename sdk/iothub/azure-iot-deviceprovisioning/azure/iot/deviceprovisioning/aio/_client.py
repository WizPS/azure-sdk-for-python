# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, TYPE_CHECKING

from azure.core import AsyncPipelineClient
from azure.core.rest import AsyncHttpResponse, HttpRequest

from .._serialization import Deserializer, Serializer
from ._configuration import DeviceProvisioningClientConfiguration
from .operations import DeviceRegistrationStateOperations, EnrollmentGroupOperations, EnrollmentOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential


class DeviceProvisioningClient:  # pylint: disable=client-accepts-api-version-keyword
    """API for service operations with the Azure IoT Hub Device Provisioning Service.

    :ivar enrollment: EnrollmentOperations operations
    :vartype enrollment: azure.iot.deviceprovisioning.aio.operations.EnrollmentOperations
    :ivar enrollment_group: EnrollmentGroupOperations operations
    :vartype enrollment_group:
     azure.iot.deviceprovisioning.aio.operations.EnrollmentGroupOperations
    :ivar device_registration_state: DeviceRegistrationStateOperations operations
    :vartype device_registration_state:
     azure.iot.deviceprovisioning.aio.operations.DeviceRegistrationStateOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :keyword endpoint: Service URL. Default value is
     "https://your-dps.azure-devices-provisioning.net".
    :paramtype endpoint: str
    :keyword api_version: Api Version. Default value is "2021-10-01". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        *,
        endpoint: str = "https://your-dps.azure-devices-provisioning.net",
        **kwargs: Any
    ) -> None:
        self._config = DeviceProvisioningClientConfiguration(credential=credential, **kwargs)
        self._client: AsyncPipelineClient = AsyncPipelineClient(base_url=endpoint, config=self._config, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.enrollment = EnrollmentOperations(self._client, self._config, self._serialize, self._deserialize)
        self.enrollment_group = EnrollmentGroupOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.device_registration_state = DeviceRegistrationStateOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

    def send_request(self, request: HttpRequest, **kwargs: Any) -> Awaitable[AsyncHttpResponse]:
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
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "DeviceProvisioningClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details: Any) -> None:
        await self._client.__aexit__(*exc_details)
