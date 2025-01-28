# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.sql.aio import SqlManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestSqlManagementExtendedServerBlobAuditingPoliciesOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(SqlManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_by_server(self, resource_group):
        response = self.client.extended_server_blob_auditing_policies.list_by_server(
            resource_group_name=resource_group.name,
            server_name="str",
            api_version="2021-11-01-preview",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get(self, resource_group):
        response = await self.client.extended_server_blob_auditing_policies.get(
            resource_group_name=resource_group.name,
            server_name="str",
            blob_auditing_policy_name="default",
            api_version="2021-11-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_create_or_update(self, resource_group):
        response = await (
            await self.client.extended_server_blob_auditing_policies.begin_create_or_update(
                resource_group_name=resource_group.name,
                server_name="str",
                parameters={
                    "auditActionsAndGroups": ["str"],
                    "id": "str",
                    "isAzureMonitorTargetEnabled": bool,
                    "isDevopsAuditEnabled": bool,
                    "isManagedIdentityInUse": bool,
                    "isStorageSecondaryKeyInUse": bool,
                    "name": "str",
                    "predicateExpression": "str",
                    "queueDelayMs": 0,
                    "retentionDays": 0,
                    "state": "str",
                    "storageAccountAccessKey": "str",
                    "storageAccountSubscriptionId": "str",
                    "storageEndpoint": "str",
                    "type": "str",
                },
                blob_auditing_policy_name="default",
                api_version="2021-11-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
