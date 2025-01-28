# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.hybridnetwork import HybridNetworkManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-hybridnetwork
# USAGE
    python site_network_service_create.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = HybridNetworkManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.site_network_services.begin_create_or_update(
        resource_group_name="rg1",
        site_network_service_name="testSiteNetworkServiceName",
        parameters={
            "location": "westUs2",
            "properties": {
                "desiredStateConfigurationGroupValueReferences": {
                    "MyVM_Configuration": {
                        "id": "/subscriptions/subid/resourcegroups/contosorg1/providers/microsoft.hybridnetwork/configurationgroupvalues/MyVM_Configuration1"
                    }
                },
                "networkServiceDesignVersionResourceReference": {
                    "id": "/subscriptions/subid/resourcegroups/rg/providers/Microsoft.HybridNetwork/publishers/TestPublisher/networkServiceDesignGroups/TestNetworkServiceDesignGroupName/networkServiceDesignVersions/1.0.0",
                    "idType": "Open",
                },
                "siteReference": {
                    "id": "/subscriptions/subid/resourcegroups/contosorg1/providers/microsoft.hybridnetwork/sites/testSite"
                },
            },
            "sku": {"name": "Standard"},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/hybridnetwork/resource-manager/Microsoft.HybridNetwork/stable/2023-09-01/examples/SiteNetworkServiceCreate.json
if __name__ == "__main__":
    main()
