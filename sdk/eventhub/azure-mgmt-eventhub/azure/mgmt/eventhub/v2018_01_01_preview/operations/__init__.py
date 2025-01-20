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

from ._clusters_operations import ClustersOperations  # type: ignore
from ._namespaces_operations import NamespacesOperations  # type: ignore
from ._private_endpoint_connections_operations import PrivateEndpointConnectionsOperations  # type: ignore
from ._private_link_resources_operations import PrivateLinkResourcesOperations  # type: ignore
from ._configuration_operations import ConfigurationOperations  # type: ignore
from ._disaster_recovery_configs_operations import DisasterRecoveryConfigsOperations  # type: ignore
from ._event_hubs_operations import EventHubsOperations  # type: ignore
from ._consumer_groups_operations import ConsumerGroupsOperations  # type: ignore
from ._operations import Operations  # type: ignore
from ._regions_operations import RegionsOperations  # type: ignore

from ._patch import __all__ as _patch_all
from ._patch import *
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ClustersOperations",
    "NamespacesOperations",
    "PrivateEndpointConnectionsOperations",
    "PrivateLinkResourcesOperations",
    "ConfigurationOperations",
    "DisasterRecoveryConfigsOperations",
    "EventHubsOperations",
    "ConsumerGroupsOperations",
    "Operations",
    "RegionsOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
