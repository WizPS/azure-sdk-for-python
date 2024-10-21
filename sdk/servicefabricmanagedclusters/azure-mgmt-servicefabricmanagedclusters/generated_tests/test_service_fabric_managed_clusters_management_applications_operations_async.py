# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.servicefabricmanagedclusters.aio import ServiceFabricManagedClustersManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestServiceFabricManagedClustersManagementApplicationsOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(ServiceFabricManagedClustersManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_read_upgrade(self, resource_group):
        response = await (
            await self.client.applications.begin_read_upgrade(
                resource_group_name=resource_group.name,
                cluster_name="str",
                application_name="str",
                api_version="2024-06-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_start_rollback(self, resource_group):
        response = await (
            await self.client.applications.begin_start_rollback(
                resource_group_name=resource_group.name,
                cluster_name="str",
                application_name="str",
                api_version="2024-06-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_resume_upgrade(self, resource_group):
        response = await (
            await self.client.applications.begin_resume_upgrade(
                resource_group_name=resource_group.name,
                cluster_name="str",
                application_name="str",
                parameters={"upgradeDomainName": "str"},
                api_version="2024-06-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get(self, resource_group):
        response = await self.client.applications.get(
            resource_group_name=resource_group.name,
            cluster_name="str",
            application_name="str",
            api_version="2024-06-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_create_or_update(self, resource_group):
        response = await (
            await self.client.applications.begin_create_or_update(
                resource_group_name=resource_group.name,
                cluster_name="str",
                application_name="str",
                parameters={
                    "id": "str",
                    "identity": {
                        "principalId": "str",
                        "tenantId": "str",
                        "type": "str",
                        "userAssignedIdentities": {"str": {"clientId": "str", "principalId": "str"}},
                    },
                    "location": "str",
                    "managedIdentities": [{"name": "str", "principalId": "str"}],
                    "name": "str",
                    "parameters": {"str": "str"},
                    "provisioningState": "str",
                    "systemData": {
                        "createdAt": "2020-02-20 00:00:00",
                        "createdBy": "str",
                        "createdByType": "str",
                        "lastModifiedAt": "2020-02-20 00:00:00",
                        "lastModifiedBy": "str",
                        "lastModifiedByType": "str",
                    },
                    "tags": {"str": "str"},
                    "type": "str",
                    "upgradePolicy": {
                        "applicationHealthPolicy": {
                            "considerWarningAsError": bool,
                            "maxPercentUnhealthyDeployedApplications": 0,
                            "defaultServiceTypeHealthPolicy": {
                                "maxPercentUnhealthyPartitionsPerService": 0,
                                "maxPercentUnhealthyReplicasPerPartition": 0,
                                "maxPercentUnhealthyServices": 0,
                            },
                            "serviceTypeHealthPolicyMap": {
                                "str": {
                                    "maxPercentUnhealthyPartitionsPerService": 0,
                                    "maxPercentUnhealthyReplicasPerPartition": 0,
                                    "maxPercentUnhealthyServices": 0,
                                }
                            },
                        },
                        "forceRestart": False,
                        "instanceCloseDelayDuration": 0,
                        "recreateApplication": bool,
                        "rollingUpgradeMonitoringPolicy": {
                            "failureAction": "str",
                            "healthCheckRetryTimeout": "str",
                            "healthCheckStableDuration": "str",
                            "healthCheckWaitDuration": "str",
                            "upgradeDomainTimeout": "str",
                            "upgradeTimeout": "str",
                        },
                        "upgradeMode": "str",
                        "upgradeReplicaSetCheckTimeout": 0,
                    },
                    "version": "str",
                },
                api_version="2024-06-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_update(self, resource_group):
        response = await self.client.applications.update(
            resource_group_name=resource_group.name,
            cluster_name="str",
            application_name="str",
            parameters={"tags": {"str": "str"}},
            api_version="2024-06-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_delete(self, resource_group):
        response = await (
            await self.client.applications.begin_delete(
                resource_group_name=resource_group.name,
                cluster_name="str",
                application_name="str",
                api_version="2024-06-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list(self, resource_group):
        response = self.client.applications.list(
            resource_group_name=resource_group.name,
            cluster_name="str",
            api_version="2024-06-01-preview",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...
