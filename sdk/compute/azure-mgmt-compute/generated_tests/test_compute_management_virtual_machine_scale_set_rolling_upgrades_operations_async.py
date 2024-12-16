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
class TestComputeManagementVirtualMachineScaleSetRollingUpgradesOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(ComputeManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_virtual_machine_scale_set_rolling_upgrades_begin_cancel(self, resource_group):
        response = await (
            await self.client.virtual_machine_scale_set_rolling_upgrades.begin_cancel(
                resource_group_name=resource_group.name,
                vm_scale_set_name="str",
                api_version="2024-07-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_virtual_machine_scale_set_rolling_upgrades_begin_start_os_upgrade(self, resource_group):
        response = await (
            await self.client.virtual_machine_scale_set_rolling_upgrades.begin_start_os_upgrade(
                resource_group_name=resource_group.name,
                vm_scale_set_name="str",
                api_version="2024-07-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_virtual_machine_scale_set_rolling_upgrades_begin_start_extension_upgrade(self, resource_group):
        response = await (
            await self.client.virtual_machine_scale_set_rolling_upgrades.begin_start_extension_upgrade(
                resource_group_name=resource_group.name,
                vm_scale_set_name="str",
                api_version="2024-07-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_virtual_machine_scale_set_rolling_upgrades_get_latest(self, resource_group):
        response = await self.client.virtual_machine_scale_set_rolling_upgrades.get_latest(
            resource_group_name=resource_group.name,
            vm_scale_set_name="str",
            api_version="2024-07-01",
        )

        # please add some check logic here by yourself
        # ...
