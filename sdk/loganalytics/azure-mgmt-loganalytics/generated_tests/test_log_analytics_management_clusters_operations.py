# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.loganalytics import LogAnalyticsManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestLogAnalyticsManagementClustersOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(LogAnalyticsManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_by_resource_group(self, resource_group):
        response = self.client.clusters.list_by_resource_group(
            resource_group_name=resource_group.name,
            api_version="2022-10-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list(self, resource_group):
        response = self.client.clusters.list(
            api_version="2022-10-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_create_or_update(self, resource_group):
        response = self.client.clusters.begin_create_or_update(
            resource_group_name=resource_group.name,
            cluster_name="str",
            parameters={
                "location": "str",
                "associatedWorkspaces": [
                    {"associateDate": "str", "resourceId": "str", "workspaceId": "str", "workspaceName": "str"}
                ],
                "billingType": "str",
                "capacityReservationProperties": {"lastSkuUpdate": "str", "minCapacity": 0},
                "clusterId": "str",
                "createdDate": "str",
                "id": "str",
                "identity": {
                    "type": "str",
                    "principalId": "str",
                    "tenantId": "str",
                    "userAssignedIdentities": {"str": {"clientId": "str", "principalId": "str"}},
                },
                "isAvailabilityZonesEnabled": bool,
                "isDoubleEncryptionEnabled": bool,
                "keyVaultProperties": {"keyName": "str", "keyRsaSize": 0, "keyVaultUri": "str", "keyVersion": "str"},
                "lastModifiedDate": "str",
                "name": "str",
                "provisioningState": "str",
                "sku": {"capacity": 0, "name": "str"},
                "tags": {"str": "str"},
                "type": "str",
            },
            api_version="2022-10-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_delete(self, resource_group):
        response = self.client.clusters.begin_delete(
            resource_group_name=resource_group.name,
            cluster_name="str",
            api_version="2022-10-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.clusters.get(
            resource_group_name=resource_group.name,
            cluster_name="str",
            api_version="2022-10-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_update(self, resource_group):
        response = self.client.clusters.begin_update(
            resource_group_name=resource_group.name,
            cluster_name="str",
            parameters={
                "billingType": "str",
                "identity": {
                    "type": "str",
                    "principalId": "str",
                    "tenantId": "str",
                    "userAssignedIdentities": {"str": {"clientId": "str", "principalId": "str"}},
                },
                "keyVaultProperties": {"keyName": "str", "keyRsaSize": 0, "keyVaultUri": "str", "keyVersion": "str"},
                "sku": {"capacity": 0, "name": "str"},
                "tags": {"str": "str"},
            },
            api_version="2022-10-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
