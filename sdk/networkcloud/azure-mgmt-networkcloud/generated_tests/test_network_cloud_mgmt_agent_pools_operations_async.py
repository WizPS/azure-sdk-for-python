# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.networkcloud.aio import NetworkCloudMgmtClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNetworkCloudMgmtAgentPoolsOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(NetworkCloudMgmtClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_by_kubernetes_cluster(self, resource_group):
        response = self.client.agent_pools.list_by_kubernetes_cluster(
            resource_group_name=resource_group.name,
            kubernetes_cluster_name="str",
            api_version="2024-06-01-preview",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get(self, resource_group):
        response = await self.client.agent_pools.get(
            resource_group_name=resource_group.name,
            kubernetes_cluster_name="str",
            agent_pool_name="str",
            api_version="2024-06-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_create_or_update(self, resource_group):
        response = await (
            await self.client.agent_pools.begin_create_or_update(
                resource_group_name=resource_group.name,
                kubernetes_cluster_name="str",
                agent_pool_name="str",
                agent_pool_parameters={
                    "count": 0,
                    "location": "str",
                    "mode": "str",
                    "vmSkuName": "str",
                    "administratorConfiguration": {"adminUsername": "str", "sshPublicKeys": [{"keyData": "str"}]},
                    "agentOptions": {"hugepagesCount": 0, "hugepagesSize": "2M"},
                    "attachedNetworkConfiguration": {
                        "l2Networks": [{"networkId": "str", "pluginType": "str"}],
                        "l3Networks": [{"networkId": "str", "ipamEnabled": "False", "pluginType": "str"}],
                        "trunkedNetworks": [{"networkId": "str", "pluginType": "str"}],
                    },
                    "availabilityZones": ["str"],
                    "detailedStatus": "str",
                    "detailedStatusMessage": "str",
                    "extendedLocation": {"name": "str", "type": "str"},
                    "id": "str",
                    "kubernetesVersion": "str",
                    "labels": [{"key": "str", "value": "str"}],
                    "name": "str",
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
                    "taints": [{"key": "str", "value": "str"}],
                    "type": "str",
                    "upgradeSettings": {"drainTimeout": 0, "maxSurge": "str", "maxUnavailable": "str"},
                },
                api_version="2024-06-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_delete(self, resource_group):
        response = await (
            await self.client.agent_pools.begin_delete(
                resource_group_name=resource_group.name,
                kubernetes_cluster_name="str",
                agent_pool_name="str",
                api_version="2024-06-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_update(self, resource_group):
        response = await (
            await self.client.agent_pools.begin_update(
                resource_group_name=resource_group.name,
                kubernetes_cluster_name="str",
                agent_pool_name="str",
                api_version="2024-06-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
