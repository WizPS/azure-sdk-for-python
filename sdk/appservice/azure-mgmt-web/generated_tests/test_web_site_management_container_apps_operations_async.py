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
class TestWebSiteManagementContainerAppsOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(WebSiteManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_container_apps_list_by_subscription(self, resource_group):
        response = self.client.container_apps.list_by_subscription(
            api_version="2024-04-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_container_apps_list_by_resource_group(self, resource_group):
        response = self.client.container_apps.list_by_resource_group(
            resource_group_name=resource_group.name,
            api_version="2024-04-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_container_apps_get(self, resource_group):
        response = await self.client.container_apps.get(
            resource_group_name=resource_group.name,
            name="str",
            api_version="2024-04-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_container_apps_begin_create_or_update(self, resource_group):
        response = await (
            await self.client.container_apps.begin_create_or_update(
                resource_group_name=resource_group.name,
                name="str",
                container_app_envelope={
                    "location": "str",
                    "configuration": {
                        "activeRevisionsMode": "str",
                        "ingress": {
                            "allowInsecure": bool,
                            "external": False,
                            "fqdn": "str",
                            "targetPort": 0,
                            "traffic": [{"latestRevision": False, "revisionName": "str", "weight": 0}],
                            "transport": "str",
                        },
                        "registries": [{"passwordSecretRef": "str", "server": "str", "username": "str"}],
                        "secrets": [{"name": "str", "value": "str"}],
                    },
                    "id": "str",
                    "kind": "str",
                    "kubeEnvironmentId": "str",
                    "latestRevisionFqdn": "str",
                    "latestRevisionName": "str",
                    "name": "str",
                    "provisioningState": "str",
                    "tags": {"str": "str"},
                    "template": {
                        "containers": [
                            {
                                "args": ["str"],
                                "command": ["str"],
                                "env": [{"name": "str", "secretRef": "str", "value": "str"}],
                                "image": "str",
                                "name": "str",
                                "resources": {"cpu": 0.0, "memory": "str"},
                            }
                        ],
                        "dapr": {
                            "appId": "str",
                            "appPort": 0,
                            "components": [
                                {
                                    "metadata": [{"name": "str", "secretRef": "str", "value": "str"}],
                                    "name": "str",
                                    "type": "str",
                                    "version": "str",
                                }
                            ],
                            "enabled": bool,
                        },
                        "revisionSuffix": "str",
                        "scale": {
                            "maxReplicas": 0,
                            "minReplicas": 0,
                            "rules": [
                                {
                                    "azureQueue": {
                                        "auth": [{"secretRef": "str", "triggerParameter": "str"}],
                                        "queueLength": 0,
                                        "queueName": "str",
                                    },
                                    "custom": {
                                        "auth": [{"secretRef": "str", "triggerParameter": "str"}],
                                        "metadata": {"str": "str"},
                                        "type": "str",
                                    },
                                    "http": {
                                        "auth": [{"secretRef": "str", "triggerParameter": "str"}],
                                        "metadata": {"str": "str"},
                                    },
                                    "name": "str",
                                }
                            ],
                        },
                    },
                    "type": "str",
                },
                api_version="2024-04-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_container_apps_begin_delete(self, resource_group):
        response = await (
            await self.client.container_apps.begin_delete(
                resource_group_name=resource_group.name,
                name="str",
                api_version="2024-04-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_container_apps_list_secrets(self, resource_group):
        response = await self.client.container_apps.list_secrets(
            name="str",
            api_version="2024-04-01",
        )

        # please add some check logic here by yourself
        # ...
