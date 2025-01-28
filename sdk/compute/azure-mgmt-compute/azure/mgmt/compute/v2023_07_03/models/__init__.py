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
    ApiError,
    ApiErrorBase,
    CommunityGallery,
    CommunityGalleryImage,
    CommunityGalleryImageIdentifier,
    CommunityGalleryImageList,
    CommunityGalleryImageVersion,
    CommunityGalleryImageVersionList,
    CommunityGalleryInfo,
    CommunityGalleryMetadata,
    DataDiskImageEncryption,
    Disallowed,
    DiskImageEncryption,
    EncryptionImages,
    ExtendedLocation,
    Gallery,
    GalleryApplication,
    GalleryApplicationCustomAction,
    GalleryApplicationCustomActionParameter,
    GalleryApplicationList,
    GalleryApplicationUpdate,
    GalleryApplicationVersion,
    GalleryApplicationVersionList,
    GalleryApplicationVersionPublishingProfile,
    GalleryApplicationVersionSafetyProfile,
    GalleryApplicationVersionUpdate,
    GalleryArtifactPublishingProfileBase,
    GalleryArtifactSafetyProfileBase,
    GalleryArtifactSource,
    GalleryArtifactVersionFullSource,
    GalleryArtifactVersionSource,
    GalleryDataDiskImage,
    GalleryDiskImage,
    GalleryDiskImageSource,
    GalleryExtendedLocation,
    GalleryIdentifier,
    GalleryImage,
    GalleryImageFeature,
    GalleryImageIdentifier,
    GalleryImageList,
    GalleryImageUpdate,
    GalleryImageVersion,
    GalleryImageVersionList,
    GalleryImageVersionPublishingProfile,
    GalleryImageVersionSafetyProfile,
    GalleryImageVersionStorageProfile,
    GalleryImageVersionUefiSettings,
    GalleryImageVersionUpdate,
    GalleryList,
    GalleryOSDiskImage,
    GalleryTargetExtendedLocation,
    GalleryUpdate,
    ImagePurchasePlan,
    ImageVersionSecurityProfile,
    InnerError,
    LatestGalleryImageVersion,
    ManagedArtifact,
    OSDiskImageEncryption,
    OSDiskImageSecurityProfile,
    PirCommunityGalleryResource,
    PirResource,
    PirSharedGalleryResource,
    PolicyViolation,
    RecommendedMachineConfiguration,
    RegionalReplicationStatus,
    RegionalSharingStatus,
    ReplicationStatus,
    Resource,
    ResourceRange,
    ResourceWithOptionalLocation,
    SharedGallery,
    SharedGalleryDataDiskImage,
    SharedGalleryDiskImage,
    SharedGalleryImage,
    SharedGalleryImageList,
    SharedGalleryImageVersion,
    SharedGalleryImageVersionList,
    SharedGalleryImageVersionStorageProfile,
    SharedGalleryList,
    SharedGalleryOSDiskImage,
    SharingProfile,
    SharingProfileGroup,
    SharingStatus,
    SharingUpdate,
    SoftDeletePolicy,
    SubResource,
    SubResourceReadOnly,
    SystemData,
    TargetRegion,
    UefiKey,
    UefiKeySignatures,
    UpdateResourceDefinition,
    UserArtifactManage,
    UserArtifactSettings,
    UserArtifactSource,
    UserAssignedIdentitiesValue,
)

from ._compute_management_client_enums import (  # type: ignore
    AggregatedReplicationState,
    Architecture,
    ConfidentialVMEncryptionType,
    EdgeZoneStorageAccountType,
    ExtendedLocationTypes,
    GalleryApplicationCustomActionParameterType,
    GalleryExpandParams,
    GalleryExtendedLocationType,
    GalleryProvisioningState,
    GallerySharingPermissionTypes,
    HostCaching,
    HyperVGeneration,
    OperatingSystemStateTypes,
    OperatingSystemTypes,
    PolicyViolationCategory,
    ReplicationMode,
    ReplicationState,
    ReplicationStatusTypes,
    SelectPermissions,
    SharedGalleryHostCaching,
    SharedToValues,
    SharingProfileGroupTypes,
    SharingState,
    SharingUpdateOperationTypes,
    StorageAccountType,
    UefiKeyType,
    UefiSignatureTemplateName,
)
from ._patch import __all__ as _patch_all
from ._patch import *
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ApiError",
    "ApiErrorBase",
    "CommunityGallery",
    "CommunityGalleryImage",
    "CommunityGalleryImageIdentifier",
    "CommunityGalleryImageList",
    "CommunityGalleryImageVersion",
    "CommunityGalleryImageVersionList",
    "CommunityGalleryInfo",
    "CommunityGalleryMetadata",
    "DataDiskImageEncryption",
    "Disallowed",
    "DiskImageEncryption",
    "EncryptionImages",
    "ExtendedLocation",
    "Gallery",
    "GalleryApplication",
    "GalleryApplicationCustomAction",
    "GalleryApplicationCustomActionParameter",
    "GalleryApplicationList",
    "GalleryApplicationUpdate",
    "GalleryApplicationVersion",
    "GalleryApplicationVersionList",
    "GalleryApplicationVersionPublishingProfile",
    "GalleryApplicationVersionSafetyProfile",
    "GalleryApplicationVersionUpdate",
    "GalleryArtifactPublishingProfileBase",
    "GalleryArtifactSafetyProfileBase",
    "GalleryArtifactSource",
    "GalleryArtifactVersionFullSource",
    "GalleryArtifactVersionSource",
    "GalleryDataDiskImage",
    "GalleryDiskImage",
    "GalleryDiskImageSource",
    "GalleryExtendedLocation",
    "GalleryIdentifier",
    "GalleryImage",
    "GalleryImageFeature",
    "GalleryImageIdentifier",
    "GalleryImageList",
    "GalleryImageUpdate",
    "GalleryImageVersion",
    "GalleryImageVersionList",
    "GalleryImageVersionPublishingProfile",
    "GalleryImageVersionSafetyProfile",
    "GalleryImageVersionStorageProfile",
    "GalleryImageVersionUefiSettings",
    "GalleryImageVersionUpdate",
    "GalleryList",
    "GalleryOSDiskImage",
    "GalleryTargetExtendedLocation",
    "GalleryUpdate",
    "ImagePurchasePlan",
    "ImageVersionSecurityProfile",
    "InnerError",
    "LatestGalleryImageVersion",
    "ManagedArtifact",
    "OSDiskImageEncryption",
    "OSDiskImageSecurityProfile",
    "PirCommunityGalleryResource",
    "PirResource",
    "PirSharedGalleryResource",
    "PolicyViolation",
    "RecommendedMachineConfiguration",
    "RegionalReplicationStatus",
    "RegionalSharingStatus",
    "ReplicationStatus",
    "Resource",
    "ResourceRange",
    "ResourceWithOptionalLocation",
    "SharedGallery",
    "SharedGalleryDataDiskImage",
    "SharedGalleryDiskImage",
    "SharedGalleryImage",
    "SharedGalleryImageList",
    "SharedGalleryImageVersion",
    "SharedGalleryImageVersionList",
    "SharedGalleryImageVersionStorageProfile",
    "SharedGalleryList",
    "SharedGalleryOSDiskImage",
    "SharingProfile",
    "SharingProfileGroup",
    "SharingStatus",
    "SharingUpdate",
    "SoftDeletePolicy",
    "SubResource",
    "SubResourceReadOnly",
    "SystemData",
    "TargetRegion",
    "UefiKey",
    "UefiKeySignatures",
    "UpdateResourceDefinition",
    "UserArtifactManage",
    "UserArtifactSettings",
    "UserArtifactSource",
    "UserAssignedIdentitiesValue",
    "AggregatedReplicationState",
    "Architecture",
    "ConfidentialVMEncryptionType",
    "EdgeZoneStorageAccountType",
    "ExtendedLocationTypes",
    "GalleryApplicationCustomActionParameterType",
    "GalleryExpandParams",
    "GalleryExtendedLocationType",
    "GalleryProvisioningState",
    "GallerySharingPermissionTypes",
    "HostCaching",
    "HyperVGeneration",
    "OperatingSystemStateTypes",
    "OperatingSystemTypes",
    "PolicyViolationCategory",
    "ReplicationMode",
    "ReplicationState",
    "ReplicationStatusTypes",
    "SelectPermissions",
    "SharedGalleryHostCaching",
    "SharedToValues",
    "SharingProfileGroupTypes",
    "SharingState",
    "SharingUpdateOperationTypes",
    "StorageAccountType",
    "UefiKeyType",
    "UefiSignatureTemplateName",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
