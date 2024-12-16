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
    AdditionalCapabilities,
    AdditionalUnattendContent,
    AlternativeOption,
    ApiEntityReference,
    ApiError,
    ApiErrorBase,
    ApplicationProfile,
    AutomaticOSUpgradePolicy,
    AutomaticOSUpgradeProperties,
    AutomaticRepairsPolicy,
    AvailabilitySet,
    AvailabilitySetListResult,
    AvailabilitySetUpdate,
    AvailablePatchSummary,
    BillingProfile,
    BootDiagnostics,
    BootDiagnosticsInstanceView,
    CapacityReservation,
    CapacityReservationGroup,
    CapacityReservationGroupInstanceView,
    CapacityReservationGroupListResult,
    CapacityReservationGroupUpdate,
    CapacityReservationInstanceView,
    CapacityReservationInstanceViewWithName,
    CapacityReservationListResult,
    CapacityReservationProfile,
    CapacityReservationUpdate,
    CapacityReservationUtilization,
    ComputeOperationListResult,
    ComputeOperationValue,
    DataDisk,
    DataDiskImage,
    DedicatedHost,
    DedicatedHostAllocatableVM,
    DedicatedHostAvailableCapacity,
    DedicatedHostGroup,
    DedicatedHostGroupInstanceView,
    DedicatedHostGroupListResult,
    DedicatedHostGroupPropertiesAdditionalCapabilities,
    DedicatedHostGroupUpdate,
    DedicatedHostInstanceView,
    DedicatedHostInstanceViewWithName,
    DedicatedHostListResult,
    DedicatedHostUpdate,
    DiagnosticsProfile,
    DiffDiskSettings,
    DisallowedConfiguration,
    DiskEncryptionSetParameters,
    DiskEncryptionSettings,
    DiskInstanceView,
    DiskRestorePointInstanceView,
    DiskRestorePointReplicationStatus,
    ExtendedLocation,
    HardwareProfile,
    Image,
    ImageDataDisk,
    ImageDeprecationStatus,
    ImageDisk,
    ImageListResult,
    ImageOSDisk,
    ImageReference,
    ImageStorageProfile,
    ImageUpdate,
    InnerError,
    InstanceViewStatus,
    KeyVaultKeyReference,
    KeyVaultSecretReference,
    LastPatchInstallationSummary,
    LinuxConfiguration,
    LinuxParameters,
    LinuxPatchSettings,
    LinuxVMGuestPatchAutomaticByPlatformSettings,
    ListUsagesResult,
    LogAnalyticsInputBase,
    LogAnalyticsOperationResult,
    LogAnalyticsOutput,
    MaintenanceRedeployStatus,
    ManagedDiskParameters,
    NetworkInterfaceReference,
    NetworkProfile,
    OSDisk,
    OSDiskImage,
    OSImageNotificationProfile,
    OSProfile,
    OSProfileProvisioningData,
    OrchestrationServiceStateInput,
    OrchestrationServiceSummary,
    PatchInstallationDetail,
    PatchSettings,
    Plan,
    PriorityMixPolicy,
    ProximityPlacementGroup,
    ProximityPlacementGroupListResult,
    ProximityPlacementGroupPropertiesIntent,
    ProximityPlacementGroupUpdate,
    ProxyResource,
    PublicIPAddressSku,
    PurchasePlan,
    RecoveryWalkResponse,
    RequestRateByIntervalInput,
    Resource,
    ResourceWithOptionalLocation,
    RestorePoint,
    RestorePointCollection,
    RestorePointCollectionListResult,
    RestorePointCollectionSourceProperties,
    RestorePointCollectionUpdate,
    RestorePointInstanceView,
    RestorePointSourceMetadata,
    RestorePointSourceVMDataDisk,
    RestorePointSourceVMOSDisk,
    RestorePointSourceVMStorageProfile,
    RetrieveBootDiagnosticsDataResult,
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
    SecurityProfile,
    ServiceArtifactReference,
    Sku,
    SpotRestorePolicy,
    SshConfiguration,
    SshPublicKey,
    SshPublicKeyGenerateKeyPairResult,
    SshPublicKeyResource,
    SshPublicKeyUpdateResource,
    SshPublicKeysGroupListResult,
    StorageProfile,
    SubResource,
    SubResourceReadOnly,
    SubResourceWithColocationStatus,
    SystemData,
    TerminateNotificationProfile,
    ThrottledRequestsInput,
    UefiSettings,
    UpdateResource,
    UpgradeOperationHistoricalStatusInfo,
    UpgradeOperationHistoricalStatusInfoProperties,
    UpgradeOperationHistoryStatus,
    UpgradePolicy,
    Usage,
    UsageName,
    UserAssignedIdentitiesValue,
    VMDiskSecurityProfile,
    VMGalleryApplication,
    VMScaleSetConvertToSinglePlacementGroupInput,
    VMSizeProperties,
    VaultCertificate,
    VaultSecretGroup,
    VirtualHardDisk,
    VirtualMachine,
    VirtualMachineAgentInstanceView,
    VirtualMachineAssessPatchesResult,
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
    VirtualMachineImageFeature,
    VirtualMachineImageResource,
    VirtualMachineInstallPatchesParameters,
    VirtualMachineInstallPatchesResult,
    VirtualMachineInstanceView,
    VirtualMachineIpTag,
    VirtualMachineListResult,
    VirtualMachineNetworkInterfaceConfiguration,
    VirtualMachineNetworkInterfaceDnsSettingsConfiguration,
    VirtualMachineNetworkInterfaceIPConfiguration,
    VirtualMachinePatchStatus,
    VirtualMachinePublicIPAddressConfiguration,
    VirtualMachinePublicIPAddressDnsSettingsConfiguration,
    VirtualMachineReimageParameters,
    VirtualMachineRunCommand,
    VirtualMachineRunCommandInstanceView,
    VirtualMachineRunCommandScriptSource,
    VirtualMachineRunCommandUpdate,
    VirtualMachineRunCommandsListResult,
    VirtualMachineScaleSet,
    VirtualMachineScaleSetDataDisk,
    VirtualMachineScaleSetExtension,
    VirtualMachineScaleSetExtensionListResult,
    VirtualMachineScaleSetExtensionProfile,
    VirtualMachineScaleSetExtensionUpdate,
    VirtualMachineScaleSetHardwareProfile,
    VirtualMachineScaleSetIPConfiguration,
    VirtualMachineScaleSetIdentity,
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
    VirtualMachineScaleSetVMExtension,
    VirtualMachineScaleSetVMExtensionUpdate,
    VirtualMachineScaleSetVMExtensionsListResult,
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
    VirtualMachineSoftwarePatchProperties,
    VirtualMachineStatusCodeCount,
    VirtualMachineUpdate,
    VmImagesInEdgeZoneListResult,
    WinRMConfiguration,
    WinRMListener,
    WindowsConfiguration,
    WindowsParameters,
    WindowsVMGuestPatchAutomaticByPlatformSettings,
)

from ._compute_management_client_enums import (  # type: ignore
    AlternativeType,
    ArchitectureTypes,
    AvailabilitySetSkuTypes,
    CachingTypes,
    CapacityReservationGroupInstanceViewTypes,
    CapacityReservationInstanceViewTypes,
    ConsistencyModeTypes,
    DedicatedHostLicenseTypes,
    DeleteOptions,
    DiffDiskOptions,
    DiffDiskPlacement,
    DiskControllerTypes,
    DiskCreateOptionTypes,
    DiskDeleteOptionTypes,
    DiskDetachOptionTypes,
    ExecutionState,
    ExpandTypesForGetCapacityReservationGroups,
    ExpandTypesForGetVMScaleSets,
    ExtendedLocationTypes,
    HyperVGeneration,
    HyperVGenerationType,
    HyperVGenerationTypes,
    IPVersion,
    IPVersions,
    ImageState,
    InstanceViewTypes,
    IntervalInMins,
    LinuxPatchAssessmentMode,
    LinuxVMGuestPatchAutomaticByPlatformRebootSetting,
    LinuxVMGuestPatchMode,
    MaintenanceOperationResultCodeTypes,
    NetworkApiVersion,
    OperatingSystemStateTypes,
    OperatingSystemType,
    OperatingSystemTypes,
    OrchestrationMode,
    OrchestrationServiceNames,
    OrchestrationServiceState,
    OrchestrationServiceStateAction,
    PatchAssessmentState,
    PatchInstallationState,
    PatchOperationStatus,
    ProtocolTypes,
    ProximityPlacementGroupType,
    PublicIPAddressSkuName,
    PublicIPAddressSkuTier,
    PublicIPAllocationMethod,
    RepairAction,
    ResourceIdentityType,
    RestorePointCollectionExpandOptions,
    RestorePointExpandOptions,
    RollingUpgradeActionType,
    RollingUpgradeStatusCode,
    SecurityEncryptionTypes,
    SecurityTypes,
    SettingNames,
    StatusLevelTypes,
    StorageAccountTypes,
    UpgradeMode,
    UpgradeOperationInvoker,
    UpgradeState,
    VMGuestPatchClassificationLinux,
    VMGuestPatchClassificationWindows,
    VMGuestPatchRebootBehavior,
    VMGuestPatchRebootSetting,
    VMGuestPatchRebootStatus,
    VirtualMachineEvictionPolicyTypes,
    VirtualMachinePriorityTypes,
    VirtualMachineScaleSetScaleInRules,
    VirtualMachineScaleSetSkuScaleType,
    VirtualMachineSizeTypes,
    VmDiskTypes,
    WindowsPatchAssessmentMode,
    WindowsVMGuestPatchAutomaticByPlatformRebootSetting,
    WindowsVMGuestPatchMode,
)
from ._patch import __all__ as _patch_all
from ._patch import *
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AdditionalCapabilities",
    "AdditionalUnattendContent",
    "AlternativeOption",
    "ApiEntityReference",
    "ApiError",
    "ApiErrorBase",
    "ApplicationProfile",
    "AutomaticOSUpgradePolicy",
    "AutomaticOSUpgradeProperties",
    "AutomaticRepairsPolicy",
    "AvailabilitySet",
    "AvailabilitySetListResult",
    "AvailabilitySetUpdate",
    "AvailablePatchSummary",
    "BillingProfile",
    "BootDiagnostics",
    "BootDiagnosticsInstanceView",
    "CapacityReservation",
    "CapacityReservationGroup",
    "CapacityReservationGroupInstanceView",
    "CapacityReservationGroupListResult",
    "CapacityReservationGroupUpdate",
    "CapacityReservationInstanceView",
    "CapacityReservationInstanceViewWithName",
    "CapacityReservationListResult",
    "CapacityReservationProfile",
    "CapacityReservationUpdate",
    "CapacityReservationUtilization",
    "ComputeOperationListResult",
    "ComputeOperationValue",
    "DataDisk",
    "DataDiskImage",
    "DedicatedHost",
    "DedicatedHostAllocatableVM",
    "DedicatedHostAvailableCapacity",
    "DedicatedHostGroup",
    "DedicatedHostGroupInstanceView",
    "DedicatedHostGroupListResult",
    "DedicatedHostGroupPropertiesAdditionalCapabilities",
    "DedicatedHostGroupUpdate",
    "DedicatedHostInstanceView",
    "DedicatedHostInstanceViewWithName",
    "DedicatedHostListResult",
    "DedicatedHostUpdate",
    "DiagnosticsProfile",
    "DiffDiskSettings",
    "DisallowedConfiguration",
    "DiskEncryptionSetParameters",
    "DiskEncryptionSettings",
    "DiskInstanceView",
    "DiskRestorePointInstanceView",
    "DiskRestorePointReplicationStatus",
    "ExtendedLocation",
    "HardwareProfile",
    "Image",
    "ImageDataDisk",
    "ImageDeprecationStatus",
    "ImageDisk",
    "ImageListResult",
    "ImageOSDisk",
    "ImageReference",
    "ImageStorageProfile",
    "ImageUpdate",
    "InnerError",
    "InstanceViewStatus",
    "KeyVaultKeyReference",
    "KeyVaultSecretReference",
    "LastPatchInstallationSummary",
    "LinuxConfiguration",
    "LinuxParameters",
    "LinuxPatchSettings",
    "LinuxVMGuestPatchAutomaticByPlatformSettings",
    "ListUsagesResult",
    "LogAnalyticsInputBase",
    "LogAnalyticsOperationResult",
    "LogAnalyticsOutput",
    "MaintenanceRedeployStatus",
    "ManagedDiskParameters",
    "NetworkInterfaceReference",
    "NetworkProfile",
    "OSDisk",
    "OSDiskImage",
    "OSImageNotificationProfile",
    "OSProfile",
    "OSProfileProvisioningData",
    "OrchestrationServiceStateInput",
    "OrchestrationServiceSummary",
    "PatchInstallationDetail",
    "PatchSettings",
    "Plan",
    "PriorityMixPolicy",
    "ProximityPlacementGroup",
    "ProximityPlacementGroupListResult",
    "ProximityPlacementGroupPropertiesIntent",
    "ProximityPlacementGroupUpdate",
    "ProxyResource",
    "PublicIPAddressSku",
    "PurchasePlan",
    "RecoveryWalkResponse",
    "RequestRateByIntervalInput",
    "Resource",
    "ResourceWithOptionalLocation",
    "RestorePoint",
    "RestorePointCollection",
    "RestorePointCollectionListResult",
    "RestorePointCollectionSourceProperties",
    "RestorePointCollectionUpdate",
    "RestorePointInstanceView",
    "RestorePointSourceMetadata",
    "RestorePointSourceVMDataDisk",
    "RestorePointSourceVMOSDisk",
    "RestorePointSourceVMStorageProfile",
    "RetrieveBootDiagnosticsDataResult",
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
    "SecurityProfile",
    "ServiceArtifactReference",
    "Sku",
    "SpotRestorePolicy",
    "SshConfiguration",
    "SshPublicKey",
    "SshPublicKeyGenerateKeyPairResult",
    "SshPublicKeyResource",
    "SshPublicKeyUpdateResource",
    "SshPublicKeysGroupListResult",
    "StorageProfile",
    "SubResource",
    "SubResourceReadOnly",
    "SubResourceWithColocationStatus",
    "SystemData",
    "TerminateNotificationProfile",
    "ThrottledRequestsInput",
    "UefiSettings",
    "UpdateResource",
    "UpgradeOperationHistoricalStatusInfo",
    "UpgradeOperationHistoricalStatusInfoProperties",
    "UpgradeOperationHistoryStatus",
    "UpgradePolicy",
    "Usage",
    "UsageName",
    "UserAssignedIdentitiesValue",
    "VMDiskSecurityProfile",
    "VMGalleryApplication",
    "VMScaleSetConvertToSinglePlacementGroupInput",
    "VMSizeProperties",
    "VaultCertificate",
    "VaultSecretGroup",
    "VirtualHardDisk",
    "VirtualMachine",
    "VirtualMachineAgentInstanceView",
    "VirtualMachineAssessPatchesResult",
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
    "VirtualMachineImageFeature",
    "VirtualMachineImageResource",
    "VirtualMachineInstallPatchesParameters",
    "VirtualMachineInstallPatchesResult",
    "VirtualMachineInstanceView",
    "VirtualMachineIpTag",
    "VirtualMachineListResult",
    "VirtualMachineNetworkInterfaceConfiguration",
    "VirtualMachineNetworkInterfaceDnsSettingsConfiguration",
    "VirtualMachineNetworkInterfaceIPConfiguration",
    "VirtualMachinePatchStatus",
    "VirtualMachinePublicIPAddressConfiguration",
    "VirtualMachinePublicIPAddressDnsSettingsConfiguration",
    "VirtualMachineReimageParameters",
    "VirtualMachineRunCommand",
    "VirtualMachineRunCommandInstanceView",
    "VirtualMachineRunCommandScriptSource",
    "VirtualMachineRunCommandUpdate",
    "VirtualMachineRunCommandsListResult",
    "VirtualMachineScaleSet",
    "VirtualMachineScaleSetDataDisk",
    "VirtualMachineScaleSetExtension",
    "VirtualMachineScaleSetExtensionListResult",
    "VirtualMachineScaleSetExtensionProfile",
    "VirtualMachineScaleSetExtensionUpdate",
    "VirtualMachineScaleSetHardwareProfile",
    "VirtualMachineScaleSetIPConfiguration",
    "VirtualMachineScaleSetIdentity",
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
    "VirtualMachineScaleSetVMExtension",
    "VirtualMachineScaleSetVMExtensionUpdate",
    "VirtualMachineScaleSetVMExtensionsListResult",
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
    "VirtualMachineSoftwarePatchProperties",
    "VirtualMachineStatusCodeCount",
    "VirtualMachineUpdate",
    "VmImagesInEdgeZoneListResult",
    "WinRMConfiguration",
    "WinRMListener",
    "WindowsConfiguration",
    "WindowsParameters",
    "WindowsVMGuestPatchAutomaticByPlatformSettings",
    "AlternativeType",
    "ArchitectureTypes",
    "AvailabilitySetSkuTypes",
    "CachingTypes",
    "CapacityReservationGroupInstanceViewTypes",
    "CapacityReservationInstanceViewTypes",
    "ConsistencyModeTypes",
    "DedicatedHostLicenseTypes",
    "DeleteOptions",
    "DiffDiskOptions",
    "DiffDiskPlacement",
    "DiskControllerTypes",
    "DiskCreateOptionTypes",
    "DiskDeleteOptionTypes",
    "DiskDetachOptionTypes",
    "ExecutionState",
    "ExpandTypesForGetCapacityReservationGroups",
    "ExpandTypesForGetVMScaleSets",
    "ExtendedLocationTypes",
    "HyperVGeneration",
    "HyperVGenerationType",
    "HyperVGenerationTypes",
    "IPVersion",
    "IPVersions",
    "ImageState",
    "InstanceViewTypes",
    "IntervalInMins",
    "LinuxPatchAssessmentMode",
    "LinuxVMGuestPatchAutomaticByPlatformRebootSetting",
    "LinuxVMGuestPatchMode",
    "MaintenanceOperationResultCodeTypes",
    "NetworkApiVersion",
    "OperatingSystemStateTypes",
    "OperatingSystemType",
    "OperatingSystemTypes",
    "OrchestrationMode",
    "OrchestrationServiceNames",
    "OrchestrationServiceState",
    "OrchestrationServiceStateAction",
    "PatchAssessmentState",
    "PatchInstallationState",
    "PatchOperationStatus",
    "ProtocolTypes",
    "ProximityPlacementGroupType",
    "PublicIPAddressSkuName",
    "PublicIPAddressSkuTier",
    "PublicIPAllocationMethod",
    "RepairAction",
    "ResourceIdentityType",
    "RestorePointCollectionExpandOptions",
    "RestorePointExpandOptions",
    "RollingUpgradeActionType",
    "RollingUpgradeStatusCode",
    "SecurityEncryptionTypes",
    "SecurityTypes",
    "SettingNames",
    "StatusLevelTypes",
    "StorageAccountTypes",
    "UpgradeMode",
    "UpgradeOperationInvoker",
    "UpgradeState",
    "VMGuestPatchClassificationLinux",
    "VMGuestPatchClassificationWindows",
    "VMGuestPatchRebootBehavior",
    "VMGuestPatchRebootSetting",
    "VMGuestPatchRebootStatus",
    "VirtualMachineEvictionPolicyTypes",
    "VirtualMachinePriorityTypes",
    "VirtualMachineScaleSetScaleInRules",
    "VirtualMachineScaleSetSkuScaleType",
    "VirtualMachineSizeTypes",
    "VmDiskTypes",
    "WindowsPatchAssessmentMode",
    "WindowsVMGuestPatchAutomaticByPlatformRebootSetting",
    "WindowsVMGuestPatchMode",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
