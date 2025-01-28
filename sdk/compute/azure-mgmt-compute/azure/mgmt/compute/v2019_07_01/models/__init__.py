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
    AccessUri,
    AdditionalCapabilities,
    AdditionalUnattendContent,
    ApiEntityReference,
    ApiError,
    ApiErrorBase,
    AutomaticOSUpgradePolicy,
    AutomaticOSUpgradeProperties,
    AutomaticRepairsPolicy,
    AvailabilitySet,
    AvailabilitySetListResult,
    AvailabilitySetUpdate,
    BillingProfile,
    BootDiagnostics,
    BootDiagnosticsInstanceView,
    ComputeOperationListResult,
    ComputeOperationValue,
    CreationData,
    DataDisk,
    DataDiskImage,
    DedicatedHost,
    DedicatedHostAllocatableVM,
    DedicatedHostAvailableCapacity,
    DedicatedHostGroup,
    DedicatedHostGroupListResult,
    DedicatedHostGroupUpdate,
    DedicatedHostInstanceView,
    DedicatedHostListResult,
    DedicatedHostUpdate,
    DiagnosticsProfile,
    DiffDiskSettings,
    Disallowed,
    Disk,
    DiskEncryptionSet,
    DiskEncryptionSetList,
    DiskEncryptionSetParameters,
    DiskEncryptionSetUpdate,
    DiskEncryptionSettings,
    DiskInstanceView,
    DiskList,
    DiskSku,
    DiskUpdate,
    Encryption,
    EncryptionSetIdentity,
    EncryptionSettingsCollection,
    EncryptionSettingsElement,
    Gallery,
    GalleryApplication,
    GalleryApplicationList,
    GalleryApplicationUpdate,
    GalleryApplicationVersion,
    GalleryApplicationVersionList,
    GalleryApplicationVersionPublishingProfile,
    GalleryApplicationVersionUpdate,
    GalleryArtifactPublishingProfileBase,
    GalleryArtifactSource,
    GalleryArtifactVersionSource,
    GalleryDataDiskImage,
    GalleryDiskImage,
    GalleryIdentifier,
    GalleryImage,
    GalleryImageIdentifier,
    GalleryImageList,
    GalleryImageUpdate,
    GalleryImageVersion,
    GalleryImageVersionList,
    GalleryImageVersionPublishingProfile,
    GalleryImageVersionStorageProfile,
    GalleryImageVersionUpdate,
    GalleryList,
    GalleryOSDiskImage,
    GalleryUpdate,
    GrantAccessData,
    HardwareProfile,
    Image,
    ImageDataDisk,
    ImageDisk,
    ImageDiskReference,
    ImageListResult,
    ImageOSDisk,
    ImagePurchasePlan,
    ImageReference,
    ImageStorageProfile,
    ImageUpdate,
    InnerError,
    InstanceViewStatus,
    KeyVaultAndKeyReference,
    KeyVaultAndSecretReference,
    KeyVaultKeyReference,
    KeyVaultSecretReference,
    LinuxConfiguration,
    ListUsagesResult,
    LogAnalyticsInputBase,
    LogAnalyticsOperationResult,
    LogAnalyticsOutput,
    MaintenanceRedeployStatus,
    ManagedArtifact,
    ManagedDiskParameters,
    NetworkInterfaceReference,
    NetworkProfile,
    OSDisk,
    OSDiskImage,
    OSProfile,
    Plan,
    ProximityPlacementGroup,
    ProximityPlacementGroupListResult,
    ProximityPlacementGroupUpdate,
    PurchasePlan,
    RecommendedMachineConfiguration,
    RecoveryWalkResponse,
    RegionalReplicationStatus,
    ReplicationStatus,
    RequestRateByIntervalInput,
    Resource,
    ResourceRange,
    RollbackStatusInfo,
    RollingUpgradePolicy,
    RollingUpgradeProgressInfo,
    RollingUpgradeRunningStatus,
    RollingUpgradeStatusInfo,
    RunCommandDocument,
    RunCommandDocumentBase,
    RunCommandInput,
    RunCommandInputParameter,
    RunCommandListResult,
    RunCommandParameterDefinition,
    RunCommandResult,
    ScaleInPolicy,
    ScheduledEventsProfile,
    Sku,
    Snapshot,
    SnapshotList,
    SnapshotSku,
    SnapshotUpdate,
    SourceVault,
    SshConfiguration,
    SshPublicKey,
    StorageProfile,
    SubResource,
    SubResourceReadOnly,
    SubResourceWithColocationStatus,
    TargetRegion,
    TerminateNotificationProfile,
    ThrottledRequestsInput,
    UpdateResource,
    UpgradeOperationHistoricalStatusInfo,
    UpgradeOperationHistoricalStatusInfoProperties,
    UpgradeOperationHistoryStatus,
    UpgradePolicy,
    Usage,
    UsageName,
    UserArtifactManage,
    UserArtifactSource,
    UserAssignedIdentitiesValue,
    VMScaleSetConvertToSinglePlacementGroupInput,
    VaultCertificate,
    VaultSecretGroup,
    VirtualHardDisk,
    VirtualMachine,
    VirtualMachineAgentInstanceView,
    VirtualMachineCaptureParameters,
    VirtualMachineCaptureResult,
    VirtualMachineExtension,
    VirtualMachineExtensionHandlerInstanceView,
    VirtualMachineExtensionImage,
    VirtualMachineExtensionInstanceView,
    VirtualMachineExtensionUpdate,
    VirtualMachineExtensionsListResult,
    VirtualMachineHealthStatus,
    VirtualMachineIdentity,
    VirtualMachineImage,
    VirtualMachineImageResource,
    VirtualMachineInstanceView,
    VirtualMachineListResult,
    VirtualMachineReimageParameters,
    VirtualMachineScaleSet,
    VirtualMachineScaleSetDataDisk,
    VirtualMachineScaleSetExtension,
    VirtualMachineScaleSetExtensionListResult,
    VirtualMachineScaleSetExtensionProfile,
    VirtualMachineScaleSetExtensionUpdate,
    VirtualMachineScaleSetIPConfiguration,
    VirtualMachineScaleSetIdentity,
    VirtualMachineScaleSetIdentityUserAssignedIdentitiesValue,
    VirtualMachineScaleSetInstanceView,
    VirtualMachineScaleSetInstanceViewStatusesSummary,
    VirtualMachineScaleSetIpTag,
    VirtualMachineScaleSetListOSUpgradeHistory,
    VirtualMachineScaleSetListResult,
    VirtualMachineScaleSetListSkusResult,
    VirtualMachineScaleSetListWithLinkResult,
    VirtualMachineScaleSetManagedDiskParameters,
    VirtualMachineScaleSetNetworkConfiguration,
    VirtualMachineScaleSetNetworkConfigurationDnsSettings,
    VirtualMachineScaleSetNetworkProfile,
    VirtualMachineScaleSetOSDisk,
    VirtualMachineScaleSetOSProfile,
    VirtualMachineScaleSetPublicIPAddressConfiguration,
    VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettings,
    VirtualMachineScaleSetReimageParameters,
    VirtualMachineScaleSetSku,
    VirtualMachineScaleSetSkuCapacity,
    VirtualMachineScaleSetStorageProfile,
    VirtualMachineScaleSetUpdate,
    VirtualMachineScaleSetUpdateIPConfiguration,
    VirtualMachineScaleSetUpdateNetworkConfiguration,
    VirtualMachineScaleSetUpdateNetworkProfile,
    VirtualMachineScaleSetUpdateOSDisk,
    VirtualMachineScaleSetUpdateOSProfile,
    VirtualMachineScaleSetUpdatePublicIPAddressConfiguration,
    VirtualMachineScaleSetUpdateStorageProfile,
    VirtualMachineScaleSetUpdateVMProfile,
    VirtualMachineScaleSetVM,
    VirtualMachineScaleSetVMExtensionsSummary,
    VirtualMachineScaleSetVMInstanceIDs,
    VirtualMachineScaleSetVMInstanceRequiredIDs,
    VirtualMachineScaleSetVMInstanceView,
    VirtualMachineScaleSetVMListResult,
    VirtualMachineScaleSetVMNetworkProfileConfiguration,
    VirtualMachineScaleSetVMProfile,
    VirtualMachineScaleSetVMProtectionPolicy,
    VirtualMachineScaleSetVMReimageParameters,
    VirtualMachineSize,
    VirtualMachineSizeListResult,
    VirtualMachineStatusCodeCount,
    VirtualMachineUpdate,
    WinRMConfiguration,
    WinRMListener,
    WindowsConfiguration,
)

from ._compute_management_client_enums import (  # type: ignore
    AccessLevel,
    AggregatedReplicationState,
    AvailabilitySetSkuTypes,
    CachingTypes,
    DedicatedHostLicenseTypes,
    DiffDiskOptions,
    DiskCreateOption,
    DiskCreateOptionTypes,
    DiskEncryptionSetIdentityType,
    DiskState,
    DiskStorageAccountTypes,
    EncryptionType,
    GalleryApplicationVersionPropertiesProvisioningState,
    GalleryImagePropertiesProvisioningState,
    GalleryImageVersionPropertiesProvisioningState,
    GalleryPropertiesProvisioningState,
    HostCaching,
    HyperVGeneration,
    HyperVGenerationType,
    HyperVGenerationTypes,
    IPVersion,
    IntervalInMins,
    MaintenanceOperationResultCodeTypes,
    OperatingSystemStateTypes,
    OperatingSystemTypes,
    ProtocolTypes,
    ProximityPlacementGroupType,
    ReplicationState,
    ReplicationStatusTypes,
    ResourceIdentityType,
    RollingUpgradeActionType,
    RollingUpgradeStatusCode,
    SettingNames,
    SnapshotStorageAccountTypes,
    StatusLevelTypes,
    StorageAccountType,
    StorageAccountTypes,
    UpgradeMode,
    UpgradeOperationInvoker,
    UpgradeState,
    VirtualMachineEvictionPolicyTypes,
    VirtualMachinePriorityTypes,
    VirtualMachineScaleSetScaleInRules,
    VirtualMachineScaleSetSkuScaleType,
    VirtualMachineSizeTypes,
)
from ._patch import __all__ as _patch_all
from ._patch import *
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AccessUri",
    "AdditionalCapabilities",
    "AdditionalUnattendContent",
    "ApiEntityReference",
    "ApiError",
    "ApiErrorBase",
    "AutomaticOSUpgradePolicy",
    "AutomaticOSUpgradeProperties",
    "AutomaticRepairsPolicy",
    "AvailabilitySet",
    "AvailabilitySetListResult",
    "AvailabilitySetUpdate",
    "BillingProfile",
    "BootDiagnostics",
    "BootDiagnosticsInstanceView",
    "ComputeOperationListResult",
    "ComputeOperationValue",
    "CreationData",
    "DataDisk",
    "DataDiskImage",
    "DedicatedHost",
    "DedicatedHostAllocatableVM",
    "DedicatedHostAvailableCapacity",
    "DedicatedHostGroup",
    "DedicatedHostGroupListResult",
    "DedicatedHostGroupUpdate",
    "DedicatedHostInstanceView",
    "DedicatedHostListResult",
    "DedicatedHostUpdate",
    "DiagnosticsProfile",
    "DiffDiskSettings",
    "Disallowed",
    "Disk",
    "DiskEncryptionSet",
    "DiskEncryptionSetList",
    "DiskEncryptionSetParameters",
    "DiskEncryptionSetUpdate",
    "DiskEncryptionSettings",
    "DiskInstanceView",
    "DiskList",
    "DiskSku",
    "DiskUpdate",
    "Encryption",
    "EncryptionSetIdentity",
    "EncryptionSettingsCollection",
    "EncryptionSettingsElement",
    "Gallery",
    "GalleryApplication",
    "GalleryApplicationList",
    "GalleryApplicationUpdate",
    "GalleryApplicationVersion",
    "GalleryApplicationVersionList",
    "GalleryApplicationVersionPublishingProfile",
    "GalleryApplicationVersionUpdate",
    "GalleryArtifactPublishingProfileBase",
    "GalleryArtifactSource",
    "GalleryArtifactVersionSource",
    "GalleryDataDiskImage",
    "GalleryDiskImage",
    "GalleryIdentifier",
    "GalleryImage",
    "GalleryImageIdentifier",
    "GalleryImageList",
    "GalleryImageUpdate",
    "GalleryImageVersion",
    "GalleryImageVersionList",
    "GalleryImageVersionPublishingProfile",
    "GalleryImageVersionStorageProfile",
    "GalleryImageVersionUpdate",
    "GalleryList",
    "GalleryOSDiskImage",
    "GalleryUpdate",
    "GrantAccessData",
    "HardwareProfile",
    "Image",
    "ImageDataDisk",
    "ImageDisk",
    "ImageDiskReference",
    "ImageListResult",
    "ImageOSDisk",
    "ImagePurchasePlan",
    "ImageReference",
    "ImageStorageProfile",
    "ImageUpdate",
    "InnerError",
    "InstanceViewStatus",
    "KeyVaultAndKeyReference",
    "KeyVaultAndSecretReference",
    "KeyVaultKeyReference",
    "KeyVaultSecretReference",
    "LinuxConfiguration",
    "ListUsagesResult",
    "LogAnalyticsInputBase",
    "LogAnalyticsOperationResult",
    "LogAnalyticsOutput",
    "MaintenanceRedeployStatus",
    "ManagedArtifact",
    "ManagedDiskParameters",
    "NetworkInterfaceReference",
    "NetworkProfile",
    "OSDisk",
    "OSDiskImage",
    "OSProfile",
    "Plan",
    "ProximityPlacementGroup",
    "ProximityPlacementGroupListResult",
    "ProximityPlacementGroupUpdate",
    "PurchasePlan",
    "RecommendedMachineConfiguration",
    "RecoveryWalkResponse",
    "RegionalReplicationStatus",
    "ReplicationStatus",
    "RequestRateByIntervalInput",
    "Resource",
    "ResourceRange",
    "RollbackStatusInfo",
    "RollingUpgradePolicy",
    "RollingUpgradeProgressInfo",
    "RollingUpgradeRunningStatus",
    "RollingUpgradeStatusInfo",
    "RunCommandDocument",
    "RunCommandDocumentBase",
    "RunCommandInput",
    "RunCommandInputParameter",
    "RunCommandListResult",
    "RunCommandParameterDefinition",
    "RunCommandResult",
    "ScaleInPolicy",
    "ScheduledEventsProfile",
    "Sku",
    "Snapshot",
    "SnapshotList",
    "SnapshotSku",
    "SnapshotUpdate",
    "SourceVault",
    "SshConfiguration",
    "SshPublicKey",
    "StorageProfile",
    "SubResource",
    "SubResourceReadOnly",
    "SubResourceWithColocationStatus",
    "TargetRegion",
    "TerminateNotificationProfile",
    "ThrottledRequestsInput",
    "UpdateResource",
    "UpgradeOperationHistoricalStatusInfo",
    "UpgradeOperationHistoricalStatusInfoProperties",
    "UpgradeOperationHistoryStatus",
    "UpgradePolicy",
    "Usage",
    "UsageName",
    "UserArtifactManage",
    "UserArtifactSource",
    "UserAssignedIdentitiesValue",
    "VMScaleSetConvertToSinglePlacementGroupInput",
    "VaultCertificate",
    "VaultSecretGroup",
    "VirtualHardDisk",
    "VirtualMachine",
    "VirtualMachineAgentInstanceView",
    "VirtualMachineCaptureParameters",
    "VirtualMachineCaptureResult",
    "VirtualMachineExtension",
    "VirtualMachineExtensionHandlerInstanceView",
    "VirtualMachineExtensionImage",
    "VirtualMachineExtensionInstanceView",
    "VirtualMachineExtensionUpdate",
    "VirtualMachineExtensionsListResult",
    "VirtualMachineHealthStatus",
    "VirtualMachineIdentity",
    "VirtualMachineImage",
    "VirtualMachineImageResource",
    "VirtualMachineInstanceView",
    "VirtualMachineListResult",
    "VirtualMachineReimageParameters",
    "VirtualMachineScaleSet",
    "VirtualMachineScaleSetDataDisk",
    "VirtualMachineScaleSetExtension",
    "VirtualMachineScaleSetExtensionListResult",
    "VirtualMachineScaleSetExtensionProfile",
    "VirtualMachineScaleSetExtensionUpdate",
    "VirtualMachineScaleSetIPConfiguration",
    "VirtualMachineScaleSetIdentity",
    "VirtualMachineScaleSetIdentityUserAssignedIdentitiesValue",
    "VirtualMachineScaleSetInstanceView",
    "VirtualMachineScaleSetInstanceViewStatusesSummary",
    "VirtualMachineScaleSetIpTag",
    "VirtualMachineScaleSetListOSUpgradeHistory",
    "VirtualMachineScaleSetListResult",
    "VirtualMachineScaleSetListSkusResult",
    "VirtualMachineScaleSetListWithLinkResult",
    "VirtualMachineScaleSetManagedDiskParameters",
    "VirtualMachineScaleSetNetworkConfiguration",
    "VirtualMachineScaleSetNetworkConfigurationDnsSettings",
    "VirtualMachineScaleSetNetworkProfile",
    "VirtualMachineScaleSetOSDisk",
    "VirtualMachineScaleSetOSProfile",
    "VirtualMachineScaleSetPublicIPAddressConfiguration",
    "VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettings",
    "VirtualMachineScaleSetReimageParameters",
    "VirtualMachineScaleSetSku",
    "VirtualMachineScaleSetSkuCapacity",
    "VirtualMachineScaleSetStorageProfile",
    "VirtualMachineScaleSetUpdate",
    "VirtualMachineScaleSetUpdateIPConfiguration",
    "VirtualMachineScaleSetUpdateNetworkConfiguration",
    "VirtualMachineScaleSetUpdateNetworkProfile",
    "VirtualMachineScaleSetUpdateOSDisk",
    "VirtualMachineScaleSetUpdateOSProfile",
    "VirtualMachineScaleSetUpdatePublicIPAddressConfiguration",
    "VirtualMachineScaleSetUpdateStorageProfile",
    "VirtualMachineScaleSetUpdateVMProfile",
    "VirtualMachineScaleSetVM",
    "VirtualMachineScaleSetVMExtensionsSummary",
    "VirtualMachineScaleSetVMInstanceIDs",
    "VirtualMachineScaleSetVMInstanceRequiredIDs",
    "VirtualMachineScaleSetVMInstanceView",
    "VirtualMachineScaleSetVMListResult",
    "VirtualMachineScaleSetVMNetworkProfileConfiguration",
    "VirtualMachineScaleSetVMProfile",
    "VirtualMachineScaleSetVMProtectionPolicy",
    "VirtualMachineScaleSetVMReimageParameters",
    "VirtualMachineSize",
    "VirtualMachineSizeListResult",
    "VirtualMachineStatusCodeCount",
    "VirtualMachineUpdate",
    "WinRMConfiguration",
    "WinRMListener",
    "WindowsConfiguration",
    "AccessLevel",
    "AggregatedReplicationState",
    "AvailabilitySetSkuTypes",
    "CachingTypes",
    "DedicatedHostLicenseTypes",
    "DiffDiskOptions",
    "DiskCreateOption",
    "DiskCreateOptionTypes",
    "DiskEncryptionSetIdentityType",
    "DiskState",
    "DiskStorageAccountTypes",
    "EncryptionType",
    "GalleryApplicationVersionPropertiesProvisioningState",
    "GalleryImagePropertiesProvisioningState",
    "GalleryImageVersionPropertiesProvisioningState",
    "GalleryPropertiesProvisioningState",
    "HostCaching",
    "HyperVGeneration",
    "HyperVGenerationType",
    "HyperVGenerationTypes",
    "IPVersion",
    "IntervalInMins",
    "MaintenanceOperationResultCodeTypes",
    "OperatingSystemStateTypes",
    "OperatingSystemTypes",
    "ProtocolTypes",
    "ProximityPlacementGroupType",
    "ReplicationState",
    "ReplicationStatusTypes",
    "ResourceIdentityType",
    "RollingUpgradeActionType",
    "RollingUpgradeStatusCode",
    "SettingNames",
    "SnapshotStorageAccountTypes",
    "StatusLevelTypes",
    "StorageAccountType",
    "StorageAccountTypes",
    "UpgradeMode",
    "UpgradeOperationInvoker",
    "UpgradeState",
    "VirtualMachineEvictionPolicyTypes",
    "VirtualMachinePriorityTypes",
    "VirtualMachineScaleSetScaleInRules",
    "VirtualMachineScaleSetSkuScaleType",
    "VirtualMachineSizeTypes",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
