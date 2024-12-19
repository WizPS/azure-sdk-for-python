# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.cognitiveservices.aio import CognitiveServicesManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestCognitiveServicesManagementRaiPoliciesOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(CognitiveServicesManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list(self, resource_group):
        response = self.client.rai_policies.list(
            resource_group_name=resource_group.name,
            account_name="str",
            api_version="2024-10-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get(self, resource_group):
        response = await self.client.rai_policies.get(
            resource_group_name=resource_group.name,
            account_name="str",
            rai_policy_name="str",
            api_version="2024-10-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_create_or_update(self, resource_group):
        response = await self.client.rai_policies.create_or_update(
            resource_group_name=resource_group.name,
            account_name="str",
            rai_policy_name="str",
            rai_policy={
                "etag": "str",
                "id": "str",
                "name": "str",
                "properties": {
                    "basePolicyName": "str",
                    "contentFilters": [
                        {"blocking": bool, "enabled": bool, "name": "str", "severityThreshold": "str", "source": "str"}
                    ],
                    "customBlocklists": [{"blocking": bool, "blocklistName": "str", "source": "str"}],
                    "mode": "str",
                    "type": "str",
                },
                "systemData": {
                    "createdAt": "2020-02-20 00:00:00",
                    "createdBy": "str",
                    "createdByType": "str",
                    "lastModifiedAt": "2020-02-20 00:00:00",
                    "lastModifiedBy": "str",
                    "lastModifiedByType": "str",
                },
                "tags": {"str": "str"},
                "type": "str",
            },
            api_version="2024-10-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_delete(self, resource_group):
        response = await (
            await self.client.rai_policies.begin_delete(
                resource_group_name=resource_group.name,
                account_name="str",
                rai_policy_name="str",
                api_version="2024-10-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
