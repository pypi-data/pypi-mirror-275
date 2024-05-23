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
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Text(google.protobuf.message.Message):
    """Preformatted text"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BODY_FIELD_NUMBER: builtins.int
    HELP_FIELD_NUMBER: builtins.int
    body: builtins.str
    """Content to display."""
    help: builtins.str
    def __init__(
        self,
        *,
        body: builtins.str = ...,
        help: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["body", b"body", "help", b"help"]) -> None: ...

global___Text = Text
