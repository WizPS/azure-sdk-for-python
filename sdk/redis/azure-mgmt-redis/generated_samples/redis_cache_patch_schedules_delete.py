# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.redis import RedisManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-redis
# USAGE
    python redis_cache_patch_schedules_delete.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = RedisManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    client.patch_schedules.delete(
        resource_group_name="rg1",
        name="cache1",
        default="default",
    )


# x-ms-original-file: specification/redis/resource-manager/Microsoft.Cache/stable/2024-11-01/examples/RedisCachePatchSchedulesDelete.json
if __name__ == "__main__":
    main()
