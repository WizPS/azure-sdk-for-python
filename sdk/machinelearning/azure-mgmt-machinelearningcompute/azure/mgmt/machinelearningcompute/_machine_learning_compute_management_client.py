# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core.rest import HttpRequest, HttpResponse
from azure.mgmt.core import ARMPipelineClient

from . import models
from ._configuration import MachineLearningComputeManagementClientConfiguration
from ._serialization import Deserializer, Serializer
from .operations import MachineLearningComputeOperations, OperationalizationClustersOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential


class MachineLearningComputeManagementClient:  # pylint: disable=client-accepts-api-version-keyword
    """These APIs allow end users to operate on Azure Machine Learning Compute resources. They support
    the following operations::code:`<ul><li>Create or update a cluster</li><li>Get a
    cluster</li><li>Patch a cluster</li><li>Delete a cluster</li><li>Get keys for a
    cluster</li><li>Check if updates are available for system services in a cluster</li><li>Update
    system services in a cluster</li><li>Get all clusters in a resource group</li><li>Get all
    clusters in a subscription</li></ul>`.

    :ivar operationalization_clusters: OperationalizationClustersOperations operations
    :vartype operationalization_clusters:
     azure.mgmt.machinelearningcompute.operations.OperationalizationClustersOperations
    :ivar machine_learning_compute: MachineLearningComputeOperations operations
    :vartype machine_learning_compute:
     azure.mgmt.machinelearningcompute.operations.MachineLearningComputeOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The Azure subscription ID. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2017-08-01-preview". Note that overriding
     this default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = MachineLearningComputeManagementClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.operationalization_clusters = OperationalizationClustersOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.machine_learning_compute = MachineLearningComputeOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

    def _send_request(self, request: HttpRequest, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> MachineLearningComputeManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
