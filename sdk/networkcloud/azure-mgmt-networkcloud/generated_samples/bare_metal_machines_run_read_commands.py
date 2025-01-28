# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.networkcloud import NetworkCloudMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-networkcloud
# USAGE
    python bare_metal_machines_run_read_commands.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = NetworkCloudMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="123e4567-e89b-12d3-a456-426655440000",
    )

    response = client.bare_metal_machines.begin_run_read_commands(
        resource_group_name="resourceGroupName",
        bare_metal_machine_name="bareMetalMachineName",
        bare_metal_machine_run_read_commands_parameters={
            "commands": [
                {"arguments": ["pods", "-A"], "command": "kubectl get"},
                {"arguments": ["192.168.0.99", "-c", "3"], "command": "ping"},
            ],
            "limitTimeSeconds": 60,
        },
    ).result()
    print(response)


# x-ms-original-file: specification/networkcloud/resource-manager/Microsoft.NetworkCloud/preview/2024-06-01-preview/examples/BareMetalMachines_RunReadCommands.json
if __name__ == "__main__":
    main()
