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
class TestNetworkManagementStaticMembersOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(NetworkManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_static_members_get(self, resource_group):
        response = self.client.static_members.get(
            resource_group_name=resource_group.name,
            network_manager_name="str",
            network_group_name="str",
            static_member_name="str",
            api_version="2024-05-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_static_members_create_or_update(self, resource_group):
        response = self.client.static_members.create_or_update(
            resource_group_name=resource_group.name,
            network_manager_name="str",
            network_group_name="str",
            static_member_name="str",
            parameters={
                "etag": "str",
                "id": "str",
                "name": "str",
                "provisioningState": "str",
                "region": "str",
                "resourceId": "str",
                "systemData": {
                    "createdAt": "2020-02-20 00:00:00",
                    "createdBy": "str",
                    "createdByType": "str",
                    "lastModifiedAt": "2020-02-20 00:00:00",
                    "lastModifiedBy": "str",
                    "lastModifiedByType": "str",
                },
                "type": "str",
            },
            api_version="2024-05-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_static_members_delete(self, resource_group):
        response = self.client.static_members.delete(
            resource_group_name=resource_group.name,
            network_manager_name="str",
            network_group_name="str",
            static_member_name="str",
            api_version="2024-05-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_static_members_list(self, resource_group):
        response = self.client.static_members.list(
            resource_group_name=resource_group.name,
            network_manager_name="str",
            network_group_name="str",
            api_version="2024-05-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
