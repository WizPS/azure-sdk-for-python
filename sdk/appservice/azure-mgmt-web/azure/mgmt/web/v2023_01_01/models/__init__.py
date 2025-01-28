# pylint: disable=too-many-lines
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


from ._models_py3 import (  # type: ignore
    AbnormalTimePeriod,
    Address,
    AddressResponse,
    AllowedAudiencesValidation,
    AllowedPrincipals,
    AnalysisData,
    AnalysisDefinition,
    ApiDefinitionInfo,
    ApiKVReference,
    ApiKVReferenceCollection,
    ApiManagementConfig,
    AppInsightsWebAppStackSettings,
    AppLogsConfiguration,
    AppRegistration,
    AppServiceCertificate,
    AppServiceCertificateCollection,
    AppServiceCertificateOrder,
    AppServiceCertificateOrderCollection,
    AppServiceCertificateOrderPatchResource,
    AppServiceCertificatePatchResource,
    AppServiceCertificateResource,
    AppServiceEnvironment,
    AppServiceEnvironmentCollection,
    AppServiceEnvironmentPatchResource,
    AppServiceEnvironmentResource,
    AppServicePlan,
    AppServicePlanCollection,
    AppServicePlanPatchResource,
    Apple,
    AppleRegistration,
    ApplicationLogsConfig,
    ApplicationStack,
    ApplicationStackCollection,
    ApplicationStackResource,
    AppserviceGithubToken,
    AppserviceGithubTokenRequest,
    ArcConfiguration,
    ArmIdWrapper,
    ArmPlan,
    AseRegion,
    AseRegionCollection,
    AseV3NetworkingConfiguration,
    AuthPlatform,
    AutoHealActions,
    AutoHealCustomAction,
    AutoHealRules,
    AutoHealTriggers,
    AzureActiveDirectory,
    AzureActiveDirectoryLogin,
    AzureActiveDirectoryRegistration,
    AzureActiveDirectoryValidation,
    AzureBlobStorageApplicationLogsConfig,
    AzureBlobStorageHttpLogsConfig,
    AzureResourceErrorInfo,
    AzureStaticWebApps,
    AzureStaticWebAppsRegistration,
    AzureStorageInfoValue,
    AzureStoragePropertyDictionaryResource,
    AzureTableStorageApplicationLogsConfig,
    BackupItem,
    BackupItemCollection,
    BackupRequest,
    BackupSchedule,
    BillingMeter,
    BillingMeterCollection,
    BlobStorageTokenStore,
    Capability,
    Certificate,
    CertificateCollection,
    CertificateDetails,
    CertificateEmail,
    CertificateOrderAction,
    CertificateOrderContact,
    CertificatePatchResource,
    ClientRegistration,
    CloningInfo,
    Configuration,
    ConnStringInfo,
    ConnStringValueTypePair,
    ConnectionStringDictionary,
    Contact,
    Container,
    ContainerApp,
    ContainerAppCollection,
    ContainerAppSecret,
    ContainerAppsConfiguration,
    ContainerCpuStatistics,
    ContainerCpuUsage,
    ContainerInfo,
    ContainerMemoryStatistics,
    ContainerNetworkInterfaceStatistics,
    ContainerResources,
    ContainerThrottlingData,
    ContentHash,
    ContentLink,
    ContinuousWebJob,
    ContinuousWebJobCollection,
    CookieExpiration,
    Correlation,
    CorsSettings,
    CsmDeploymentStatus,
    CsmDeploymentStatusCollection,
    CsmMoveResourceEnvelope,
    CsmOperationCollection,
    CsmOperationDescription,
    CsmOperationDescriptionProperties,
    CsmOperationDisplay,
    CsmPublishingCredentialsPoliciesEntity,
    CsmPublishingProfileOptions,
    CsmSlotEntity,
    CsmUsageQuota,
    CsmUsageQuotaCollection,
    CustomDnsSuffixConfiguration,
    CustomHostnameAnalysisResult,
    CustomHostnameSites,
    CustomHostnameSitesCollection,
    CustomOpenIdConnectProvider,
    CustomScaleRule,
    Dapr,
    DaprComponent,
    DaprConfig,
    DaprMetadata,
    DataProviderMetadata,
    DataSource,
    DataTableResponseColumn,
    DataTableResponseObject,
    DatabaseBackupSetting,
    DatabaseConnection,
    DatabaseConnectionCollection,
    DatabaseConnectionOverview,
    DatabaseConnectionPatchRequest,
    DefaultAuthorizationPolicy,
    DefaultErrorResponse,
    DefaultErrorResponseError,
    DefaultErrorResponseErrorDetailsItem,
    DeletedAppRestoreRequest,
    DeletedSite,
    DeletedWebAppCollection,
    Deployment,
    DeploymentCollection,
    DeploymentLocations,
    DetectorAbnormalTimePeriod,
    DetectorDefinition,
    DetectorDefinitionResource,
    DetectorInfo,
    DetectorResponse,
    DetectorResponseCollection,
    DiagnosticAnalysis,
    DiagnosticAnalysisCollection,
    DiagnosticCategory,
    DiagnosticCategoryCollection,
    DiagnosticData,
    DiagnosticDetectorCollection,
    DiagnosticDetectorResponse,
    DiagnosticMetricSample,
    DiagnosticMetricSet,
    Dimension,
    Domain,
    DomainAvailabilityCheckResult,
    DomainCollection,
    DomainControlCenterSsoRequest,
    DomainOwnershipIdentifier,
    DomainOwnershipIdentifierCollection,
    DomainPatchResource,
    DomainPurchaseConsent,
    DomainRecommendationSearchParameters,
    EnabledConfig,
    EndpointDependency,
    EndpointDetail,
    EnvironmentVar,
    ErrorEntity,
    ErrorInfo,
    ErrorProperties,
    ErrorResponse,
    Experiments,
    Expression,
    ExpressionRoot,
    ExpressionTraces,
    ExtendedLocation,
    Facebook,
    FileSystemApplicationLogsConfig,
    FileSystemHttpLogsConfig,
    FileSystemTokenStore,
    FlowAccessControlConfiguration,
    FlowAccessControlConfigurationPolicy,
    FlowEndpoints,
    FlowEndpointsConfiguration,
    ForwardProxy,
    FrontEndConfiguration,
    FunctionAppMajorVersion,
    FunctionAppMinorVersion,
    FunctionAppRuntimeSettings,
    FunctionAppRuntimes,
    FunctionAppStack,
    FunctionAppStackCollection,
    FunctionEnvelope,
    FunctionEnvelopeCollection,
    FunctionSecrets,
    GeoRegion,
    GeoRegionCollection,
    GitHub,
    GitHubActionCodeConfiguration,
    GitHubActionConfiguration,
    GitHubActionContainerConfiguration,
    GitHubActionWebAppStackSettings,
    GlobalCsmSkuDescription,
    GlobalValidation,
    Google,
    HandlerMapping,
    HostKeys,
    HostName,
    HostNameBinding,
    HostNameBindingCollection,
    HostNameSslState,
    HostingEnvironmentDeploymentInfo,
    HostingEnvironmentDiagnostics,
    HostingEnvironmentProfile,
    HttpLogsConfig,
    HttpScaleRule,
    HttpSettings,
    HttpSettingsRoutes,
    HybridConnection,
    HybridConnectionCollection,
    HybridConnectionKey,
    HybridConnectionLimits,
    Identifier,
    IdentifierCollection,
    IdentityProviders,
    InboundEnvironmentEndpoint,
    InboundEnvironmentEndpointCollection,
    Ingress,
    IpAddress,
    IpAddressRange,
    IpSecurityRestriction,
    JsonSchema,
    JwtClaimChecks,
    KeyInfo,
    KeyValuePairStringObject,
    KubeEnvironment,
    KubeEnvironmentCollection,
    KubeEnvironmentPatchResource,
    KubeEnvironmentProfile,
    LegacyMicrosoftAccount,
    LinuxJavaContainerSettings,
    LocalizableString,
    LogAnalyticsConfiguration,
    LogSpecification,
    Login,
    LoginRoutes,
    LoginScopes,
    MSDeploy,
    MSDeployLog,
    MSDeployLogEntry,
    MSDeployStatus,
    ManagedServiceIdentity,
    MetricAvailability,
    MetricSpecification,
    MigrateMySqlRequest,
    MigrateMySqlStatus,
    NameIdentifier,
    NameIdentifierCollection,
    NameValuePair,
    NetworkFeatures,
    NetworkTrace,
    Nonce,
    OpenAuthenticationAccessPolicies,
    OpenAuthenticationAccessPolicy,
    OpenAuthenticationPolicyClaim,
    OpenIdConnectClientCredential,
    OpenIdConnectConfig,
    OpenIdConnectLogin,
    OpenIdConnectRegistration,
    Operation,
    OperationResult,
    OperationResultProperties,
    OutboundEnvironmentEndpoint,
    OutboundEnvironmentEndpointCollection,
    PerfMonCounterCollection,
    PerfMonResponse,
    PerfMonSample,
    PerfMonSet,
    PremierAddOn,
    PremierAddOnOffer,
    PremierAddOnOfferCollection,
    PremierAddOnPatchResource,
    PrivateAccess,
    PrivateAccessSubnet,
    PrivateAccessVirtualNetwork,
    PrivateEndpointConnectionCollection,
    PrivateLinkConnectionApprovalRequestResource,
    PrivateLinkConnectionState,
    PrivateLinkResource,
    PrivateLinkResourceProperties,
    PrivateLinkResourcesWrapper,
    ProcessInfo,
    ProcessInfoCollection,
    ProcessModuleInfo,
    ProcessModuleInfoCollection,
    ProcessThreadInfo,
    ProcessThreadInfoCollection,
    ProxyOnlyResource,
    PublicCertificate,
    PublicCertificateCollection,
    PublishingCredentialsPoliciesCollection,
    PushSettings,
    QueryUtterancesResult,
    QueryUtterancesResults,
    QueueScaleRule,
    RampUpRule,
    Recommendation,
    RecommendationCollection,
    RecommendationRule,
    RecurrenceSchedule,
    RecurrenceScheduleOccurrence,
    RegenerateActionParameter,
    RegistryCredentials,
    ReissueCertificateOrderRequest,
    RelayServiceConnectionEntity,
    RemotePrivateEndpointConnection,
    RemotePrivateEndpointConnectionARMResource,
    Rendering,
    RenewCertificateOrderRequest,
    RepetitionIndex,
    Request,
    RequestHistory,
    RequestHistoryListResult,
    RequestHistoryProperties,
    RequestsBasedTrigger,
    Resource,
    ResourceCollection,
    ResourceConfig,
    ResourceHealthMetadata,
    ResourceHealthMetadataCollection,
    ResourceMetricAvailability,
    ResourceMetricDefinition,
    ResourceMetricDefinitionCollection,
    ResourceNameAvailability,
    ResourceNameAvailabilityRequest,
    ResourceReference,
    Response,
    ResponseMessageEnvelopeRemotePrivateEndpointConnection,
    ResponseMetaData,
    RestoreRequest,
    RetryHistory,
    Revision,
    RevisionCollection,
    RunActionCorrelation,
    RunCorrelation,
    SampleUtterance,
    Scale,
    ScaleRule,
    ScaleRuleAuth,
    Secret,
    SecretsCollection,
    ServiceSpecification,
    Site,
    SiteAuthSettings,
    SiteAuthSettingsV2,
    SiteCloneability,
    SiteCloneabilityCriterion,
    SiteConfig,
    SiteConfigPropertiesDictionary,
    SiteConfigResource,
    SiteConfigResourceCollection,
    SiteConfigurationSnapshotInfo,
    SiteConfigurationSnapshotInfoCollection,
    SiteExtensionInfo,
    SiteExtensionInfoCollection,
    SiteLimits,
    SiteLogsConfig,
    SiteMachineKey,
    SitePatchResource,
    SitePhpErrorLogFlag,
    SiteSeal,
    SiteSealRequest,
    SiteSourceControl,
    SkuCapacity,
    SkuDescription,
    SkuInfo,
    SkuInfoCollection,
    SkuInfos,
    SlotConfigNamesResource,
    SlotDifference,
    SlotDifferenceCollection,
    SlotSwapStatus,
    SlowRequestsBasedTrigger,
    Snapshot,
    SnapshotCollection,
    SnapshotRecoverySource,
    SnapshotRestoreRequest,
    Solution,
    SourceControl,
    SourceControlCollection,
    StackMajorVersion,
    StackMinorVersion,
    StampCapacity,
    StampCapacityCollection,
    StaticSiteARMResource,
    StaticSiteBasicAuthPropertiesARMResource,
    StaticSiteBasicAuthPropertiesCollection,
    StaticSiteBuildARMResource,
    StaticSiteBuildCollection,
    StaticSiteBuildProperties,
    StaticSiteCollection,
    StaticSiteCustomDomainOverviewARMResource,
    StaticSiteCustomDomainOverviewCollection,
    StaticSiteCustomDomainRequestPropertiesARMResource,
    StaticSiteDatabaseConnectionConfigurationFileOverview,
    StaticSiteFunctionOverviewARMResource,
    StaticSiteFunctionOverviewCollection,
    StaticSiteLinkedBackend,
    StaticSiteLinkedBackendARMResource,
    StaticSiteLinkedBackendsCollection,
    StaticSitePatchResource,
    StaticSiteResetPropertiesARMResource,
    StaticSiteTemplateOptions,
    StaticSiteUserARMResource,
    StaticSiteUserCollection,
    StaticSiteUserInvitationRequestResource,
    StaticSiteUserInvitationResponseResource,
    StaticSiteUserProvidedFunctionApp,
    StaticSiteUserProvidedFunctionAppARMResource,
    StaticSiteUserProvidedFunctionAppsCollection,
    StaticSiteZipDeploymentARMResource,
    StaticSitesWorkflowPreview,
    StaticSitesWorkflowPreviewRequest,
    Status,
    StatusCodesBasedTrigger,
    StatusCodesRangeBasedTrigger,
    StorageMigrationOptions,
    StorageMigrationResponse,
    StringDictionary,
    StringList,
    SubResource,
    SupportTopic,
    SwiftVirtualNetwork,
    Template,
    TldLegalAgreement,
    TldLegalAgreementCollection,
    TokenStore,
    TopLevelDomain,
    TopLevelDomainAgreementOption,
    TopLevelDomainCollection,
    TrafficWeight,
    TriggeredJobHistory,
    TriggeredJobHistoryCollection,
    TriggeredJobRun,
    TriggeredWebJob,
    TriggeredWebJobCollection,
    Twitter,
    TwitterRegistration,
    Usage,
    UsageCollection,
    User,
    UserAssignedIdentity,
    ValidateRequest,
    ValidateResponse,
    ValidateResponseError,
    VirtualApplication,
    VirtualDirectory,
    VirtualIPMapping,
    VirtualNetworkProfile,
    VnetGateway,
    VnetInfo,
    VnetInfoResource,
    VnetParameters,
    VnetRoute,
    VnetValidationFailureDetails,
    VnetValidationTestFailure,
    WebAppCollection,
    WebAppInstanceStatusCollection,
    WebAppMajorVersion,
    WebAppMinorVersion,
    WebAppRuntimeSettings,
    WebAppRuntimes,
    WebAppStack,
    WebAppStackCollection,
    WebJob,
    WebJobCollection,
    WebSiteInstanceStatus,
    WindowsJavaContainerSettings,
    WorkerPoolCollection,
    WorkerPoolResource,
    Workflow,
    WorkflowArtifacts,
    WorkflowEnvelope,
    WorkflowEnvelopeCollection,
    WorkflowEnvelopeProperties,
    WorkflowFilter,
    WorkflowHealth,
    WorkflowListResult,
    WorkflowOutputParameter,
    WorkflowParameter,
    WorkflowResource,
    WorkflowRun,
    WorkflowRunAction,
    WorkflowRunActionFilter,
    WorkflowRunActionListResult,
    WorkflowRunActionRepetitionDefinition,
    WorkflowRunActionRepetitionDefinitionCollection,
    WorkflowRunActionRepetitionProperties,
    WorkflowRunFilter,
    WorkflowRunListResult,
    WorkflowRunTrigger,
    WorkflowSku,
    WorkflowTrigger,
    WorkflowTriggerCallbackUrl,
    WorkflowTriggerFilter,
    WorkflowTriggerHistory,
    WorkflowTriggerHistoryFilter,
    WorkflowTriggerHistoryListResult,
    WorkflowTriggerListCallbackUrlQueries,
    WorkflowTriggerListResult,
    WorkflowTriggerRecurrence,
    WorkflowVersion,
    WorkflowVersionListResult,
)

from ._web_site_management_client_enums import (  # type: ignore
    ActiveRevisionsMode,
    AppServicePlanRestrictions,
    AutoHealActionType,
    AzureResourceType,
    AzureStorageState,
    AzureStorageType,
    BackupItemStatus,
    BackupRestoreOperationType,
    BasicAuthName,
    BuildStatus,
    BuiltInAuthenticationProvider,
    CertificateOrderActionType,
    CertificateOrderStatus,
    CertificateProductType,
    Channels,
    CheckNameResourceTypes,
    ClientCertMode,
    CloneAbilityResult,
    ComputeModeOptions,
    ConnectionStringType,
    ContainerAppProvisioningState,
    ContinuousWebJobStatus,
    CookieExpirationConvention,
    CustomDnsSuffixProvisioningState,
    CustomDomainStatus,
    CustomHostNameDnsRecordType,
    DaprLogLevel,
    DatabaseType,
    DayOfWeek,
    DaysOfWeek,
    DefaultAction,
    DeploymentBuildStatus,
    DetectorType,
    DnsType,
    DnsVerificationTestResult,
    DomainStatus,
    DomainType,
    EnterpriseGradeCdnStatus,
    ForwardProxyConvention,
    FrequencyUnit,
    FrontEndServiceType,
    FtpsState,
    HostNameType,
    HostType,
    HostingEnvironmentStatus,
    InAvailabilityReasonType,
    IngressTransportMethod,
    InsightStatus,
    IpFilterTag,
    IssueType,
    KeyType,
    KeyVaultSecretStatus,
    Kind,
    KubeEnvironmentProvisioningState,
    LoadBalancingMode,
    LogLevel,
    MSDeployLogEntryType,
    MSDeployProvisioningState,
    ManagedPipelineMode,
    ManagedServiceIdentityType,
    MySqlMigrationType,
    NotificationLevel,
    OpenAuthenticationProviderType,
    OperationStatus,
    ParameterType,
    ProviderOsTypeSelected,
    ProviderStackOsType,
    ProvisioningState,
    PublicCertificateLocation,
    PublishingProfileFormat,
    RecurrenceFrequency,
    RedundancyMode,
    RenderingType,
    ResolveStatus,
    ResourceNotRenewableReason,
    ResourceScopeType,
    RevisionHealthState,
    RevisionProvisioningState,
    RouteType,
    ScmType,
    SiteAvailabilityState,
    SiteExtensionType,
    SiteLoadBalancing,
    SiteRuntimeState,
    SkuName,
    SolutionType,
    SslState,
    StackPreferredOs,
    StagingEnvironmentPolicy,
    StatusOptions,
    StorageType,
    SupportedTlsVersions,
    TlsCipherSuites,
    TriggerTypes,
    TriggeredWebJobStatus,
    UnauthenticatedClientAction,
    UnauthenticatedClientActionV2,
    UpgradeAvailability,
    UpgradePreference,
    UsageState,
    ValidateResourceTypes,
    WebJobType,
    WorkerSizeOptions,
    WorkflowHealthState,
    WorkflowProvisioningState,
    WorkflowSkuName,
    WorkflowState,
    WorkflowStatus,
    WorkflowTriggerProvisioningState,
)
from ._patch import __all__ as _patch_all
from ._patch import *
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AbnormalTimePeriod",
    "Address",
    "AddressResponse",
    "AllowedAudiencesValidation",
    "AllowedPrincipals",
    "AnalysisData",
    "AnalysisDefinition",
    "ApiDefinitionInfo",
    "ApiKVReference",
    "ApiKVReferenceCollection",
    "ApiManagementConfig",
    "AppInsightsWebAppStackSettings",
    "AppLogsConfiguration",
    "AppRegistration",
    "AppServiceCertificate",
    "AppServiceCertificateCollection",
    "AppServiceCertificateOrder",
    "AppServiceCertificateOrderCollection",
    "AppServiceCertificateOrderPatchResource",
    "AppServiceCertificatePatchResource",
    "AppServiceCertificateResource",
    "AppServiceEnvironment",
    "AppServiceEnvironmentCollection",
    "AppServiceEnvironmentPatchResource",
    "AppServiceEnvironmentResource",
    "AppServicePlan",
    "AppServicePlanCollection",
    "AppServicePlanPatchResource",
    "Apple",
    "AppleRegistration",
    "ApplicationLogsConfig",
    "ApplicationStack",
    "ApplicationStackCollection",
    "ApplicationStackResource",
    "AppserviceGithubToken",
    "AppserviceGithubTokenRequest",
    "ArcConfiguration",
    "ArmIdWrapper",
    "ArmPlan",
    "AseRegion",
    "AseRegionCollection",
    "AseV3NetworkingConfiguration",
    "AuthPlatform",
    "AutoHealActions",
    "AutoHealCustomAction",
    "AutoHealRules",
    "AutoHealTriggers",
    "AzureActiveDirectory",
    "AzureActiveDirectoryLogin",
    "AzureActiveDirectoryRegistration",
    "AzureActiveDirectoryValidation",
    "AzureBlobStorageApplicationLogsConfig",
    "AzureBlobStorageHttpLogsConfig",
    "AzureResourceErrorInfo",
    "AzureStaticWebApps",
    "AzureStaticWebAppsRegistration",
    "AzureStorageInfoValue",
    "AzureStoragePropertyDictionaryResource",
    "AzureTableStorageApplicationLogsConfig",
    "BackupItem",
    "BackupItemCollection",
    "BackupRequest",
    "BackupSchedule",
    "BillingMeter",
    "BillingMeterCollection",
    "BlobStorageTokenStore",
    "Capability",
    "Certificate",
    "CertificateCollection",
    "CertificateDetails",
    "CertificateEmail",
    "CertificateOrderAction",
    "CertificateOrderContact",
    "CertificatePatchResource",
    "ClientRegistration",
    "CloningInfo",
    "Configuration",
    "ConnStringInfo",
    "ConnStringValueTypePair",
    "ConnectionStringDictionary",
    "Contact",
    "Container",
    "ContainerApp",
    "ContainerAppCollection",
    "ContainerAppSecret",
    "ContainerAppsConfiguration",
    "ContainerCpuStatistics",
    "ContainerCpuUsage",
    "ContainerInfo",
    "ContainerMemoryStatistics",
    "ContainerNetworkInterfaceStatistics",
    "ContainerResources",
    "ContainerThrottlingData",
    "ContentHash",
    "ContentLink",
    "ContinuousWebJob",
    "ContinuousWebJobCollection",
    "CookieExpiration",
    "Correlation",
    "CorsSettings",
    "CsmDeploymentStatus",
    "CsmDeploymentStatusCollection",
    "CsmMoveResourceEnvelope",
    "CsmOperationCollection",
    "CsmOperationDescription",
    "CsmOperationDescriptionProperties",
    "CsmOperationDisplay",
    "CsmPublishingCredentialsPoliciesEntity",
    "CsmPublishingProfileOptions",
    "CsmSlotEntity",
    "CsmUsageQuota",
    "CsmUsageQuotaCollection",
    "CustomDnsSuffixConfiguration",
    "CustomHostnameAnalysisResult",
    "CustomHostnameSites",
    "CustomHostnameSitesCollection",
    "CustomOpenIdConnectProvider",
    "CustomScaleRule",
    "Dapr",
    "DaprComponent",
    "DaprConfig",
    "DaprMetadata",
    "DataProviderMetadata",
    "DataSource",
    "DataTableResponseColumn",
    "DataTableResponseObject",
    "DatabaseBackupSetting",
    "DatabaseConnection",
    "DatabaseConnectionCollection",
    "DatabaseConnectionOverview",
    "DatabaseConnectionPatchRequest",
    "DefaultAuthorizationPolicy",
    "DefaultErrorResponse",
    "DefaultErrorResponseError",
    "DefaultErrorResponseErrorDetailsItem",
    "DeletedAppRestoreRequest",
    "DeletedSite",
    "DeletedWebAppCollection",
    "Deployment",
    "DeploymentCollection",
    "DeploymentLocations",
    "DetectorAbnormalTimePeriod",
    "DetectorDefinition",
    "DetectorDefinitionResource",
    "DetectorInfo",
    "DetectorResponse",
    "DetectorResponseCollection",
    "DiagnosticAnalysis",
    "DiagnosticAnalysisCollection",
    "DiagnosticCategory",
    "DiagnosticCategoryCollection",
    "DiagnosticData",
    "DiagnosticDetectorCollection",
    "DiagnosticDetectorResponse",
    "DiagnosticMetricSample",
    "DiagnosticMetricSet",
    "Dimension",
    "Domain",
    "DomainAvailabilityCheckResult",
    "DomainCollection",
    "DomainControlCenterSsoRequest",
    "DomainOwnershipIdentifier",
    "DomainOwnershipIdentifierCollection",
    "DomainPatchResource",
    "DomainPurchaseConsent",
    "DomainRecommendationSearchParameters",
    "EnabledConfig",
    "EndpointDependency",
    "EndpointDetail",
    "EnvironmentVar",
    "ErrorEntity",
    "ErrorInfo",
    "ErrorProperties",
    "ErrorResponse",
    "Experiments",
    "Expression",
    "ExpressionRoot",
    "ExpressionTraces",
    "ExtendedLocation",
    "Facebook",
    "FileSystemApplicationLogsConfig",
    "FileSystemHttpLogsConfig",
    "FileSystemTokenStore",
    "FlowAccessControlConfiguration",
    "FlowAccessControlConfigurationPolicy",
    "FlowEndpoints",
    "FlowEndpointsConfiguration",
    "ForwardProxy",
    "FrontEndConfiguration",
    "FunctionAppMajorVersion",
    "FunctionAppMinorVersion",
    "FunctionAppRuntimeSettings",
    "FunctionAppRuntimes",
    "FunctionAppStack",
    "FunctionAppStackCollection",
    "FunctionEnvelope",
    "FunctionEnvelopeCollection",
    "FunctionSecrets",
    "GeoRegion",
    "GeoRegionCollection",
    "GitHub",
    "GitHubActionCodeConfiguration",
    "GitHubActionConfiguration",
    "GitHubActionContainerConfiguration",
    "GitHubActionWebAppStackSettings",
    "GlobalCsmSkuDescription",
    "GlobalValidation",
    "Google",
    "HandlerMapping",
    "HostKeys",
    "HostName",
    "HostNameBinding",
    "HostNameBindingCollection",
    "HostNameSslState",
    "HostingEnvironmentDeploymentInfo",
    "HostingEnvironmentDiagnostics",
    "HostingEnvironmentProfile",
    "HttpLogsConfig",
    "HttpScaleRule",
    "HttpSettings",
    "HttpSettingsRoutes",
    "HybridConnection",
    "HybridConnectionCollection",
    "HybridConnectionKey",
    "HybridConnectionLimits",
    "Identifier",
    "IdentifierCollection",
    "IdentityProviders",
    "InboundEnvironmentEndpoint",
    "InboundEnvironmentEndpointCollection",
    "Ingress",
    "IpAddress",
    "IpAddressRange",
    "IpSecurityRestriction",
    "JsonSchema",
    "JwtClaimChecks",
    "KeyInfo",
    "KeyValuePairStringObject",
    "KubeEnvironment",
    "KubeEnvironmentCollection",
    "KubeEnvironmentPatchResource",
    "KubeEnvironmentProfile",
    "LegacyMicrosoftAccount",
    "LinuxJavaContainerSettings",
    "LocalizableString",
    "LogAnalyticsConfiguration",
    "LogSpecification",
    "Login",
    "LoginRoutes",
    "LoginScopes",
    "MSDeploy",
    "MSDeployLog",
    "MSDeployLogEntry",
    "MSDeployStatus",
    "ManagedServiceIdentity",
    "MetricAvailability",
    "MetricSpecification",
    "MigrateMySqlRequest",
    "MigrateMySqlStatus",
    "NameIdentifier",
    "NameIdentifierCollection",
    "NameValuePair",
    "NetworkFeatures",
    "NetworkTrace",
    "Nonce",
    "OpenAuthenticationAccessPolicies",
    "OpenAuthenticationAccessPolicy",
    "OpenAuthenticationPolicyClaim",
    "OpenIdConnectClientCredential",
    "OpenIdConnectConfig",
    "OpenIdConnectLogin",
    "OpenIdConnectRegistration",
    "Operation",
    "OperationResult",
    "OperationResultProperties",
    "OutboundEnvironmentEndpoint",
    "OutboundEnvironmentEndpointCollection",
    "PerfMonCounterCollection",
    "PerfMonResponse",
    "PerfMonSample",
    "PerfMonSet",
    "PremierAddOn",
    "PremierAddOnOffer",
    "PremierAddOnOfferCollection",
    "PremierAddOnPatchResource",
    "PrivateAccess",
    "PrivateAccessSubnet",
    "PrivateAccessVirtualNetwork",
    "PrivateEndpointConnectionCollection",
    "PrivateLinkConnectionApprovalRequestResource",
    "PrivateLinkConnectionState",
    "PrivateLinkResource",
    "PrivateLinkResourceProperties",
    "PrivateLinkResourcesWrapper",
    "ProcessInfo",
    "ProcessInfoCollection",
    "ProcessModuleInfo",
    "ProcessModuleInfoCollection",
    "ProcessThreadInfo",
    "ProcessThreadInfoCollection",
    "ProxyOnlyResource",
    "PublicCertificate",
    "PublicCertificateCollection",
    "PublishingCredentialsPoliciesCollection",
    "PushSettings",
    "QueryUtterancesResult",
    "QueryUtterancesResults",
    "QueueScaleRule",
    "RampUpRule",
    "Recommendation",
    "RecommendationCollection",
    "RecommendationRule",
    "RecurrenceSchedule",
    "RecurrenceScheduleOccurrence",
    "RegenerateActionParameter",
    "RegistryCredentials",
    "ReissueCertificateOrderRequest",
    "RelayServiceConnectionEntity",
    "RemotePrivateEndpointConnection",
    "RemotePrivateEndpointConnectionARMResource",
    "Rendering",
    "RenewCertificateOrderRequest",
    "RepetitionIndex",
    "Request",
    "RequestHistory",
    "RequestHistoryListResult",
    "RequestHistoryProperties",
    "RequestsBasedTrigger",
    "Resource",
    "ResourceCollection",
    "ResourceConfig",
    "ResourceHealthMetadata",
    "ResourceHealthMetadataCollection",
    "ResourceMetricAvailability",
    "ResourceMetricDefinition",
    "ResourceMetricDefinitionCollection",
    "ResourceNameAvailability",
    "ResourceNameAvailabilityRequest",
    "ResourceReference",
    "Response",
    "ResponseMessageEnvelopeRemotePrivateEndpointConnection",
    "ResponseMetaData",
    "RestoreRequest",
    "RetryHistory",
    "Revision",
    "RevisionCollection",
    "RunActionCorrelation",
    "RunCorrelation",
    "SampleUtterance",
    "Scale",
    "ScaleRule",
    "ScaleRuleAuth",
    "Secret",
    "SecretsCollection",
    "ServiceSpecification",
    "Site",
    "SiteAuthSettings",
    "SiteAuthSettingsV2",
    "SiteCloneability",
    "SiteCloneabilityCriterion",
    "SiteConfig",
    "SiteConfigPropertiesDictionary",
    "SiteConfigResource",
    "SiteConfigResourceCollection",
    "SiteConfigurationSnapshotInfo",
    "SiteConfigurationSnapshotInfoCollection",
    "SiteExtensionInfo",
    "SiteExtensionInfoCollection",
    "SiteLimits",
    "SiteLogsConfig",
    "SiteMachineKey",
    "SitePatchResource",
    "SitePhpErrorLogFlag",
    "SiteSeal",
    "SiteSealRequest",
    "SiteSourceControl",
    "SkuCapacity",
    "SkuDescription",
    "SkuInfo",
    "SkuInfoCollection",
    "SkuInfos",
    "SlotConfigNamesResource",
    "SlotDifference",
    "SlotDifferenceCollection",
    "SlotSwapStatus",
    "SlowRequestsBasedTrigger",
    "Snapshot",
    "SnapshotCollection",
    "SnapshotRecoverySource",
    "SnapshotRestoreRequest",
    "Solution",
    "SourceControl",
    "SourceControlCollection",
    "StackMajorVersion",
    "StackMinorVersion",
    "StampCapacity",
    "StampCapacityCollection",
    "StaticSiteARMResource",
    "StaticSiteBasicAuthPropertiesARMResource",
    "StaticSiteBasicAuthPropertiesCollection",
    "StaticSiteBuildARMResource",
    "StaticSiteBuildCollection",
    "StaticSiteBuildProperties",
    "StaticSiteCollection",
    "StaticSiteCustomDomainOverviewARMResource",
    "StaticSiteCustomDomainOverviewCollection",
    "StaticSiteCustomDomainRequestPropertiesARMResource",
    "StaticSiteDatabaseConnectionConfigurationFileOverview",
    "StaticSiteFunctionOverviewARMResource",
    "StaticSiteFunctionOverviewCollection",
    "StaticSiteLinkedBackend",
    "StaticSiteLinkedBackendARMResource",
    "StaticSiteLinkedBackendsCollection",
    "StaticSitePatchResource",
    "StaticSiteResetPropertiesARMResource",
    "StaticSiteTemplateOptions",
    "StaticSiteUserARMResource",
    "StaticSiteUserCollection",
    "StaticSiteUserInvitationRequestResource",
    "StaticSiteUserInvitationResponseResource",
    "StaticSiteUserProvidedFunctionApp",
    "StaticSiteUserProvidedFunctionAppARMResource",
    "StaticSiteUserProvidedFunctionAppsCollection",
    "StaticSiteZipDeploymentARMResource",
    "StaticSitesWorkflowPreview",
    "StaticSitesWorkflowPreviewRequest",
    "Status",
    "StatusCodesBasedTrigger",
    "StatusCodesRangeBasedTrigger",
    "StorageMigrationOptions",
    "StorageMigrationResponse",
    "StringDictionary",
    "StringList",
    "SubResource",
    "SupportTopic",
    "SwiftVirtualNetwork",
    "Template",
    "TldLegalAgreement",
    "TldLegalAgreementCollection",
    "TokenStore",
    "TopLevelDomain",
    "TopLevelDomainAgreementOption",
    "TopLevelDomainCollection",
    "TrafficWeight",
    "TriggeredJobHistory",
    "TriggeredJobHistoryCollection",
    "TriggeredJobRun",
    "TriggeredWebJob",
    "TriggeredWebJobCollection",
    "Twitter",
    "TwitterRegistration",
    "Usage",
    "UsageCollection",
    "User",
    "UserAssignedIdentity",
    "ValidateRequest",
    "ValidateResponse",
    "ValidateResponseError",
    "VirtualApplication",
    "VirtualDirectory",
    "VirtualIPMapping",
    "VirtualNetworkProfile",
    "VnetGateway",
    "VnetInfo",
    "VnetInfoResource",
    "VnetParameters",
    "VnetRoute",
    "VnetValidationFailureDetails",
    "VnetValidationTestFailure",
    "WebAppCollection",
    "WebAppInstanceStatusCollection",
    "WebAppMajorVersion",
    "WebAppMinorVersion",
    "WebAppRuntimeSettings",
    "WebAppRuntimes",
    "WebAppStack",
    "WebAppStackCollection",
    "WebJob",
    "WebJobCollection",
    "WebSiteInstanceStatus",
    "WindowsJavaContainerSettings",
    "WorkerPoolCollection",
    "WorkerPoolResource",
    "Workflow",
    "WorkflowArtifacts",
    "WorkflowEnvelope",
    "WorkflowEnvelopeCollection",
    "WorkflowEnvelopeProperties",
    "WorkflowFilter",
    "WorkflowHealth",
    "WorkflowListResult",
    "WorkflowOutputParameter",
    "WorkflowParameter",
    "WorkflowResource",
    "WorkflowRun",
    "WorkflowRunAction",
    "WorkflowRunActionFilter",
    "WorkflowRunActionListResult",
    "WorkflowRunActionRepetitionDefinition",
    "WorkflowRunActionRepetitionDefinitionCollection",
    "WorkflowRunActionRepetitionProperties",
    "WorkflowRunFilter",
    "WorkflowRunListResult",
    "WorkflowRunTrigger",
    "WorkflowSku",
    "WorkflowTrigger",
    "WorkflowTriggerCallbackUrl",
    "WorkflowTriggerFilter",
    "WorkflowTriggerHistory",
    "WorkflowTriggerHistoryFilter",
    "WorkflowTriggerHistoryListResult",
    "WorkflowTriggerListCallbackUrlQueries",
    "WorkflowTriggerListResult",
    "WorkflowTriggerRecurrence",
    "WorkflowVersion",
    "WorkflowVersionListResult",
    "ActiveRevisionsMode",
    "AppServicePlanRestrictions",
    "AutoHealActionType",
    "AzureResourceType",
    "AzureStorageState",
    "AzureStorageType",
    "BackupItemStatus",
    "BackupRestoreOperationType",
    "BasicAuthName",
    "BuildStatus",
    "BuiltInAuthenticationProvider",
    "CertificateOrderActionType",
    "CertificateOrderStatus",
    "CertificateProductType",
    "Channels",
    "CheckNameResourceTypes",
    "ClientCertMode",
    "CloneAbilityResult",
    "ComputeModeOptions",
    "ConnectionStringType",
    "ContainerAppProvisioningState",
    "ContinuousWebJobStatus",
    "CookieExpirationConvention",
    "CustomDnsSuffixProvisioningState",
    "CustomDomainStatus",
    "CustomHostNameDnsRecordType",
    "DaprLogLevel",
    "DatabaseType",
    "DayOfWeek",
    "DaysOfWeek",
    "DefaultAction",
    "DeploymentBuildStatus",
    "DetectorType",
    "DnsType",
    "DnsVerificationTestResult",
    "DomainStatus",
    "DomainType",
    "EnterpriseGradeCdnStatus",
    "ForwardProxyConvention",
    "FrequencyUnit",
    "FrontEndServiceType",
    "FtpsState",
    "HostNameType",
    "HostType",
    "HostingEnvironmentStatus",
    "InAvailabilityReasonType",
    "IngressTransportMethod",
    "InsightStatus",
    "IpFilterTag",
    "IssueType",
    "KeyType",
    "KeyVaultSecretStatus",
    "Kind",
    "KubeEnvironmentProvisioningState",
    "LoadBalancingMode",
    "LogLevel",
    "MSDeployLogEntryType",
    "MSDeployProvisioningState",
    "ManagedPipelineMode",
    "ManagedServiceIdentityType",
    "MySqlMigrationType",
    "NotificationLevel",
    "OpenAuthenticationProviderType",
    "OperationStatus",
    "ParameterType",
    "ProviderOsTypeSelected",
    "ProviderStackOsType",
    "ProvisioningState",
    "PublicCertificateLocation",
    "PublishingProfileFormat",
    "RecurrenceFrequency",
    "RedundancyMode",
    "RenderingType",
    "ResolveStatus",
    "ResourceNotRenewableReason",
    "ResourceScopeType",
    "RevisionHealthState",
    "RevisionProvisioningState",
    "RouteType",
    "ScmType",
    "SiteAvailabilityState",
    "SiteExtensionType",
    "SiteLoadBalancing",
    "SiteRuntimeState",
    "SkuName",
    "SolutionType",
    "SslState",
    "StackPreferredOs",
    "StagingEnvironmentPolicy",
    "StatusOptions",
    "StorageType",
    "SupportedTlsVersions",
    "TlsCipherSuites",
    "TriggerTypes",
    "TriggeredWebJobStatus",
    "UnauthenticatedClientAction",
    "UnauthenticatedClientActionV2",
    "UpgradeAvailability",
    "UpgradePreference",
    "UsageState",
    "ValidateResourceTypes",
    "WebJobType",
    "WorkerSizeOptions",
    "WorkflowHealthState",
    "WorkflowProvisioningState",
    "WorkflowSkuName",
    "WorkflowState",
    "WorkflowStatus",
    "WorkflowTriggerProvisioningState",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
