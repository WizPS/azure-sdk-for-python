# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.quota.aio import QuotaMgmtClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestQuotaMgmtGroupQuotaSubscriptionAllocationRequestOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(QuotaMgmtClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_group_quota_subscription_allocation_request_begin_update(self, resource_group):
        response = await (
            await self.client.group_quota_subscription_allocation_request.begin_update(
                management_group_id="str",
                group_quota_name="str",
                resource_provider_name="str",
                location="str",
                allocate_quota_request={
                    "id": "str",
                    "name": "str",
                    "properties": {
                        "nextLink": "str",
                        "provisioningState": "str",
                        "value": [
                            {
                                "properties": {
                                    "limit": 0,
                                    "name": {"localizedValue": "str", "value": "str"},
                                    "resourceName": "str",
                                    "shareableQuota": 0,
                                }
                            }
                        ],
                    },
                    "systemData": {
                        "createdAt": "2020-02-20 00:00:00",
                        "createdBy": "str",
                        "createdByType": "str",
                        "lastModifiedAt": "2020-02-20 00:00:00",
                        "lastModifiedBy": "str",
                        "lastModifiedByType": "str",
                    },
                    "type": "str",
                },
                api_version="2024-12-18-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_group_quota_subscription_allocation_request_get(self, resource_group):
        response = await self.client.group_quota_subscription_allocation_request.get(
            management_group_id="str",
            group_quota_name="str",
            resource_provider_name="str",
            allocation_id="str",
            api_version="2024-12-18-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_group_quota_subscription_allocation_request_list(self, resource_group):
        response = self.client.group_quota_subscription_allocation_request.list(
            management_group_id="str",
            group_quota_name="str",
            resource_provider_name="str",
            filter="str",
            api_version="2024-12-18-preview",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...
