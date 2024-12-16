# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.compute import ComputeManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-compute
# USAGE
    python virtual_machine_scale_set_vm_update_maximum_set_gen.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ComputeManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="{subscription-id}",
    )

    response = client.virtual_machine_scale_set_vms.begin_update(
        resource_group_name="rgcompute",
        vm_scale_set_name="aaaaaaaaaaaaaa",
        instance_id="aaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        parameters={
            "location": "westus",
            "plan": {
                "name": "aaaaaaaaaa",
                "product": "aaaaaaaaaaaaaaaaaaaa",
                "promotionCode": "aaaaaaaaaaaaaaaaaaaa",
                "publisher": "aaaaaaaaaaaaaaaaaaaaaa",
            },
            "properties": {
                "additionalCapabilities": {"hibernationEnabled": True, "ultraSSDEnabled": True},
                "availabilitySet": {
                    "id": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}"
                },
                "diagnosticsProfile": {"bootDiagnostics": {"enabled": True, "storageUri": "aaaaaaaaaaaaa"}},
                "hardwareProfile": {
                    "vmSize": "Basic_A0",
                    "vmSizeProperties": {"vCPUsAvailable": 9, "vCPUsPerCore": 12},
                },
                "instanceView": {
                    "bootDiagnostics": {
                        "status": {
                            "code": "aaaaaaaaaaaaaaaaaaaaaaa",
                            "displayStatus": "aaaaaa",
                            "level": "Info",
                            "message": "a",
                            "time": "2021-11-30T12:58:26.522Z",
                        }
                    },
                    "disks": [
                        {
                            "encryptionSettings": [
                                {
                                    "diskEncryptionKey": {
                                        "secretUrl": "aaaaaaaa",
                                        "sourceVault": {
                                            "id": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}"
                                        },
                                    },
                                    "enabled": True,
                                    "keyEncryptionKey": {
                                        "keyUrl": "aaaaaaaaaaaaaa",
                                        "sourceVault": {
                                            "id": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}"
                                        },
                                    },
                                }
                            ],
                            "name": "aaaaaaaaaaa",
                            "statuses": [
                                {
                                    "code": "aaaaaaaaaaaaaaaaaaaaaaa",
                                    "displayStatus": "aaaaaa",
                                    "level": "Info",
                                    "message": "a",
                                    "time": "2021-11-30T12:58:26.522Z",
                                }
                            ],
                        }
                    ],
                    "extensions": [
                        {
                            "name": "aaaaaaaaaaaaaaaaa",
                            "statuses": [
                                {
                                    "code": "aaaaaaaaaaaaaaaaaaaaaaa",
                                    "displayStatus": "aaaaaa",
                                    "level": "Info",
                                    "message": "a",
                                    "time": "2021-11-30T12:58:26.522Z",
                                }
                            ],
                            "substatuses": [
                                {
                                    "code": "aaaaaaaaaaaaaaaaaaaaaaa",
                                    "displayStatus": "aaaaaa",
                                    "level": "Info",
                                    "message": "a",
                                    "time": "2021-11-30T12:58:26.522Z",
                                }
                            ],
                            "type": "aaaaaaaaa",
                            "typeHandlerVersion": "aaaaaaaaaaaaaaaaaaaaaaaaaa",
                        }
                    ],
                    "maintenanceRedeployStatus": {
                        "isCustomerInitiatedMaintenanceAllowed": True,
                        "lastOperationMessage": "aaaaaa",
                        "lastOperationResultCode": "None",
                        "maintenanceWindowEndTime": "2021-11-30T12:58:26.531Z",
                        "maintenanceWindowStartTime": "2021-11-30T12:58:26.531Z",
                        "preMaintenanceWindowEndTime": "2021-11-30T12:58:26.531Z",
                        "preMaintenanceWindowStartTime": "2021-11-30T12:58:26.531Z",
                    },
                    "placementGroupId": "aaa",
                    "platformFaultDomain": 14,
                    "platformUpdateDomain": 23,
                    "rdpThumbPrint": "aaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "statuses": [
                        {
                            "code": "aaaaaaaaaaaaaaaaaaaaaaa",
                            "displayStatus": "aaaaaa",
                            "level": "Info",
                            "message": "a",
                            "time": "2021-11-30T12:58:26.522Z",
                        }
                    ],
                    "vmAgent": {
                        "extensionHandlers": [
                            {
                                "status": {
                                    "code": "aaaaaaaaaaaaaaaaaaaaaaa",
                                    "displayStatus": "aaaaaa",
                                    "level": "Info",
                                    "message": "a",
                                    "time": "2021-11-30T12:58:26.522Z",
                                },
                                "type": "aaaaaaaaaaaaa",
                                "typeHandlerVersion": "aaaaa",
                            }
                        ],
                        "statuses": [
                            {
                                "code": "aaaaaaaaaaaaaaaaaaaaaaa",
                                "displayStatus": "aaaaaa",
                                "level": "Info",
                                "message": "a",
                                "time": "2021-11-30T12:58:26.522Z",
                            }
                        ],
                        "vmAgentVersion": "aaaaaaaaaaaaaaaaaaaaaaa",
                    },
                    "vmHealth": {
                        "status": {
                            "code": "aaaaaaaaaaaaaaaaaaaaaaa",
                            "displayStatus": "aaaaaa",
                            "level": "Info",
                            "message": "a",
                            "time": "2021-11-30T12:58:26.522Z",
                        }
                    },
                },
                "licenseType": "aaaaaaaaaa",
                "networkProfile": {
                    "networkApiVersion": "2020-11-01",
                    "networkInterfaceConfigurations": [
                        {
                            "name": "aaaaaaaaaaa",
                            "properties": {
                                "deleteOption": "Delete",
                                "dnsSettings": {"dnsServers": ["aaaaaa"]},
                                "dscpConfiguration": {
                                    "id": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}"
                                },
                                "enableAcceleratedNetworking": True,
                                "enableFpga": True,
                                "enableIPForwarding": True,
                                "ipConfigurations": [
                                    {
                                        "name": "aa",
                                        "properties": {
                                            "applicationGatewayBackendAddressPools": [
                                                {
                                                    "id": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}"
                                                }
                                            ],
                                            "applicationSecurityGroups": [
                                                {
                                                    "id": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}"
                                                }
                                            ],
                                            "loadBalancerBackendAddressPools": [
                                                {
                                                    "id": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}"
                                                }
                                            ],
                                            "primary": True,
                                            "privateIPAddressVersion": "IPv4",
                                            "publicIPAddressConfiguration": {
                                                "name": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                                                "properties": {
                                                    "deleteOption": "Delete",
                                                    "dnsSettings": {"domainNameLabel": "aaaaaaaaaaaaaaaaaaaaaaaaa"},
                                                    "idleTimeoutInMinutes": 2,
                                                    "ipTags": [
                                                        {
                                                            "ipTagType": "aaaaaaaaaaaaaaaaaaaaaaaaa",
                                                            "tag": "aaaaaaaaaaaaaaaaaaaa",
                                                        }
                                                    ],
                                                    "publicIPAddressVersion": "IPv4",
                                                    "publicIPAllocationMethod": "Dynamic",
                                                    "publicIPPrefix": {
                                                        "id": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}"
                                                    },
                                                },
                                                "sku": {"name": "Basic", "tier": "Regional"},
                                            },
                                            "subnet": {
                                                "id": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}"
                                            },
                                        },
                                    }
                                ],
                                "networkSecurityGroup": {
                                    "id": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}"
                                },
                                "primary": True,
                            },
                        }
                    ],
                    "networkInterfaces": [
                        {
                            "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/virtualMachineScaleSets/{vmss-name}/virtualMachines/0/networkInterfaces/vmsstestnetconfig5415",
                            "properties": {"deleteOption": "Delete", "primary": True},
                        }
                    ],
                },
                "networkProfileConfiguration": {
                    "networkInterfaceConfigurations": [
                        {
                            "name": "vmsstestnetconfig5415",
                            "properties": {
                                "deleteOption": "Delete",
                                "dnsSettings": {"dnsServers": []},
                                "enableAcceleratedNetworking": True,
                                "enableFpga": True,
                                "enableIPForwarding": True,
                                "ipConfigurations": [
                                    {
                                        "name": "vmsstestnetconfig9693",
                                        "properties": {
                                            "applicationGatewayBackendAddressPools": [
                                                {
                                                    "id": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}"
                                                }
                                            ],
                                            "applicationSecurityGroups": [
                                                {
                                                    "id": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}"
                                                }
                                            ],
                                            "loadBalancerBackendAddressPools": [
                                                {
                                                    "id": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}"
                                                }
                                            ],
                                            "loadBalancerInboundNatPools": [
                                                {
                                                    "id": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}"
                                                }
                                            ],
                                            "primary": True,
                                            "privateIPAddressVersion": "IPv4",
                                            "publicIPAddressConfiguration": {
                                                "name": "aaaaaaaaaaaaaaaaaa",
                                                "properties": {
                                                    "deleteOption": "Delete",
                                                    "dnsSettings": {"domainNameLabel": "aaaaaaaaaaaaaaaaaa"},
                                                    "idleTimeoutInMinutes": 18,
                                                    "ipTags": [
                                                        {"ipTagType": "aaaaaaa", "tag": "aaaaaaaaaaaaaaaaaaaaaaaaaaa"}
                                                    ],
                                                    "publicIPAddressVersion": "IPv4",
                                                    "publicIPPrefix": {
                                                        "id": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}"
                                                    },
                                                },
                                                "sku": {"name": "Basic", "tier": "Regional"},
                                            },
                                            "subnet": {
                                                "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualNetworks/vn4071/subnets/sn5503"
                                            },
                                        },
                                    }
                                ],
                                "networkSecurityGroup": {
                                    "id": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}"
                                },
                                "primary": True,
                            },
                        }
                    ]
                },
                "osProfile": {
                    "adminPassword": "aaaaaaaaaaaaaaaa",
                    "adminUsername": "Foo12",
                    "allowExtensionOperations": True,
                    "computerName": "test000000",
                    "customData": "aaaa",
                    "linuxConfiguration": {
                        "disablePasswordAuthentication": True,
                        "patchSettings": {"assessmentMode": "ImageDefault", "patchMode": "ImageDefault"},
                        "provisionVMAgent": True,
                        "ssh": {"publicKeys": [{"keyData": "aaaaaa", "path": "aaa"}]},
                    },
                    "requireGuestProvisionSignal": True,
                    "secrets": [],
                    "windowsConfiguration": {
                        "additionalUnattendContent": [
                            {
                                "componentName": "Microsoft-Windows-Shell-Setup",
                                "content": "aaaaaaaaaaaaaaaaaaaa",
                                "passName": "OobeSystem",
                                "settingName": "AutoLogon",
                            }
                        ],
                        "enableAutomaticUpdates": True,
                        "patchSettings": {
                            "assessmentMode": "ImageDefault",
                            "enableHotpatching": True,
                            "patchMode": "Manual",
                        },
                        "provisionVMAgent": True,
                        "timeZone": "aaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "winRM": {"listeners": [{"certificateUrl": "aaaaaaaaaaaaaaaaaaaaaa", "protocol": "Http"}]},
                    },
                },
                "protectionPolicy": {"protectFromScaleIn": True, "protectFromScaleSetActions": True},
                "securityProfile": {
                    "encryptionAtHost": True,
                    "securityType": "TrustedLaunch",
                    "uefiSettings": {"secureBootEnabled": True, "vTpmEnabled": True},
                },
                "storageProfile": {
                    "dataDisks": [
                        {
                            "caching": "None",
                            "createOption": "Empty",
                            "deleteOption": "Delete",
                            "detachOption": "ForceDetach",
                            "diskSizeGB": 128,
                            "image": {
                                "uri": "https://{storageAccountName}.blob.core.windows.net/{containerName}/{vhdName}.vhd"
                            },
                            "lun": 1,
                            "managedDisk": {
                                "diskEncryptionSet": {"id": "aaaaaaaaaaaa"},
                                "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/vmss3176_vmss3176_0_disk2_6c4f554bdafa49baa780eb2d128ff39d",
                                "storageAccountType": "Standard_LRS",
                            },
                            "name": "vmss3176_vmss3176_0_disk2_6c4f554bdafa49baa780eb2d128ff39d",
                            "toBeDetached": True,
                            "vhd": {
                                "uri": "https://{storageAccountName}.blob.core.windows.net/{containerName}/{vhdName}.vhd"
                            },
                            "writeAcceleratorEnabled": True,
                        }
                    ],
                    "imageReference": {
                        "id": "a",
                        "offer": "WindowsServer",
                        "publisher": "MicrosoftWindowsServer",
                        "sharedGalleryImageId": "aaaaaaaaaaaaaaaaaaaa",
                        "sku": "2012-R2-Datacenter",
                        "version": "4.127.20180315",
                    },
                    "osDisk": {
                        "caching": "None",
                        "createOption": "FromImage",
                        "deleteOption": "Delete",
                        "diffDiskSettings": {"option": "Local", "placement": "CacheDisk"},
                        "diskSizeGB": 127,
                        "encryptionSettings": {
                            "diskEncryptionKey": {
                                "secretUrl": "aaaaaaaa",
                                "sourceVault": {
                                    "id": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}"
                                },
                            },
                            "enabled": True,
                            "keyEncryptionKey": {
                                "keyUrl": "aaaaaaaaaaaaaa",
                                "sourceVault": {
                                    "id": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}"
                                },
                            },
                        },
                        "image": {
                            "uri": "https://{storageAccountName}.blob.core.windows.net/{containerName}/{vhdName}.vhd"
                        },
                        "managedDisk": {
                            "diskEncryptionSet": {"id": "aaaaaaaaaaaa"},
                            "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/vmss3176_vmss3176_0_OsDisk_1_6d72b805e50e4de6830303c5055077fc",
                            "storageAccountType": "Standard_LRS",
                        },
                        "name": "vmss3176_vmss3176_0_OsDisk_1_6d72b805e50e4de6830303c5055077fc",
                        "osType": "Windows",
                        "vhd": {
                            "uri": "https://{storageAccountName}.blob.core.windows.net/{containerName}/{vhdName}.vhd"
                        },
                        "writeAcceleratorEnabled": True,
                    },
                },
                "userData": "RXhhbXBsZSBVc2VyRGF0YQ==",
            },
            "sku": {"capacity": 29, "name": "Classic", "tier": "aaaaaaaaaaaaaa"},
            "tags": {},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/compute/resource-manager/Microsoft.Compute/ComputeRP/stable/2024-07-01/examples/virtualMachineScaleSetExamples/VirtualMachineScaleSetVM_Update_MaximumSet_Gen.json
if __name__ == "__main__":
    main()
