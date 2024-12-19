# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.cognitiveservices import CognitiveServicesManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-cognitiveservices
# USAGE
    python delete_private_endpoint_connection.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = CognitiveServicesManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="{subscription-id}",
    )

    client.private_endpoint_connections.begin_delete(
        resource_group_name="res6977",
        account_name="sto2527",
        private_endpoint_connection_name="{privateEndpointConnectionName}",
    ).result()


# x-ms-original-file: specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices/stable/2024-10-01/examples/DeletePrivateEndpointConnection.json
if __name__ == "__main__":
    main()
