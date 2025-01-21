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
class TestStorageManagementTableOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(StorageManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_table_create(self, resource_group):
        response = self.client.table.create(
            resource_group_name=resource_group.name,
            account_name="str",
            table_name="str",
            api_version="2023-05-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_table_update(self, resource_group):
        response = self.client.table.update(
            resource_group_name=resource_group.name,
            account_name="str",
            table_name="str",
            api_version="2023-05-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_table_get(self, resource_group):
        response = self.client.table.get(
            resource_group_name=resource_group.name,
            account_name="str",
            table_name="str",
            api_version="2023-05-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_table_delete(self, resource_group):
        response = self.client.table.delete(
            resource_group_name=resource_group.name,
            account_name="str",
            table_name="str",
            api_version="2023-05-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_table_list(self, resource_group):
        response = self.client.table.list(
            resource_group_name=resource_group.name,
            account_name="str",
            api_version="2023-05-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
