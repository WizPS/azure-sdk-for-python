# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.deviceregistry import DeviceRegistryMgmtClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestDeviceRegistryMgmtSchemasOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(DeviceRegistryMgmtClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_schemas_get(self, resource_group):
        response = self.client.schemas.get(
            resource_group_name=resource_group.name,
            schema_registry_name="str",
            schema_name="str",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_schemas_create_or_replace(self, resource_group):
        response = self.client.schemas.create_or_replace(
            resource_group_name=resource_group.name,
            schema_registry_name="str",
            schema_name="str",
            resource={
                "id": "str",
                "name": "str",
                "properties": {
                    "format": "str",
                    "schemaType": "str",
                    "description": "str",
                    "displayName": "str",
                    "provisioningState": "str",
                    "tags": {"str": "str"},
                    "uuid": "str",
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
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_schemas_delete(self, resource_group):
        response = self.client.schemas.delete(
            resource_group_name=resource_group.name,
            schema_registry_name="str",
            schema_name="str",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_schemas_list_by_schema_registry(self, resource_group):
        response = self.client.schemas.list_by_schema_registry(
            resource_group_name=resource_group.name,
            schema_registry_name="str",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
