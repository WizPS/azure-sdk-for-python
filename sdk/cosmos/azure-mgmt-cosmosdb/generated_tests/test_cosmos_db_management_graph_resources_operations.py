# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.cosmosdb import CosmosDBManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestCosmosDBManagementGraphResourcesOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(CosmosDBManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_graphs(self, resource_group):
        response = self.client.graph_resources.list_graphs(
            resource_group_name=resource_group.name,
            account_name="str",
            api_version="2024-09-01-preview",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get_graph(self, resource_group):
        response = self.client.graph_resources.get_graph(
            resource_group_name=resource_group.name,
            account_name="str",
            graph_name="str",
            api_version="2024-09-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_create_update_graph(self, resource_group):
        response = self.client.graph_resources.begin_create_update_graph(
            resource_group_name=resource_group.name,
            account_name="str",
            graph_name="str",
            create_update_graph_parameters={
                "resource": {"id": "str"},
                "id": "str",
                "identity": {
                    "principalId": "str",
                    "tenantId": "str",
                    "type": "str",
                    "userAssignedIdentities": {"str": {"clientId": "str", "principalId": "str"}},
                },
                "location": "str",
                "name": "str",
                "options": {"autoscaleSettings": {"maxThroughput": 0}, "throughput": 0},
                "tags": {"str": "str"},
                "type": "str",
            },
            api_version="2024-09-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_delete_graph_resource(self, resource_group):
        response = self.client.graph_resources.begin_delete_graph_resource(
            resource_group_name=resource_group.name,
            account_name="str",
            graph_name="str",
            api_version="2024-09-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
