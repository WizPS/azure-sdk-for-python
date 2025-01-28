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
class TestComputeManagementDedicatedHostsOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(ComputeManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_dedicated_hosts_begin_create_or_update(self, resource_group):
        response = await (
            await self.client.dedicated_hosts.begin_create_or_update(
                resource_group_name=resource_group.name,
                host_group_name="str",
                host_name="str",
                parameters={
                    "location": "str",
                    "sku": {"capacity": 0, "name": "str", "tier": "str"},
                    "autoReplaceOnFailure": bool,
                    "hostId": "str",
                    "id": "str",
                    "instanceView": {
                        "assetId": "str",
                        "availableCapacity": {"allocatableVMs": [{"count": 0.0, "vmSize": "str"}]},
                        "statuses": [
                            {
                                "code": "str",
                                "displayStatus": "str",
                                "level": "str",
                                "message": "str",
                                "time": "2020-02-20 00:00:00",
                            }
                        ],
                    },
                    "licenseType": "str",
                    "name": "str",
                    "platformFaultDomain": 0,
                    "provisioningState": "str",
                    "provisioningTime": "2020-02-20 00:00:00",
                    "tags": {"str": "str"},
                    "timeCreated": "2020-02-20 00:00:00",
                    "type": "str",
                    "virtualMachines": [{"id": "str"}],
                },
                api_version="2024-07-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_dedicated_hosts_begin_update(self, resource_group):
        response = await (
            await self.client.dedicated_hosts.begin_update(
                resource_group_name=resource_group.name,
                host_group_name="str",
                host_name="str",
                parameters={
                    "autoReplaceOnFailure": bool,
                    "hostId": "str",
                    "instanceView": {
                        "assetId": "str",
                        "availableCapacity": {"allocatableVMs": [{"count": 0.0, "vmSize": "str"}]},
                        "statuses": [
                            {
                                "code": "str",
                                "displayStatus": "str",
                                "level": "str",
                                "message": "str",
                                "time": "2020-02-20 00:00:00",
                            }
                        ],
                    },
                    "licenseType": "str",
                    "platformFaultDomain": 0,
                    "provisioningState": "str",
                    "provisioningTime": "2020-02-20 00:00:00",
                    "sku": {"capacity": 0, "name": "str", "tier": "str"},
                    "tags": {"str": "str"},
                    "timeCreated": "2020-02-20 00:00:00",
                    "virtualMachines": [{"id": "str"}],
                },
                api_version="2024-07-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_dedicated_hosts_begin_delete(self, resource_group):
        response = await (
            await self.client.dedicated_hosts.begin_delete(
                resource_group_name=resource_group.name,
                host_group_name="str",
                host_name="str",
                api_version="2024-07-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_dedicated_hosts_get(self, resource_group):
        response = await self.client.dedicated_hosts.get(
            resource_group_name=resource_group.name,
            host_group_name="str",
            host_name="str",
            api_version="2024-07-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_dedicated_hosts_list_by_host_group(self, resource_group):
        response = self.client.dedicated_hosts.list_by_host_group(
            resource_group_name=resource_group.name,
            host_group_name="str",
            api_version="2024-07-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_dedicated_hosts_begin_restart(self, resource_group):
        response = await (
            await self.client.dedicated_hosts.begin_restart(
                resource_group_name=resource_group.name,
                host_group_name="str",
                host_name="str",
                api_version="2024-07-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_dedicated_hosts_begin_redeploy(self, resource_group):
        response = await (
            await self.client.dedicated_hosts.begin_redeploy(
                resource_group_name=resource_group.name,
                host_group_name="str",
                host_name="str",
                api_version="2024-07-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_dedicated_hosts_list_available_sizes(self, resource_group):
        response = self.client.dedicated_hosts.list_available_sizes(
            resource_group_name=resource_group.name,
            host_group_name="str",
            host_name="str",
            api_version="2024-07-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...
