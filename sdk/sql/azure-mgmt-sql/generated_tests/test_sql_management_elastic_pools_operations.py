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
class TestSqlManagementElasticPoolsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(SqlManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_metrics(self, resource_group):
        response = self.client.elastic_pools.list_metrics(
            resource_group_name=resource_group.name,
            server_name="str",
            elastic_pool_name="str",
            filter="str",
            api_version="2014-04-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_metric_definitions(self, resource_group):
        response = self.client.elastic_pools.list_metric_definitions(
            resource_group_name=resource_group.name,
            server_name="str",
            elastic_pool_name="str",
            api_version="2014-04-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_by_server(self, resource_group):
        response = self.client.elastic_pools.list_by_server(
            resource_group_name=resource_group.name,
            server_name="str",
            api_version="2022-08-01-preview",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.elastic_pools.get(
            resource_group_name=resource_group.name,
            server_name="str",
            elastic_pool_name="str",
            api_version="2022-08-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_create_or_update(self, resource_group):
        response = self.client.elastic_pools.begin_create_or_update(
            resource_group_name=resource_group.name,
            server_name="str",
            elastic_pool_name="str",
            parameters={
                "location": "str",
                "availabilityZone": "str",
                "creationDate": "2020-02-20 00:00:00",
                "highAvailabilityReplicaCount": 0,
                "id": "str",
                "kind": "str",
                "licenseType": "str",
                "maintenanceConfigurationId": "str",
                "maxSizeBytes": 0,
                "minCapacity": 0.0,
                "name": "str",
                "perDatabaseSettings": {"maxCapacity": 0.0, "minCapacity": 0.0},
                "preferredEnclaveType": "str",
                "sku": {"name": "str", "capacity": 0, "family": "str", "size": "str", "tier": "str"},
                "state": "str",
                "tags": {"str": "str"},
                "type": "str",
                "zoneRedundant": bool,
            },
            api_version="2022-08-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_delete(self, resource_group):
        response = self.client.elastic_pools.begin_delete(
            resource_group_name=resource_group.name,
            server_name="str",
            elastic_pool_name="str",
            api_version="2022-08-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_update(self, resource_group):
        response = self.client.elastic_pools.begin_update(
            resource_group_name=resource_group.name,
            server_name="str",
            elastic_pool_name="str",
            parameters={
                "availabilityZone": "str",
                "highAvailabilityReplicaCount": 0,
                "licenseType": "str",
                "maintenanceConfigurationId": "str",
                "maxSizeBytes": 0,
                "minCapacity": 0.0,
                "perDatabaseSettings": {"maxCapacity": 0.0, "minCapacity": 0.0},
                "preferredEnclaveType": "str",
                "sku": {"name": "str", "capacity": 0, "family": "str", "size": "str", "tier": "str"},
                "tags": {"str": "str"},
                "zoneRedundant": bool,
            },
            api_version="2022-08-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_failover(self, resource_group):
        response = self.client.elastic_pools.begin_failover(
            resource_group_name=resource_group.name,
            server_name="str",
            elastic_pool_name="str",
            api_version="2022-08-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
