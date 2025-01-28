# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.web import WebSiteManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-web
# USAGE
    python create_or_update_function_app_flex_consumption.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = WebSiteManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="34adfa4f-cedf-4dc0-ba29-b6d1a69ab345",
    )

    response = client.web_apps.begin_create_or_update(
        resource_group_name="testrg123",
        name="sitef6141",
        site_envelope={
            "kind": "functionapp,linux",
            "location": "East US",
            "properties": {
                "functionAppConfig": {
                    "deployment": {
                        "storage": {
                            "authentication": {
                                "storageAccountConnectionStringName": "TheAppSettingName",
                                "type": "StorageAccountConnectionString",
                            },
                            "type": "blobContainer",
                            "value": "https://storageAccountName.blob.core.windows.net/containername",
                        }
                    },
                    "runtime": {"name": "python", "version": "3.11"},
                    "scaleAndConcurrency": {"instanceMemoryMB": 2048, "maximumInstanceCount": 100},
                },
                "siteConfig": {
                    "appSettings": [
                        {
                            "name": "AzureWebJobsStorage",
                            "value": "DefaultEndpointsProtocol=https;AccountName=StorageAccountName;AccountKey=Sanitized;EndpointSuffix=core.windows.net",
                        },
                        {
                            "name": "APPLICATIONINSIGHTS_CONNECTION_STRING",
                            "value": "InstrumentationKey=Sanitized;IngestionEndpoint=Sanitized;LiveEndpoint=Sanitized",
                        },
                    ]
                },
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/web/resource-manager/Microsoft.Web/stable/2024-04-01/examples/CreateOrUpdateFunctionAppFlexConsumption.json
if __name__ == "__main__":
    main()
