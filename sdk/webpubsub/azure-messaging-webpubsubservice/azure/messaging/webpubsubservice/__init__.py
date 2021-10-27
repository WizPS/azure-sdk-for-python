# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._web_pub_sub_service_client import WebPubSubServiceClient
from ._version import VERSION

__version__ = VERSION
__all__ = ['WebPubSubServiceClient']

try:
    from ._patch import get_client_access_token
    from ._patch import WebPubSubServiceClient
    __all__ = ['WebPubSubServiceClient', 'get_client_access_token']
except ImportError:
    pass
