# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.healthdataaiservices import HealthDataAIServicesMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-healthdataaiservices
# USAGE
    python deid_services_create_maximum_set_gen.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = HealthDataAIServicesMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="SUBSCRIPTION_ID",
    )

    response = client.deid_services.begin_create(
        resource_group_name="rgopenapi",
        deid_service_name="deidTest",
        resource={
            "identity": {"type": "None", "userAssignedIdentities": {}},
            "location": "qwyhvdwcsjulggagdqxlmazcl",
            "properties": {"publicNetworkAccess": "Enabled"},
            "tags": {},
        },
    ).result()
    print(response)


# x-ms-original-file: 2024-09-20/DeidServices_Create_MaximumSet_Gen.json
if __name__ == "__main__":
    main()
