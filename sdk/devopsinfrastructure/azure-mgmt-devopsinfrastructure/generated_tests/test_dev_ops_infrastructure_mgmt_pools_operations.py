# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.devopsinfrastructure import DevOpsInfrastructureMgmtClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestDevOpsInfrastructureMgmtPoolsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(DevOpsInfrastructureMgmtClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_pools_get(self, resource_group):
        response = self.client.pools.get(
            resource_group_name=resource_group.name,
            pool_name="str",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_pools_begin_create_or_update(self, resource_group):
        response = self.client.pools.begin_create_or_update(
            resource_group_name=resource_group.name,
            pool_name="str",
            resource={
                "location": "str",
                "id": "str",
                "identity": {
                    "type": "str",
                    "principalId": "str",
                    "tenantId": "str",
                    "userAssignedIdentities": {"str": {"clientId": "str", "principalId": "str"}},
                },
                "name": "str",
                "properties": {
                    "agentProfile": "agent_profile",
                    "devCenterProjectResourceId": "str",
                    "fabricProfile": "fabric_profile",
                    "maximumConcurrency": 0,
                    "organizationProfile": "organization_profile",
                    "provisioningState": "str",
                },
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
            },
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_pools_begin_update(self, resource_group):
        response = self.client.pools.begin_update(
            resource_group_name=resource_group.name,
            pool_name="str",
            properties={
                "identity": {
                    "type": "str",
                    "principalId": "str",
                    "tenantId": "str",
                    "userAssignedIdentities": {"str": {"clientId": "str", "principalId": "str"}},
                },
                "properties": {
                    "agentProfile": "agent_profile",
                    "devCenterProjectResourceId": "str",
                    "fabricProfile": "fabric_profile",
                    "maximumConcurrency": 0,
                    "organizationProfile": "organization_profile",
                    "provisioningState": "str",
                },
                "tags": {"str": "str"},
            },
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_pools_begin_delete(self, resource_group):
        response = self.client.pools.begin_delete(
            resource_group_name=resource_group.name,
            pool_name="str",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_pools_list_by_resource_group(self, resource_group):
        response = self.client.pools.list_by_resource_group(
            resource_group_name=resource_group.name,
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_pools_list_by_subscription(self, resource_group):
        response = self.client.pools.list_by_subscription()
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
