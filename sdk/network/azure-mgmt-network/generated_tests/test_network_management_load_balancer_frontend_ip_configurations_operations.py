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
class TestNetworkManagementLoadBalancerFrontendIPConfigurationsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(NetworkManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_load_balancer_frontend_ip_configurations_list(self, resource_group):
        response = self.client.load_balancer_frontend_ip_configurations.list(
            resource_group_name=resource_group.name,
            load_balancer_name="str",
            api_version="2024-05-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_load_balancer_frontend_ip_configurations_get(self, resource_group):
        response = self.client.load_balancer_frontend_ip_configurations.get(
            resource_group_name=resource_group.name,
            load_balancer_name="str",
            frontend_ip_configuration_name="str",
            api_version="2024-05-01",
        )

        # please add some check logic here by yourself
        # ...
