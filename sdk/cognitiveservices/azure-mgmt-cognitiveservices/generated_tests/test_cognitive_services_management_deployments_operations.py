# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.cognitiveservices import CognitiveServicesManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestCognitiveServicesManagementDeploymentsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(CognitiveServicesManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list(self, resource_group):
        response = self.client.deployments.list(
            resource_group_name=resource_group.name,
            account_name="str",
            api_version="2024-10-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.deployments.get(
            resource_group_name=resource_group.name,
            account_name="str",
            deployment_name="str",
            api_version="2024-10-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_create_or_update(self, resource_group):
        response = self.client.deployments.begin_create_or_update(
            resource_group_name=resource_group.name,
            account_name="str",
            deployment_name="str",
            deployment={
                "etag": "str",
                "id": "str",
                "name": "str",
                "properties": {
                    "callRateLimit": {
                        "count": 0.0,
                        "renewalPeriod": 0.0,
                        "rules": [
                            {
                                "count": 0.0,
                                "dynamicThrottlingEnabled": bool,
                                "key": "str",
                                "matchPatterns": [{"method": "str", "path": "str"}],
                                "minCount": 0.0,
                                "renewalPeriod": 0.0,
                            }
                        ],
                    },
                    "capabilities": {"str": "str"},
                    "capacitySettings": {"designatedCapacity": 0, "priority": 0},
                    "currentCapacity": 0,
                    "dynamicThrottlingEnabled": bool,
                    "model": {
                        "callRateLimit": {
                            "count": 0.0,
                            "renewalPeriod": 0.0,
                            "rules": [
                                {
                                    "count": 0.0,
                                    "dynamicThrottlingEnabled": bool,
                                    "key": "str",
                                    "matchPatterns": [{"method": "str", "path": "str"}],
                                    "minCount": 0.0,
                                    "renewalPeriod": 0.0,
                                }
                            ],
                        },
                        "format": "str",
                        "name": "str",
                        "publisher": "str",
                        "source": "str",
                        "sourceAccount": "str",
                        "version": "str",
                    },
                    "parentDeploymentName": "str",
                    "provisioningState": "str",
                    "raiPolicyName": "str",
                    "rateLimits": [
                        {
                            "count": 0.0,
                            "dynamicThrottlingEnabled": bool,
                            "key": "str",
                            "matchPatterns": [{"method": "str", "path": "str"}],
                            "minCount": 0.0,
                            "renewalPeriod": 0.0,
                        }
                    ],
                    "scaleSettings": {"activeCapacity": 0, "capacity": 0, "scaleType": "str"},
                    "versionUpgradeOption": "str",
                },
                "sku": {"name": "str", "capacity": 0, "family": "str", "size": "str", "tier": "str"},
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
            },
            api_version="2024-10-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_update(self, resource_group):
        response = self.client.deployments.begin_update(
            resource_group_name=resource_group.name,
            account_name="str",
            deployment_name="str",
            deployment={
                "sku": {"name": "str", "capacity": 0, "family": "str", "size": "str", "tier": "str"},
                "tags": {"str": "str"},
            },
            api_version="2024-10-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_delete(self, resource_group):
        response = self.client.deployments.begin_delete(
            resource_group_name=resource_group.name,
            account_name="str",
            deployment_name="str",
            api_version="2024-10-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_skus(self, resource_group):
        response = self.client.deployments.list_skus(
            resource_group_name=resource_group.name,
            account_name="str",
            deployment_name="str",
            api_version="2024-10-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
