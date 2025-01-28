# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.network import NetworkManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNetworkManagementSecurityRulesOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(NetworkManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_security_rules_begin_delete(self, resource_group):
        response = self.client.security_rules.begin_delete(
            resource_group_name=resource_group.name,
            network_security_group_name="str",
            security_rule_name="str",
            api_version="2024-05-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_security_rules_get(self, resource_group):
        response = self.client.security_rules.get(
            resource_group_name=resource_group.name,
            network_security_group_name="str",
            security_rule_name="str",
            api_version="2024-05-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_security_rules_begin_create_or_update(self, resource_group):
        response = self.client.security_rules.begin_create_or_update(
            resource_group_name=resource_group.name,
            network_security_group_name="str",
            security_rule_name="str",
            security_rule_parameters={
                "access": "str",
                "description": "str",
                "destinationAddressPrefix": "str",
                "destinationAddressPrefixes": ["str"],
                "destinationApplicationSecurityGroups": [
                    {
                        "etag": "str",
                        "id": "str",
                        "location": "str",
                        "name": "str",
                        "provisioningState": "str",
                        "resourceGuid": "str",
                        "tags": {"str": "str"},
                        "type": "str",
                    }
                ],
                "destinationPortRange": "str",
                "destinationPortRanges": ["str"],
                "direction": "str",
                "etag": "str",
                "id": "str",
                "name": "str",
                "priority": 0,
                "protocol": "str",
                "provisioningState": "str",
                "sourceAddressPrefix": "str",
                "sourceAddressPrefixes": ["str"],
                "sourceApplicationSecurityGroups": [
                    {
                        "etag": "str",
                        "id": "str",
                        "location": "str",
                        "name": "str",
                        "provisioningState": "str",
                        "resourceGuid": "str",
                        "tags": {"str": "str"},
                        "type": "str",
                    }
                ],
                "sourcePortRange": "str",
                "sourcePortRanges": ["str"],
                "type": "str",
            },
            api_version="2024-05-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_security_rules_list(self, resource_group):
        response = self.client.security_rules.list(
            resource_group_name=resource_group.name,
            network_security_group_name="str",
            api_version="2024-05-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
