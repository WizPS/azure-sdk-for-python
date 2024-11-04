# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.devtestlabs.aio import DevTestLabsClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestDevTestLabsSecretsOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(DevTestLabsClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list(self, resource_group):
        response = self.client.secrets.list(
            resource_group_name=resource_group.name,
            lab_name="str",
            user_name="str",
            api_version="2018-09-15",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get(self, resource_group):
        response = await self.client.secrets.get(
            resource_group_name=resource_group.name,
            lab_name="str",
            user_name="str",
            name="str",
            api_version="2018-09-15",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_create_or_update(self, resource_group):
        response = await (
            await self.client.secrets.begin_create_or_update(
                resource_group_name=resource_group.name,
                lab_name="str",
                user_name="str",
                name="str",
                secret={
                    "id": "str",
                    "location": "str",
                    "name": "str",
                    "provisioningState": "str",
                    "tags": {"str": "str"},
                    "type": "str",
                    "uniqueIdentifier": "str",
                    "value": "str",
                },
                api_version="2018-09-15",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_delete(self, resource_group):
        response = await self.client.secrets.delete(
            resource_group_name=resource_group.name,
            lab_name="str",
            user_name="str",
            name="str",
            api_version="2018-09-15",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_update(self, resource_group):
        response = await self.client.secrets.update(
            resource_group_name=resource_group.name,
            lab_name="str",
            user_name="str",
            name="str",
            api_version="2018-09-15",
        )

        # please add some check logic here by yourself
        # ...
