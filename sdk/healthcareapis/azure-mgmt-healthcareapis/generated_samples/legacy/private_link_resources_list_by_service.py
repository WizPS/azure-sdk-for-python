# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.healthcareapis import HealthcareApisManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-healthcareapis
# USAGE
    python private_link_resources_list_by_service.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = HealthcareApisManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.private_link_resources.list_by_service(
        resource_group_name="rgname",
        resource_name="service1",
    )
    print(response)


# x-ms-original-file: specification/healthcareapis/resource-manager/Microsoft.HealthcareApis/stable/2024-03-31/examples/legacy/PrivateLinkResourcesListByService.json
if __name__ == "__main__":
    main()
