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
import streamlit.proto.Arrow_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class ArrowNamedDataSet(google.protobuf.message.Message):
    """A dataset that can be referenced by name."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    HAS_NAME_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    name: builtins.str
    """The dataset name."""
    has_name: builtins.bool
    """True if the name field (above) was manually set. This is used to get
    around proto3 not having a way to check whether something was set.
    """
    @property
    def data(self) -> streamlit.proto.Arrow_pb2.Arrow:
        """The data itself."""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        has_name: builtins.bool = ...,
        data: streamlit.proto.Arrow_pb2.Arrow | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["data", b"data"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["data", b"data", "has_name", b"has_name", "name", b"name"]) -> None: ...

global___ArrowNamedDataSet = ArrowNamedDataSet
