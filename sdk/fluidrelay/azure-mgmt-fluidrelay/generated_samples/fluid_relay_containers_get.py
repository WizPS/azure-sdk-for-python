# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.fluidrelay import FluidRelayManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-fluidrelay
# USAGE
    python fluid_relay_containers_get.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = FluidRelayManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="xxxx-xxxx-xxxx-xxxx",
    )

    response = client.fluid_relay_containers.get(
        resource_group="myResourceGroup",
        fluid_relay_server_name="myFluidRelayServer",
        fluid_relay_container_name="myFluidRelayContainer",
    )
    print(response)


# x-ms-original-file: specification/fluidrelay/resource-manager/Microsoft.FluidRelay/stable/2022-06-01/examples/FluidRelayContainers_Get.json
if __name__ == "__main__":
    main()
