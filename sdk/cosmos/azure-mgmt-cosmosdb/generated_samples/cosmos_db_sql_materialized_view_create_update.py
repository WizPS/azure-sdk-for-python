# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.cosmosdb import CosmosDBManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-cosmosdb
# USAGE
    python cosmos_db_sql_materialized_view_create_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = CosmosDBManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.sql_resources.begin_create_update_sql_container(
        resource_group_name="rg1",
        account_name="ddb1",
        database_name="databaseName",
        container_name="mvContainerName",
        create_update_sql_container_parameters={
            "location": "West US",
            "properties": {
                "options": {},
                "resource": {
                    "id": "mvContainerName",
                    "indexingPolicy": {
                        "automatic": True,
                        "excludedPaths": [],
                        "includedPaths": [
                            {
                                "indexes": [
                                    {"dataType": "String", "kind": "Range", "precision": -1},
                                    {"dataType": "Number", "kind": "Range", "precision": -1},
                                ],
                                "path": "/*",
                            }
                        ],
                        "indexingMode": "consistent",
                    },
                    "materializedViewDefinition": {
                        "definition": "select * from ROOT",
                        "sourceCollectionId": "sourceContainerName",
                    },
                    "partitionKey": {"kind": "Hash", "paths": ["/mvpk"]},
                },
            },
            "tags": {},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/cosmos-db/resource-manager/Microsoft.DocumentDB/preview/2024-12-01-preview/examples/CosmosDBSqlMaterializedViewCreateUpdate.json
if __name__ == "__main__":
    main()
