"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
*!
Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022-2024)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import streamlit.proto.LabelVisibilityMessage_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Checkbox(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _StyleType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StyleTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Checkbox._StyleType.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        DEFAULT: Checkbox._StyleType.ValueType  # 0
        TOGGLE: Checkbox._StyleType.ValueType  # 1

    class StyleType(_StyleType, metaclass=_StyleTypeEnumTypeWrapper): ...
    DEFAULT: Checkbox.StyleType.ValueType  # 0
    TOGGLE: Checkbox.StyleType.ValueType  # 1

    ID_FIELD_NUMBER: builtins.int
    LABEL_FIELD_NUMBER: builtins.int
    DEFAULT_FIELD_NUMBER: builtins.int
    HELP_FIELD_NUMBER: builtins.int
    FORM_ID_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    SET_VALUE_FIELD_NUMBER: builtins.int
    DISABLED_FIELD_NUMBER: builtins.int
    LABEL_VISIBILITY_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    id: builtins.str
    label: builtins.str
    default: builtins.bool
    help: builtins.str
    form_id: builtins.str
    value: builtins.bool
    set_value: builtins.bool
    disabled: builtins.bool
    @property
    def label_visibility(self) -> streamlit.proto.LabelVisibilityMessage_pb2.LabelVisibilityMessage: ...
    type: global___Checkbox.StyleType.ValueType
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        label: builtins.str = ...,
        default: builtins.bool = ...,
        help: builtins.str = ...,
        form_id: builtins.str = ...,
        value: builtins.bool = ...,
        set_value: builtins.bool = ...,
        disabled: builtins.bool = ...,
        label_visibility: streamlit.proto.LabelVisibilityMessage_pb2.LabelVisibilityMessage | None = ...,
        type: global___Checkbox.StyleType.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["label_visibility", b"label_visibility"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["default", b"default", "disabled", b"disabled", "form_id", b"form_id", "help", b"help", "id", b"id", "label", b"label", "label_visibility", b"label_visibility", "set_value", b"set_value", "type", b"type", "value", b"value"]) -> None: ...

global___Checkbox = Checkbox
