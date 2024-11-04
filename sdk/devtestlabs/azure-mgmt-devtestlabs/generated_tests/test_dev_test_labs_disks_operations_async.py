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
class TestDevTestLabsDisksOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(DevTestLabsClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list(self, resource_group):
        response = self.client.disks.list(
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
        response = await self.client.disks.get(
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
            await self.client.disks.begin_create_or_update(
                resource_group_name=resource_group.name,
                lab_name="str",
                user_name="str",
                name="str",
                disk={
                    "createdDate": "2020-02-20 00:00:00",
                    "diskBlobName": "str",
                    "diskSizeGiB": 0,
                    "diskType": "str",
                    "diskUri": "str",
                    "hostCaching": "str",
                    "id": "str",
                    "leasedByLabVmId": "str",
                    "location": "str",
                    "managedDiskId": "str",
                    "name": "str",
                    "provisioningState": "str",
                    "storageAccountId": "str",
                    "tags": {"str": "str"},
                    "type": "str",
                    "uniqueIdentifier": "str",
                },
                api_version="2018-09-15",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_delete(self, resource_group):
        response = await (
            await self.client.disks.begin_delete(
                resource_group_name=resource_group.name,
                lab_name="str",
                user_name="str",
                name="str",
                api_version="2018-09-15",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_update(self, resource_group):
        response = await self.client.disks.update(
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
    async def test_begin_attach(self, resource_group):
        response = await (
            await self.client.disks.begin_attach(
                resource_group_name=resource_group.name,
                lab_name="str",
                user_name="str",
                name="str",
                api_version="2018-09-15",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_detach(self, resource_group):
        response = await (
            await self.client.disks.begin_detach(
                resource_group_name=resource_group.name,
                lab_name="str",
                user_name="str",
                name="str",
                api_version="2018-09-15",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
