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
class TestNetworkManagementVpnGatewaysOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(NetworkManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_vpn_gateways_get(self, resource_group):
        response = await self.client.vpn_gateways.get(
            resource_group_name=resource_group.name,
            gateway_name="str",
            api_version="2024-05-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_vpn_gateways_begin_create_or_update(self, resource_group):
        response = await (
            await self.client.vpn_gateways.begin_create_or_update(
                resource_group_name=resource_group.name,
                gateway_name="str",
                vpn_gateway_parameters={
                    "bgpSettings": {
                        "asn": 0,
                        "bgpPeeringAddress": "str",
                        "bgpPeeringAddresses": [
                            {
                                "customBgpIpAddresses": ["str"],
                                "defaultBgpIpAddresses": ["str"],
                                "ipconfigurationId": "str",
                                "tunnelIpAddresses": ["str"],
                            }
                        ],
                        "peerWeight": 0,
                    },
                    "connections": [
                        {
                            "connectionBandwidth": 0,
                            "connectionStatus": "str",
                            "dpdTimeoutSeconds": 0,
                            "egressBytesTransferred": 0,
                            "enableBgp": bool,
                            "enableInternetSecurity": bool,
                            "enableRateLimiting": bool,
                            "etag": "str",
                            "id": "str",
                            "ingressBytesTransferred": 0,
                            "ipsecPolicies": [
                                {
                                    "dhGroup": "str",
                                    "ikeEncryption": "str",
                                    "ikeIntegrity": "str",
                                    "ipsecEncryption": "str",
                                    "ipsecIntegrity": "str",
                                    "pfsGroup": "str",
                                    "saDataSizeKilobytes": 0,
                                    "saLifeTimeSeconds": 0,
                                }
                            ],
                            "name": "str",
                            "provisioningState": "str",
                            "remoteVpnSite": {"id": "str"},
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
                            "routingWeight": 0,
                            "sharedKey": "str",
                            "trafficSelectorPolicies": [
                                {"localAddressRanges": ["str"], "remoteAddressRanges": ["str"]}
                            ],
                            "useLocalAzureIpAddress": bool,
                            "usePolicyBasedTrafficSelectors": bool,
                            "vpnConnectionProtocolType": "str",
                            "vpnLinkConnections": [
                                {
                                    "connectionBandwidth": 0,
                                    "connectionStatus": "str",
                                    "dpdTimeoutSeconds": 0,
                                    "egressBytesTransferred": 0,
                                    "egressNatRules": [{"id": "str"}],
                                    "enableBgp": bool,
                                    "enableRateLimiting": bool,
                                    "etag": "str",
                                    "id": "str",
                                    "ingressBytesTransferred": 0,
                                    "ingressNatRules": [{"id": "str"}],
                                    "ipsecPolicies": [
                                        {
                                            "dhGroup": "str",
                                            "ikeEncryption": "str",
                                            "ikeIntegrity": "str",
                                            "ipsecEncryption": "str",
                                            "ipsecIntegrity": "str",
                                            "pfsGroup": "str",
                                            "saDataSizeKilobytes": 0,
                                            "saLifeTimeSeconds": 0,
                                        }
                                    ],
                                    "name": "str",
                                    "provisioningState": "str",
                                    "routingWeight": 0,
                                    "sharedKey": "str",
                                    "type": "str",
                                    "useLocalAzureIpAddress": bool,
                                    "usePolicyBasedTrafficSelectors": bool,
                                    "vpnConnectionProtocolType": "str",
                                    "vpnGatewayCustomBgpAddresses": [
                                        {"customBgpIpAddress": "str", "ipConfigurationId": "str"}
                                    ],
                                    "vpnLinkConnectionMode": "str",
                                    "vpnSiteLink": {"id": "str"},
                                }
                            ],
                        }
                    ],
                    "enableBgpRouteTranslationForNat": bool,
                    "etag": "str",
                    "id": "str",
                    "ipConfigurations": [{"id": "str", "privateIpAddress": "str", "publicIpAddress": "str"}],
                    "isRoutingPreferenceInternet": bool,
                    "location": "str",
                    "name": "str",
                    "natRules": [
                        {
                            "egressVpnSiteLinkConnections": [{"id": "str"}],
                            "etag": "str",
                            "externalMappings": [{"addressSpace": "str", "portRange": "str"}],
                            "id": "str",
                            "ingressVpnSiteLinkConnections": [{"id": "str"}],
                            "internalMappings": [{"addressSpace": "str", "portRange": "str"}],
                            "ipConfigurationId": "str",
                            "mode": "str",
                            "name": "str",
                            "provisioningState": "str",
                            "type": "str",
                        }
                    ],
                    "provisioningState": "str",
                    "tags": {"str": "str"},
                    "type": "str",
                    "virtualHub": {"id": "str"},
                    "vpnGatewayScaleUnit": 0,
                },
                api_version="2024-05-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_vpn_gateways_begin_update_tags(self, resource_group):
        response = await (
            await self.client.vpn_gateways.begin_update_tags(
                resource_group_name=resource_group.name,
                gateway_name="str",
                vpn_gateway_parameters={"tags": {"str": "str"}},
                api_version="2024-05-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_vpn_gateways_begin_delete(self, resource_group):
        response = await (
            await self.client.vpn_gateways.begin_delete(
                resource_group_name=resource_group.name,
                gateway_name="str",
                api_version="2024-05-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_vpn_gateways_begin_reset(self, resource_group):
        response = await (
            await self.client.vpn_gateways.begin_reset(
                resource_group_name=resource_group.name,
                gateway_name="str",
                api_version="2024-05-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_vpn_gateways_begin_start_packet_capture(self, resource_group):
        response = await (
            await self.client.vpn_gateways.begin_start_packet_capture(
                resource_group_name=resource_group.name,
                gateway_name="str",
                api_version="2024-05-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_vpn_gateways_begin_stop_packet_capture(self, resource_group):
        response = await (
            await self.client.vpn_gateways.begin_stop_packet_capture(
                resource_group_name=resource_group.name,
                gateway_name="str",
                api_version="2024-05-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_vpn_gateways_list_by_resource_group(self, resource_group):
        response = self.client.vpn_gateways.list_by_resource_group(
            resource_group_name=resource_group.name,
            api_version="2024-05-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_vpn_gateways_list(self, resource_group):
        response = self.client.vpn_gateways.list(
            api_version="2024-05-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...
