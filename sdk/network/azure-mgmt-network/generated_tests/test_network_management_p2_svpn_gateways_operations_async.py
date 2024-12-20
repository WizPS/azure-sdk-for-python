# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.network.aio import NetworkManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNetworkManagementP2SVpnGatewaysOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(NetworkManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_p2_svpn_gateways_get(self, resource_group):
        response = await self.client.p2_svpn_gateways.get(
            resource_group_name=resource_group.name,
            gateway_name="str",
            api_version="2024-05-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_p2_svpn_gateways_begin_create_or_update(self, resource_group):
        response = await (
            await self.client.p2_svpn_gateways.begin_create_or_update(
                resource_group_name=resource_group.name,
                gateway_name="str",
                p2_s_vpn_gateway_parameters={
                    "customDnsServers": ["str"],
                    "etag": "str",
                    "id": "str",
                    "isRoutingPreferenceInternet": bool,
                    "location": "str",
                    "name": "str",
                    "p2SConnectionConfigurations": [
                        {
                            "configurationPolicyGroupAssociations": [{"id": "str"}],
                            "enableInternetSecurity": bool,
                            "etag": "str",
                            "id": "str",
                            "name": "str",
                            "previousConfigurationPolicyGroupAssociations": [
                                {
                                    "etag": "str",
                                    "id": "str",
                                    "isDefault": bool,
                                    "name": "str",
                                    "p2SConnectionConfigurations": [{"id": "str"}],
                                    "policyMembers": [{"attributeType": "str", "attributeValue": "str", "name": "str"}],
                                    "priority": 0,
                                    "provisioningState": "str",
                                    "type": "str",
                                }
                            ],
                            "provisioningState": "str",
                            "routingConfiguration": {
                                "associatedRouteTable": {"id": "str"},
                                "inboundRouteMap": {"id": "str"},
                                "outboundRouteMap": {"id": "str"},
                                "propagatedRouteTables": {"ids": [{"id": "str"}], "labels": ["str"]},
                                "vnetRoutes": {
                                    "bgpConnections": [{"id": "str"}],
                                    "staticRoutes": [
                                        {"addressPrefixes": ["str"], "name": "str", "nextHopIpAddress": "str"}
                                    ],
                                    "staticRoutesConfig": {
                                        "propagateStaticRoutes": bool,
                                        "vnetLocalRouteOverrideCriteria": "str",
                                    },
                                },
                            },
                            "vpnClientAddressPool": {
                                "addressPrefixes": ["str"],
                                "ipamPoolPrefixAllocations": [
                                    {"allocatedAddressPrefixes": ["str"], "id": "str", "numberOfIpAddresses": "str"}
                                ],
                            },
                        }
                    ],
                    "provisioningState": "str",
                    "tags": {"str": "str"},
                    "type": "str",
                    "virtualHub": {"id": "str"},
                    "vpnClientConnectionHealth": {
                        "allocatedIpAddresses": ["str"],
                        "totalEgressBytesTransferred": 0,
                        "totalIngressBytesTransferred": 0,
                        "vpnClientConnectionsCount": 0,
                    },
                    "vpnGatewayScaleUnit": 0,
                    "vpnServerConfiguration": {"id": "str"},
                },
                api_version="2024-05-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_p2_svpn_gateways_begin_update_tags(self, resource_group):
        response = await (
            await self.client.p2_svpn_gateways.begin_update_tags(
                resource_group_name=resource_group.name,
                gateway_name="str",
                p2_s_vpn_gateway_parameters={"tags": {"str": "str"}},
                api_version="2024-05-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_p2_svpn_gateways_begin_delete(self, resource_group):
        response = await (
            await self.client.p2_svpn_gateways.begin_delete(
                resource_group_name=resource_group.name,
                gateway_name="str",
                api_version="2024-05-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_p2_svpn_gateways_list_by_resource_group(self, resource_group):
        response = self.client.p2_svpn_gateways.list_by_resource_group(
            resource_group_name=resource_group.name,
            api_version="2024-05-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_p2_svpn_gateways_list(self, resource_group):
        response = self.client.p2_svpn_gateways.list(
            api_version="2024-05-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_p2_svpn_gateways_begin_reset(self, resource_group):
        response = await (
            await self.client.p2_svpn_gateways.begin_reset(
                resource_group_name=resource_group.name,
                gateway_name="str",
                api_version="2024-05-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_p2_svpn_gateways_begin_generate_vpn_profile(self, resource_group):
        response = await (
            await self.client.p2_svpn_gateways.begin_generate_vpn_profile(
                resource_group_name=resource_group.name,
                gateway_name="str",
                parameters={"authenticationMethod": "str"},
                api_version="2024-05-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_p2_svpn_gateways_begin_get_p2_s_vpn_connection_health(self, resource_group):
        response = await (
            await self.client.p2_svpn_gateways.begin_get_p2_s_vpn_connection_health(
                resource_group_name=resource_group.name,
                gateway_name="str",
                api_version="2024-05-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_p2_svpn_gateways_begin_get_p2_s_vpn_connection_health_detailed(self, resource_group):
        response = await (
            await self.client.p2_svpn_gateways.begin_get_p2_s_vpn_connection_health_detailed(
                resource_group_name=resource_group.name,
                gateway_name="str",
                request={"outputBlobSasUrl": "str", "vpnUserNamesFilter": ["str"]},
                api_version="2024-05-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_p2_svpn_gateways_begin_disconnect_p2_s_vpn_connections(self, resource_group):
        response = await (
            await self.client.p2_svpn_gateways.begin_disconnect_p2_s_vpn_connections(
                resource_group_name=resource_group.name,
                p2_s_vpn_gateway_name="str",
                request={"vpnConnectionIds": ["str"]},
                api_version="2024-05-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
