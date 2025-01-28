# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.qumulo import QumuloMgmtClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestQumuloMgmtFileSystemsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(QumuloMgmtClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_by_subscription(self, resource_group):
        response = self.client.file_systems.list_by_subscription(
            api_version="2024-06-19",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_by_resource_group(self, resource_group):
        response = self.client.file_systems.list_by_resource_group(
            resource_group_name=resource_group.name,
            api_version="2024-06-19",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.file_systems.get(
            resource_group_name=resource_group.name,
            file_system_name="str",
            api_version="2024-06-19",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_create_or_update(self, resource_group):
        response = self.client.file_systems.begin_create_or_update(
            resource_group_name=resource_group.name,
            file_system_name="str",
            resource={
                "location": "str",
                "adminPassword": "str",
                "availabilityZone": "str",
                "clusterLoginUrl": "str",
                "delegatedSubnetId": "str",
                "id": "str",
                "identity": {
                    "type": "str",
                    "principalId": "str",
                    "tenantId": "str",
                    "userAssignedIdentities": {"str": {"clientId": "str", "principalId": "str"}},
                },
                "marketplaceDetails": {
                    "offerId": "str",
                    "planId": "str",
                    "marketplaceSubscriptionId": "str",
                    "marketplaceSubscriptionStatus": "str",
                    "publisherId": "str",
                    "termUnit": "str",
                },
                "name": "str",
                "privateIPs": ["str"],
                "provisioningState": "str",
                "storageSku": "str",
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
                "userDetails": {"email": "str"},
            },
            api_version="2024-06-19",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_update(self, resource_group):
        response = self.client.file_systems.update(
            resource_group_name=resource_group.name,
            file_system_name="str",
            properties={
                "identity": {
                    "type": "str",
                    "principalId": "str",
                    "tenantId": "str",
                    "userAssignedIdentities": {"str": {"clientId": "str", "principalId": "str"}},
                },
                "properties": {
                    "delegatedSubnetId": "str",
                    "marketplaceDetails": {
                        "offerId": "str",
                        "planId": "str",
                        "marketplaceSubscriptionId": "str",
                        "marketplaceSubscriptionStatus": "str",
                        "publisherId": "str",
                        "termUnit": "str",
                    },
                    "userDetails": {"email": "str"},
                },
                "tags": {"str": "str"},
            },
            api_version="2024-06-19",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_delete(self, resource_group):
        response = self.client.file_systems.begin_delete(
            resource_group_name=resource_group.name,
            file_system_name="str",
            api_version="2024-06-19",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
