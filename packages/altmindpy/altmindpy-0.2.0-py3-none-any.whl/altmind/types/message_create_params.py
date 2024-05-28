# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "MessageCreateParams",
    "ContentUnionMember1",
    "ContentUnionMember1TextContent",
    "ContentUnionMember1TextContentText",
    "ContentUnionMember1ImageFileContent",
    "ContentUnionMember1ImageFileContentImageFile",
    "ContentUnionMember1ToolContent",
    "ContentUnionMember1ToolContentTool",
]


class MessageCreateParams(TypedDict, total=False):
    content: Required[Union[str, Iterable[ContentUnionMember1]]]

    message_metadata: object

    original_role: Optional[Literal["user", "assistant", "system", "tool"]]

    role: Optional[Literal["user", "assistant", "system", "tool"]]

    thread_id: Optional[int]

    tool_calls: Optional[Iterable[object]]


class ContentUnionMember1TextContentText(TypedDict, total=False):
    value: Required[str]


class ContentUnionMember1TextContent(TypedDict, total=False):
    text: Required[ContentUnionMember1TextContentText]

    type: Literal["text"]


class ContentUnionMember1ImageFileContentImageFile(TypedDict, total=False):
    file_id: Required[str]


class ContentUnionMember1ImageFileContent(TypedDict, total=False):
    image_file: Required[ContentUnionMember1ImageFileContentImageFile]

    type: Literal["image_file"]


class ContentUnionMember1ToolContentTool(TypedDict, total=False):
    content: Optional[object]

    name: Optional[str]

    tool_call_id: Optional[str]


class ContentUnionMember1ToolContent(TypedDict, total=False):
    tool: Required[ContentUnionMember1ToolContentTool]

    type: Literal["tool"]


ContentUnionMember1 = Union[
    ContentUnionMember1TextContent, ContentUnionMember1ImageFileContent, ContentUnionMember1ToolContent
]
