# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.selfhelp import SelfHelpMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-selfhelp
# USAGE
    python check_name_availability_for_diagnostic_when_name_is_available.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = SelfHelpMgmtClient(
        credential=DefaultAzureCredential(),
    )

    response = client.check_name_availability.check_availability(
        scope="subscriptions/0d0fcd2e-c4fd-4349-8497-200edb3923c6",
    )
    print(response)


# x-ms-original-file: specification/help/resource-manager/Microsoft.Help/preview/2024-03-01-preview/examples/CheckNameAvailabilityForDiagnosticWhenNameIsAvailable.json
if __name__ == "__main__":
    main()
