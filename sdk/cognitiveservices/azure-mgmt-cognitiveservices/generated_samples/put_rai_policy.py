# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.cognitiveservices import CognitiveServicesManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-cognitiveservices
# USAGE
    python put_rai_policy.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = CognitiveServicesManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    response = client.rai_policies.create_or_update(
        resource_group_name="resourceGroupName",
        account_name="accountName",
        rai_policy_name="raiPolicyName",
        rai_policy={
            "properties": {
                "basePolicyName": "Microsoft.Default",
                "contentFilters": [
                    {
                        "blocking": False,
                        "enabled": False,
                        "name": "Hate",
                        "severityThreshold": "High",
                        "source": "Prompt",
                    },
                    {
                        "blocking": True,
                        "enabled": True,
                        "name": "Hate",
                        "severityThreshold": "Medium",
                        "source": "Completion",
                    },
                    {
                        "blocking": True,
                        "enabled": True,
                        "name": "Sexual",
                        "severityThreshold": "High",
                        "source": "Prompt",
                    },
                    {
                        "blocking": True,
                        "enabled": True,
                        "name": "Sexual",
                        "severityThreshold": "Medium",
                        "source": "Completion",
                    },
                    {
                        "blocking": True,
                        "enabled": True,
                        "name": "Selfharm",
                        "severityThreshold": "High",
                        "source": "Prompt",
                    },
                    {
                        "blocking": True,
                        "enabled": True,
                        "name": "Selfharm",
                        "severityThreshold": "Medium",
                        "source": "Completion",
                    },
                    {
                        "blocking": True,
                        "enabled": True,
                        "name": "Violence",
                        "severityThreshold": "Medium",
                        "source": "Prompt",
                    },
                    {
                        "blocking": True,
                        "enabled": True,
                        "name": "Violence",
                        "severityThreshold": "Medium",
                        "source": "Completion",
                    },
                    {"blocking": True, "enabled": True, "name": "Jailbreak", "source": "Prompt"},
                    {"blocking": True, "enabled": True, "name": "Protected Material Text", "source": "Completion"},
                    {"blocking": True, "enabled": True, "name": "Protected Material Code", "source": "Completion"},
                    {"blocking": True, "enabled": True, "name": "Profanity", "source": "Prompt"},
                ],
                "mode": "Asynchronous_filter",
            }
        },
    )
    print(response)


# x-ms-original-file: specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices/stable/2024-10-01/examples/PutRaiPolicy.json
if __name__ == "__main__":
    main()
