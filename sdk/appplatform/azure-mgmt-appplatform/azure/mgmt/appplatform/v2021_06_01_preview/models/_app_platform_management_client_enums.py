# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum. Indicates the action type. "Internal" refers to actions that are for internal only APIs."""

    INTERNAL = "Internal"


class AppResourceProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Provisioning state of the App."""

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CREATING = "Creating"
    UPDATING = "Updating"


class ConfigServerState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """State of the config server."""

    NOT_AVAILABLE = "NotAvailable"
    DELETED = "Deleted"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    UPDATING = "Updating"


class DeploymentResourceProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Provisioning state of the Deployment."""

    CREATING = "Creating"
    UPDATING = "Updating"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"


class DeploymentResourceStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Status of the Deployment."""

    UNKNOWN = "Unknown"
    STOPPED = "Stopped"
    RUNNING = "Running"
    FAILED = "Failed"
    ALLOCATING = "Allocating"
    UPGRADING = "Upgrading"
    COMPILING = "Compiling"


class ManagedIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of the managed identity."""

    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"


class MonitoringSettingState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """State of the Monitoring Setting."""

    NOT_AVAILABLE = "NotAvailable"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    UPDATING = "Updating"


class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Provisioning state of the Service."""

    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    DELETED = "Deleted"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    MOVING = "Moving"
    MOVED = "Moved"
    MOVE_FAILED = "MoveFailed"


class ResourceSkuRestrictionsReasonCode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets the reason for restriction. Possible values include: 'QuotaId',
    'NotAvailableForSubscription'.
    """

    QUOTA_ID = "QuotaId"
    NOT_AVAILABLE_FOR_SUBSCRIPTION = "NotAvailableForSubscription"


class ResourceSkuRestrictionsType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets the type of restrictions. Possible values include: 'Location', 'Zone'."""

    LOCATION = "Location"
    ZONE = "Zone"


class RuntimeVersion(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Runtime version."""

    JAVA8 = "Java_8"
    JAVA11 = "Java_11"
    NET_CORE31 = "NetCore_31"


class SkuScaleType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets or sets the type of the scale."""

    NONE = "None"
    MANUAL = "Manual"
    AUTOMATIC = "Automatic"


class SupportedRuntimePlatform(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The platform of this runtime version (possible values: "Java" or ".NET")."""

    JAVA = "Java"
    _NET_CORE = ".NET Core"


class SupportedRuntimeValue(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The raw value which could be passed to deployment CRUD operations."""

    JAVA8 = "Java_8"
    JAVA11 = "Java_11"
    NET_CORE31 = "NetCore_31"


class TestKeyType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of the test key."""

    PRIMARY = "Primary"
    SECONDARY = "Secondary"


class TrafficDirection(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The direction of required traffic."""

    INBOUND = "Inbound"
    OUTBOUND = "Outbound"


class UserSourceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of the source uploaded."""

    JAR = "Jar"
    NET_CORE_ZIP = "NetCoreZip"
    SOURCE = "Source"
    CONTAINER = "Container"
