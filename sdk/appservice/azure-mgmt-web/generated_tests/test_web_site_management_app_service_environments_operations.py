# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.web import WebSiteManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestWebSiteManagementAppServiceEnvironmentsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(WebSiteManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_list(self, resource_group):
        response = self.client.app_service_environments.list(
            api_version="2024-04-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_list_by_resource_group(self, resource_group):
        response = self.client.app_service_environments.list_by_resource_group(
            resource_group_name=resource_group.name,
            api_version="2024-04-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_get(self, resource_group):
        response = self.client.app_service_environments.get(
            resource_group_name=resource_group.name,
            name="str",
            api_version="2024-04-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_begin_create_or_update(self, resource_group):
        response = self.client.app_service_environments.begin_create_or_update(
            resource_group_name=resource_group.name,
            name="str",
            hosting_environment_envelope={
                "location": "str",
                "clusterSettings": [{"name": "str", "value": "str"}],
                "customDnsSuffixConfiguration": {
                    "certificateUrl": "str",
                    "dnsSuffix": "str",
                    "id": "str",
                    "keyVaultReferenceIdentity": "str",
                    "kind": "str",
                    "name": "str",
                    "provisioningDetails": "str",
                    "provisioningState": "str",
                    "type": "str",
                },
                "dedicatedHostCount": 0,
                "dnsSuffix": "str",
                "frontEndScaleFactor": 0,
                "hasLinuxWorkers": bool,
                "id": "str",
                "internalLoadBalancingMode": "str",
                "ipsslAddressCount": 0,
                "kind": "str",
                "maximumNumberOfMachines": 0,
                "multiRoleCount": 0,
                "multiSize": "str",
                "name": "str",
                "networkingConfiguration": {
                    "allowNewPrivateEndpointConnections": bool,
                    "externalInboundIpAddresses": ["str"],
                    "ftpEnabled": bool,
                    "id": "str",
                    "inboundIpAddressOverride": "str",
                    "internalInboundIpAddresses": ["str"],
                    "kind": "str",
                    "linuxOutboundIpAddresses": ["str"],
                    "name": "str",
                    "remoteDebugEnabled": bool,
                    "type": "str",
                    "windowsOutboundIpAddresses": ["str"],
                },
                "provisioningState": "str",
                "status": "str",
                "suspended": bool,
                "tags": {"str": "str"},
                "type": "str",
                "upgradeAvailability": "str",
                "upgradePreference": "None",
                "userWhitelistedIpRanges": ["str"],
                "virtualNetwork": {"id": "str", "name": "str", "subnet": "str", "type": "str"},
                "zoneRedundant": bool,
            },
            api_version="2024-04-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_begin_delete(self, resource_group):
        response = self.client.app_service_environments.begin_delete(
            resource_group_name=resource_group.name,
            name="str",
            api_version="2024-04-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_update(self, resource_group):
        response = self.client.app_service_environments.update(
            resource_group_name=resource_group.name,
            name="str",
            hosting_environment_envelope={
                "clusterSettings": [{"name": "str", "value": "str"}],
                "customDnsSuffixConfiguration": {
                    "certificateUrl": "str",
                    "dnsSuffix": "str",
                    "id": "str",
                    "keyVaultReferenceIdentity": "str",
                    "kind": "str",
                    "name": "str",
                    "provisioningDetails": "str",
                    "provisioningState": "str",
                    "type": "str",
                },
                "dedicatedHostCount": 0,
                "dnsSuffix": "str",
                "frontEndScaleFactor": 0,
                "hasLinuxWorkers": bool,
                "id": "str",
                "internalLoadBalancingMode": "str",
                "ipsslAddressCount": 0,
                "kind": "str",
                "maximumNumberOfMachines": 0,
                "multiRoleCount": 0,
                "multiSize": "str",
                "name": "str",
                "networkingConfiguration": {
                    "allowNewPrivateEndpointConnections": bool,
                    "externalInboundIpAddresses": ["str"],
                    "ftpEnabled": bool,
                    "id": "str",
                    "inboundIpAddressOverride": "str",
                    "internalInboundIpAddresses": ["str"],
                    "kind": "str",
                    "linuxOutboundIpAddresses": ["str"],
                    "name": "str",
                    "remoteDebugEnabled": bool,
                    "type": "str",
                    "windowsOutboundIpAddresses": ["str"],
                },
                "provisioningState": "str",
                "status": "str",
                "suspended": bool,
                "type": "str",
                "upgradeAvailability": "str",
                "upgradePreference": "None",
                "userWhitelistedIpRanges": ["str"],
                "virtualNetwork": {"id": "str", "name": "str", "subnet": "str", "type": "str"},
                "zoneRedundant": bool,
            },
            api_version="2024-04-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_list_capacities(self, resource_group):
        response = self.client.app_service_environments.list_capacities(
            resource_group_name=resource_group.name,
            name="str",
            api_version="2024-04-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_get_vip_info(self, resource_group):
        response = self.client.app_service_environments.get_vip_info(
            resource_group_name=resource_group.name,
            name="str",
            api_version="2024-04-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_begin_change_vnet(self, resource_group):
        response = self.client.app_service_environments.begin_change_vnet(
            resource_group_name=resource_group.name,
            name="str",
            vnet_info={"id": "str", "name": "str", "subnet": "str", "type": "str"},
            api_version="2024-04-01",
        ).result()  # call '.result()' to poll until service return final result
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_get_ase_custom_dns_suffix_configuration(self, resource_group):
        response = self.client.app_service_environments.get_ase_custom_dns_suffix_configuration(
            resource_group_name=resource_group.name,
            name="str",
            api_version="2024-04-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_update_ase_custom_dns_suffix_configuration(self, resource_group):
        response = self.client.app_service_environments.update_ase_custom_dns_suffix_configuration(
            resource_group_name=resource_group.name,
            name="str",
            custom_dns_suffix_configuration={
                "certificateUrl": "str",
                "dnsSuffix": "str",
                "id": "str",
                "keyVaultReferenceIdentity": "str",
                "kind": "str",
                "name": "str",
                "provisioningDetails": "str",
                "provisioningState": "str",
                "type": "str",
            },
            api_version="2024-04-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_delete_ase_custom_dns_suffix_configuration(self, resource_group):
        response = self.client.app_service_environments.delete_ase_custom_dns_suffix_configuration(
            resource_group_name=resource_group.name,
            name="str",
            api_version="2024-04-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_get_ase_v3_networking_configuration(self, resource_group):
        response = self.client.app_service_environments.get_ase_v3_networking_configuration(
            resource_group_name=resource_group.name,
            name="str",
            api_version="2024-04-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_update_ase_networking_configuration(self, resource_group):
        response = self.client.app_service_environments.update_ase_networking_configuration(
            resource_group_name=resource_group.name,
            name="str",
            ase_networking_configuration={
                "allowNewPrivateEndpointConnections": bool,
                "externalInboundIpAddresses": ["str"],
                "ftpEnabled": bool,
                "id": "str",
                "inboundIpAddressOverride": "str",
                "internalInboundIpAddresses": ["str"],
                "kind": "str",
                "linuxOutboundIpAddresses": ["str"],
                "name": "str",
                "remoteDebugEnabled": bool,
                "type": "str",
                "windowsOutboundIpAddresses": ["str"],
            },
            api_version="2024-04-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_list_diagnostics(self, resource_group):
        response = self.client.app_service_environments.list_diagnostics(
            resource_group_name=resource_group.name,
            name="str",
            api_version="2024-04-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_get_diagnostics_item(self, resource_group):
        response = self.client.app_service_environments.get_diagnostics_item(
            resource_group_name=resource_group.name,
            name="str",
            diagnostics_name="str",
            api_version="2024-04-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_get_inbound_network_dependencies_endpoints(self, resource_group):
        response = self.client.app_service_environments.get_inbound_network_dependencies_endpoints(
            resource_group_name=resource_group.name,
            name="str",
            api_version="2024-04-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_list_multi_role_pools(self, resource_group):
        response = self.client.app_service_environments.list_multi_role_pools(
            resource_group_name=resource_group.name,
            name="str",
            api_version="2024-04-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_get_multi_role_pool(self, resource_group):
        response = self.client.app_service_environments.get_multi_role_pool(
            resource_group_name=resource_group.name,
            name="str",
            api_version="2024-04-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_begin_create_or_update_multi_role_pool(self, resource_group):
        response = self.client.app_service_environments.begin_create_or_update_multi_role_pool(
            resource_group_name=resource_group.name,
            name="str",
            multi_role_pool_envelope={
                "computeMode": "str",
                "id": "str",
                "instanceNames": ["str"],
                "kind": "str",
                "name": "str",
                "sku": {
                    "capabilities": [{"name": "str", "reason": "str", "value": "str"}],
                    "capacity": 0,
                    "family": "str",
                    "locations": ["str"],
                    "name": "str",
                    "size": "str",
                    "skuCapacity": {"default": 0, "elasticMaximum": 0, "maximum": 0, "minimum": 0, "scaleType": "str"},
                    "tier": "str",
                },
                "type": "str",
                "workerCount": 0,
                "workerSize": "str",
                "workerSizeId": 0,
            },
            api_version="2024-04-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_update_multi_role_pool(self, resource_group):
        response = self.client.app_service_environments.update_multi_role_pool(
            resource_group_name=resource_group.name,
            name="str",
            multi_role_pool_envelope={
                "computeMode": "str",
                "id": "str",
                "instanceNames": ["str"],
                "kind": "str",
                "name": "str",
                "sku": {
                    "capabilities": [{"name": "str", "reason": "str", "value": "str"}],
                    "capacity": 0,
                    "family": "str",
                    "locations": ["str"],
                    "name": "str",
                    "size": "str",
                    "skuCapacity": {"default": 0, "elasticMaximum": 0, "maximum": 0, "minimum": 0, "scaleType": "str"},
                    "tier": "str",
                },
                "type": "str",
                "workerCount": 0,
                "workerSize": "str",
                "workerSizeId": 0,
            },
            api_version="2024-04-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_list_multi_role_pool_instance_metric_definitions(self, resource_group):
        response = self.client.app_service_environments.list_multi_role_pool_instance_metric_definitions(
            resource_group_name=resource_group.name,
            name="str",
            instance="str",
            api_version="2024-04-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_list_multi_role_metric_definitions(self, resource_group):
        response = self.client.app_service_environments.list_multi_role_metric_definitions(
            resource_group_name=resource_group.name,
            name="str",
            api_version="2024-04-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_list_multi_role_pool_skus(self, resource_group):
        response = self.client.app_service_environments.list_multi_role_pool_skus(
            resource_group_name=resource_group.name,
            name="str",
            api_version="2024-04-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_test_upgrade_available_notification(self, resource_group):
        response = self.client.app_service_environments.test_upgrade_available_notification(
            resource_group_name=resource_group.name,
            name="str",
            api_version="2024-04-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_begin_upgrade(self, resource_group):
        response = self.client.app_service_environments.begin_upgrade(
            resource_group_name=resource_group.name,
            name="str",
            api_version="2024-04-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_list_multi_role_usages(self, resource_group):
        response = self.client.app_service_environments.list_multi_role_usages(
            resource_group_name=resource_group.name,
            name="str",
            api_version="2024-04-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_list_operations(self, resource_group):
        response = self.client.app_service_environments.list_operations(
            resource_group_name=resource_group.name,
            name="str",
            api_version="2024-04-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_get_outbound_network_dependencies_endpoints(self, resource_group):
        response = self.client.app_service_environments.get_outbound_network_dependencies_endpoints(
            resource_group_name=resource_group.name,
            name="str",
            api_version="2024-04-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_get_private_endpoint_connection_list(self, resource_group):
        response = self.client.app_service_environments.get_private_endpoint_connection_list(
            resource_group_name=resource_group.name,
            name="str",
            api_version="2024-04-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_get_private_endpoint_connection(self, resource_group):
        response = self.client.app_service_environments.get_private_endpoint_connection(
            resource_group_name=resource_group.name,
            name="str",
            private_endpoint_connection_name="str",
            api_version="2024-04-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_begin_approve_or_reject_private_endpoint_connection(self, resource_group):
        response = self.client.app_service_environments.begin_approve_or_reject_private_endpoint_connection(
            resource_group_name=resource_group.name,
            name="str",
            private_endpoint_connection_name="str",
            private_endpoint_wrapper={
                "id": "str",
                "ipAddresses": ["str"],
                "kind": "str",
                "name": "str",
                "privateEndpoint": {"id": "str"},
                "privateLinkServiceConnectionState": {"actionsRequired": "str", "description": "str", "status": "str"},
                "provisioningState": "str",
                "type": "str",
            },
            api_version="2024-04-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_begin_delete_private_endpoint_connection(self, resource_group):
        response = self.client.app_service_environments.begin_delete_private_endpoint_connection(
            resource_group_name=resource_group.name,
            name="str",
            private_endpoint_connection_name="str",
            api_version="2024-04-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_get_private_link_resources(self, resource_group):
        response = self.client.app_service_environments.get_private_link_resources(
            resource_group_name=resource_group.name,
            name="str",
            api_version="2024-04-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_reboot(self, resource_group):
        response = self.client.app_service_environments.reboot(
            resource_group_name=resource_group.name,
            name="str",
            api_version="2024-04-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_begin_resume(self, resource_group):
        response = self.client.app_service_environments.begin_resume(
            resource_group_name=resource_group.name,
            name="str",
            api_version="2024-04-01",
        ).result()  # call '.result()' to poll until service return final result
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_list_app_service_plans(self, resource_group):
        response = self.client.app_service_environments.list_app_service_plans(
            resource_group_name=resource_group.name,
            name="str",
            api_version="2024-04-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_list_web_apps(self, resource_group):
        response = self.client.app_service_environments.list_web_apps(
            resource_group_name=resource_group.name,
            name="str",
            api_version="2024-04-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_begin_suspend(self, resource_group):
        response = self.client.app_service_environments.begin_suspend(
            resource_group_name=resource_group.name,
            name="str",
            api_version="2024-04-01",
        ).result()  # call '.result()' to poll until service return final result
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_list_usages(self, resource_group):
        response = self.client.app_service_environments.list_usages(
            resource_group_name=resource_group.name,
            name="str",
            api_version="2024-04-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_list_worker_pools(self, resource_group):
        response = self.client.app_service_environments.list_worker_pools(
            resource_group_name=resource_group.name,
            name="str",
            api_version="2024-04-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_get_worker_pool(self, resource_group):
        response = self.client.app_service_environments.get_worker_pool(
            resource_group_name=resource_group.name,
            name="str",
            worker_pool_name="str",
            api_version="2024-04-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_begin_create_or_update_worker_pool(self, resource_group):
        response = self.client.app_service_environments.begin_create_or_update_worker_pool(
            resource_group_name=resource_group.name,
            name="str",
            worker_pool_name="str",
            worker_pool_envelope={
                "computeMode": "str",
                "id": "str",
                "instanceNames": ["str"],
                "kind": "str",
                "name": "str",
                "sku": {
                    "capabilities": [{"name": "str", "reason": "str", "value": "str"}],
                    "capacity": 0,
                    "family": "str",
                    "locations": ["str"],
                    "name": "str",
                    "size": "str",
                    "skuCapacity": {"default": 0, "elasticMaximum": 0, "maximum": 0, "minimum": 0, "scaleType": "str"},
                    "tier": "str",
                },
                "type": "str",
                "workerCount": 0,
                "workerSize": "str",
                "workerSizeId": 0,
            },
            api_version="2024-04-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_update_worker_pool(self, resource_group):
        response = self.client.app_service_environments.update_worker_pool(
            resource_group_name=resource_group.name,
            name="str",
            worker_pool_name="str",
            worker_pool_envelope={
                "computeMode": "str",
                "id": "str",
                "instanceNames": ["str"],
                "kind": "str",
                "name": "str",
                "sku": {
                    "capabilities": [{"name": "str", "reason": "str", "value": "str"}],
                    "capacity": 0,
                    "family": "str",
                    "locations": ["str"],
                    "name": "str",
                    "size": "str",
                    "skuCapacity": {"default": 0, "elasticMaximum": 0, "maximum": 0, "minimum": 0, "scaleType": "str"},
                    "tier": "str",
                },
                "type": "str",
                "workerCount": 0,
                "workerSize": "str",
                "workerSizeId": 0,
            },
            api_version="2024-04-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_list_worker_pool_instance_metric_definitions(self, resource_group):
        response = self.client.app_service_environments.list_worker_pool_instance_metric_definitions(
            resource_group_name=resource_group.name,
            name="str",
            worker_pool_name="str",
            instance="str",
            api_version="2024-04-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_list_web_worker_metric_definitions(self, resource_group):
        response = self.client.app_service_environments.list_web_worker_metric_definitions(
            resource_group_name=resource_group.name,
            name="str",
            worker_pool_name="str",
            api_version="2024-04-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_list_worker_pool_skus(self, resource_group):
        response = self.client.app_service_environments.list_worker_pool_skus(
            resource_group_name=resource_group.name,
            name="str",
            worker_pool_name="str",
            api_version="2024-04-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_app_service_environments_list_web_worker_usages(self, resource_group):
        response = self.client.app_service_environments.list_web_worker_usages(
            resource_group_name=resource_group.name,
            name="str",
            worker_pool_name="str",
            api_version="2024-04-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
