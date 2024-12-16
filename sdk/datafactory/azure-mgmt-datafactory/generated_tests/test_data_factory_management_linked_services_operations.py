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
class TestDataFactoryManagementLinkedServicesOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(DataFactoryManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_linked_services_list_by_factory(self, resource_group):
        response = self.client.linked_services.list_by_factory(
            resource_group_name=resource_group.name,
            factory_name="str",
            api_version="2018-06-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_linked_services_create_or_update(self, resource_group):
        response = self.client.linked_services.create_or_update(
            resource_group_name=resource_group.name,
            factory_name="str",
            linked_service_name="str",
            linked_service={"properties": "linked_service", "etag": "str", "id": "str", "name": "str", "type": "str"},
            api_version="2018-06-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_linked_services_get(self, resource_group):
        response = self.client.linked_services.get(
            resource_group_name=resource_group.name,
            factory_name="str",
            linked_service_name="str",
            api_version="2018-06-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_linked_services_delete(self, resource_group):
        response = self.client.linked_services.delete(
            resource_group_name=resource_group.name,
            factory_name="str",
            linked_service_name="str",
            api_version="2018-06-01",
        )

        # please add some check logic here by yourself
        # ...
