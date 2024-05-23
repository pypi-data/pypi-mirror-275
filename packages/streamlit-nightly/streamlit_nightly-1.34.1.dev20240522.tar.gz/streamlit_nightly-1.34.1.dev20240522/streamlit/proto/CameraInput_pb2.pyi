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
import google.protobuf.message
import streamlit.proto.LabelVisibilityMessage_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class CameraInput(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    LABEL_FIELD_NUMBER: builtins.int
    HELP_FIELD_NUMBER: builtins.int
    FORM_ID_FIELD_NUMBER: builtins.int
    DISABLED_FIELD_NUMBER: builtins.int
    LABEL_VISIBILITY_FIELD_NUMBER: builtins.int
    id: builtins.str
    label: builtins.str
    help: builtins.str
    form_id: builtins.str
    disabled: builtins.bool
    @property
    def label_visibility(self) -> streamlit.proto.LabelVisibilityMessage_pb2.LabelVisibilityMessage: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        label: builtins.str = ...,
        help: builtins.str = ...,
        form_id: builtins.str = ...,
        disabled: builtins.bool = ...,
        label_visibility: streamlit.proto.LabelVisibilityMessage_pb2.LabelVisibilityMessage | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["label_visibility", b"label_visibility"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["disabled", b"disabled", "form_id", b"form_id", "help", b"help", "id", b"id", "label", b"label", "label_visibility", b"label_visibility"]) -> None: ...

global___CameraInput = CameraInput
