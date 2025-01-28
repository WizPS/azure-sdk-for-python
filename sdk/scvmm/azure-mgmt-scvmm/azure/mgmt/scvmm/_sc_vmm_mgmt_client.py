# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core.pipeline import policies
from azure.core.rest import HttpRequest, HttpResponse
from azure.mgmt.core import ARMPipelineClient
from azure.mgmt.core.policies import ARMAutoResourceProviderRegistrationPolicy

from . import models as _models
from ._configuration import ScVmmMgmtClientConfiguration
from ._serialization import Deserializer, Serializer
from .operations import (
    AvailabilitySetsOperations,
    CloudsOperations,
    GuestAgentsOperations,
    InventoryItemsOperations,
    Operations,
    VirtualMachineInstancesOperations,
    VirtualMachineTemplatesOperations,
    VirtualNetworksOperations,
    VmInstanceHybridIdentityMetadatasOperations,
    VmmServersOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential


class ScVmmMgmtClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """The Microsoft.ScVmm Rest API spec.

    :ivar virtual_machine_instances: VirtualMachineInstancesOperations operations
    :vartype virtual_machine_instances:
     azure.mgmt.scvmm.operations.VirtualMachineInstancesOperations
    :ivar guest_agents: GuestAgentsOperations operations
    :vartype guest_agents: azure.mgmt.scvmm.operations.GuestAgentsOperations
    :ivar vm_instance_hybrid_identity_metadatas: VmInstanceHybridIdentityMetadatasOperations
     operations
    :vartype vm_instance_hybrid_identity_metadatas:
     azure.mgmt.scvmm.operations.VmInstanceHybridIdentityMetadatasOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.scvmm.operations.Operations
    :ivar availability_sets: AvailabilitySetsOperations operations
    :vartype availability_sets: azure.mgmt.scvmm.operations.AvailabilitySetsOperations
    :ivar clouds: CloudsOperations operations
    :vartype clouds: azure.mgmt.scvmm.operations.CloudsOperations
    :ivar virtual_machine_templates: VirtualMachineTemplatesOperations operations
    :vartype virtual_machine_templates:
     azure.mgmt.scvmm.operations.VirtualMachineTemplatesOperations
    :ivar virtual_networks: VirtualNetworksOperations operations
    :vartype virtual_networks: azure.mgmt.scvmm.operations.VirtualNetworksOperations
    :ivar vmm_servers: VmmServersOperations operations
    :vartype vmm_servers: azure.mgmt.scvmm.operations.VmmServersOperations
    :ivar inventory_items: InventoryItemsOperations operations
    :vartype inventory_items: azure.mgmt.scvmm.operations.InventoryItemsOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription. The value must be an UUID. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2023-10-07". Note that overriding this
     default value may result in unsupported behavior.
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
        self._config = ScVmmMgmtClientConfiguration(credential=credential, subscription_id=subscription_id, **kwargs)
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
        self.virtual_machine_instances = VirtualMachineInstancesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.guest_agents = GuestAgentsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.vm_instance_hybrid_identity_metadatas = VmInstanceHybridIdentityMetadatasOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.availability_sets = AvailabilitySetsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.clouds = CloudsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.virtual_machine_templates = VirtualMachineTemplatesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.virtual_networks = VirtualNetworksOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.vmm_servers = VmmServersOperations(self._client, self._config, self._serialize, self._deserialize)
        self.inventory_items = InventoryItemsOperations(self._client, self._config, self._serialize, self._deserialize)

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

    def __enter__(self) -> "ScVmmMgmtClient":
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)
