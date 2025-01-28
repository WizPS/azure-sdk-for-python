# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.network.aio import NetworkManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNetworkManagementVirtualNetworkGatewayNatRulesOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(NetworkManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_virtual_network_gateway_nat_rules_get(self, resource_group):
        response = await self.client.virtual_network_gateway_nat_rules.get(
            resource_group_name=resource_group.name,
            virtual_network_gateway_name="str",
            nat_rule_name="str",
            api_version="2024-05-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_virtual_network_gateway_nat_rules_begin_create_or_update(self, resource_group):
        response = await (
            await self.client.virtual_network_gateway_nat_rules.begin_create_or_update(
                resource_group_name=resource_group.name,
                virtual_network_gateway_name="str",
                nat_rule_name="str",
                nat_rule_parameters={
                    "etag": "str",
                    "externalMappings": [{"addressSpace": "str", "portRange": "str"}],
                    "id": "str",
                    "internalMappings": [{"addressSpace": "str", "portRange": "str"}],
                    "ipConfigurationId": "str",
                    "mode": "str",
                    "name": "str",
                    "provisioningState": "str",
                    "type": "str",
                },
                api_version="2024-05-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_virtual_network_gateway_nat_rules_begin_delete(self, resource_group):
        response = await (
            await self.client.virtual_network_gateway_nat_rules.begin_delete(
                resource_group_name=resource_group.name,
                virtual_network_gateway_name="str",
                nat_rule_name="str",
                api_version="2024-05-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_virtual_network_gateway_nat_rules_list_by_virtual_network_gateway(self, resource_group):
        response = self.client.virtual_network_gateway_nat_rules.list_by_virtual_network_gateway(
            resource_group_name=resource_group.name,
            virtual_network_gateway_name="str",
            api_version="2024-05-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...
