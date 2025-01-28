# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.databox.aio import DataBoxManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestDataBoxManagementServiceOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(DataBoxManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_available_skus_by_resource_group(self, resource_group):
        response = self.client.service.list_available_skus_by_resource_group(
            resource_group_name=resource_group.name,
            location="str",
            available_sku_request={"country": "str", "location": "str", "transferType": "str", "skuNames": ["str"]},
            api_version="2022-12-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_validate_address(self, resource_group):
        response = await self.client.service.validate_address(
            location="str",
            validate_address={
                "deviceType": "str",
                "shippingAddress": {
                    "country": "str",
                    "streetAddress1": "str",
                    "addressType": "None",
                    "city": "str",
                    "companyName": "str",
                    "postalCode": "str",
                    "skipAddressValidation": bool,
                    "stateOrProvince": "str",
                    "streetAddress2": "str",
                    "streetAddress3": "str",
                    "taxIdentificationNumber": "str",
                    "zipExtendedCode": "str",
                },
                "validationType": "ValidateAddress",
                "transportPreferences": {"preferredShipmentType": "str", "isUpdated": bool},
            },
            api_version="2022-12-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_validate_inputs_by_resource_group(self, resource_group):
        response = await self.client.service.validate_inputs_by_resource_group(
            resource_group_name=resource_group.name,
            location="str",
            validation_request={
                "individualRequestDetails": ["validation_input_request"],
                "validationCategory": "JobCreationValidation",
            },
            api_version="2022-12-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_validate_inputs(self, resource_group):
        response = await self.client.service.validate_inputs(
            location="str",
            validation_request={
                "individualRequestDetails": ["validation_input_request"],
                "validationCategory": "JobCreationValidation",
            },
            api_version="2022-12-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_region_configuration(self, resource_group):
        response = await self.client.service.region_configuration(
            location="str",
            region_configuration_request={
                "datacenterAddressRequest": {"skuName": "str", "storageLocation": "str"},
                "scheduleAvailabilityRequest": "schedule_availability_request",
                "transportAvailabilityRequest": {"skuName": "str"},
            },
            api_version="2022-12-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_region_configuration_by_resource_group(self, resource_group):
        response = await self.client.service.region_configuration_by_resource_group(
            resource_group_name=resource_group.name,
            location="str",
            region_configuration_request={
                "datacenterAddressRequest": {"skuName": "str", "storageLocation": "str"},
                "scheduleAvailabilityRequest": "schedule_availability_request",
                "transportAvailabilityRequest": {"skuName": "str"},
            },
            api_version="2022-12-01",
        )

        # please add some check logic here by yourself
        # ...
