# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.databox import DataBoxManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-databox
# USAGE
    python jobs_create.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = DataBoxManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="YourSubscriptionId",
    )

    response = client.jobs.begin_create(
        resource_group_name="YourResourceGroupName",
        job_name="TestJobName1",
        job_resource={
            "location": "westus",
            "properties": {
                "details": {
                    "contactDetails": {
                        "contactName": "XXXX XXXX",
                        "emailList": ["xxxx@xxxx.xxx"],
                        "phone": "0000000000",
                        "phoneExtension": "",
                    },
                    "dataImportDetails": [
                        {
                            "accountDetails": {
                                "dataAccountType": "StorageAccount",
                                "storageAccountId": "/subscriptions/YourSubscriptionId/resourcegroups/YourResourceGroupName/providers/Microsoft.Storage/storageAccounts/YourStorageAccountName",
                            }
                        }
                    ],
                    "jobDetailsType": "DataBox",
                    "shippingAddress": {
                        "addressType": "Commercial",
                        "city": "XXXX XXXX",
                        "companyName": "XXXX XXXX",
                        "country": "XX",
                        "postalCode": "00000",
                        "stateOrProvince": "XX",
                        "streetAddress1": "XXXX XXXX",
                        "streetAddress2": "XXXX XXXX",
                    },
                },
                "transferType": "ImportToAzure",
            },
            "sku": {"name": "DataBox"},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/databox/resource-manager/Microsoft.DataBox/stable/2022-12-01/examples/JobsCreate.json
if __name__ == "__main__":
    main()
