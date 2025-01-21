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
    python storage_account_update_object_replication_policy_on_source.py

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

    response = client.object_replication_policies.create_or_update(
        resource_group_name="res7687",
        account_name="src1122",
        object_replication_policy_id="2a20bb73-5717-4635-985a-5d4cf777438f",
        properties={
            "properties": {
                "destinationAccount": "dst112",
                "rules": [
                    {
                        "destinationContainer": "dcont139",
                        "filters": {"prefixMatch": ["blobA", "blobB"]},
                        "ruleId": "d5d18a48-8801-4554-aeaa-74faf65f5ef9",
                        "sourceContainer": "scont139",
                    },
                    {
                        "destinationContainer": "dcont179",
                        "ruleId": "cfbb4bc2-8b60-429f-b05a-d1e0942b33b2",
                        "sourceContainer": "scont179",
                    },
                ],
                "sourceAccount": "src1122",
            }
        },
    )
    print(response)


# x-ms-original-file: specification/storage/resource-manager/Microsoft.Storage/stable/2023-05-01/examples/StorageAccountUpdateObjectReplicationPolicyOnSource.json
if __name__ == "__main__":
    main()
