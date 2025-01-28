# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.containerorchestratorruntime import ContainerOrchestratorRuntimeMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-containerorchestratorruntime
# USAGE
    python storage_class_create_or_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ContainerOrchestratorRuntimeMgmtClient(
        credential=DefaultAzureCredential(),
    )

    response = client.storage_class.begin_create_or_update(
        resource_uri="subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/example/providers/Microsoft.Kubernetes/connectedClusters/cluster1",
        storage_class_name="testrwx",
        resource={"properties": {"typeProperties": {"backingStorageClassName": "default", "type": "RWX"}}},
    ).result()
    print(response)


# x-ms-original-file: 2024-03-01/StorageClass_CreateOrUpdate.json
if __name__ == "__main__":
    main()
