# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.compute.aio import ComputeManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestComputeManagementSshPublicKeysOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(ComputeManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_ssh_public_keys_list_by_subscription(self, resource_group):
        response = self.client.ssh_public_keys.list_by_subscription(
            api_version="2024-07-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_ssh_public_keys_list_by_resource_group(self, resource_group):
        response = self.client.ssh_public_keys.list_by_resource_group(
            resource_group_name=resource_group.name,
            api_version="2024-07-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_ssh_public_keys_create(self, resource_group):
        response = await self.client.ssh_public_keys.create(
            resource_group_name=resource_group.name,
            ssh_public_key_name="str",
            parameters={
                "location": "str",
                "id": "str",
                "name": "str",
                "publicKey": "str",
                "tags": {"str": "str"},
                "type": "str",
            },
            api_version="2024-07-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_ssh_public_keys_update(self, resource_group):
        response = await self.client.ssh_public_keys.update(
            resource_group_name=resource_group.name,
            ssh_public_key_name="str",
            parameters={"publicKey": "str", "tags": {"str": "str"}},
            api_version="2024-07-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_ssh_public_keys_delete(self, resource_group):
        response = await self.client.ssh_public_keys.delete(
            resource_group_name=resource_group.name,
            ssh_public_key_name="str",
            api_version="2024-07-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_ssh_public_keys_get(self, resource_group):
        response = await self.client.ssh_public_keys.get(
            resource_group_name=resource_group.name,
            ssh_public_key_name="str",
            api_version="2024-07-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_ssh_public_keys_generate_key_pair(self, resource_group):
        response = await self.client.ssh_public_keys.generate_key_pair(
            resource_group_name=resource_group.name,
            ssh_public_key_name="str",
            api_version="2024-07-01",
        )

        # please add some check logic here by yourself
        # ...
