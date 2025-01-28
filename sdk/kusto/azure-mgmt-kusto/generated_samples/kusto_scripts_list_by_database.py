# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.kusto import KustoManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-kusto
# USAGE
    python kusto_scripts_list_by_database.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = KustoManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="12345678-1234-1234-1234-123456789098",
    )

    response = client.scripts.list_by_database(
        resource_group_name="kustorptest",
        cluster_name="kustoCluster",
        database_name="Kustodatabase8",
    )
    for item in response:
        print(item)


# x-ms-original-file: specification/azure-kusto/resource-manager/Microsoft.Kusto/stable/2024-04-13/examples/KustoScriptsListByDatabase.json
if __name__ == "__main__":
    main()
