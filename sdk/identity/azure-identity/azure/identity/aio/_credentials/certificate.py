# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
from typing import Optional, Any

from azure.core.credentials import AccessTokenInfo
from .._internal import AadClient, AsyncContextManager
from .._internal.get_token_mixin import GetTokenMixin
from ..._credentials.certificate import get_client_credential
from ..._internal import AadClientCertificate, validate_tenant_id


class CertificateCredential(AsyncContextManager, GetTokenMixin):
    """Authenticates as a service principal using a certificate.

    The certificate must have an RSA private key, because this credential signs assertions using RS256. See
    `Microsoft Entra ID documentation
    <https://learn.microsoft.com/entra/identity-platform/certificate-credentials#register-your-certificate-with-microsoft-identity-platform>`__
    for more information on configuring certificate authentication.

    :param str tenant_id: ID of the service principal's tenant. Also called its 'directory' ID.
    :param str client_id: The service principal's client ID
    :param str certificate_path: Path to a PEM-encoded certificate file including the private key. If not provided,
          `certificate_data` is required.

    :keyword str authority: Authority of a Microsoft Entra endpoint, for example 'login.microsoftonline.com',
          the authority for Azure Public Cloud (which is the default). :class:`~azure.identity.AzureAuthorityHosts`
          defines authorities for other clouds.
    :keyword bytes certificate_data: The bytes of a certificate in PEM format, including the private key
    :keyword password: The certificate's password. If a unicode string, it will be encoded as UTF-8. If the certificate
          requires a different encoding, pass appropriately encoded bytes instead.
    :paramtype password: str or bytes
    :keyword cache_persistence_options: Configuration for persistent token caching. If unspecified, the credential
          will cache tokens in memory.
    :paramtype cache_persistence_options: ~azure.identity.TokenCachePersistenceOptions
    :keyword List[str] additionally_allowed_tenants: Specifies tenants in addition to the specified "tenant_id"
        for which the credential may acquire tokens. Add the wildcard value "*" to allow the credential to
        acquire tokens for any tenant the application can access.

    .. admonition:: Example:

        .. literalinclude:: ../samples/credential_creation_code_snippets.py
            :start-after: [START create_certificate_credential_async]
            :end-before: [END create_certificate_credential_async]
            :language: python
            :dedent: 4
            :caption: Create a CertificateCredential.
    """

    def __init__(self, tenant_id: str, client_id: str, certificate_path: Optional[str] = None, **kwargs: Any) -> None:
        validate_tenant_id(tenant_id)

        client_credential = get_client_credential(certificate_path, **kwargs)

        self._certificate = AadClientCertificate(
            client_credential["private_key"], password=client_credential.get("passphrase")
        )

        self._client = AadClient(tenant_id, client_id, **kwargs)
        self._client_id = client_id
        super().__init__()

    async def __aenter__(self) -> "CertificateCredential":
        await self._client.__aenter__()
        return self

    async def close(self) -> None:
        """Close the credential's transport session."""

        await self._client.__aexit__()

    async def _acquire_token_silently(self, *scopes: str, **kwargs: Any) -> Optional[AccessTokenInfo]:
        return self._client.get_cached_access_token(scopes, **kwargs)

    async def _request_token(self, *scopes: str, **kwargs: Any) -> AccessTokenInfo:
        return await self._client.obtain_token_by_client_certificate(scopes, self._certificate, **kwargs)
