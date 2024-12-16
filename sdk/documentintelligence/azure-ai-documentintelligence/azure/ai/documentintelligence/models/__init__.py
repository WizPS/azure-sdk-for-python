# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
# pylint: disable=wrong-import-position

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._patch import *  # pylint: disable=unused-wildcard-import


from ._models import (  # type: ignore
    AddressValue,
    AnalyzeBatchDocumentsRequest,
    AnalyzeBatchOperation,
    AnalyzeBatchOperationDetail,
    AnalyzeBatchResult,
    AnalyzeDocumentRequest,
    AnalyzeResult,
    AnalyzedDocument,
    AuthorizeClassifierCopyRequest,
    AuthorizeCopyRequest,
    AzureBlobContentSource,
    AzureBlobFileListContentSource,
    BoundingRegion,
    BuildDocumentClassifierRequest,
    BuildDocumentModelRequest,
    ClassifierCopyAuthorization,
    ClassifierDocumentTypeDetails,
    ClassifyDocumentRequest,
    ComposeDocumentModelRequest,
    CurrencyValue,
    CustomDocumentModelsDetails,
    DocumentBarcode,
    DocumentCaption,
    DocumentClassifierBuildOperationDetails,
    DocumentClassifierCopyToOperationDetails,
    DocumentClassifierDetails,
    DocumentField,
    DocumentFieldSchema,
    DocumentFigure,
    DocumentFootnote,
    DocumentFormula,
    DocumentIntelligenceError,
    DocumentIntelligenceErrorResponse,
    DocumentIntelligenceInnerError,
    DocumentIntelligenceOperationDetails,
    DocumentIntelligenceResourceDetails,
    DocumentIntelligenceWarning,
    DocumentKeyValueElement,
    DocumentKeyValuePair,
    DocumentLanguage,
    DocumentLine,
    DocumentModelBuildOperationDetails,
    DocumentModelComposeOperationDetails,
    DocumentModelCopyToOperationDetails,
    DocumentModelDetails,
    DocumentPage,
    DocumentParagraph,
    DocumentSection,
    DocumentSelectionMark,
    DocumentSpan,
    DocumentStyle,
    DocumentTable,
    DocumentTableCell,
    DocumentTypeDetails,
    DocumentWord,
    ModelCopyAuthorization,
)

from ._enums import (  # type: ignore
    AnalyzeOutputOption,
    ContentSourceKind,
    DocumentAnalysisFeature,
    DocumentBarcodeKind,
    DocumentBuildMode,
    DocumentContentFormat,
    DocumentFieldType,
    DocumentFontStyle,
    DocumentFontWeight,
    DocumentFormulaKind,
    DocumentIntelligenceOperationStatus,
    DocumentSelectionMarkState,
    DocumentSignatureType,
    DocumentTableCellKind,
    LengthUnit,
    OperationKind,
    ParagraphRole,
    SplitMode,
    StringIndexType,
)
from ._patch import __all__ as _patch_all
from ._patch import *
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AddressValue",
    "AnalyzeBatchDocumentsRequest",
    "AnalyzeBatchOperation",
    "AnalyzeBatchOperationDetail",
    "AnalyzeBatchResult",
    "AnalyzeDocumentRequest",
    "AnalyzeResult",
    "AnalyzedDocument",
    "AuthorizeClassifierCopyRequest",
    "AuthorizeCopyRequest",
    "AzureBlobContentSource",
    "AzureBlobFileListContentSource",
    "BoundingRegion",
    "BuildDocumentClassifierRequest",
    "BuildDocumentModelRequest",
    "ClassifierCopyAuthorization",
    "ClassifierDocumentTypeDetails",
    "ClassifyDocumentRequest",
    "ComposeDocumentModelRequest",
    "CurrencyValue",
    "CustomDocumentModelsDetails",
    "DocumentBarcode",
    "DocumentCaption",
    "DocumentClassifierBuildOperationDetails",
    "DocumentClassifierCopyToOperationDetails",
    "DocumentClassifierDetails",
    "DocumentField",
    "DocumentFieldSchema",
    "DocumentFigure",
    "DocumentFootnote",
    "DocumentFormula",
    "DocumentIntelligenceError",
    "DocumentIntelligenceErrorResponse",
    "DocumentIntelligenceInnerError",
    "DocumentIntelligenceOperationDetails",
    "DocumentIntelligenceResourceDetails",
    "DocumentIntelligenceWarning",
    "DocumentKeyValueElement",
    "DocumentKeyValuePair",
    "DocumentLanguage",
    "DocumentLine",
    "DocumentModelBuildOperationDetails",
    "DocumentModelComposeOperationDetails",
    "DocumentModelCopyToOperationDetails",
    "DocumentModelDetails",
    "DocumentPage",
    "DocumentParagraph",
    "DocumentSection",
    "DocumentSelectionMark",
    "DocumentSpan",
    "DocumentStyle",
    "DocumentTable",
    "DocumentTableCell",
    "DocumentTypeDetails",
    "DocumentWord",
    "ModelCopyAuthorization",
    "AnalyzeOutputOption",
    "ContentSourceKind",
    "DocumentAnalysisFeature",
    "DocumentBarcodeKind",
    "DocumentBuildMode",
    "DocumentContentFormat",
    "DocumentFieldType",
    "DocumentFontStyle",
    "DocumentFontWeight",
    "DocumentFormulaKind",
    "DocumentIntelligenceOperationStatus",
    "DocumentSelectionMarkState",
    "DocumentSignatureType",
    "DocumentTableCellKind",
    "LengthUnit",
    "OperationKind",
    "ParagraphRole",
    "SplitMode",
    "StringIndexType",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
