# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
# pylint: disable=wrong-import-position

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._patch import *  # pylint: disable=unused-wildcard-import


from ._models_py3 import (  # type: ignore
    AccessKeys,
    ApplicationGroup,
    ApplicationGroupListResult,
    ApplicationGroupPolicy,
    ArmDisasterRecovery,
    ArmDisasterRecoveryListResult,
    AuthorizationRule,
    AuthorizationRuleListResult,
    AvailableCluster,
    AvailableClustersList,
    CaptureDescription,
    CheckNameAvailabilityParameter,
    CheckNameAvailabilityResult,
    Cluster,
    ClusterListResult,
    ClusterQuotaConfigurationProperties,
    ClusterSku,
    ConnectionState,
    ConsumerGroup,
    ConsumerGroupListResult,
    Destination,
    EHNamespace,
    EHNamespaceIdContainer,
    EHNamespaceIdListResult,
    EHNamespaceListResult,
    Encryption,
    ErrorAdditionalInfo,
    ErrorDetail,
    ErrorResponse,
    EventHubListResult,
    Eventhub,
    Identity,
    KeyVaultProperties,
    NWRuleSetIpRules,
    NWRuleSetVirtualNetworkRules,
    NetworkRuleSet,
    NetworkRuleSetListResult,
    NetworkSecurityPerimeter,
    NetworkSecurityPerimeterConfiguration,
    NetworkSecurityPerimeterConfigurationList,
    NetworkSecurityPerimeterConfigurationPropertiesProfile,
    NetworkSecurityPerimeterConfigurationPropertiesResourceAssociation,
    NspAccessRule,
    NspAccessRuleProperties,
    NspAccessRulePropertiesSubscriptionsItem,
    Operation,
    OperationDisplay,
    OperationListResult,
    PrivateEndpoint,
    PrivateEndpointConnection,
    PrivateEndpointConnectionListResult,
    PrivateLinkResource,
    PrivateLinkResourcesListResult,
    ProvisioningIssue,
    ProvisioningIssueProperties,
    ProxyResource,
    RegenerateAccessKeyParameters,
    Resource,
    RetentionDescription,
    SchemaGroup,
    SchemaGroupListResult,
    Sku,
    Subnet,
    SystemData,
    ThrottlingPolicy,
    TrackedResource,
    UserAssignedIdentity,
    UserAssignedIdentityProperties,
)

from ._event_hub_management_client_enums import (  # type: ignore
    AccessRights,
    ApplicationGroupPolicyType,
    CleanupPolicyRetentionDescription,
    ClusterSkuName,
    CreatedByType,
    DefaultAction,
    EncodingCaptureDescription,
    EndPointProvisioningState,
    EntityStatus,
    KeyType,
    ManagedServiceIdentityType,
    MetricId,
    NetworkRuleIPAction,
    NetworkSecurityPerimeterConfigurationProvisioningState,
    NspAccessRuleDirection,
    PrivateLinkConnectionStatus,
    ProvisioningStateDR,
    PublicNetworkAccess,
    PublicNetworkAccessFlag,
    ResourceAssociationAccessMode,
    RoleDisasterRecovery,
    SchemaCompatibility,
    SchemaType,
    SkuName,
    SkuTier,
    TlsVersion,
    UnavailableReason,
)
from ._patch import __all__ as _patch_all
from ._patch import *
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AccessKeys",
    "ApplicationGroup",
    "ApplicationGroupListResult",
    "ApplicationGroupPolicy",
    "ArmDisasterRecovery",
    "ArmDisasterRecoveryListResult",
    "AuthorizationRule",
    "AuthorizationRuleListResult",
    "AvailableCluster",
    "AvailableClustersList",
    "CaptureDescription",
    "CheckNameAvailabilityParameter",
    "CheckNameAvailabilityResult",
    "Cluster",
    "ClusterListResult",
    "ClusterQuotaConfigurationProperties",
    "ClusterSku",
    "ConnectionState",
    "ConsumerGroup",
    "ConsumerGroupListResult",
    "Destination",
    "EHNamespace",
    "EHNamespaceIdContainer",
    "EHNamespaceIdListResult",
    "EHNamespaceListResult",
    "Encryption",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorResponse",
    "EventHubListResult",
    "Eventhub",
    "Identity",
    "KeyVaultProperties",
    "NWRuleSetIpRules",
    "NWRuleSetVirtualNetworkRules",
    "NetworkRuleSet",
    "NetworkRuleSetListResult",
    "NetworkSecurityPerimeter",
    "NetworkSecurityPerimeterConfiguration",
    "NetworkSecurityPerimeterConfigurationList",
    "NetworkSecurityPerimeterConfigurationPropertiesProfile",
    "NetworkSecurityPerimeterConfigurationPropertiesResourceAssociation",
    "NspAccessRule",
    "NspAccessRuleProperties",
    "NspAccessRulePropertiesSubscriptionsItem",
    "Operation",
    "OperationDisplay",
    "OperationListResult",
    "PrivateEndpoint",
    "PrivateEndpointConnection",
    "PrivateEndpointConnectionListResult",
    "PrivateLinkResource",
    "PrivateLinkResourcesListResult",
    "ProvisioningIssue",
    "ProvisioningIssueProperties",
    "ProxyResource",
    "RegenerateAccessKeyParameters",
    "Resource",
    "RetentionDescription",
    "SchemaGroup",
    "SchemaGroupListResult",
    "Sku",
    "Subnet",
    "SystemData",
    "ThrottlingPolicy",
    "TrackedResource",
    "UserAssignedIdentity",
    "UserAssignedIdentityProperties",
    "AccessRights",
    "ApplicationGroupPolicyType",
    "CleanupPolicyRetentionDescription",
    "ClusterSkuName",
    "CreatedByType",
    "DefaultAction",
    "EncodingCaptureDescription",
    "EndPointProvisioningState",
    "EntityStatus",
    "KeyType",
    "ManagedServiceIdentityType",
    "MetricId",
    "NetworkRuleIPAction",
    "NetworkSecurityPerimeterConfigurationProvisioningState",
    "NspAccessRuleDirection",
    "PrivateLinkConnectionStatus",
    "ProvisioningStateDR",
    "PublicNetworkAccess",
    "PublicNetworkAccessFlag",
    "ResourceAssociationAccessMode",
    "RoleDisasterRecovery",
    "SchemaCompatibility",
    "SchemaType",
    "SkuName",
    "SkuTier",
    "TlsVersion",
    "UnavailableReason",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
