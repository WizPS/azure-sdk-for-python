# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import ArmIdentity
from ._models_py3 import ArmUserIdentity
from ._models_py3 import CertificateBodyDescription
from ._models_py3 import CertificateDescription
from ._models_py3 import CertificateListDescription
from ._models_py3 import CertificateProperties
from ._models_py3 import CertificatePropertiesWithNonce
from ._models_py3 import CertificateVerificationDescription
from ._models_py3 import CertificateWithNonceDescription
from ._models_py3 import CloudToDeviceProperties
from ._models_py3 import EndpointHealthData
from ._models_py3 import EndpointHealthDataListResult
from ._models_py3 import EnrichmentProperties
from ._models_py3 import ErrorDetails
from ._models_py3 import EventHubConsumerGroupBodyDescription
from ._models_py3 import EventHubConsumerGroupInfo
from ._models_py3 import EventHubConsumerGroupName
from ._models_py3 import EventHubConsumerGroupsListResult
from ._models_py3 import EventHubProperties
from ._models_py3 import ExportDevicesRequest
from ._models_py3 import FailoverInput
from ._models_py3 import FallbackRouteProperties
from ._models_py3 import FeedbackProperties
from ._models_py3 import GroupIdInformation
from ._models_py3 import GroupIdInformationProperties
from ._models_py3 import ImportDevicesRequest
from ._models_py3 import IotHubCapacity
from ._models_py3 import IotHubDescription
from ._models_py3 import IotHubDescriptionListResult
from ._models_py3 import IotHubLocationDescription
from ._models_py3 import IotHubNameAvailabilityInfo
from ._models_py3 import IotHubProperties
from ._models_py3 import IotHubQuotaMetricInfo
from ._models_py3 import IotHubQuotaMetricInfoListResult
from ._models_py3 import IotHubSkuDescription
from ._models_py3 import IotHubSkuDescriptionListResult
from ._models_py3 import IotHubSkuInfo
from ._models_py3 import IpFilterRule
from ._models_py3 import JobResponse
from ._models_py3 import JobResponseListResult
from ._models_py3 import ManagedIdentity
from ._models_py3 import MatchedRoute
from ._models_py3 import MessagingEndpointProperties
from ._models_py3 import Name
from ._models_py3 import NetworkRuleSetIpRule
from ._models_py3 import NetworkRuleSetProperties
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationInputs
from ._models_py3 import OperationListResult
from ._models_py3 import PrivateEndpoint
from ._models_py3 import PrivateEndpointConnection
from ._models_py3 import PrivateEndpointConnectionProperties
from ._models_py3 import PrivateLinkResources
from ._models_py3 import PrivateLinkServiceConnectionState
from ._models_py3 import RegistryStatistics
from ._models_py3 import Resource
from ._models_py3 import RouteCompilationError
from ._models_py3 import RouteErrorPosition
from ._models_py3 import RouteErrorRange
from ._models_py3 import RouteProperties
from ._models_py3 import RoutingCosmosDBSqlApiProperties
from ._models_py3 import RoutingEndpoints
from ._models_py3 import RoutingEventHubProperties
from ._models_py3 import RoutingMessage
from ._models_py3 import RoutingProperties
from ._models_py3 import RoutingServiceBusQueueEndpointProperties
from ._models_py3 import RoutingServiceBusTopicEndpointProperties
from ._models_py3 import RoutingStorageContainerProperties
from ._models_py3 import RoutingTwin
from ._models_py3 import RoutingTwinProperties
from ._models_py3 import SharedAccessSignatureAuthorizationRule
from ._models_py3 import SharedAccessSignatureAuthorizationRuleListResult
from ._models_py3 import StorageEndpointProperties
from ._models_py3 import SystemData
from ._models_py3 import TagsResource
from ._models_py3 import TestAllRoutesInput
from ._models_py3 import TestAllRoutesResult
from ._models_py3 import TestRouteInput
from ._models_py3 import TestRouteResult
from ._models_py3 import TestRouteResultDetails
from ._models_py3 import UserSubscriptionQuota
from ._models_py3 import UserSubscriptionQuotaListResult

from ._iot_hub_client_enums import AccessRights
from ._iot_hub_client_enums import AuthenticationType
from ._iot_hub_client_enums import Capabilities
from ._iot_hub_client_enums import CreatedByType
from ._iot_hub_client_enums import DefaultAction
from ._iot_hub_client_enums import EndpointHealthStatus
from ._iot_hub_client_enums import IotHubNameUnavailabilityReason
from ._iot_hub_client_enums import IotHubReplicaRoleType
from ._iot_hub_client_enums import IotHubScaleType
from ._iot_hub_client_enums import IotHubSku
from ._iot_hub_client_enums import IotHubSkuTier
from ._iot_hub_client_enums import IpFilterActionType
from ._iot_hub_client_enums import JobStatus
from ._iot_hub_client_enums import JobType
from ._iot_hub_client_enums import NetworkRuleIPAction
from ._iot_hub_client_enums import PrivateLinkServiceConnectionStatus
from ._iot_hub_client_enums import PublicNetworkAccess
from ._iot_hub_client_enums import ResourceIdentityType
from ._iot_hub_client_enums import RouteErrorSeverity
from ._iot_hub_client_enums import RoutingSource
from ._iot_hub_client_enums import RoutingStorageContainerPropertiesEncoding
from ._iot_hub_client_enums import TestResultStatus
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ArmIdentity",
    "ArmUserIdentity",
    "CertificateBodyDescription",
    "CertificateDescription",
    "CertificateListDescription",
    "CertificateProperties",
    "CertificatePropertiesWithNonce",
    "CertificateVerificationDescription",
    "CertificateWithNonceDescription",
    "CloudToDeviceProperties",
    "EndpointHealthData",
    "EndpointHealthDataListResult",
    "EnrichmentProperties",
    "ErrorDetails",
    "EventHubConsumerGroupBodyDescription",
    "EventHubConsumerGroupInfo",
    "EventHubConsumerGroupName",
    "EventHubConsumerGroupsListResult",
    "EventHubProperties",
    "ExportDevicesRequest",
    "FailoverInput",
    "FallbackRouteProperties",
    "FeedbackProperties",
    "GroupIdInformation",
    "GroupIdInformationProperties",
    "ImportDevicesRequest",
    "IotHubCapacity",
    "IotHubDescription",
    "IotHubDescriptionListResult",
    "IotHubLocationDescription",
    "IotHubNameAvailabilityInfo",
    "IotHubProperties",
    "IotHubQuotaMetricInfo",
    "IotHubQuotaMetricInfoListResult",
    "IotHubSkuDescription",
    "IotHubSkuDescriptionListResult",
    "IotHubSkuInfo",
    "IpFilterRule",
    "JobResponse",
    "JobResponseListResult",
    "ManagedIdentity",
    "MatchedRoute",
    "MessagingEndpointProperties",
    "Name",
    "NetworkRuleSetIpRule",
    "NetworkRuleSetProperties",
    "Operation",
    "OperationDisplay",
    "OperationInputs",
    "OperationListResult",
    "PrivateEndpoint",
    "PrivateEndpointConnection",
    "PrivateEndpointConnectionProperties",
    "PrivateLinkResources",
    "PrivateLinkServiceConnectionState",
    "RegistryStatistics",
    "Resource",
    "RouteCompilationError",
    "RouteErrorPosition",
    "RouteErrorRange",
    "RouteProperties",
    "RoutingCosmosDBSqlApiProperties",
    "RoutingEndpoints",
    "RoutingEventHubProperties",
    "RoutingMessage",
    "RoutingProperties",
    "RoutingServiceBusQueueEndpointProperties",
    "RoutingServiceBusTopicEndpointProperties",
    "RoutingStorageContainerProperties",
    "RoutingTwin",
    "RoutingTwinProperties",
    "SharedAccessSignatureAuthorizationRule",
    "SharedAccessSignatureAuthorizationRuleListResult",
    "StorageEndpointProperties",
    "SystemData",
    "TagsResource",
    "TestAllRoutesInput",
    "TestAllRoutesResult",
    "TestRouteInput",
    "TestRouteResult",
    "TestRouteResultDetails",
    "UserSubscriptionQuota",
    "UserSubscriptionQuotaListResult",
    "AccessRights",
    "AuthenticationType",
    "Capabilities",
    "CreatedByType",
    "DefaultAction",
    "EndpointHealthStatus",
    "IotHubNameUnavailabilityReason",
    "IotHubReplicaRoleType",
    "IotHubScaleType",
    "IotHubSku",
    "IotHubSkuTier",
    "IpFilterActionType",
    "JobStatus",
    "JobType",
    "NetworkRuleIPAction",
    "PrivateLinkServiceConnectionStatus",
    "PublicNetworkAccess",
    "ResourceIdentityType",
    "RouteErrorSeverity",
    "RoutingSource",
    "RoutingStorageContainerPropertiesEncoding",
    "TestResultStatus",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
