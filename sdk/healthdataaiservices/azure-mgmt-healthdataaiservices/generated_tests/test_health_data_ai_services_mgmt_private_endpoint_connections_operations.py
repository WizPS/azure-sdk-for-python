# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.healthdataaiservices import HealthDataAIServicesMgmtClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestHealthDataAIServicesMgmtPrivateEndpointConnectionsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(HealthDataAIServicesMgmtClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_private_endpoint_connections_get(self, resource_group):
        response = self.client.private_endpoint_connections.get(
            resource_group_name=resource_group.name,
            deid_service_name="str",
            private_endpoint_connection_name="str",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_private_endpoint_connections_begin_create(self, resource_group):
        response = self.client.private_endpoint_connections.begin_create(
            resource_group_name=resource_group.name,
            deid_service_name="str",
            private_endpoint_connection_name="str",
            resource={
                "id": "str",
                "name": "str",
                "properties": {
                    "privateLinkServiceConnectionState": {
                        "actionsRequired": "str",
                        "description": "str",
                        "status": "str",
                    },
                    "groupIds": ["str"],
                    "privateEndpoint": {"id": "str"},
                    "provisioningState": "str",
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
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_private_endpoint_connections_begin_delete(self, resource_group):
        response = self.client.private_endpoint_connections.begin_delete(
            resource_group_name=resource_group.name,
            deid_service_name="str",
            private_endpoint_connection_name="str",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_private_endpoint_connections_list_by_deid_service(self, resource_group):
        response = self.client.private_endpoint_connections.list_by_deid_service(
            resource_group_name=resource_group.name,
            deid_service_name="str",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
