# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.managementgroups import ManagementGroupsAPI

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestManagementGroupsAPI(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(ManagementGroupsAPI)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_check_name_availability(self, resource_group):
        response = self.client.check_name_availability(
            check_name_availability_request={"name": "str", "type": "Microsoft.Management/managementGroups"},
            api_version="2021-04-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_start_tenant_backfill(self, resource_group):
        response = self.client.start_tenant_backfill(
            api_version="2021-04-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_tenant_backfill_status(self, resource_group):
        response = self.client.tenant_backfill_status(
            api_version="2021-04-01",
        )

        # please add some check logic here by yourself
        # ...
