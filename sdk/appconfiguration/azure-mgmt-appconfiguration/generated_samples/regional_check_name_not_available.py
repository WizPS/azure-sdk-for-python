# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.appconfiguration import AppConfigurationManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-appconfiguration
# USAGE
    python regional_check_name_not_available.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = AppConfigurationManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="c80fb759-c965-4c6a-9110-9b2b2d038882",
    )

    response = client.operations.regional_check_name_availability(
        location="westus",
        check_name_availability_parameters={
            "name": "contoso",
            "type": "Microsoft.AppConfiguration/configurationStores",
        },
    )
    print(response)


# x-ms-original-file: specification/appconfiguration/resource-manager/Microsoft.AppConfiguration/stable/2024-05-01/examples/RegionalCheckNameNotAvailable.json
if __name__ == "__main__":
    main()
