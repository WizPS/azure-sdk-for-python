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


@pytest.mark.live_test_only
class TestTrustedSigningMgmtCodeSigningAccountsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(TrustedSigningMgmtClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_code_signing_accounts_list_by_resource_group(self, resource_group):
        response = self.client.code_signing_accounts.list_by_resource_group(
            resource_group_name=resource_group.name,
        )
        result = [r for r in response]
        assert result == []
        

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_code_signing_accounts_list_by_subscription(self, resource_group):
        response = self.client.code_signing_accounts.list_by_subscription()
        result = [r for r in response]
        assert response
        