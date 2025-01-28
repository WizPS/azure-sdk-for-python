# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ChatCompletionsToolChoicePreset(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Represents a generic policy for how a chat completions tool may be selected."""

    AUTO = "auto"
    """Specifies that the model may either use any of the tools provided in this chat completions
    request or
    instead return a standard chat completions response as if no tools were provided."""
    NONE = "none"
    """Specifies that the model should not respond with a tool call and should instead provide a
    standard chat
    completions response. Response content may still be influenced by the provided tool
    definitions."""
    REQUIRED = "required"
    """Specifies that the model should respond with a call to one or more tools."""


class ChatRole(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """A description of the intended purpose of a message within a chat completions interaction."""

    SYSTEM = "system"
    """The role that instructs or sets the behavior of the assistant."""
    USER = "user"
    """The role that provides input for chat completions."""
    ASSISTANT = "assistant"
    """The role that provides responses to system-instructed, user-prompted input."""
    TOOL = "tool"
    """The role that represents extension tool activity within a chat completions operation."""


class CompletionsFinishReason(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Representation of the manner in which a completions response concluded."""

    STOPPED = "stop"
    """Completions ended normally and reached its end of token generation."""
    TOKEN_LIMIT_REACHED = "length"
    """Completions exhausted available token limits before generation could complete."""
    CONTENT_FILTERED = "content_filter"
    """Completions generated a response that was identified as potentially sensitive per content
    moderation policies."""
    TOOL_CALLS = "tool_calls"
    """Completion ended with the model calling a provided tool for output."""


class EmbeddingEncodingFormat(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The format of the embeddings result.
    Returns a 422 error if the model doesn't support the value or parameter.
    """

    BASE64 = "base64"
    """Base64"""
    BINARY = "binary"
    """Binary"""
    FLOAT = "float"
    """Floating point"""
    INT8 = "int8"
    """Signed 8-bit integer"""
    UBINARY = "ubinary"
    """ubinary"""
    UINT8 = "uint8"
    """Unsigned 8-bit integer"""


class EmbeddingInputType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Represents the input types used for embedding search."""

    TEXT = "text"
    """Indicates the input is a general text input."""
    QUERY = "query"
    """Indicates the input represents a search query to find the most relevant documents in your
    vector database."""
    DOCUMENT = "document"
    """Indicates the input represents a document that is stored in a vector database."""


class ExtraParameters(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Controls what happens if extra parameters, undefined by the REST API, are passed in the JSON
    request payload.
    """

    ERROR = "error"
    """The service will error if it detected extra parameters in the request payload. This is the
    service default."""
    DROP = "drop"
    """The service will ignore (drop) extra parameters in the request payload. It will only pass the
    known parameters to the back-end AI model."""
    PASS_THROUGH = "pass-through"
    """The service will pass extra parameters to the back-end AI model."""


class ImageDetailLevel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """A representation of the possible image detail levels for image-based chat completions message
    content.
    """

    AUTO = "auto"
    """Specifies that the model should determine which detail level to apply using heuristics like
    image size."""
    LOW = "low"
    """Specifies that image evaluation should be constrained to the 'low-res' model that may be faster
    and consume fewer
    tokens but may also be less accurate for highly detailed images."""
    HIGH = "high"
    """Specifies that image evaluation should enable the 'high-res' model that may be more accurate
    for highly detailed
    images but may also be slower and consume more tokens."""


class ModelType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of AI model."""

    EMBEDDINGS = "embeddings"
    """A model capable of generating embeddings from a text"""
    IMAGE_GENERATION = "image_generation"
    """A model capable of generating images from an image and text description"""
    TEXT_GENERATION = "text_generation"
    """A text generation model"""
    IMAGE_EMBEDDINGS = "image_embeddings"
    """A model capable of generating embeddings from an image"""
    AUDIO_GENERATION = "audio_generation"
    """A text-to-audio generative model"""
    CHAT_COMPLETION = "chat_completion"
    """A model capable of taking chat-formatted messages and generate responses"""
