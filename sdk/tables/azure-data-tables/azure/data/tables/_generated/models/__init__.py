# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models import AccessPolicy
from ._models import CorsRule
from ._models import GeoReplication
from ._models import Logging
from ._models import Metrics
from ._models import RetentionPolicy
from ._models import SignedIdentifier
from ._models import TableEntityQueryResponse
from ._models import TableProperties
from ._models import TableQueryResponse
from ._models import TableResponse
from ._models import TableResponseProperties
from ._models import TableServiceError
from ._models import TableServiceProperties
from ._models import TableServiceStats

from ._enums import GeoReplicationStatusType
from ._enums import OdataMetadataFormat
from ._enums import ResponseFormat
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AccessPolicy",
    "CorsRule",
    "GeoReplication",
    "Logging",
    "Metrics",
    "RetentionPolicy",
    "SignedIdentifier",
    "TableEntityQueryResponse",
    "TableProperties",
    "TableQueryResponse",
    "TableResponse",
    "TableResponseProperties",
    "TableServiceError",
    "TableServiceProperties",
    "TableServiceStats",
    "GeoReplicationStatusType",
    "OdataMetadataFormat",
    "ResponseFormat",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
