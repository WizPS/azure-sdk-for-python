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
class TestNetworkCloudMgmtVirtualMachinesOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(NetworkCloudMgmtClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_by_subscription(self, resource_group):
        response = self.client.virtual_machines.list_by_subscription(
            api_version="2024-06-01-preview",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_by_resource_group(self, resource_group):
        response = self.client.virtual_machines.list_by_resource_group(
            resource_group_name=resource_group.name,
            api_version="2024-06-01-preview",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.virtual_machines.get(
            resource_group_name=resource_group.name,
            virtual_machine_name="str",
            api_version="2024-06-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_create_or_update(self, resource_group):
        response = self.client.virtual_machines.begin_create_or_update(
            resource_group_name=resource_group.name,
            virtual_machine_name="str",
            virtual_machine_parameters={
                "adminUsername": "str",
                "cloudServicesNetworkAttachment": {
                    "attachedNetworkId": "str",
                    "ipAllocationMethod": "str",
                    "defaultGateway": "str",
                    "ipv4Address": "str",
                    "ipv6Address": "str",
                    "macAddress": "str",
                    "networkAttachmentName": "str",
                },
                "cpuCores": 0,
                "extendedLocation": {"name": "str", "type": "str"},
                "location": "str",
                "memorySizeGB": 0,
                "storageProfile": {
                    "osDisk": {"diskSizeGB": 0, "createOption": "Ephemeral", "deleteOption": "Delete"},
                    "volumeAttachments": ["str"],
                },
                "vmImage": "str",
                "availabilityZone": "str",
                "bareMetalMachineId": "str",
                "bootMethod": "UEFI",
                "clusterId": "str",
                "detailedStatus": "str",
                "detailedStatusMessage": "str",
                "id": "str",
                "isolateEmulatorThread": "True",
                "name": "str",
                "networkAttachments": [
                    {
                        "attachedNetworkId": "str",
                        "ipAllocationMethod": "str",
                        "defaultGateway": "str",
                        "ipv4Address": "str",
                        "ipv6Address": "str",
                        "macAddress": "str",
                        "networkAttachmentName": "str",
                    }
                ],
                "networkData": "str",
                "placementHints": [
                    {"hintType": "str", "resourceId": "str", "schedulingExecution": "str", "scope": "str"}
                ],
                "powerState": "str",
                "provisioningState": "str",
                "sshPublicKeys": [{"keyData": "str"}],
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
                "userData": "str",
                "virtioInterface": "Modern",
                "vmDeviceModel": "T2",
                "vmImageRepositoryCredentials": {"password": "str", "registryUrl": "str", "username": "str"},
                "volumes": ["str"],
            },
            api_version="2024-06-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_delete(self, resource_group):
        response = self.client.virtual_machines.begin_delete(
            resource_group_name=resource_group.name,
            virtual_machine_name="str",
            api_version="2024-06-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_update(self, resource_group):
        response = self.client.virtual_machines.begin_update(
            resource_group_name=resource_group.name,
            virtual_machine_name="str",
            api_version="2024-06-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_power_off(self, resource_group):
        response = self.client.virtual_machines.begin_power_off(
            resource_group_name=resource_group.name,
            virtual_machine_name="str",
            api_version="2024-06-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_reimage(self, resource_group):
        response = self.client.virtual_machines.begin_reimage(
            resource_group_name=resource_group.name,
            virtual_machine_name="str",
            api_version="2024-06-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_restart(self, resource_group):
        response = self.client.virtual_machines.begin_restart(
            resource_group_name=resource_group.name,
            virtual_machine_name="str",
            api_version="2024-06-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_start(self, resource_group):
        response = self.client.virtual_machines.begin_start(
            resource_group_name=resource_group.name,
            virtual_machine_name="str",
            api_version="2024-06-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
