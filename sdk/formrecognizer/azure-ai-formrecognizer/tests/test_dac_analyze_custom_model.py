# coding=utf-8
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

import pytest
import functools
from devtools_testutils import recorded_by_proxy, set_bodiless_matcher
from azure.ai.formrecognizer import DocumentAnalysisClient, DocumentModelAdministrationClient, AnalyzeResult
from azure.ai.formrecognizer._generated.v2023_07_31.models import AnalyzeResultOperation
from testcase import FormRecognizerTest
from preparers import FormRecognizerPreparer, get_sync_client
from conftest import skip_flaky_test

get_dma_client = functools.partial(get_sync_client, DocumentModelAdministrationClient)
get_da_client = functools.partial(get_sync_client, DocumentAnalysisClient)

class TestDACAnalyzeCustomModel(FormRecognizerTest):

    @FormRecognizerPreparer()
    def test_analyze_document_none_model_id(self, **kwargs):
        client = get_da_client()
        with pytest.raises(ValueError) as e:
            client.begin_analyze_document(model_id=None, document=b"xx")
        assert "model_id cannot be None or empty." in str(e.value)

    @FormRecognizerPreparer()
    def test_analyze_document_empty_model_id(self, **kwargs):
        client = get_da_client()
        with pytest.raises(ValueError) as e:
            client.begin_analyze_document(model_id="", document=b"xx")
        assert "model_id cannot be None or empty." in str(e.value)

    @skip_flaky_test
    @FormRecognizerPreparer()
    @recorded_by_proxy
    def test_custom_document_transform(self, formrecognizer_storage_container_sas_url, **kwargs):
        client = get_dma_client()
        set_bodiless_matcher()
        da_client = client.get_document_analysis_client()

        poller = client.begin_build_document_model("template", blob_container_url=formrecognizer_storage_container_sas_url)
        model = poller.result()

        responses = []

        def callback(raw_response, _, headers):
            analyze_result = da_client._deserialize(AnalyzeResultOperation, raw_response)
            document = AnalyzeResult._from_generated(analyze_result.analyze_result)
            responses.append(analyze_result)
            responses.append(document)

        with open(self.form_jpg, "rb") as fd:
            my_file = fd.read()

        poller = da_client.begin_analyze_document(
            model.model_id,
            my_file,
            cls=callback
        )
        document = poller.result()

        raw_analyze_result = responses[0].analyze_result
        returned_model = responses[1]

        # Check AnalyzeResult
        assert returned_model.model_id == raw_analyze_result.model_id
        assert returned_model.api_version == raw_analyze_result.api_version
        assert returned_model.content == raw_analyze_result.content

        self.assertDocumentPagesTransformCorrect(returned_model.pages, raw_analyze_result.pages)
        self.assertDocumentTransformCorrect(returned_model.documents, raw_analyze_result.documents)
        self.assertDocumentTablesTransformCorrect(returned_model.tables, raw_analyze_result.tables)
        self.assertDocumentKeyValuePairsTransformCorrect(returned_model.key_value_pairs, raw_analyze_result.key_value_pairs)
        self.assertDocumentStylesTransformCorrect(returned_model.styles, raw_analyze_result.styles)

        # check page range
        assert len(raw_analyze_result.pages) == len(returned_model.pages)

    @skip_flaky_test
    @FormRecognizerPreparer()
    @recorded_by_proxy
    def test_custom_document_multipage_transform(self, formrecognizer_multipage_storage_container_sas_url, **kwargs):
        client = get_dma_client()
        set_bodiless_matcher()
        da_client = client.get_document_analysis_client()

        poller = client.begin_build_document_model("template", blob_container_url=formrecognizer_multipage_storage_container_sas_url)
        model = poller.result()

        responses = []

        def callback(raw_response, _, headers):
            analyze_result = da_client._deserialize(AnalyzeResultOperation, raw_response)
            document = AnalyzeResult._from_generated(analyze_result.analyze_result)
            responses.append(analyze_result)
            responses.append(document)

        with open(self.multipage_invoice_pdf, "rb") as fd:
            my_file = fd.read()

        poller = da_client.begin_analyze_document(
            model.model_id,
            my_file,
            cls=callback
        )
        document = poller.result()

        raw_analyze_result = responses[0].analyze_result
        returned_model = responses[1]

        # Check AnalyzeResult
        assert returned_model.model_id == raw_analyze_result.model_id
        assert returned_model.api_version == raw_analyze_result.api_version
        assert returned_model.content == raw_analyze_result.content

        self.assertDocumentPagesTransformCorrect(returned_model.pages, raw_analyze_result.pages)
        self.assertDocumentTransformCorrect(returned_model.documents, raw_analyze_result.documents)
        self.assertDocumentTablesTransformCorrect(returned_model.tables, raw_analyze_result.tables)
        self.assertDocumentKeyValuePairsTransformCorrect(returned_model.key_value_pairs, raw_analyze_result.key_value_pairs)
        self.assertDocumentStylesTransformCorrect(returned_model.styles, raw_analyze_result.styles)

        # check page range
        assert len(raw_analyze_result.pages) == len(returned_model.pages)

    @skip_flaky_test
    @FormRecognizerPreparer()
    @recorded_by_proxy
    def test_custom_document_selection_mark(self, formrecognizer_selection_mark_storage_container_sas_url, **kwargs):
        client = get_dma_client()
        set_bodiless_matcher()
        da_client = client.get_document_analysis_client()

        poller = client.begin_build_document_model("template", blob_container_url=formrecognizer_selection_mark_storage_container_sas_url)
        model = poller.result()

        with open(self.selection_form_pdf, "rb") as fd:
            my_file = fd.read()

        responses = []

        def callback(raw_response, _, headers):
            analyze_result = da_client._deserialize(AnalyzeResultOperation, raw_response)
            document = AnalyzeResult._from_generated(analyze_result.analyze_result)
            responses.append(analyze_result)
            responses.append(document)

        poller = da_client.begin_analyze_document(
            model.model_id,
            my_file,
            cls=callback
        )
        document = poller.result()

        raw_analyze_result = responses[0].analyze_result
        returned_model = responses[1]

        # Check AnalyzeResult
        assert returned_model.model_id == raw_analyze_result.model_id
        assert returned_model.api_version == raw_analyze_result.api_version
        assert returned_model.content == raw_analyze_result.content

        self.assertDocumentPagesTransformCorrect(returned_model.pages, raw_analyze_result.pages)
        self.assertDocumentTransformCorrect(returned_model.documents, raw_analyze_result.documents)
        self.assertDocumentTablesTransformCorrect(returned_model.tables, raw_analyze_result.tables)
        self.assertDocumentKeyValuePairsTransformCorrect(returned_model.key_value_pairs, raw_analyze_result.key_value_pairs)
        self.assertDocumentStylesTransformCorrect(returned_model.styles, raw_analyze_result.styles)

        # check page range
        assert len(raw_analyze_result.pages) == len(returned_model.pages)

    @skip_flaky_test
    @FormRecognizerPreparer()
    @recorded_by_proxy
    def test_pages_kwarg_specified(self, formrecognizer_storage_container_sas_url, **kwargs):
        client = get_dma_client()
        set_bodiless_matcher()
        da_client = client.get_document_analysis_client()

        with open(self.form_jpg, "rb") as fd:
            my_file = fd.read()

        build_poller = client.begin_build_document_model("template", blob_container_url=formrecognizer_storage_container_sas_url)
        model = build_poller.result()

        poller = da_client.begin_analyze_document(model.model_id, my_file, pages="1")
        assert '1' == poller._polling_method._initial_response.http_response.request.query['pages']
        result = poller.result()
        assert result

    @skip_flaky_test
    @FormRecognizerPreparer()
    @recorded_by_proxy
    def test_custom_document_signature_field(self, formrecognizer_storage_container_sas_url, **kwargs):
        client = get_dma_client()
        set_bodiless_matcher()
        da_client = client.get_document_analysis_client()

        with open(self.form_jpg, "rb") as fd:
            my_file = fd.read()

        build_polling = client.begin_build_document_model("template", blob_container_url=formrecognizer_storage_container_sas_url)
        model = build_polling.result()

        poller = da_client.begin_analyze_document(
            model.model_id,
            my_file,
        )
        result = poller.result()

        assert result.documents[0].fields.get("FullSignature").value == "signed"
        assert result.documents[0].fields.get("FullSignature").value_type == "signature"
        # this will notify us of changes in the service, currently expecting to get a None content for signature type fields
        assert result.documents[0].fields.get("FullSignature").content == None

    @skip_flaky_test
    @FormRecognizerPreparer()
    @recorded_by_proxy
    def test_custom_document_blank_pdf(self, formrecognizer_storage_container_sas_url, **kwargs):
        client = get_dma_client()
        set_bodiless_matcher()
        da_client = client.get_document_analysis_client()

        with open(self.blank_pdf, "rb") as fd:
            my_file = fd.read()

        build_polling = client.begin_build_document_model("template", blob_container_url=formrecognizer_storage_container_sas_url)
        model = build_polling.result()

        poller = da_client.begin_analyze_document(
            model.model_id,
            my_file,
        )
        result = poller.result()

        assert result is not None
        assert len(result.pages) == 1
        assert len(result.pages[0].lines) == 0
