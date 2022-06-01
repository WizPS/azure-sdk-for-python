# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from abc import ABC
from typing import TYPE_CHECKING

from ._configuration import MetricsAdvisorClientConfiguration

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from msrest import Deserializer, Serializer

    from azure.core import PipelineClient


def _format_url_section(template, **kwargs):
    components = template.split("/")
    while components:
        try:
            return template.format(**kwargs)
        except KeyError as key:
            formatted_components = template.split("/")
            components = [c for c in formatted_components if "{}".format(key.args[0]) not in c]
            template = "/".join(components)


class MixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "PipelineClient"
    _config: MetricsAdvisorClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"
