# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.compute import ComputeManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestComputeManagementAvailabilitySetsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(ComputeManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_availability_sets_create_or_update(self, resource_group):
        response = self.client.availability_sets.create_or_update(
            resource_group_name=resource_group.name,
            availability_set_name="str",
            parameters={
                "location": "str",
                "id": "str",
                "name": "str",
                "platformFaultDomainCount": 0,
                "platformUpdateDomainCount": 0,
                "proximityPlacementGroup": {"id": "str"},
                "scheduledEventsPolicy": {
                    "scheduledEventsAdditionalPublishingTargets": {"eventGridAndResourceGraph": {"enable": bool}},
                    "userInitiatedReboot": {"automaticallyApprove": bool},
                    "userInitiatedRedeploy": {"automaticallyApprove": bool},
                },
                "sku": {"capacity": 0, "name": "str", "tier": "str"},
                "statuses": [
                    {
                        "code": "str",
                        "displayStatus": "str",
                        "level": "str",
                        "message": "str",
                        "time": "2020-02-20 00:00:00",
                    }
                ],
                "tags": {"str": "str"},
                "type": "str",
                "virtualMachines": [{"id": "str"}],
            },
            api_version="2024-07-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_availability_sets_update(self, resource_group):
        response = self.client.availability_sets.update(
            resource_group_name=resource_group.name,
            availability_set_name="str",
            parameters={
                "platformFaultDomainCount": 0,
                "platformUpdateDomainCount": 0,
                "proximityPlacementGroup": {"id": "str"},
                "scheduledEventsPolicy": {
                    "scheduledEventsAdditionalPublishingTargets": {"eventGridAndResourceGraph": {"enable": bool}},
                    "userInitiatedReboot": {"automaticallyApprove": bool},
                    "userInitiatedRedeploy": {"automaticallyApprove": bool},
                },
                "sku": {"capacity": 0, "name": "str", "tier": "str"},
                "statuses": [
                    {
                        "code": "str",
                        "displayStatus": "str",
                        "level": "str",
                        "message": "str",
                        "time": "2020-02-20 00:00:00",
                    }
                ],
                "tags": {"str": "str"},
                "virtualMachines": [{"id": "str"}],
            },
            api_version="2024-07-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_availability_sets_delete(self, resource_group):
        response = self.client.availability_sets.delete(
            resource_group_name=resource_group.name,
            availability_set_name="str",
            api_version="2024-07-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_availability_sets_get(self, resource_group):
        response = self.client.availability_sets.get(
            resource_group_name=resource_group.name,
            availability_set_name="str",
            api_version="2024-07-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_availability_sets_list_by_subscription(self, resource_group):
        response = self.client.availability_sets.list_by_subscription(
            api_version="2024-07-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_availability_sets_list(self, resource_group):
        response = self.client.availability_sets.list(
            resource_group_name=resource_group.name,
            api_version="2024-07-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_availability_sets_list_available_sizes(self, resource_group):
        response = self.client.availability_sets.list_available_sizes(
            resource_group_name=resource_group.name,
            availability_set_name="str",
            api_version="2024-07-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
