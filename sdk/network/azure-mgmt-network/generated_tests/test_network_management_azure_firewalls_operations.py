# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.network import NetworkManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNetworkManagementAzureFirewallsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(NetworkManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_azure_firewalls_begin_delete(self, resource_group):
        response = self.client.azure_firewalls.begin_delete(
            resource_group_name=resource_group.name,
            azure_firewall_name="str",
            api_version="2024-05-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_azure_firewalls_get(self, resource_group):
        response = self.client.azure_firewalls.get(
            resource_group_name=resource_group.name,
            azure_firewall_name="str",
            api_version="2024-05-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_azure_firewalls_begin_create_or_update(self, resource_group):
        response = self.client.azure_firewalls.begin_create_or_update(
            resource_group_name=resource_group.name,
            azure_firewall_name="str",
            parameters={
                "applicationRuleCollections": [
                    {
                        "action": {"type": "str"},
                        "etag": "str",
                        "id": "str",
                        "name": "str",
                        "priority": 0,
                        "provisioningState": "str",
                        "rules": [
                            {
                                "description": "str",
                                "fqdnTags": ["str"],
                                "name": "str",
                                "protocols": [{"port": 0, "protocolType": "str"}],
                                "sourceAddresses": ["str"],
                                "sourceIpGroups": ["str"],
                                "targetFqdns": ["str"],
                            }
                        ],
                    }
                ],
                "autoscaleConfiguration": {"maxCapacity": 0, "minCapacity": 0},
                "etag": "str",
                "firewallPolicy": {"id": "str"},
                "hubIPAddresses": {
                    "privateIPAddress": "str",
                    "publicIPs": {"addresses": [{"address": "str"}], "count": 0},
                },
                "id": "str",
                "ipConfigurations": [
                    {
                        "etag": "str",
                        "id": "str",
                        "name": "str",
                        "privateIPAddress": "str",
                        "provisioningState": "str",
                        "publicIPAddress": {"id": "str"},
                        "subnet": {"id": "str"},
                        "type": "str",
                    }
                ],
                "ipGroups": [{"changeNumber": "str", "id": "str"}],
                "location": "str",
                "managementIpConfiguration": {
                    "etag": "str",
                    "id": "str",
                    "name": "str",
                    "privateIPAddress": "str",
                    "provisioningState": "str",
                    "publicIPAddress": {"id": "str"},
                    "subnet": {"id": "str"},
                    "type": "str",
                },
                "name": "str",
                "natRuleCollections": [
                    {
                        "action": {"type": "str"},
                        "etag": "str",
                        "id": "str",
                        "name": "str",
                        "priority": 0,
                        "provisioningState": "str",
                        "rules": [
                            {
                                "description": "str",
                                "destinationAddresses": ["str"],
                                "destinationPorts": ["str"],
                                "name": "str",
                                "protocols": ["str"],
                                "sourceAddresses": ["str"],
                                "sourceIpGroups": ["str"],
                                "translatedAddress": "str",
                                "translatedFqdn": "str",
                                "translatedPort": "str",
                            }
                        ],
                    }
                ],
                "networkRuleCollections": [
                    {
                        "action": {"type": "str"},
                        "etag": "str",
                        "id": "str",
                        "name": "str",
                        "priority": 0,
                        "provisioningState": "str",
                        "rules": [
                            {
                                "description": "str",
                                "destinationAddresses": ["str"],
                                "destinationFqdns": ["str"],
                                "destinationIpGroups": ["str"],
                                "destinationPorts": ["str"],
                                "name": "str",
                                "protocols": ["str"],
                                "sourceAddresses": ["str"],
                                "sourceIpGroups": ["str"],
                            }
                        ],
                    }
                ],
                "provisioningState": "str",
                "sku": {"name": "str", "tier": "str"},
                "tags": {"str": "str"},
                "threatIntelMode": "str",
                "type": "str",
                "virtualHub": {"id": "str"},
                "zones": ["str"],
            },
            api_version="2024-05-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_azure_firewalls_begin_update_tags(self, resource_group):
        response = self.client.azure_firewalls.begin_update_tags(
            resource_group_name=resource_group.name,
            azure_firewall_name="str",
            parameters={"tags": {"str": "str"}},
            api_version="2024-05-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_azure_firewalls_list(self, resource_group):
        response = self.client.azure_firewalls.list(
            resource_group_name=resource_group.name,
            api_version="2024-05-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_azure_firewalls_list_all(self, resource_group):
        response = self.client.azure_firewalls.list_all(
            api_version="2024-05-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_azure_firewalls_begin_list_learned_prefixes(self, resource_group):
        response = self.client.azure_firewalls.begin_list_learned_prefixes(
            resource_group_name=resource_group.name,
            azure_firewall_name="str",
            api_version="2024-05-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_azure_firewalls_begin_packet_capture(self, resource_group):
        response = self.client.azure_firewalls.begin_packet_capture(
            resource_group_name=resource_group.name,
            azure_firewall_name="str",
            parameters={
                "durationInSeconds": 0,
                "fileName": "str",
                "filters": [{"destinationPorts": ["str"], "destinations": ["str"], "sources": ["str"]}],
                "flags": [{"type": "str"}],
                "numberOfPacketsToCapture": 0,
                "protocol": "str",
                "sasUrl": "str",
            },
            api_version="2024-05-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
