# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.trustedsigning import TrustedSigningMgmtClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestTrustedSigningMgmtCertificateProfilesOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(TrustedSigningMgmtClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_certificate_profiles_get(self, resource_group):
        response = self.client.certificate_profiles.get(
            resource_group_name=resource_group.name,
            account_name="str",
            profile_name="str",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_certificate_profiles_begin_create(self, resource_group):
        response = self.client.certificate_profiles.begin_create(
            resource_group_name=resource_group.name,
            account_name="str",
            profile_name="str",
            resource={
                "id": "str",
                "name": "str",
                "properties": {
                    "profileType": "str",
                    "certificates": [
                        {
                            "createdDate": "str",
                            "expiryDate": "str",
                            "revocation": {
                                "effectiveAt": "2020-02-20 00:00:00",
                                "failureReason": "str",
                                "reason": "str",
                                "remarks": "str",
                                "requestedAt": "2020-02-20 00:00:00",
                                "status": "str",
                            },
                            "serialNumber": "str",
                            "status": "str",
                            "subjectName": "str",
                            "thumbprint": "str",
                        }
                    ],
                    "city": "str",
                    "commonName": "str",
                    "country": "str",
                    "enhancedKeyUsage": "str",
                    "identityValidationId": "str",
                    "includeCity": bool,
                    "includeCountry": bool,
                    "includePostalCode": bool,
                    "includeState": bool,
                    "includeStreetAddress": bool,
                    "organization": "str",
                    "organizationUnit": "str",
                    "postalCode": "str",
                    "provisioningState": "str",
                    "state": "str",
                    "status": "str",
                    "streetAddress": "str",
                },
                "systemData": {
                    "createdAt": "2020-02-20 00:00:00",
                    "createdBy": "str",
                    "createdByType": "str",
                    "lastModifiedAt": "2020-02-20 00:00:00",
                    "lastModifiedBy": "str",
                    "lastModifiedByType": "str",
                },
                "type": "str",
            },
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_certificate_profiles_begin_delete(self, resource_group):
        response = self.client.certificate_profiles.begin_delete(
            resource_group_name=resource_group.name,
            account_name="str",
            profile_name="str",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_certificate_profiles_list_by_code_signing_account(self, resource_group):
        response = self.client.certificate_profiles.list_by_code_signing_account(
            resource_group_name=resource_group.name,
            account_name="str",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_certificate_profiles_revoke_certificate(self, resource_group):
        response = self.client.certificate_profiles.revoke_certificate(
            resource_group_name=resource_group.name,
            account_name="str",
            profile_name="str",
            body={
                "effectiveAt": "2020-02-20 00:00:00",
                "reason": "str",
                "serialNumber": "str",
                "thumbprint": "str",
                "remarks": "str",
            },
        )

        # please add some check logic here by yourself
        # ...
