# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.quota import QuotaMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-quota
# USAGE
    python subscription_quota_allocation_requests_get_compute.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = QuotaMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    response = client.group_quota_subscription_allocation_request.get(
        management_group_id="E7EC67B3-7657-4966-BFFC-41EFD36BAA09",
        group_quota_name="groupquota1",
        resource_provider_name="Microsoft.Compute",
        allocation_id="AE000000-0000-0000-0000-00000000000A",
    )
    print(response)


# x-ms-original-file: specification/quota/resource-manager/Microsoft.Quota/preview/2024-12-18-preview/examples/SubscriptionQuotaAllocationRequests/SubscriptionQuotaAllocationRequests_Get-Compute.json
if __name__ == "__main__":
    main()
