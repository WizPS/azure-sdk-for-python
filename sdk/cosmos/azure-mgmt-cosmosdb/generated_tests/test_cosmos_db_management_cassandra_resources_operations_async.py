# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.cosmosdb.aio import CosmosDBManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestCosmosDBManagementCassandraResourcesOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(CosmosDBManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_cassandra_resources_list_cassandra_keyspaces(self, resource_group):
        response = self.client.cassandra_resources.list_cassandra_keyspaces(
            resource_group_name=resource_group.name,
            account_name="str",
            api_version="2024-12-01-preview",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_cassandra_resources_get_cassandra_keyspace(self, resource_group):
        response = await self.client.cassandra_resources.get_cassandra_keyspace(
            resource_group_name=resource_group.name,
            account_name="str",
            keyspace_name="str",
            api_version="2024-12-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_cassandra_resources_begin_create_update_cassandra_keyspace(self, resource_group):
        response = await (
            await self.client.cassandra_resources.begin_create_update_cassandra_keyspace(
                resource_group_name=resource_group.name,
                account_name="str",
                keyspace_name="str",
                create_update_cassandra_keyspace_parameters={
                    "resource": {"id": "str"},
                    "id": "str",
                    "identity": {
                        "principalId": "str",
                        "tenantId": "str",
                        "type": "str",
                        "userAssignedIdentities": {"str": {"clientId": "str", "principalId": "str"}},
                    },
                    "location": "str",
                    "name": "str",
                    "options": {"autoscaleSettings": {"maxThroughput": 0}, "throughput": 0},
                    "tags": {"str": "str"},
                    "type": "str",
                },
                api_version="2024-12-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_cassandra_resources_begin_delete_cassandra_keyspace(self, resource_group):
        response = await (
            await self.client.cassandra_resources.begin_delete_cassandra_keyspace(
                resource_group_name=resource_group.name,
                account_name="str",
                keyspace_name="str",
                api_version="2024-12-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_cassandra_resources_get_cassandra_keyspace_throughput(self, resource_group):
        response = await self.client.cassandra_resources.get_cassandra_keyspace_throughput(
            resource_group_name=resource_group.name,
            account_name="str",
            keyspace_name="str",
            api_version="2024-12-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_cassandra_resources_begin_update_cassandra_keyspace_throughput(self, resource_group):
        response = await (
            await self.client.cassandra_resources.begin_update_cassandra_keyspace_throughput(
                resource_group_name=resource_group.name,
                account_name="str",
                keyspace_name="str",
                update_throughput_parameters={
                    "resource": {
                        "autoscaleSettings": {
                            "maxThroughput": 0,
                            "autoUpgradePolicy": {"throughputPolicy": {"incrementPercent": 0, "isEnabled": bool}},
                            "targetMaxThroughput": 0,
                        },
                        "instantMaximumThroughput": "str",
                        "minimumThroughput": "str",
                        "offerReplacePending": "str",
                        "softAllowedMaximumThroughput": "str",
                        "throughput": 0,
                        "throughputBuckets": [{"id": 0, "maxThroughputPercentage": 0}],
                    },
                    "id": "str",
                    "identity": {
                        "principalId": "str",
                        "tenantId": "str",
                        "type": "str",
                        "userAssignedIdentities": {"str": {"clientId": "str", "principalId": "str"}},
                    },
                    "location": "str",
                    "name": "str",
                    "tags": {"str": "str"},
                    "type": "str",
                },
                api_version="2024-12-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_cassandra_resources_begin_migrate_cassandra_keyspace_to_autoscale(self, resource_group):
        response = await (
            await self.client.cassandra_resources.begin_migrate_cassandra_keyspace_to_autoscale(
                resource_group_name=resource_group.name,
                account_name="str",
                keyspace_name="str",
                api_version="2024-12-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_cassandra_resources_begin_migrate_cassandra_keyspace_to_manual_throughput(self, resource_group):
        response = await (
            await self.client.cassandra_resources.begin_migrate_cassandra_keyspace_to_manual_throughput(
                resource_group_name=resource_group.name,
                account_name="str",
                keyspace_name="str",
                api_version="2024-12-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_cassandra_resources_list_cassandra_tables(self, resource_group):
        response = self.client.cassandra_resources.list_cassandra_tables(
            resource_group_name=resource_group.name,
            account_name="str",
            keyspace_name="str",
            api_version="2024-12-01-preview",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_cassandra_resources_get_cassandra_table(self, resource_group):
        response = await self.client.cassandra_resources.get_cassandra_table(
            resource_group_name=resource_group.name,
            account_name="str",
            keyspace_name="str",
            table_name="str",
            api_version="2024-12-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_cassandra_resources_begin_create_update_cassandra_table(self, resource_group):
        response = await (
            await self.client.cassandra_resources.begin_create_update_cassandra_table(
                resource_group_name=resource_group.name,
                account_name="str",
                keyspace_name="str",
                table_name="str",
                create_update_cassandra_table_parameters={
                    "resource": {
                        "id": "str",
                        "analyticalStorageTtl": 0,
                        "defaultTtl": 0,
                        "schema": {
                            "clusterKeys": [{"name": "str", "orderBy": "str"}],
                            "columns": [{"name": "str", "type": "str"}],
                            "partitionKeys": [{"name": "str"}],
                        },
                    },
                    "id": "str",
                    "identity": {
                        "principalId": "str",
                        "tenantId": "str",
                        "type": "str",
                        "userAssignedIdentities": {"str": {"clientId": "str", "principalId": "str"}},
                    },
                    "location": "str",
                    "name": "str",
                    "options": {"autoscaleSettings": {"maxThroughput": 0}, "throughput": 0},
                    "tags": {"str": "str"},
                    "type": "str",
                },
                api_version="2024-12-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_cassandra_resources_begin_delete_cassandra_table(self, resource_group):
        response = await (
            await self.client.cassandra_resources.begin_delete_cassandra_table(
                resource_group_name=resource_group.name,
                account_name="str",
                keyspace_name="str",
                table_name="str",
                api_version="2024-12-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_cassandra_resources_get_cassandra_table_throughput(self, resource_group):
        response = await self.client.cassandra_resources.get_cassandra_table_throughput(
            resource_group_name=resource_group.name,
            account_name="str",
            keyspace_name="str",
            table_name="str",
            api_version="2024-12-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_cassandra_resources_begin_update_cassandra_table_throughput(self, resource_group):
        response = await (
            await self.client.cassandra_resources.begin_update_cassandra_table_throughput(
                resource_group_name=resource_group.name,
                account_name="str",
                keyspace_name="str",
                table_name="str",
                update_throughput_parameters={
                    "resource": {
                        "autoscaleSettings": {
                            "maxThroughput": 0,
                            "autoUpgradePolicy": {"throughputPolicy": {"incrementPercent": 0, "isEnabled": bool}},
                            "targetMaxThroughput": 0,
                        },
                        "instantMaximumThroughput": "str",
                        "minimumThroughput": "str",
                        "offerReplacePending": "str",
                        "softAllowedMaximumThroughput": "str",
                        "throughput": 0,
                        "throughputBuckets": [{"id": 0, "maxThroughputPercentage": 0}],
                    },
                    "id": "str",
                    "identity": {
                        "principalId": "str",
                        "tenantId": "str",
                        "type": "str",
                        "userAssignedIdentities": {"str": {"clientId": "str", "principalId": "str"}},
                    },
                    "location": "str",
                    "name": "str",
                    "tags": {"str": "str"},
                    "type": "str",
                },
                api_version="2024-12-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_cassandra_resources_begin_migrate_cassandra_table_to_autoscale(self, resource_group):
        response = await (
            await self.client.cassandra_resources.begin_migrate_cassandra_table_to_autoscale(
                resource_group_name=resource_group.name,
                account_name="str",
                keyspace_name="str",
                table_name="str",
                api_version="2024-12-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_cassandra_resources_begin_migrate_cassandra_table_to_manual_throughput(self, resource_group):
        response = await (
            await self.client.cassandra_resources.begin_migrate_cassandra_table_to_manual_throughput(
                resource_group_name=resource_group.name,
                account_name="str",
                keyspace_name="str",
                table_name="str",
                api_version="2024-12-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_cassandra_resources_list_cassandra_views(self, resource_group):
        response = self.client.cassandra_resources.list_cassandra_views(
            resource_group_name=resource_group.name,
            account_name="str",
            keyspace_name="str",
            api_version="2024-12-01-preview",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_cassandra_resources_get_cassandra_view(self, resource_group):
        response = await self.client.cassandra_resources.get_cassandra_view(
            resource_group_name=resource_group.name,
            account_name="str",
            keyspace_name="str",
            view_name="str",
            api_version="2024-12-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_cassandra_resources_begin_create_update_cassandra_view(self, resource_group):
        response = await (
            await self.client.cassandra_resources.begin_create_update_cassandra_view(
                resource_group_name=resource_group.name,
                account_name="str",
                keyspace_name="str",
                view_name="str",
                create_update_cassandra_view_parameters={
                    "resource": {"id": "str", "viewDefinition": "str"},
                    "id": "str",
                    "identity": {
                        "principalId": "str",
                        "tenantId": "str",
                        "type": "str",
                        "userAssignedIdentities": {"str": {"clientId": "str", "principalId": "str"}},
                    },
                    "location": "str",
                    "name": "str",
                    "options": {"autoscaleSettings": {"maxThroughput": 0}, "throughput": 0},
                    "tags": {"str": "str"},
                    "type": "str",
                },
                api_version="2024-12-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_cassandra_resources_begin_delete_cassandra_view(self, resource_group):
        response = await (
            await self.client.cassandra_resources.begin_delete_cassandra_view(
                resource_group_name=resource_group.name,
                account_name="str",
                keyspace_name="str",
                view_name="str",
                api_version="2024-12-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_cassandra_resources_get_cassandra_view_throughput(self, resource_group):
        response = await self.client.cassandra_resources.get_cassandra_view_throughput(
            resource_group_name=resource_group.name,
            account_name="str",
            keyspace_name="str",
            view_name="str",
            api_version="2024-12-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_cassandra_resources_begin_update_cassandra_view_throughput(self, resource_group):
        response = await (
            await self.client.cassandra_resources.begin_update_cassandra_view_throughput(
                resource_group_name=resource_group.name,
                account_name="str",
                keyspace_name="str",
                view_name="str",
                update_throughput_parameters={
                    "resource": {
                        "autoscaleSettings": {
                            "maxThroughput": 0,
                            "autoUpgradePolicy": {"throughputPolicy": {"incrementPercent": 0, "isEnabled": bool}},
                            "targetMaxThroughput": 0,
                        },
                        "instantMaximumThroughput": "str",
                        "minimumThroughput": "str",
                        "offerReplacePending": "str",
                        "softAllowedMaximumThroughput": "str",
                        "throughput": 0,
                        "throughputBuckets": [{"id": 0, "maxThroughputPercentage": 0}],
                    },
                    "id": "str",
                    "identity": {
                        "principalId": "str",
                        "tenantId": "str",
                        "type": "str",
                        "userAssignedIdentities": {"str": {"clientId": "str", "principalId": "str"}},
                    },
                    "location": "str",
                    "name": "str",
                    "tags": {"str": "str"},
                    "type": "str",
                },
                api_version="2024-12-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_cassandra_resources_begin_migrate_cassandra_view_to_autoscale(self, resource_group):
        response = await (
            await self.client.cassandra_resources.begin_migrate_cassandra_view_to_autoscale(
                resource_group_name=resource_group.name,
                account_name="str",
                keyspace_name="str",
                view_name="str",
                api_version="2024-12-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_cassandra_resources_begin_migrate_cassandra_view_to_manual_throughput(self, resource_group):
        response = await (
            await self.client.cassandra_resources.begin_migrate_cassandra_view_to_manual_throughput(
                resource_group_name=resource_group.name,
                account_name="str",
                keyspace_name="str",
                view_name="str",
                api_version="2024-12-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
