# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.storage import StorageManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-storage
# USAGE
    python storage_account_create_premium_block_blob_storage.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = StorageManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="{subscription-id}",
    )

    response = client.storage_accounts.begin_create(
        resource_group_name="res9101",
        account_name="sto4445",
        parameters={
            "kind": "BlockBlobStorage",
            "location": "eastus",
            "properties": {
                "allowSharedKeyAccess": True,
                "encryption": {
                    "keySource": "Microsoft.Storage",
                    "requireInfrastructureEncryption": False,
                    "services": {
                        "blob": {"enabled": True, "keyType": "Account"},
                        "file": {"enabled": True, "keyType": "Account"},
                    },
                },
                "minimumTlsVersion": "TLS1_2",
            },
            "sku": {"name": "Premium_LRS"},
            "tags": {"key1": "value1", "key2": "value2"},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/storage/resource-manager/Microsoft.Storage/stable/2023-05-01/examples/StorageAccountCreatePremiumBlockBlobStorage.json
if __name__ == "__main__":
    main()
