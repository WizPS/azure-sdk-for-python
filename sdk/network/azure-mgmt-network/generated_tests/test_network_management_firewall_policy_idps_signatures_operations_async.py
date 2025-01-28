# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.network.aio import NetworkManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNetworkManagementFirewallPolicyIdpsSignaturesOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(NetworkManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_firewall_policy_idps_signatures_list(self, resource_group):
        response = await self.client.firewall_policy_idps_signatures.list(
            resource_group_name=resource_group.name,
            firewall_policy_name="str",
            parameters={
                "filters": [{"field": "str", "values": ["str"]}],
                "orderBy": {"field": "str", "order": "str"},
                "resultsPerPage": 0,
                "search": "str",
                "skip": 0,
            },
            api_version="2024-05-01",
        )

        # please add some check logic here by yourself
        # ...
