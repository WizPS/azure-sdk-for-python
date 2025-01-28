# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.datafactory.aio import DataFactoryManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestDataFactoryManagementTriggerRunsOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(DataFactoryManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_trigger_runs_rerun(self, resource_group):
        response = await self.client.trigger_runs.rerun(
            resource_group_name=resource_group.name,
            factory_name="str",
            trigger_name="str",
            run_id="str",
            api_version="2018-06-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_trigger_runs_cancel(self, resource_group):
        response = await self.client.trigger_runs.cancel(
            resource_group_name=resource_group.name,
            factory_name="str",
            trigger_name="str",
            run_id="str",
            api_version="2018-06-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_trigger_runs_query_by_factory(self, resource_group):
        response = await self.client.trigger_runs.query_by_factory(
            resource_group_name=resource_group.name,
            factory_name="str",
            filter_parameters={
                "lastUpdatedAfter": "2020-02-20 00:00:00",
                "lastUpdatedBefore": "2020-02-20 00:00:00",
                "continuationToken": "str",
                "filters": [{"operand": "str", "operator": "str", "values": ["str"]}],
                "orderBy": [{"order": "str", "orderBy": "str"}],
            },
            api_version="2018-06-01",
        )

        # please add some check logic here by yourself
        # ...
