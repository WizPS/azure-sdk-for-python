# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class CloudServiceUpgradeMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Update mode for the cloud service. Role instances are allocated to update domains when the
    service is deployed. Updates can be initiated manually in each update domain or initiated
    automatically in all update domains.
    Possible Values are :code:`<br />`\\ :code:`<br />`\\ **Auto**\\ :code:`<br />`\\ :code:`<br
    />`\\ **Manual** :code:`<br />`\\ :code:`<br />`\\ **Simultaneous**\\ :code:`<br />`\\
    :code:`<br />`
    If not specified, the default value is Auto. If set to Manual, PUT UpdateDomain must be called
    to apply the update. If set to Auto, the update is automatically applied to each update domain
    in sequence.
    """

    AUTO = "Auto"
    MANUAL = "Manual"
    SIMULTANEOUS = "Simultaneous"


class StatusLevelTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The level code."""

    INFO = "Info"
    WARNING = "Warning"
    ERROR = "Error"
