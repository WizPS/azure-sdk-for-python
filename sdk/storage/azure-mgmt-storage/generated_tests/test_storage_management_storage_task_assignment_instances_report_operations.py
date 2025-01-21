# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.storage import StorageManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestStorageManagementStorageTaskAssignmentInstancesReportOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(StorageManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_storage_task_assignment_instances_report_list(self, resource_group):
        response = self.client.storage_task_assignment_instances_report.list(
            resource_group_name=resource_group.name,
            account_name="str",
            storage_task_assignment_name="str",
            api_version="2023-05-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
