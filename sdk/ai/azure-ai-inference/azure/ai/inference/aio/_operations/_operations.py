# pylint: disable=too-many-locals
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import json
import sys
from typing import Any, Callable, Dict, IO, List, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    StreamClosedError,
    StreamConsumedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ..._model_base import SdkJSONEncoder, _deserialize
from ..._operations._operations import (
    build_chat_completions_complete_request,
    build_chat_completions_get_model_info_request,
    build_embeddings_embed_request,
    build_embeddings_get_model_info_request,
    build_image_embeddings_embed_request,
    build_image_embeddings_get_model_info_request,
)
from .._vendor import ChatCompletionsClientMixinABC, EmbeddingsClientMixinABC, ImageEmbeddingsClientMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
_Unset: Any = object()
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ChatCompletionsClientOperationsMixin(ChatCompletionsClientMixinABC):

    @overload
    async def _complete(
        self,
        body: JSON,
        *,
        extra_params: Optional[Union[str, _models._enums.ExtraParameters]] = None,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ChatCompletions: ...
    @overload
    async def _complete(
        self,
        *,
        messages: List[_models._models.ChatRequestMessage],
        extra_params: Optional[Union[str, _models._enums.ExtraParameters]] = None,
        content_type: str = "application/json",
        frequency_penalty: Optional[float] = None,
        stream_parameter: Optional[bool] = None,
        presence_penalty: Optional[float] = None,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        max_tokens: Optional[int] = None,
        response_format: Optional[_models._models.ChatCompletionsResponseFormat] = None,
        stop: Optional[List[str]] = None,
        tools: Optional[List[_models.ChatCompletionsToolDefinition]] = None,
        tool_choice: Optional[
            Union[str, _models.ChatCompletionsToolChoicePreset, _models.ChatCompletionsNamedToolChoice]
        ] = None,
        seed: Optional[int] = None,
        model: Optional[str] = None,
        **kwargs: Any
    ) -> _models.ChatCompletions: ...
    @overload
    async def _complete(
        self,
        body: IO[bytes],
        *,
        extra_params: Optional[Union[str, _models._enums.ExtraParameters]] = None,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ChatCompletions: ...

    @distributed_trace_async
    async def _complete(
        self,
        body: Union[JSON, IO[bytes]] = _Unset,
        *,
        messages: List[_models._models.ChatRequestMessage] = _Unset,
        extra_params: Optional[Union[str, _models._enums.ExtraParameters]] = None,
        frequency_penalty: Optional[float] = None,
        stream_parameter: Optional[bool] = None,
        presence_penalty: Optional[float] = None,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        max_tokens: Optional[int] = None,
        response_format: Optional[_models._models.ChatCompletionsResponseFormat] = None,
        stop: Optional[List[str]] = None,
        tools: Optional[List[_models.ChatCompletionsToolDefinition]] = None,
        tool_choice: Optional[
            Union[str, _models.ChatCompletionsToolChoicePreset, _models.ChatCompletionsNamedToolChoice]
        ] = None,
        seed: Optional[int] = None,
        model: Optional[str] = None,
        **kwargs: Any
    ) -> _models.ChatCompletions:
        """Gets chat completions for the provided chat messages.
        Completions support a wide variety of tasks and generate text that continues from or
        "completes"
        provided prompt data. The method makes a REST API call to the ``/chat/completions`` route
        on the given endpoint.

        :param body: Is either a JSON type or a IO[bytes] type. Required.
        :type body: JSON or IO[bytes]
        :keyword messages: The collection of context messages associated with this chat completions
         request.
         Typical usage begins with a chat message for the System role that provides instructions for
         the behavior of the assistant, followed by alternating messages between the User and
         Assistant roles. Required.
        :paramtype messages: list[~azure.ai.inference.models._models.ChatRequestMessage]
        :keyword extra_params: Controls what happens if extra parameters, undefined by the REST API,
         are passed in the JSON request payload.
         This sets the HTTP request header ``extra-parameters``. Known values are: "error", "drop", and
         "pass-through". Default value is None.
        :paramtype extra_params: str or ~azure.ai.inference.models.ExtraParameters
        :keyword frequency_penalty: A value that influences the probability of generated tokens
         appearing based on their cumulative
         frequency in generated text.
         Positive values will make tokens less likely to appear as their frequency increases and
         decrease the likelihood of the model repeating the same statements verbatim.
         Supported range is [-2, 2]. Default value is None.
        :paramtype frequency_penalty: float
        :keyword stream_parameter: A value indicating whether chat completions should be streamed for
         this request. Default value is None.
        :paramtype stream_parameter: bool
        :keyword presence_penalty: A value that influences the probability of generated tokens
         appearing based on their existing
         presence in generated text.
         Positive values will make tokens less likely to appear when they already exist and increase
         the
         model's likelihood to output new topics.
         Supported range is [-2, 2]. Default value is None.
        :paramtype presence_penalty: float
        :keyword temperature: The sampling temperature to use that controls the apparent creativity of
         generated completions.
         Higher values will make output more random while lower values will make results more focused
         and deterministic.
         It is not recommended to modify temperature and top_p for the same completions request as the
         interaction of these two settings is difficult to predict.
         Supported range is [0, 1]. Default value is None.
        :paramtype temperature: float
        :keyword top_p: An alternative to sampling with temperature called nucleus sampling. This value
         causes the
         model to consider the results of tokens with the provided probability mass. As an example, a
         value of 0.15 will cause only the tokens comprising the top 15% of probability mass to be
         considered.
         It is not recommended to modify temperature and top_p for the same completions request as the
         interaction of these two settings is difficult to predict.
         Supported range is [0, 1]. Default value is None.
        :paramtype top_p: float
        :keyword max_tokens: The maximum number of tokens to generate. Default value is None.
        :paramtype max_tokens: int
        :keyword response_format: An object specifying the format that the model must output.

         Setting to ``{ "type": "json_schema", "json_schema": {...} }`` enables Structured Outputs
         which ensures the model will match your supplied JSON schema.

         Setting to ``{ "type": "json_object" }`` enables JSON mode, which ensures the message the
         model generates is valid JSON.

         **Important:** when using JSON mode, you **must** also instruct the model to produce JSON
         yourself via a system or user message. Without this, the model may generate an unending stream
         of whitespace until the generation reaches the token limit, resulting in a long-running and
         seemingly "stuck" request. Also note that the message content may be partially cut off if
         ``finish_reason="length"``\\ , which indicates the generation exceeded ``max_tokens`` or the
         conversation exceeded the max context length. Default value is None.
        :paramtype response_format: ~azure.ai.inference.models._models.ChatCompletionsResponseFormat
        :keyword stop: A collection of textual sequences that will end completions generation. Default
         value is None.
        :paramtype stop: list[str]
        :keyword tools: A list of tools the model may request to call. Currently, only functions are
         supported as a tool. The model
         may response with a function call request and provide the input arguments in JSON format for
         that function. Default value is None.
        :paramtype tools: list[~azure.ai.inference.models.ChatCompletionsToolDefinition]
        :keyword tool_choice: If specified, the model will configure which of the provided tools it can
         use for the chat completions response. Is either a Union[str,
         "_models.ChatCompletionsToolChoicePreset"] type or a ChatCompletionsNamedToolChoice type.
         Default value is None.
        :paramtype tool_choice: str or ~azure.ai.inference.models.ChatCompletionsToolChoicePreset or
         ~azure.ai.inference.models.ChatCompletionsNamedToolChoice
        :keyword seed: If specified, the system will make a best effort to sample deterministically
         such that repeated requests with the
         same seed and parameters should return the same result. Determinism is not guaranteed. Default
         value is None.
        :paramtype seed: int
        :keyword model: ID of the specific AI model to use, if more than one model is available on the
         endpoint. Default value is None.
        :paramtype model: str
        :return: ChatCompletions. The ChatCompletions is compatible with MutableMapping
        :rtype: ~azure.ai.inference.models.ChatCompletions
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ChatCompletions] = kwargs.pop("cls", None)

        if body is _Unset:
            if messages is _Unset:
                raise TypeError("missing required argument: messages")
            body = {
                "frequency_penalty": frequency_penalty,
                "max_tokens": max_tokens,
                "messages": messages,
                "model": model,
                "presence_penalty": presence_penalty,
                "response_format": response_format,
                "seed": seed,
                "stop": stop,
                "stream": stream_parameter,
                "temperature": temperature,
                "tool_choice": tool_choice,
                "tools": tools,
                "top_p": top_p,
            }
            body = {k: v for k, v in body.items() if v is not None}
        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_chat_completions_complete_request(
            extra_params=extra_params,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.ChatCompletions, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def _get_model_info(self, **kwargs: Any) -> _models.ModelInfo:
        """Returns information about the AI model.
        The method makes a REST API call to the ``/info`` route on the given endpoint.
        This method will only work when using Serverless API or Managed Compute endpoint.
        It will not work for GitHub Models endpoint or Azure OpenAI endpoint.

        :return: ModelInfo. The ModelInfo is compatible with MutableMapping
        :rtype: ~azure.ai.inference.models.ModelInfo
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.ModelInfo] = kwargs.pop("cls", None)

        _request = build_chat_completions_get_model_info_request(
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.ModelInfo, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore


class EmbeddingsClientOperationsMixin(EmbeddingsClientMixinABC):

    @overload
    async def _embed(
        self,
        body: JSON,
        *,
        extra_params: Optional[Union[str, _models._enums.ExtraParameters]] = None,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.EmbeddingsResult: ...
    @overload
    async def _embed(
        self,
        *,
        input: List[str],
        extra_params: Optional[Union[str, _models._enums.ExtraParameters]] = None,
        content_type: str = "application/json",
        dimensions: Optional[int] = None,
        encoding_format: Optional[Union[str, _models.EmbeddingEncodingFormat]] = None,
        input_type: Optional[Union[str, _models.EmbeddingInputType]] = None,
        model: Optional[str] = None,
        **kwargs: Any
    ) -> _models.EmbeddingsResult: ...
    @overload
    async def _embed(
        self,
        body: IO[bytes],
        *,
        extra_params: Optional[Union[str, _models._enums.ExtraParameters]] = None,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.EmbeddingsResult: ...

    @distributed_trace_async
    async def _embed(
        self,
        body: Union[JSON, IO[bytes]] = _Unset,
        *,
        input: List[str] = _Unset,
        extra_params: Optional[Union[str, _models._enums.ExtraParameters]] = None,
        dimensions: Optional[int] = None,
        encoding_format: Optional[Union[str, _models.EmbeddingEncodingFormat]] = None,
        input_type: Optional[Union[str, _models.EmbeddingInputType]] = None,
        model: Optional[str] = None,
        **kwargs: Any
    ) -> _models.EmbeddingsResult:
        """Return the embedding vectors for given text prompts.
        The method makes a REST API call to the ``/embeddings`` route on the given endpoint.

        :param body: Is either a JSON type or a IO[bytes] type. Required.
        :type body: JSON or IO[bytes]
        :keyword input: Input text to embed, encoded as a string or array of tokens.
         To embed multiple inputs in a single request, pass an array
         of strings or array of token arrays. Required.
        :paramtype input: list[str]
        :keyword extra_params: Controls what happens if extra parameters, undefined by the REST API,
         are passed in the JSON request payload.
         This sets the HTTP request header ``extra-parameters``. Known values are: "error", "drop", and
         "pass-through". Default value is None.
        :paramtype extra_params: str or ~azure.ai.inference.models.ExtraParameters
        :keyword dimensions: Optional. The number of dimensions the resulting output embeddings should
         have.
         Passing null causes the model to use its default value.
         Returns a 422 error if the model doesn't support the value or parameter. Default value is
         None.
        :paramtype dimensions: int
        :keyword encoding_format: Optional. The desired format for the returned embeddings. Known
         values are: "base64", "binary", "float", "int8", "ubinary", and "uint8". Default value is None.
        :paramtype encoding_format: str or ~azure.ai.inference.models.EmbeddingEncodingFormat
        :keyword input_type: Optional. The type of the input.
         Returns a 422 error if the model doesn't support the value or parameter. Known values are:
         "text", "query", and "document". Default value is None.
        :paramtype input_type: str or ~azure.ai.inference.models.EmbeddingInputType
        :keyword model: ID of the specific AI model to use, if more than one model is available on the
         endpoint. Default value is None.
        :paramtype model: str
        :return: EmbeddingsResult. The EmbeddingsResult is compatible with MutableMapping
        :rtype: ~azure.ai.inference.models.EmbeddingsResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.EmbeddingsResult] = kwargs.pop("cls", None)

        if body is _Unset:
            if input is _Unset:
                raise TypeError("missing required argument: input")
            body = {
                "dimensions": dimensions,
                "encoding_format": encoding_format,
                "input": input,
                "input_type": input_type,
                "model": model,
            }
            body = {k: v for k, v in body.items() if v is not None}
        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_embeddings_embed_request(
            extra_params=extra_params,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.EmbeddingsResult, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def _get_model_info(self, **kwargs: Any) -> _models.ModelInfo:
        """Returns information about the AI model.
        The method makes a REST API call to the ``/info`` route on the given endpoint.
        This method will only work when using Serverless API or Managed Compute endpoint.
        It will not work for GitHub Models endpoint or Azure OpenAI endpoint.

        :return: ModelInfo. The ModelInfo is compatible with MutableMapping
        :rtype: ~azure.ai.inference.models.ModelInfo
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.ModelInfo] = kwargs.pop("cls", None)

        _request = build_embeddings_get_model_info_request(
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.ModelInfo, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore


class ImageEmbeddingsClientOperationsMixin(ImageEmbeddingsClientMixinABC):

    @overload
    async def _embed(
        self,
        body: JSON,
        *,
        extra_params: Optional[Union[str, _models._enums.ExtraParameters]] = None,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.EmbeddingsResult: ...
    @overload
    async def _embed(
        self,
        *,
        input: List[_models.ImageEmbeddingInput],
        extra_params: Optional[Union[str, _models._enums.ExtraParameters]] = None,
        content_type: str = "application/json",
        dimensions: Optional[int] = None,
        encoding_format: Optional[Union[str, _models.EmbeddingEncodingFormat]] = None,
        input_type: Optional[Union[str, _models.EmbeddingInputType]] = None,
        model: Optional[str] = None,
        **kwargs: Any
    ) -> _models.EmbeddingsResult: ...
    @overload
    async def _embed(
        self,
        body: IO[bytes],
        *,
        extra_params: Optional[Union[str, _models._enums.ExtraParameters]] = None,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.EmbeddingsResult: ...

    @distributed_trace_async
    async def _embed(
        self,
        body: Union[JSON, IO[bytes]] = _Unset,
        *,
        input: List[_models.ImageEmbeddingInput] = _Unset,
        extra_params: Optional[Union[str, _models._enums.ExtraParameters]] = None,
        dimensions: Optional[int] = None,
        encoding_format: Optional[Union[str, _models.EmbeddingEncodingFormat]] = None,
        input_type: Optional[Union[str, _models.EmbeddingInputType]] = None,
        model: Optional[str] = None,
        **kwargs: Any
    ) -> _models.EmbeddingsResult:
        """Return the embedding vectors for given images.
        The method makes a REST API call to the ``/images/embeddings`` route on the given endpoint.

        :param body: Is either a JSON type or a IO[bytes] type. Required.
        :type body: JSON or IO[bytes]
        :keyword input: Input image to embed. To embed multiple inputs in a single request, pass an
         array.
         The input must not exceed the max input tokens for the model. Required.
        :paramtype input: list[~azure.ai.inference.models.ImageEmbeddingInput]
        :keyword extra_params: Controls what happens if extra parameters, undefined by the REST API,
         are passed in the JSON request payload.
         This sets the HTTP request header ``extra-parameters``. Known values are: "error", "drop", and
         "pass-through". Default value is None.
        :paramtype extra_params: str or ~azure.ai.inference.models.ExtraParameters
        :keyword dimensions: Optional. The number of dimensions the resulting output embeddings should
         have.
         Passing null causes the model to use its default value.
         Returns a 422 error if the model doesn't support the value or parameter. Default value is
         None.
        :paramtype dimensions: int
        :keyword encoding_format: Optional. The number of dimensions the resulting output embeddings
         should have.
         Passing null causes the model to use its default value.
         Returns a 422 error if the model doesn't support the value or parameter. Known values are:
         "base64", "binary", "float", "int8", "ubinary", and "uint8". Default value is None.
        :paramtype encoding_format: str or ~azure.ai.inference.models.EmbeddingEncodingFormat
        :keyword input_type: Optional. The type of the input.
         Returns a 422 error if the model doesn't support the value or parameter. Known values are:
         "text", "query", and "document". Default value is None.
        :paramtype input_type: str or ~azure.ai.inference.models.EmbeddingInputType
        :keyword model: ID of the specific AI model to use, if more than one model is available on the
         endpoint. Default value is None.
        :paramtype model: str
        :return: EmbeddingsResult. The EmbeddingsResult is compatible with MutableMapping
        :rtype: ~azure.ai.inference.models.EmbeddingsResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.EmbeddingsResult] = kwargs.pop("cls", None)

        if body is _Unset:
            if input is _Unset:
                raise TypeError("missing required argument: input")
            body = {
                "dimensions": dimensions,
                "encoding_format": encoding_format,
                "input": input,
                "input_type": input_type,
                "model": model,
            }
            body = {k: v for k, v in body.items() if v is not None}
        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_image_embeddings_embed_request(
            extra_params=extra_params,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.EmbeddingsResult, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def _get_model_info(self, **kwargs: Any) -> _models.ModelInfo:
        """Returns information about the AI model.
        The method makes a REST API call to the ``/info`` route on the given endpoint.
        This method will only work when using Serverless API or Managed Compute endpoint.
        It will not work for GitHub Models endpoint or Azure OpenAI endpoint.

        :return: ModelInfo. The ModelInfo is compatible with MutableMapping
        :rtype: ~azure.ai.inference.models.ModelInfo
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.ModelInfo] = kwargs.pop("cls", None)

        _request = build_image_embeddings_get_model_info_request(
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.ModelInfo, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
