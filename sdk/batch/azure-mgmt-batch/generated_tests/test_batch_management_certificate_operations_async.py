# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.batch.aio import BatchManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestBatchManagementCertificateOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(BatchManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_by_batch_account(self, resource_group):
        response = self.client.certificate.list_by_batch_account(
            resource_group_name=resource_group.name,
            account_name="str",
            api_version="2024-07-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_create(self, resource_group):
        response = await self.client.certificate.create(
            resource_group_name=resource_group.name,
            account_name="str",
            certificate_name="str",
            parameters={
                "data": "str",
                "etag": "str",
                "format": "str",
                "id": "str",
                "name": "str",
                "password": "str",
                "tags": {"str": "str"},
                "thumbprint": "str",
                "thumbprintAlgorithm": "str",
                "type": "str",
            },
            api_version="2024-07-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_update(self, resource_group):
        response = await self.client.certificate.update(
            resource_group_name=resource_group.name,
            account_name="str",
            certificate_name="str",
            parameters={
                "data": "str",
                "etag": "str",
                "format": "str",
                "id": "str",
                "name": "str",
                "password": "str",
                "tags": {"str": "str"},
                "thumbprint": "str",
                "thumbprintAlgorithm": "str",
                "type": "str",
            },
            api_version="2024-07-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_delete(self, resource_group):
        response = await (
            await self.client.certificate.begin_delete(
                resource_group_name=resource_group.name,
                account_name="str",
                certificate_name="str",
                api_version="2024-07-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get(self, resource_group):
        response = await self.client.certificate.get(
            resource_group_name=resource_group.name,
            account_name="str",
            certificate_name="str",
            api_version="2024-07-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_cancel_deletion(self, resource_group):
        response = await self.client.certificate.cancel_deletion(
            resource_group_name=resource_group.name,
            account_name="str",
            certificate_name="str",
            api_version="2024-07-01",
        )

        # please add some check logic here by yourself
        # ...
