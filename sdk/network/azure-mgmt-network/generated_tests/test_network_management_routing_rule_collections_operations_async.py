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
class TestNetworkManagementRoutingRuleCollectionsOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(NetworkManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_routing_rule_collections_list(self, resource_group):
        response = self.client.routing_rule_collections.list(
            resource_group_name=resource_group.name,
            network_manager_name="str",
            configuration_name="str",
            api_version="2024-05-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_routing_rule_collections_get(self, resource_group):
        response = await self.client.routing_rule_collections.get(
            resource_group_name=resource_group.name,
            network_manager_name="str",
            configuration_name="str",
            rule_collection_name="str",
            api_version="2024-05-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_routing_rule_collections_create_or_update(self, resource_group):
        response = await self.client.routing_rule_collections.create_or_update(
            resource_group_name=resource_group.name,
            network_manager_name="str",
            configuration_name="str",
            rule_collection_name="str",
            rule_collection={
                "appliesTo": [{"networkGroupId": "str"}],
                "description": "str",
                "disableBgpRoutePropagation": "str",
                "etag": "str",
                "id": "str",
                "name": "str",
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
    @recorded_by_proxy_async
    async def test_routing_rule_collections_begin_delete(self, resource_group):
        response = await (
            await self.client.routing_rule_collections.begin_delete(
                resource_group_name=resource_group.name,
                network_manager_name="str",
                configuration_name="str",
                rule_collection_name="str",
                api_version="2024-05-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
