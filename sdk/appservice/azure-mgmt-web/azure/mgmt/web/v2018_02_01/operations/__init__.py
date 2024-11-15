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

from ._app_service_certificate_orders_operations import AppServiceCertificateOrdersOperations  # type: ignore
from ._certificate_registration_provider_operations import CertificateRegistrationProviderOperations  # type: ignore
from ._domains_operations import DomainsOperations  # type: ignore
from ._top_level_domains_operations import TopLevelDomainsOperations  # type: ignore
from ._domain_registration_provider_operations import DomainRegistrationProviderOperations  # type: ignore
from ._certificates_operations import CertificatesOperations  # type: ignore
from ._deleted_web_apps_operations import DeletedWebAppsOperations  # type: ignore
from ._diagnostics_operations import DiagnosticsOperations  # type: ignore
from ._provider_operations import ProviderOperations  # type: ignore
from ._recommendations_operations import RecommendationsOperations  # type: ignore
from ._web_site_management_client_operations import WebSiteManagementClientOperationsMixin  # type: ignore
from ._web_apps_operations import WebAppsOperations  # type: ignore
from ._app_service_environments_operations import AppServiceEnvironmentsOperations  # type: ignore
from ._app_service_plans_operations import AppServicePlansOperations  # type: ignore
from ._resource_health_metadata_operations import ResourceHealthMetadataOperations  # type: ignore

from ._patch import __all__ as _patch_all
from ._patch import *
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AppServiceCertificateOrdersOperations",
    "CertificateRegistrationProviderOperations",
    "DomainsOperations",
    "TopLevelDomainsOperations",
    "DomainRegistrationProviderOperations",
    "CertificatesOperations",
    "DeletedWebAppsOperations",
    "DiagnosticsOperations",
    "ProviderOperations",
    "RecommendationsOperations",
    "WebSiteManagementClientOperationsMixin",
    "WebAppsOperations",
    "AppServiceEnvironmentsOperations",
    "AppServicePlansOperations",
    "ResourceHealthMetadataOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
