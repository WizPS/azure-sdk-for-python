# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

import asyncio
import logging
import os
import time
from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional, Union

from azure.core.credentials import TokenCredential
from azure.identity import DefaultAzureCredential, ManagedIdentityCredential

AZURE_TOKEN_REFRESH_INTERVAL = 600  # seconds


class TokenScope(Enum):
    """Token scopes for Azure endpoints"""

    DEFAULT_AZURE_MANAGEMENT = "https://management.azure.com/.default"


class APITokenManager(ABC):
    """Base class for managing API tokens. Subclasses should implement the get_token method.

    :param logger: Logger object
    :type logger: logging.Logger
    :param auth_header: Authorization header prefix. Defaults to "Bearer"
    :type auth_header: str
    :param credential: Azure credential object
    :type credential: Optional[TokenCredential]
    """

    def __init__(
        self,
        logger: logging.Logger,
        auth_header: str = "Bearer",
        credential: Optional[TokenCredential] = None,
    ) -> None:
        self.logger = logger
        self.auth_header = auth_header
        self._lock: Optional[asyncio.Lock] = None
        if credential is not None:
            self.credential = credential
        else:
            self.credential = self.get_aad_credential()
        self.token: Optional[str] = None
        self.last_refresh_time: Optional[float] = None

    @property
    def lock(self) -> asyncio.Lock:
        """Return object for managing concurrent access to the token.

        If the lock object does not exist, it will be created first.

        :return: Lock object
        :rtype: asyncio.Lock
        """
        if self._lock is None:
            self._lock = asyncio.Lock()
        return self._lock

    def get_aad_credential(self) -> Union[DefaultAzureCredential, ManagedIdentityCredential]:
        """Return the AAD credential object.

        If the environment variable DEFAULT_IDENTITY_CLIENT_ID is set, ManagedIdentityCredential will be used with
        the specified client ID. Otherwise, DefaultAzureCredential will be used.

        :return: The AAD credential object
        :rtype: Union[DefaultAzureCredential, ManagedIdentityCredential]
        """
        identity_client_id = os.environ.get("DEFAULT_IDENTITY_CLIENT_ID", None)
        if identity_client_id is not None:
            self.logger.info(f"Using DEFAULT_IDENTITY_CLIENT_ID: {identity_client_id}")
            return ManagedIdentityCredential(client_id=identity_client_id)

        self.logger.info("Environment variable DEFAULT_IDENTITY_CLIENT_ID is not set, using DefaultAzureCredential")
        return DefaultAzureCredential()

    @abstractmethod
    def get_token(self) -> str:
        """Async method to get the API token. Subclasses should implement this method.

        :return: API token
        :rtype: str
        """


class ManagedIdentityAPITokenManager(APITokenManager):
    """API Token Manager for Azure Managed Identity

    :param token_scope: Token scope for Azure endpoint
    :type token_scope: ~azure.ai.evaluation.simulator._model_tools.TokenScope
    :param logger: Logger object
    :type logger: logging.Logger
    :keyword kwargs: Additional keyword arguments
    :paramtype kwargs: Dict
    """

    def __init__(
        self,
        token_scope: TokenScope,
        logger: logging.Logger,
        *,
        auth_header: str = "Bearer",
        credential: Optional[TokenCredential] = None,
    ):
        super().__init__(logger, auth_header=auth_header, credential=credential)
        self.token_scope = token_scope

    def get_token(self) -> str:
        """Get the API token. If the token is not available or has expired, refresh the token.

        :return: API token
        :rtype: str
        """
        if (
            self.token is None
            or self.last_refresh_time is None
            or time.time() - self.last_refresh_time > AZURE_TOKEN_REFRESH_INTERVAL
        ):
            self.last_refresh_time = time.time()
            self.token = self.credential.get_token(self.token_scope.value).token
            self.logger.info("Refreshed Azure endpoint token.")

        return self.token


class PlainTokenManager(APITokenManager):
    """Plain API Token Manager

    :param openapi_key: OpenAPI key
    :type openapi_key: str
    :param logger: Logger object
    :type logger: logging.Logger
    :keyword kwargs: Optional keyword arguments
    :paramtype kwargs: Dict
    """

    def __init__(
        self,
        openapi_key: str,
        logger: logging.Logger,
        *,
        auth_header: str = "Bearer",
        credential: Optional[TokenCredential] = None,
    ) -> None:
        super().__init__(logger, auth_header=auth_header, credential=credential)
        self.token: str = openapi_key

    def get_token(self) -> str:
        """Get the API token

        :return: API token
        :rtype: str
        """
        return self.token
