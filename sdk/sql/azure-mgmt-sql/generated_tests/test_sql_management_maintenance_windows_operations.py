# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.sql import SqlManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestSqlManagementMaintenanceWindowsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(SqlManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.maintenance_windows.get(
            resource_group_name=resource_group.name,
            server_name="str",
            database_name="str",
            maintenance_window_name="str",
            api_version="2020-11-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_create_or_update(self, resource_group):
        response = self.client.maintenance_windows.create_or_update(
            resource_group_name=resource_group.name,
            server_name="str",
            database_name="str",
            maintenance_window_name="str",
            parameters={
                "id": "str",
                "name": "str",
                "timeRanges": [{"dayOfWeek": "str", "duration": "str", "startTime": "str"}],
                "type": "str",
            },
            api_version="2020-11-01-preview",
        )

        # please add some check logic here by yourself
        # ...
