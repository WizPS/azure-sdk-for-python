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
class TestNetworkCloudMgmtKubernetesClusterFeaturesOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(NetworkCloudMgmtClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_by_kubernetes_cluster(self, resource_group):
        response = self.client.kubernetes_cluster_features.list_by_kubernetes_cluster(
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
        response = await self.client.kubernetes_cluster_features.get(
            resource_group_name=resource_group.name,
            kubernetes_cluster_name="str",
            feature_name="str",
            api_version="2024-06-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_create_or_update(self, resource_group):
        response = await (
            await self.client.kubernetes_cluster_features.begin_create_or_update(
                resource_group_name=resource_group.name,
                kubernetes_cluster_name="str",
                feature_name="str",
                kubernetes_cluster_feature_parameters={
                    "location": "str",
                    "availabilityLifecycle": "str",
                    "detailedStatus": "str",
                    "detailedStatusMessage": "str",
                    "id": "str",
                    "name": "str",
                    "options": [{"key": "str", "value": "str"}],
                    "provisioningState": "str",
                    "required": "str",
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
                    "version": "str",
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
            await self.client.kubernetes_cluster_features.begin_delete(
                resource_group_name=resource_group.name,
                kubernetes_cluster_name="str",
                feature_name="str",
                api_version="2024-06-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_update(self, resource_group):
        response = await (
            await self.client.kubernetes_cluster_features.begin_update(
                resource_group_name=resource_group.name,
                kubernetes_cluster_name="str",
                feature_name="str",
                api_version="2024-06-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
