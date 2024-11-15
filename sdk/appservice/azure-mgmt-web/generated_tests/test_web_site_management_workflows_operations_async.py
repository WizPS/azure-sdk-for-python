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
class TestWebSiteManagementWorkflowsOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(WebSiteManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_workflows_regenerate_access_key(self, resource_group):
        response = await self.client.workflows.regenerate_access_key(
            resource_group_name=resource_group.name,
            name="str",
            workflow_name="str",
            key_type={"keyType": "str"},
            api_version="2024-04-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_workflows_validate(self, resource_group):
        response = await self.client.workflows.validate(
            resource_group_name=resource_group.name,
            name="str",
            workflow_name="str",
            validate={
                "accessControl": {
                    "actions": {
                        "allowedCallerIpAddresses": [{"addressRange": "str"}],
                        "openAuthenticationPolicies": {
                            "policies": {"str": {"claims": [{"name": "str", "value": "str"}], "type": "str"}}
                        },
                    },
                    "contents": {
                        "allowedCallerIpAddresses": [{"addressRange": "str"}],
                        "openAuthenticationPolicies": {
                            "policies": {"str": {"claims": [{"name": "str", "value": "str"}], "type": "str"}}
                        },
                    },
                    "triggers": {
                        "allowedCallerIpAddresses": [{"addressRange": "str"}],
                        "openAuthenticationPolicies": {
                            "policies": {"str": {"claims": [{"name": "str", "value": "str"}], "type": "str"}}
                        },
                    },
                    "workflowManagement": {
                        "allowedCallerIpAddresses": [{"addressRange": "str"}],
                        "openAuthenticationPolicies": {
                            "policies": {"str": {"claims": [{"name": "str", "value": "str"}], "type": "str"}}
                        },
                    },
                },
                "accessEndpoint": "str",
                "changedTime": "2020-02-20 00:00:00",
                "createdTime": "2020-02-20 00:00:00",
                "definition": {},
                "endpointsConfiguration": {
                    "connector": {
                        "accessEndpointIpAddresses": [{"address": "str"}],
                        "outgoingIpAddresses": [{"address": "str"}],
                    },
                    "workflow": {
                        "accessEndpointIpAddresses": [{"address": "str"}],
                        "outgoingIpAddresses": [{"address": "str"}],
                    },
                },
                "id": "str",
                "identity": {
                    "principalId": "str",
                    "tenantId": "str",
                    "type": "str",
                    "userAssignedIdentities": {"str": {"clientId": "str", "principalId": "str"}},
                },
                "integrationAccount": {"id": "str", "name": "str", "type": "str"},
                "integrationServiceEnvironment": {"id": "str", "name": "str", "type": "str"},
                "kind": "str",
                "location": "str",
                "name": "str",
                "parameters": {"str": {"description": "str", "metadata": {}, "type": "str", "value": {}}},
                "provisioningState": "str",
                "sku": {"name": "str", "plan": {"id": "str", "name": "str", "type": "str"}},
                "state": "str",
                "tags": {"str": "str"},
                "type": "str",
                "version": "str",
            },
            api_version="2024-04-01",
        )

        # please add some check logic here by yourself
        # ...
