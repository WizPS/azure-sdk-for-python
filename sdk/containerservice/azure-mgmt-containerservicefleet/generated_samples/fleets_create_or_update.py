# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.containerservicefleet import ContainerServiceFleetMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-containerservicefleet
# USAGE
    python fleets_create_or_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ContainerServiceFleetMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid1",
    )

    response = client.fleets.begin_create_or_update(
        resource_group_name="rg1",
        fleet_name="fleet1",
        resource={
            "location": "East US",
            "properties": {"hubProfile": {"agentProfile": {"vmSize": "Standard_DS1"}, "dnsPrefix": "dnsprefix1"}},
            "tags": {"archv2": "", "tier": "production"},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/containerservice/resource-manager/Microsoft.ContainerService/fleet/stable/2024-04-01/examples/Fleets_CreateOrUpdate.json
if __name__ == "__main__":
    main()
