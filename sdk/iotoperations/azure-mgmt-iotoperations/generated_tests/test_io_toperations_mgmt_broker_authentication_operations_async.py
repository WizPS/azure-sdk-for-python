# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.iotoperations.aio import IoTOperationsMgmtClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestIoTOperationsMgmtBrokerAuthenticationOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(IoTOperationsMgmtClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_broker_authentication_get(self, resource_group):
        response = await self.client.broker_authentication.get(
            resource_group_name=resource_group.name,
            instance_name="str",
            broker_name="str",
            authentication_name="str",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_broker_authentication_begin_create_or_update(self, resource_group):
        response = await (
            await self.client.broker_authentication.begin_create_or_update(
                resource_group_name=resource_group.name,
                instance_name="str",
                broker_name="str",
                authentication_name="str",
                resource={
                    "extendedLocation": {"name": "str", "type": "str"},
                    "id": "str",
                    "name": "str",
                    "properties": {
                        "authenticationMethods": [
                            {
                                "method": "str",
                                "customSettings": {
                                    "endpoint": "str",
                                    "auth": {"x509": {"secretRef": "str"}},
                                    "caCertConfigMap": "str",
                                    "headers": {"str": "str"},
                                },
                                "serviceAccountTokenSettings": {"audiences": ["str"]},
                                "x509Settings": {
                                    "authorizationAttributes": {
                                        "str": {"attributes": {"str": "str"}, "subject": "str"}
                                    },
                                    "trustedClientCaCert": "str",
                                },
                            }
                        ],
                        "provisioningState": "str",
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
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_broker_authentication_begin_delete(self, resource_group):
        response = await (
            await self.client.broker_authentication.begin_delete(
                resource_group_name=resource_group.name,
                instance_name="str",
                broker_name="str",
                authentication_name="str",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_broker_authentication_list_by_resource_group(self, resource_group):
        response = self.client.broker_authentication.list_by_resource_group(
            resource_group_name=resource_group.name,
            instance_name="str",
            broker_name="str",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...
