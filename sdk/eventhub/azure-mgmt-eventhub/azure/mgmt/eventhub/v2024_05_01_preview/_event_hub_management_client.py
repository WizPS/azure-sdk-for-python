# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING
from typing_extensions import Self

from azure.core.pipeline import policies
from azure.core.rest import HttpRequest, HttpResponse
from azure.mgmt.core import ARMPipelineClient
from azure.mgmt.core.policies import ARMAutoResourceProviderRegistrationPolicy

from . import models as _models
from .._serialization import Deserializer, Serializer
from ._configuration import EventHubManagementClientConfiguration
from .operations import (
    ApplicationGroupOperations,
    ClustersOperations,
    ConfigurationOperations,
    ConsumerGroupsOperations,
    DisasterRecoveryConfigsOperations,
    EventHubsOperations,
    NamespacesOperations,
    NetworkSecurityPerimeterConfigurationOperations,
    NetworkSecurityPerimeterConfigurationsOperations,
    Operations,
    PrivateEndpointConnectionsOperations,
    PrivateLinkResourcesOperations,
    SchemaRegistryOperations,
)

if TYPE_CHECKING:
    from azure.core.credentials import TokenCredential


class EventHubManagementClient:  # pylint: disable=too-many-instance-attributes
    """Azure Event Hubs client for managing Event Hubs Cluster, IPFilter Rules and VirtualNetworkRules
    resources.

    :ivar clusters: ClustersOperations operations
    :vartype clusters: azure.mgmt.eventhub.v2024_05_01_preview.operations.ClustersOperations
    :ivar namespaces: NamespacesOperations operations
    :vartype namespaces: azure.mgmt.eventhub.v2024_05_01_preview.operations.NamespacesOperations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections:
     azure.mgmt.eventhub.v2024_05_01_preview.operations.PrivateEndpointConnectionsOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources:
     azure.mgmt.eventhub.v2024_05_01_preview.operations.PrivateLinkResourcesOperations
    :ivar network_security_perimeter_configuration: NetworkSecurityPerimeterConfigurationOperations
     operations
    :vartype network_security_perimeter_configuration:
     azure.mgmt.eventhub.v2024_05_01_preview.operations.NetworkSecurityPerimeterConfigurationOperations
    :ivar network_security_perimeter_configurations:
     NetworkSecurityPerimeterConfigurationsOperations operations
    :vartype network_security_perimeter_configurations:
     azure.mgmt.eventhub.v2024_05_01_preview.operations.NetworkSecurityPerimeterConfigurationsOperations
    :ivar configuration: ConfigurationOperations operations
    :vartype configuration:
     azure.mgmt.eventhub.v2024_05_01_preview.operations.ConfigurationOperations
    :ivar disaster_recovery_configs: DisasterRecoveryConfigsOperations operations
    :vartype disaster_recovery_configs:
     azure.mgmt.eventhub.v2024_05_01_preview.operations.DisasterRecoveryConfigsOperations
    :ivar event_hubs: EventHubsOperations operations
    :vartype event_hubs: azure.mgmt.eventhub.v2024_05_01_preview.operations.EventHubsOperations
    :ivar consumer_groups: ConsumerGroupsOperations operations
    :vartype consumer_groups:
     azure.mgmt.eventhub.v2024_05_01_preview.operations.ConsumerGroupsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.eventhub.v2024_05_01_preview.operations.Operations
    :ivar schema_registry: SchemaRegistryOperations operations
    :vartype schema_registry:
     azure.mgmt.eventhub.v2024_05_01_preview.operations.SchemaRegistryOperations
    :ivar application_group: ApplicationGroupOperations operations
    :vartype application_group:
     azure.mgmt.eventhub.v2024_05_01_preview.operations.ApplicationGroupOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure
     subscription. The subscription ID forms part of the URI for every service call. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2024-05-01-preview". Note that overriding
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
        self._config = EventHubManagementClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        _policies = kwargs.pop("policies", None)
        if _policies is None:
            _policies = [
                policies.RequestIdPolicy(**kwargs),
                self._config.headers_policy,
                self._config.user_agent_policy,
                self._config.proxy_policy,
                policies.ContentDecodePolicy(**kwargs),
                ARMAutoResourceProviderRegistrationPolicy(),
                self._config.redirect_policy,
                self._config.retry_policy,
                self._config.authentication_policy,
                self._config.custom_hook_policy,
                self._config.logging_policy,
                policies.DistributedTracingPolicy(**kwargs),
                policies.SensitiveHeaderCleanupPolicy(**kwargs) if self._config.redirect_policy else None,
                self._config.http_logging_policy,
            ]
        self._client: ARMPipelineClient = ARMPipelineClient(base_url=base_url, policies=_policies, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.clusters = ClustersOperations(
            self._client, self._config, self._serialize, self._deserialize, "2024-05-01-preview"
        )
        self.namespaces = NamespacesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2024-05-01-preview"
        )
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2024-05-01-preview"
        )
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2024-05-01-preview"
        )
        self.network_security_perimeter_configuration = NetworkSecurityPerimeterConfigurationOperations(
            self._client, self._config, self._serialize, self._deserialize, "2024-05-01-preview"
        )
        self.network_security_perimeter_configurations = NetworkSecurityPerimeterConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2024-05-01-preview"
        )
        self.configuration = ConfigurationOperations(
            self._client, self._config, self._serialize, self._deserialize, "2024-05-01-preview"
        )
        self.disaster_recovery_configs = DisasterRecoveryConfigsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2024-05-01-preview"
        )
        self.event_hubs = EventHubsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2024-05-01-preview"
        )
        self.consumer_groups = ConsumerGroupsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2024-05-01-preview"
        )
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize, "2024-05-01-preview"
        )
        self.schema_registry = SchemaRegistryOperations(
            self._client, self._config, self._serialize, self._deserialize, "2024-05-01-preview"
        )
        self.application_group = ApplicationGroupOperations(
            self._client, self._config, self._serialize, self._deserialize, "2024-05-01-preview"
        )

    def _send_request(self, request: HttpRequest, *, stream: bool = False, **kwargs: Any) -> HttpResponse:
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
        return self._client.send_request(request_copy, stream=stream, **kwargs)  # type: ignore

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> Self:
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)
