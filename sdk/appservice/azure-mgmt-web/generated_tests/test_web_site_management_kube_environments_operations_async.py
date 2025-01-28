# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.web.aio import WebSiteManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestWebSiteManagementKubeEnvironmentsOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(WebSiteManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_kube_environments_list_by_subscription(self, resource_group):
        response = self.client.kube_environments.list_by_subscription(
            api_version="2024-04-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_kube_environments_list_by_resource_group(self, resource_group):
        response = self.client.kube_environments.list_by_resource_group(
            resource_group_name=resource_group.name,
            api_version="2024-04-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_kube_environments_get(self, resource_group):
        response = await self.client.kube_environments.get(
            resource_group_name=resource_group.name,
            name="str",
            api_version="2024-04-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_kube_environments_begin_create_or_update(self, resource_group):
        response = await (
            await self.client.kube_environments.begin_create_or_update(
                resource_group_name=resource_group.name,
                name="str",
                kube_environment_envelope={
                    "location": "str",
                    "aksResourceID": "str",
                    "appLogsConfiguration": {
                        "destination": "str",
                        "logAnalyticsConfiguration": {"customerId": "str", "sharedKey": "str"},
                    },
                    "arcConfiguration": {
                        "artifactStorageAccessMode": "str",
                        "artifactStorageClassName": "str",
                        "artifactStorageMountPath": "str",
                        "artifactStorageNodeName": "str",
                        "artifactsStorageType": "str",
                        "frontEndServiceConfiguration": {"kind": "str"},
                        "kubeConfig": "str",
                    },
                    "containerAppsConfiguration": {
                        "appSubnetResourceId": "str",
                        "controlPlaneSubnetResourceId": "str",
                        "daprAIInstrumentationKey": "str",
                        "dockerBridgeCidr": "str",
                        "platformReservedCidr": "str",
                        "platformReservedDnsIP": "str",
                    },
                    "defaultDomain": "str",
                    "deploymentErrors": "str",
                    "environmentType": "str",
                    "extendedLocation": {"name": "str", "type": "str"},
                    "id": "str",
                    "internalLoadBalancerEnabled": bool,
                    "kind": "str",
                    "name": "str",
                    "provisioningState": "str",
                    "staticIp": "str",
                    "tags": {"str": "str"},
                    "type": "str",
                },
                api_version="2024-04-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_kube_environments_begin_delete(self, resource_group):
        response = await (
            await self.client.kube_environments.begin_delete(
                resource_group_name=resource_group.name,
                name="str",
                api_version="2024-04-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_kube_environments_update(self, resource_group):
        response = await self.client.kube_environments.update(
            resource_group_name=resource_group.name,
            name="str",
            kube_environment_envelope={
                "aksResourceID": "str",
                "appLogsConfiguration": {
                    "destination": "str",
                    "logAnalyticsConfiguration": {"customerId": "str", "sharedKey": "str"},
                },
                "arcConfiguration": {
                    "artifactStorageAccessMode": "str",
                    "artifactStorageClassName": "str",
                    "artifactStorageMountPath": "str",
                    "artifactStorageNodeName": "str",
                    "artifactsStorageType": "str",
                    "frontEndServiceConfiguration": {"kind": "str"},
                    "kubeConfig": "str",
                },
                "containerAppsConfiguration": {
                    "appSubnetResourceId": "str",
                    "controlPlaneSubnetResourceId": "str",
                    "daprAIInstrumentationKey": "str",
                    "dockerBridgeCidr": "str",
                    "platformReservedCidr": "str",
                    "platformReservedDnsIP": "str",
                },
                "defaultDomain": "str",
                "deploymentErrors": "str",
                "id": "str",
                "internalLoadBalancerEnabled": bool,
                "kind": "str",
                "name": "str",
                "provisioningState": "str",
                "staticIp": "str",
                "type": "str",
            },
            api_version="2024-04-01",
        )

        # please add some check logic here by yourself
        # ...
