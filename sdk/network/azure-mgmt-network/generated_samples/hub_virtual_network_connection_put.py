# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.network import NetworkManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-network
# USAGE
    python hub_virtual_network_connection_put.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = NetworkManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.hub_virtual_network_connections.begin_create_or_update(
        resource_group_name="rg1",
        virtual_hub_name="virtualHub1",
        connection_name="connection1",
        hub_virtual_network_connection_parameters={
            "properties": {
                "enableInternetSecurity": False,
                "remoteVirtualNetwork": {
                    "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/virtualNetworks/SpokeVnet1"
                },
                "routingConfiguration": {
                    "associatedRouteTable": {
                        "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/virtualHubs/virtualHub1/hubRouteTables/hubRouteTable1"
                    },
                    "inboundRouteMap": {
                        "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/virtualHubs/virtualHub1/routeMaps/routeMap1"
                    },
                    "outboundRouteMap": {
                        "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/virtualHubs/virtualHub1/routeMaps/routeMap2"
                    },
                    "propagatedRouteTables": {
                        "ids": [
                            {
                                "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/virtualHubs/virtualHub1/hubRouteTables/hubRouteTable1"
                            }
                        ],
                        "labels": ["label1", "label2"],
                    },
                    "vnetRoutes": {
                        "staticRoutes": [
                            {
                                "addressPrefixes": ["10.1.0.0/16", "10.2.0.0/16"],
                                "name": "route1",
                                "nextHopIpAddress": "10.0.0.68",
                            },
                            {
                                "addressPrefixes": ["10.3.0.0/16", "10.4.0.0/16"],
                                "name": "route2",
                                "nextHopIpAddress": "10.0.0.65",
                            },
                        ],
                        "staticRoutesConfig": {"vnetLocalRouteOverrideCriteria": "Equal"},
                    },
                },
            }
        },
    ).result()
    print(response)


# x-ms-original-file: specification/network/resource-manager/Microsoft.Network/stable/2024-05-01/examples/HubVirtualNetworkConnectionPut.json
if __name__ == "__main__":
    main()
