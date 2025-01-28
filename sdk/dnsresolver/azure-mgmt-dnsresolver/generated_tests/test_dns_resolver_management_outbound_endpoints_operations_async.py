# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.dnsresolver.aio import DnsResolverManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestDnsResolverManagementOutboundEndpointsOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(DnsResolverManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_create_or_update(self, resource_group):
        response = await (
            await self.client.outbound_endpoints.begin_create_or_update(
                resource_group_name=resource_group.name,
                dns_resolver_name="str",
                outbound_endpoint_name="str",
                parameters={
                    "location": "str",
                    "subnet": {"id": "str"},
                    "etag": "str",
                    "id": "str",
                    "name": "str",
                    "provisioningState": "str",
                    "resourceGuid": "str",
                    "systemData": {
                        "createdAt": "2020-02-20 00:00:00",
                        "createdBy": "str",
                        "createdByType": "str",
                        "lastModifiedAt": "2020-02-20 00:00:00",
                        "lastModifiedBy": "str",
                        "lastModifiedByType": "str",
                    },
                    "tags": {"str": "str"},
                    "type": "str",
                },
                api_version="2023-07-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_update(self, resource_group):
        response = await (
            await self.client.outbound_endpoints.begin_update(
                resource_group_name=resource_group.name,
                dns_resolver_name="str",
                outbound_endpoint_name="str",
                parameters={"tags": {"str": "str"}},
                api_version="2023-07-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_delete(self, resource_group):
        response = await (
            await self.client.outbound_endpoints.begin_delete(
                resource_group_name=resource_group.name,
                dns_resolver_name="str",
                outbound_endpoint_name="str",
                api_version="2023-07-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get(self, resource_group):
        response = await self.client.outbound_endpoints.get(
            resource_group_name=resource_group.name,
            dns_resolver_name="str",
            outbound_endpoint_name="str",
            api_version="2023-07-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list(self, resource_group):
        response = self.client.outbound_endpoints.list(
            resource_group_name=resource_group.name,
            dns_resolver_name="str",
            api_version="2023-07-01-preview",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...
