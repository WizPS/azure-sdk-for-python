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

from ._operations import DisksOperations  # type: ignore
from ._operations import SnapshotsOperations  # type: ignore
from ._operations import DiskEncryptionSetsOperations  # type: ignore
from ._operations import DiskAccessesOperations  # type: ignore
from ._operations import DiskRestorePointOperations  # type: ignore
from ._operations import GalleriesOperations  # type: ignore
from ._operations import GalleryImagesOperations  # type: ignore
from ._operations import GalleryImageVersionsOperations  # type: ignore
from ._operations import GalleryApplicationsOperations  # type: ignore
from ._operations import GalleryApplicationVersionsOperations  # type: ignore
from ._operations import GallerySharingProfileOperations  # type: ignore
from ._operations import SharedGalleriesOperations  # type: ignore
from ._operations import SharedGalleryImagesOperations  # type: ignore
from ._operations import SharedGalleryImageVersionsOperations  # type: ignore

from ._patch import __all__ as _patch_all
from ._patch import *
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "DisksOperations",
    "SnapshotsOperations",
    "DiskEncryptionSetsOperations",
    "DiskAccessesOperations",
    "DiskRestorePointOperations",
    "GalleriesOperations",
    "GalleryImagesOperations",
    "GalleryImageVersionsOperations",
    "GalleryApplicationsOperations",
    "GalleryApplicationVersionsOperations",
    "GallerySharingProfileOperations",
    "SharedGalleriesOperations",
    "SharedGalleryImagesOperations",
    "SharedGalleryImageVersionsOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
