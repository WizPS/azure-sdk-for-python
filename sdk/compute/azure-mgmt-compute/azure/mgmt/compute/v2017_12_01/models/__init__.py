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
    AdditionalUnattendContent,
    ApiEntityReference,
    ApiError,
    ApiErrorBase,
    AutoOSUpgradePolicy,
    AvailabilitySet,
    AvailabilitySetListResult,
    AvailabilitySetUpdate,
    BootDiagnostics,
    BootDiagnosticsInstanceView,
    ComputeLongRunningOperationProperties,
    ComputeOperationListResult,
    ComputeOperationValue,
    DataDisk,
    DataDiskImage,
    DiagnosticsProfile,
    DiskEncryptionSettings,
    DiskInstanceView,
    HardwareProfile,
    Image,
    ImageDataDisk,
    ImageListResult,
    ImageOSDisk,
    ImageReference,
    ImageStorageProfile,
    ImageUpdate,
    InnerError,
    InstanceViewStatus,
    KeyVaultKeyReference,
    KeyVaultSecretReference,
    LinuxConfiguration,
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
    OSProfile,
    OperationStatusResponse,
    Plan,
    PurchasePlan,
    RecoveryWalkResponse,
    RequestRateByIntervalInput,
    Resource,
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
    Sku,
    SshConfiguration,
    SshPublicKey,
    StorageProfile,
    SubResource,
    SubResourceReadOnly,
    ThrottledRequestsInput,
    UpdateResource,
    UpgradeOperationHistoricalStatusInfo,
    UpgradeOperationHistoricalStatusInfoProperties,
    UpgradeOperationHistoryStatus,
    UpgradePolicy,
    Usage,
    UsageName,
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
    VirtualMachineScaleSet,
    VirtualMachineScaleSetDataDisk,
    VirtualMachineScaleSetExtension,
    VirtualMachineScaleSetExtensionListResult,
    VirtualMachineScaleSetExtensionProfile,
    VirtualMachineScaleSetIPConfiguration,
    VirtualMachineScaleSetIdentity,
    VirtualMachineScaleSetInstanceView,
    VirtualMachineScaleSetInstanceViewStatusesSummary,
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
    VirtualMachineScaleSetVMProfile,
    VirtualMachineSize,
    VirtualMachineSizeListResult,
    VirtualMachineStatusCodeCount,
    VirtualMachineUpdate,
    WinRMConfiguration,
    WinRMListener,
    WindowsConfiguration,
)

from ._compute_management_client_enums import (  # type: ignore
    CachingTypes,
    DiskCreateOptionTypes,
    IPVersion,
    IntervalInMins,
    MaintenanceOperationResultCodeTypes,
    OperatingSystemStateTypes,
    OperatingSystemTypes,
    ProtocolTypes,
    ResourceIdentityType,
    RollingUpgradeActionType,
    RollingUpgradeStatusCode,
    SettingNames,
    StatusLevelTypes,
    StorageAccountTypes,
    UpgradeMode,
    UpgradeOperationInvoker,
    UpgradeState,
    VirtualMachineEvictionPolicyTypes,
    VirtualMachinePriorityTypes,
    VirtualMachineScaleSetSkuScaleType,
    VirtualMachineSizeTypes,
)
from ._patch import __all__ as _patch_all
from ._patch import *
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AdditionalUnattendContent",
    "ApiEntityReference",
    "ApiError",
    "ApiErrorBase",
    "AutoOSUpgradePolicy",
    "AvailabilitySet",
    "AvailabilitySetListResult",
    "AvailabilitySetUpdate",
    "BootDiagnostics",
    "BootDiagnosticsInstanceView",
    "ComputeLongRunningOperationProperties",
    "ComputeOperationListResult",
    "ComputeOperationValue",
    "DataDisk",
    "DataDiskImage",
    "DiagnosticsProfile",
    "DiskEncryptionSettings",
    "DiskInstanceView",
    "HardwareProfile",
    "Image",
    "ImageDataDisk",
    "ImageListResult",
    "ImageOSDisk",
    "ImageReference",
    "ImageStorageProfile",
    "ImageUpdate",
    "InnerError",
    "InstanceViewStatus",
    "KeyVaultKeyReference",
    "KeyVaultSecretReference",
    "LinuxConfiguration",
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
    "OSProfile",
    "OperationStatusResponse",
    "Plan",
    "PurchasePlan",
    "RecoveryWalkResponse",
    "RequestRateByIntervalInput",
    "Resource",
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
    "Sku",
    "SshConfiguration",
    "SshPublicKey",
    "StorageProfile",
    "SubResource",
    "SubResourceReadOnly",
    "ThrottledRequestsInput",
    "UpdateResource",
    "UpgradeOperationHistoricalStatusInfo",
    "UpgradeOperationHistoricalStatusInfoProperties",
    "UpgradeOperationHistoryStatus",
    "UpgradePolicy",
    "Usage",
    "UsageName",
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
    "VirtualMachineScaleSet",
    "VirtualMachineScaleSetDataDisk",
    "VirtualMachineScaleSetExtension",
    "VirtualMachineScaleSetExtensionListResult",
    "VirtualMachineScaleSetExtensionProfile",
    "VirtualMachineScaleSetIPConfiguration",
    "VirtualMachineScaleSetIdentity",
    "VirtualMachineScaleSetInstanceView",
    "VirtualMachineScaleSetInstanceViewStatusesSummary",
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
    "VirtualMachineScaleSetVMProfile",
    "VirtualMachineSize",
    "VirtualMachineSizeListResult",
    "VirtualMachineStatusCodeCount",
    "VirtualMachineUpdate",
    "WinRMConfiguration",
    "WinRMListener",
    "WindowsConfiguration",
    "CachingTypes",
    "DiskCreateOptionTypes",
    "IPVersion",
    "IntervalInMins",
    "MaintenanceOperationResultCodeTypes",
    "OperatingSystemStateTypes",
    "OperatingSystemTypes",
    "ProtocolTypes",
    "ResourceIdentityType",
    "RollingUpgradeActionType",
    "RollingUpgradeStatusCode",
    "SettingNames",
    "StatusLevelTypes",
    "StorageAccountTypes",
    "UpgradeMode",
    "UpgradeOperationInvoker",
    "UpgradeState",
    "VirtualMachineEvictionPolicyTypes",
    "VirtualMachinePriorityTypes",
    "VirtualMachineScaleSetSkuScaleType",
    "VirtualMachineSizeTypes",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
