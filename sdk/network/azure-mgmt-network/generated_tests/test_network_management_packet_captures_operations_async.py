# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.network.aio import NetworkManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNetworkManagementPacketCapturesOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(NetworkManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_packet_captures_begin_create(self, resource_group):
        response = await (
            await self.client.packet_captures.begin_create(
                resource_group_name=resource_group.name,
                network_watcher_name="str",
                packet_capture_name="str",
                parameters={
                    "storageLocation": {
                        "filePath": "str",
                        "localPath": "str",
                        "storageId": "str",
                        "storagePath": "str",
                    },
                    "target": "str",
                    "bytesToCapturePerPacket": 0,
                    "captureSettings": {
                        "fileCount": 10,
                        "fileSizeInBytes": 104857600,
                        "sessionTimeLimitInSeconds": 86400,
                    },
                    "continuousCapture": bool,
                    "filters": [
                        {
                            "localIPAddress": "str",
                            "localPort": "str",
                            "protocol": "Any",
                            "remoteIPAddress": "str",
                            "remotePort": "str",
                        }
                    ],
                    "scope": {"exclude": ["str"], "include": ["str"]},
                    "targetType": "str",
                    "timeLimitInSeconds": 18000,
                    "totalBytesPerSession": 1073741824,
                },
                api_version="2024-05-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_packet_captures_get(self, resource_group):
        response = await self.client.packet_captures.get(
            resource_group_name=resource_group.name,
            network_watcher_name="str",
            packet_capture_name="str",
            api_version="2024-05-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_packet_captures_begin_delete(self, resource_group):
        response = await (
            await self.client.packet_captures.begin_delete(
                resource_group_name=resource_group.name,
                network_watcher_name="str",
                packet_capture_name="str",
                api_version="2024-05-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_packet_captures_begin_stop(self, resource_group):
        response = await (
            await self.client.packet_captures.begin_stop(
                resource_group_name=resource_group.name,
                network_watcher_name="str",
                packet_capture_name="str",
                api_version="2024-05-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_packet_captures_begin_get_status(self, resource_group):
        response = await (
            await self.client.packet_captures.begin_get_status(
                resource_group_name=resource_group.name,
                network_watcher_name="str",
                packet_capture_name="str",
                api_version="2024-05-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_packet_captures_list(self, resource_group):
        response = self.client.packet_captures.list(
            resource_group_name=resource_group.name,
            network_watcher_name="str",
            api_version="2024-05-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...
