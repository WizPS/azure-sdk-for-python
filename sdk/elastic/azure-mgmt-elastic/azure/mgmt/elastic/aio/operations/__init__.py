# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._operations import Operations
from ._monitors_operations import MonitorsOperations
from ._elastic_versions_operations import ElasticVersionsOperations
from ._monitored_subscriptions_operations import MonitoredSubscriptionsOperations
from ._monitored_resources_operations import MonitoredResourcesOperations
from ._deployment_info_operations import DeploymentInfoOperations
from ._external_user_operations import ExternalUserOperations
from ._billing_info_operations import BillingInfoOperations
from ._connected_partner_resources_operations import ConnectedPartnerResourcesOperations
from ._open_ai_operations import OpenAIOperations
from ._tag_rules_operations import TagRulesOperations
from ._vm_host_operations import VMHostOperations
from ._vm_ingestion_operations import VMIngestionOperations
from ._vm_collection_operations import VMCollectionOperations
from ._upgradable_versions_operations import UpgradableVersionsOperations
from ._monitor_operations import MonitorOperations
from ._all_traffic_filters_operations import AllTrafficFiltersOperations
from ._list_associated_traffic_filters_operations import ListAssociatedTrafficFiltersOperations
from ._create_and_associate_ip_filter_operations import CreateAndAssociateIPFilterOperations
from ._create_and_associate_pl_filter_operations import CreateAndAssociatePLFilterOperations
from ._associate_traffic_filter_operations import AssociateTrafficFilterOperations
from ._detach_and_delete_traffic_filter_operations import DetachAndDeleteTrafficFilterOperations
from ._detach_traffic_filter_operations import DetachTrafficFilterOperations
from ._traffic_filters_operations import TrafficFiltersOperations
from ._organizations_operations import OrganizationsOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "Operations",
    "MonitorsOperations",
    "ElasticVersionsOperations",
    "MonitoredSubscriptionsOperations",
    "MonitoredResourcesOperations",
    "DeploymentInfoOperations",
    "ExternalUserOperations",
    "BillingInfoOperations",
    "ConnectedPartnerResourcesOperations",
    "OpenAIOperations",
    "TagRulesOperations",
    "VMHostOperations",
    "VMIngestionOperations",
    "VMCollectionOperations",
    "UpgradableVersionsOperations",
    "MonitorOperations",
    "AllTrafficFiltersOperations",
    "ListAssociatedTrafficFiltersOperations",
    "CreateAndAssociateIPFilterOperations",
    "CreateAndAssociatePLFilterOperations",
    "AssociateTrafficFilterOperations",
    "DetachAndDeleteTrafficFilterOperations",
    "DetachTrafficFilterOperations",
    "TrafficFiltersOperations",
    "OrganizationsOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
