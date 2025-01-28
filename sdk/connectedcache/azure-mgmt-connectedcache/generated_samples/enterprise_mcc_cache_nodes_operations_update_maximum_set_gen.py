# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.connectedcache import ConnectedCacheMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-connectedcache
# USAGE
    python enterprise_mcc_cache_nodes_operations_update_maximum_set_gen.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ConnectedCacheMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="SUBSCRIPTION_ID",
    )

    response = client.enterprise_mcc_cache_nodes_operations.update(
        resource_group_name="rgConnectedCache",
        customer_resource_name="qanjqtvrxzjkljdysdjvdiqcxkttskpdzykzuefhbhz",
        cache_node_resource_name="kllmlvazrcxmfjfozulzqnsgvspgwmhogcafvauchunlgfr",
        properties={"tags": {"key1653": "nzjczrhclhkndesgy"}},
    )
    print(response)


# x-ms-original-file: 2023-05-01-preview/EnterpriseMccCacheNodesOperations_Update_MaximumSet_Gen.json
if __name__ == "__main__":
    main()
