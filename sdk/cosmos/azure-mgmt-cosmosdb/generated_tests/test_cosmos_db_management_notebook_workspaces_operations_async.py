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
class TestCosmosDBManagementNotebookWorkspacesOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(CosmosDBManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_notebook_workspaces_list_by_database_account(self, resource_group):
        response = self.client.notebook_workspaces.list_by_database_account(
            resource_group_name=resource_group.name,
            account_name="str",
            api_version="2024-12-01-preview",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_notebook_workspaces_get(self, resource_group):
        response = await self.client.notebook_workspaces.get(
            resource_group_name=resource_group.name,
            account_name="str",
            notebook_workspace_name="str",
            api_version="2024-12-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_notebook_workspaces_begin_create_or_update(self, resource_group):
        response = await (
            await self.client.notebook_workspaces.begin_create_or_update(
                resource_group_name=resource_group.name,
                account_name="str",
                notebook_workspace_name="str",
                notebook_create_update_parameters={"id": "str", "name": "str", "type": "str"},
                api_version="2024-12-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_notebook_workspaces_begin_delete(self, resource_group):
        response = await (
            await self.client.notebook_workspaces.begin_delete(
                resource_group_name=resource_group.name,
                account_name="str",
                notebook_workspace_name="str",
                api_version="2024-12-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_notebook_workspaces_list_connection_info(self, resource_group):
        response = await self.client.notebook_workspaces.list_connection_info(
            resource_group_name=resource_group.name,
            account_name="str",
            notebook_workspace_name="str",
            api_version="2024-12-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_notebook_workspaces_begin_regenerate_auth_token(self, resource_group):
        response = await (
            await self.client.notebook_workspaces.begin_regenerate_auth_token(
                resource_group_name=resource_group.name,
                account_name="str",
                notebook_workspace_name="str",
                api_version="2024-12-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_notebook_workspaces_begin_start(self, resource_group):
        response = await (
            await self.client.notebook_workspaces.begin_start(
                resource_group_name=resource_group.name,
                account_name="str",
                notebook_workspace_name="str",
                api_version="2024-12-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
