# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.networkcloud import NetworkCloudMgmtClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNetworkCloudMgmtBareMetalMachinesOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(NetworkCloudMgmtClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_by_subscription(self, resource_group):
        response = self.client.bare_metal_machines.list_by_subscription(
            api_version="2024-06-01-preview",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_by_resource_group(self, resource_group):
        response = self.client.bare_metal_machines.list_by_resource_group(
            resource_group_name=resource_group.name,
            api_version="2024-06-01-preview",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.bare_metal_machines.get(
            resource_group_name=resource_group.name,
            bare_metal_machine_name="str",
            api_version="2024-06-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_create_or_update(self, resource_group):
        response = self.client.bare_metal_machines.begin_create_or_update(
            resource_group_name=resource_group.name,
            bare_metal_machine_name="str",
            bare_metal_machine_parameters={
                "bmcConnectionString": "str",
                "bmcCredentials": {"password": "str", "username": "str"},
                "bmcMacAddress": "str",
                "bootMacAddress": "str",
                "extendedLocation": {"name": "str", "type": "str"},
                "location": "str",
                "machineDetails": "str",
                "machineName": "str",
                "machineSkuId": "str",
                "rackId": "str",
                "rackSlot": 0,
                "serialNumber": "str",
                "associatedResourceIds": ["str"],
                "clusterId": "str",
                "cordonStatus": "str",
                "detailedStatus": "str",
                "detailedStatusMessage": "str",
                "hardwareInventory": {
                    "additionalHostInformation": "str",
                    "interfaces": [
                        {"linkStatus": "str", "macAddress": "str", "name": "str", "networkInterfaceId": "str"}
                    ],
                    "nics": [
                        {
                            "lldpNeighbor": {
                                "portDescription": "str",
                                "portName": "str",
                                "systemDescription": "str",
                                "systemName": "str",
                            },
                            "macAddress": "str",
                            "name": "str",
                        }
                    ],
                },
                "hardwareValidationStatus": {"lastValidationTime": "2020-02-20 00:00:00", "result": "str"},
                "hybridAksClustersAssociatedIds": ["str"],
                "id": "str",
                "kubernetesNodeName": "str",
                "kubernetesVersion": "str",
                "machineClusterVersion": "str",
                "machineRoles": ["str"],
                "name": "str",
                "oamIpv4Address": "str",
                "oamIpv6Address": "str",
                "osImage": "str",
                "powerState": "str",
                "provisioningState": "str",
                "readyState": "str",
                "runtimeProtectionStatus": {
                    "definitionsLastUpdated": "2020-02-20 00:00:00",
                    "definitionsVersion": "str",
                    "scanCompletedTime": "2020-02-20 00:00:00",
                    "scanScheduledTime": "2020-02-20 00:00:00",
                    "scanStartedTime": "2020-02-20 00:00:00",
                },
                "secretRotationStatus": [
                    {
                        "expirePeriodDays": 0,
                        "lastRotationTime": "2020-02-20 00:00:00",
                        "rotationPeriodDays": 0,
                        "secretArchiveReference": {"keyVaultId": "str", "secretName": "str", "secretVersion": "str"},
                        "secretType": "str",
                    }
                ],
                "serviceTag": "str",
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
                "virtualMachinesAssociatedIds": ["str"],
            },
            api_version="2024-06-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_delete(self, resource_group):
        response = self.client.bare_metal_machines.begin_delete(
            resource_group_name=resource_group.name,
            bare_metal_machine_name="str",
            api_version="2024-06-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_update(self, resource_group):
        response = self.client.bare_metal_machines.begin_update(
            resource_group_name=resource_group.name,
            bare_metal_machine_name="str",
            api_version="2024-06-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_cordon(self, resource_group):
        response = self.client.bare_metal_machines.begin_cordon(
            resource_group_name=resource_group.name,
            bare_metal_machine_name="str",
            api_version="2024-06-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_power_off(self, resource_group):
        response = self.client.bare_metal_machines.begin_power_off(
            resource_group_name=resource_group.name,
            bare_metal_machine_name="str",
            api_version="2024-06-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_reimage(self, resource_group):
        response = self.client.bare_metal_machines.begin_reimage(
            resource_group_name=resource_group.name,
            bare_metal_machine_name="str",
            api_version="2024-06-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_replace(self, resource_group):
        response = self.client.bare_metal_machines.begin_replace(
            resource_group_name=resource_group.name,
            bare_metal_machine_name="str",
            api_version="2024-06-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_restart(self, resource_group):
        response = self.client.bare_metal_machines.begin_restart(
            resource_group_name=resource_group.name,
            bare_metal_machine_name="str",
            api_version="2024-06-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_run_command(self, resource_group):
        response = self.client.bare_metal_machines.begin_run_command(
            resource_group_name=resource_group.name,
            bare_metal_machine_name="str",
            bare_metal_machine_run_command_parameters={"limitTimeSeconds": 0, "script": "str", "arguments": ["str"]},
            api_version="2024-06-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_run_data_extracts(self, resource_group):
        response = self.client.bare_metal_machines.begin_run_data_extracts(
            resource_group_name=resource_group.name,
            bare_metal_machine_name="str",
            bare_metal_machine_run_data_extracts_parameters={
                "commands": [{"command": "str", "arguments": ["str"]}],
                "limitTimeSeconds": 0,
            },
            api_version="2024-06-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_run_read_commands(self, resource_group):
        response = self.client.bare_metal_machines.begin_run_read_commands(
            resource_group_name=resource_group.name,
            bare_metal_machine_name="str",
            bare_metal_machine_run_read_commands_parameters={
                "commands": [{"command": "str", "arguments": ["str"]}],
                "limitTimeSeconds": 0,
            },
            api_version="2024-06-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_start(self, resource_group):
        response = self.client.bare_metal_machines.begin_start(
            resource_group_name=resource_group.name,
            bare_metal_machine_name="str",
            api_version="2024-06-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_uncordon(self, resource_group):
        response = self.client.bare_metal_machines.begin_uncordon(
            resource_group_name=resource_group.name,
            bare_metal_machine_name="str",
            api_version="2024-06-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
