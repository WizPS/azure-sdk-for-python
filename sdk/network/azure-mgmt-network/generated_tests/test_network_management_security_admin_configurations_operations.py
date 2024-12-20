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
class TestNetworkManagementSecurityAdminConfigurationsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(NetworkManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_security_admin_configurations_list(self, resource_group):
        response = self.client.security_admin_configurations.list(
            resource_group_name=resource_group.name,
            network_manager_name="str",
            api_version="2024-05-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_security_admin_configurations_get(self, resource_group):
        response = self.client.security_admin_configurations.get(
            resource_group_name=resource_group.name,
            network_manager_name="str",
            configuration_name="str",
            api_version="2024-05-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_security_admin_configurations_create_or_update(self, resource_group):
        response = self.client.security_admin_configurations.create_or_update(
            resource_group_name=resource_group.name,
            network_manager_name="str",
            configuration_name="str",
            security_admin_configuration={
                "applyOnNetworkIntentPolicyBasedServices": ["str"],
                "description": "str",
                "etag": "str",
                "id": "str",
                "name": "str",
                "networkGroupAddressSpaceAggregationOption": "str",
                "provisioningState": "str",
                "resourceGuid": "str",
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
    def test_security_admin_configurations_begin_delete(self, resource_group):
        response = self.client.security_admin_configurations.begin_delete(
            resource_group_name=resource_group.name,
            network_manager_name="str",
            configuration_name="str",
            api_version="2024-05-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
