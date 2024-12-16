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
class TestComputeManagementVirtualMachineImagesOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(ComputeManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_virtual_machine_images_get(self, resource_group):
        response = await self.client.virtual_machine_images.get(
            location="str",
            publisher_name="str",
            offer="str",
            skus="str",
            version="str",
            api_version="2024-07-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_virtual_machine_images_list(self, resource_group):
        response = await self.client.virtual_machine_images.list(
            location="str",
            publisher_name="str",
            offer="str",
            skus="str",
            api_version="2024-07-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_virtual_machine_images_list_offers(self, resource_group):
        response = await self.client.virtual_machine_images.list_offers(
            location="str",
            publisher_name="str",
            api_version="2024-07-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_virtual_machine_images_list_publishers(self, resource_group):
        response = await self.client.virtual_machine_images.list_publishers(
            location="str",
            api_version="2024-07-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_virtual_machine_images_list_skus(self, resource_group):
        response = await self.client.virtual_machine_images.list_skus(
            location="str",
            publisher_name="str",
            offer="str",
            api_version="2024-07-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_virtual_machine_images_list_by_edge_zone(self, resource_group):
        response = await self.client.virtual_machine_images.list_by_edge_zone(
            location="str",
            edge_zone="str",
            api_version="2024-07-01",
        )

        # please add some check logic here by yourself
        # ...
