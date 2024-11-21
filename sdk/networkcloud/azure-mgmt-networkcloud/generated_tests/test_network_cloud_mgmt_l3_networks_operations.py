# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.networkcloud import NetworkCloudMgmtClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNetworkCloudMgmtL3NetworksOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(NetworkCloudMgmtClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_by_subscription(self, resource_group):
        response = self.client.l3_networks.list_by_subscription(
            api_version="2024-06-01-preview",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_by_resource_group(self, resource_group):
        response = self.client.l3_networks.list_by_resource_group(
            resource_group_name=resource_group.name,
            api_version="2024-06-01-preview",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.l3_networks.get(
            resource_group_name=resource_group.name,
            l3_network_name="str",
            api_version="2024-06-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_create_or_update(self, resource_group):
        response = self.client.l3_networks.begin_create_or_update(
            resource_group_name=resource_group.name,
            l3_network_name="str",
            l3_network_parameters={
                "extendedLocation": {"name": "str", "type": "str"},
                "l3IsolationDomainId": "str",
                "location": "str",
                "vlan": 0,
                "associatedResourceIds": ["str"],
                "clusterId": "str",
                "detailedStatus": "str",
                "detailedStatusMessage": "str",
                "hybridAksClustersAssociatedIds": ["str"],
                "hybridAksIpamEnabled": "True",
                "hybridAksPluginType": "str",
                "id": "str",
                "interfaceName": "str",
                "ipAllocationType": "DualStack",
                "ipv4ConnectedPrefix": "str",
                "ipv6ConnectedPrefix": "str",
                "name": "str",
                "provisioningState": "str",
                "systemData": {
                    "createdAt": "2020-02-20 00:00:00",
                    "createdBy": "str",
                    "createdByType": "str",
                    "lastModifiedAt": "2020-02-20 00:00:00",
                    "lastModifiedBy": "str",
                    "lastModifiedByType": "str",
                },
                "tags": {"str": "str"},
                "type": "str",
                "virtualMachinesAssociatedIds": ["str"],
            },
            api_version="2024-06-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_delete(self, resource_group):
        response = self.client.l3_networks.begin_delete(
            resource_group_name=resource_group.name,
            l3_network_name="str",
            api_version="2024-06-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_update(self, resource_group):
        response = self.client.l3_networks.update(
            resource_group_name=resource_group.name,
            l3_network_name="str",
            api_version="2024-06-01-preview",
        )

        # please add some check logic here by yourself
        # ...
