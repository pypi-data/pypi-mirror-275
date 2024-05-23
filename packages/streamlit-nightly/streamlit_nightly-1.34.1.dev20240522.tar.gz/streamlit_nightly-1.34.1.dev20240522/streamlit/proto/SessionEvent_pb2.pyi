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
import streamlit.proto.Exception_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class SessionEvent(google.protobuf.message.Message):
    """A transient event sent to all browsers connected to an associated app."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SCRIPT_CHANGED_ON_DISK_FIELD_NUMBER: builtins.int
    SCRIPT_WAS_MANUALLY_STOPPED_FIELD_NUMBER: builtins.int
    SCRIPT_COMPILATION_EXCEPTION_FIELD_NUMBER: builtins.int
    script_changed_on_disk: builtins.bool
    """The app's script changed on disk, but is *not* being re-run
    automatically. The browser should prompt the user to re-run.
    """
    script_was_manually_stopped: builtins.bool
    """The app's script was running, but it was manually stopped before
    completion.
    """
    @property
    def script_compilation_exception(self) -> streamlit.proto.Exception_pb2.Exception:
        """Script compilation failed with an exception.
        We can't start running the script.
        """
    def __init__(
        self,
        *,
        script_changed_on_disk: builtins.bool = ...,
        script_was_manually_stopped: builtins.bool = ...,
        script_compilation_exception: streamlit.proto.Exception_pb2.Exception | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["script_changed_on_disk", b"script_changed_on_disk", "script_compilation_exception", b"script_compilation_exception", "script_was_manually_stopped", b"script_was_manually_stopped", "type", b"type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["script_changed_on_disk", b"script_changed_on_disk", "script_compilation_exception", b"script_compilation_exception", "script_was_manually_stopped", b"script_was_manually_stopped", "type", b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["type", b"type"]) -> typing_extensions.Literal["script_changed_on_disk", "script_was_manually_stopped", "script_compilation_exception"] | None: ...

global___SessionEvent = SessionEvent
