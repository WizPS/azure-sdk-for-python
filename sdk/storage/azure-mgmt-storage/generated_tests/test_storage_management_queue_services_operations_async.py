# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.storage.aio import StorageManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestStorageManagementQueueServicesOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(StorageManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_queue_services_list(self, resource_group):
        response = await self.client.queue_services.list(
            resource_group_name=resource_group.name,
            account_name="str",
            api_version="2023-05-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_queue_services_set_service_properties(self, resource_group):
        response = await self.client.queue_services.set_service_properties(
            resource_group_name=resource_group.name,
            account_name="str",
            parameters={
                "cors": {
                    "corsRules": [
                        {
                            "allowedHeaders": ["str"],
                            "allowedMethods": ["str"],
                            "allowedOrigins": ["str"],
                            "exposedHeaders": ["str"],
                            "maxAgeInSeconds": 0,
                        }
                    ]
                },
                "id": "str",
                "name": "str",
                "type": "str",
            },
            api_version="2023-05-01",
            queue_service_name="default",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_queue_services_get_service_properties(self, resource_group):
        response = await self.client.queue_services.get_service_properties(
            resource_group_name=resource_group.name,
            account_name="str",
            api_version="2023-05-01",
            queue_service_name="default",
        )

        # please add some check logic here by yourself
        # ...
