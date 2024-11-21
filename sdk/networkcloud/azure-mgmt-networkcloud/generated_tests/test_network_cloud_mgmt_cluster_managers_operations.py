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
class TestNetworkCloudMgmtClusterManagersOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(NetworkCloudMgmtClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_by_subscription(self, resource_group):
        response = self.client.cluster_managers.list_by_subscription(
            api_version="2024-06-01-preview",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_by_resource_group(self, resource_group):
        response = self.client.cluster_managers.list_by_resource_group(
            resource_group_name=resource_group.name,
            api_version="2024-06-01-preview",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.cluster_managers.get(
            resource_group_name=resource_group.name,
            cluster_manager_name="str",
            api_version="2024-06-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_create_or_update(self, resource_group):
        response = self.client.cluster_managers.begin_create_or_update(
            resource_group_name=resource_group.name,
            cluster_manager_name="str",
            cluster_manager_parameters={
                "fabricControllerId": "str",
                "location": "str",
                "analyticsWorkspaceId": "str",
                "availabilityZones": ["str"],
                "clusterVersions": [{"supportExpiryDate": "str", "targetClusterVersion": "str"}],
                "detailedStatus": "str",
                "detailedStatusMessage": "str",
                "id": "str",
                "identity": {
                    "type": "str",
                    "principalId": "str",
                    "tenantId": "str",
                    "userAssignedIdentities": {"str": {"clientId": "str", "principalId": "str"}},
                },
                "managedResourceGroupConfiguration": {"location": "str", "name": "str"},
                "managerExtendedLocation": {"name": "str", "type": "str"},
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
                "vmSize": "str",
            },
            api_version="2024-06-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_delete(self, resource_group):
        response = self.client.cluster_managers.begin_delete(
            resource_group_name=resource_group.name,
            cluster_manager_name="str",
            api_version="2024-06-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_update(self, resource_group):
        response = self.client.cluster_managers.update(
            resource_group_name=resource_group.name,
            cluster_manager_name="str",
            api_version="2024-06-01-preview",
        )

        # please add some check logic here by yourself
        # ...
