# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.eventhub.aio import EventHubManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestEventHubManagementClustersOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(EventHubManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_clusters_list_available_cluster_region(self, resource_group):
        response = await self.client.clusters.list_available_cluster_region(
            api_version="2024-01-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_clusters_list_by_subscription(self, resource_group):
        response = self.client.clusters.list_by_subscription(
            api_version="2024-01-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_clusters_list_by_resource_group(self, resource_group):
        response = self.client.clusters.list_by_resource_group(
            resource_group_name=resource_group.name,
            api_version="2024-01-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_clusters_get(self, resource_group):
        response = await self.client.clusters.get(
            resource_group_name=resource_group.name,
            cluster_name="str",
            api_version="2024-01-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_clusters_begin_create_or_update(self, resource_group):
        response = await (
            await self.client.clusters.begin_create_or_update(
                resource_group_name=resource_group.name,
                cluster_name="str",
                parameters={
                    "createdAt": "str",
                    "id": "str",
                    "location": "str",
                    "metricId": "str",
                    "name": "str",
                    "provisioningState": "str",
                    "sku": {"name": "str", "capacity": 0},
                    "status": "str",
                    "supportsScaling": bool,
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
                    "updatedAt": "str",
                },
                api_version="2024-01-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_clusters_begin_update(self, resource_group):
        response = await (
            await self.client.clusters.begin_update(
                resource_group_name=resource_group.name,
                cluster_name="str",
                parameters={
                    "createdAt": "str",
                    "id": "str",
                    "location": "str",
                    "metricId": "str",
                    "name": "str",
                    "provisioningState": "str",
                    "sku": {"name": "str", "capacity": 0},
                    "status": "str",
                    "supportsScaling": bool,
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
                    "updatedAt": "str",
                },
                api_version="2024-01-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_clusters_begin_delete(self, resource_group):
        response = await (
            await self.client.clusters.begin_delete(
                resource_group_name=resource_group.name,
                cluster_name="str",
                api_version="2024-01-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_clusters_list_namespaces(self, resource_group):
        response = await self.client.clusters.list_namespaces(
            resource_group_name=resource_group.name,
            cluster_name="str",
            api_version="2024-01-01",
        )

        # please add some check logic here by yourself
        # ...
