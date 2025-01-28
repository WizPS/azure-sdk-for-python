# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.datafactory import DataFactoryManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestDataFactoryManagementPipelineRunsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(DataFactoryManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_pipeline_runs_query_by_factory(self, resource_group):
        response = self.client.pipeline_runs.query_by_factory(
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

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_pipeline_runs_get(self, resource_group):
        response = self.client.pipeline_runs.get(
            resource_group_name=resource_group.name,
            factory_name="str",
            run_id="str",
            api_version="2018-06-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_pipeline_runs_cancel(self, resource_group):
        response = self.client.pipeline_runs.cancel(
            resource_group_name=resource_group.name,
            factory_name="str",
            run_id="str",
            api_version="2018-06-01",
        )

        # please add some check logic here by yourself
        # ...
