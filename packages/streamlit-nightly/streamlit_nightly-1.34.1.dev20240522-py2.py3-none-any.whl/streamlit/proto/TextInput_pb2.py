# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streamlit/proto/TextInput.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from streamlit.proto import LabelVisibilityMessage_pb2 as streamlit_dot_proto_dot_LabelVisibilityMessage__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fstreamlit/proto/TextInput.proto\x1a,streamlit/proto/LabelVisibilityMessage.proto\"\xdd\x02\n\tTextInput\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12\x14\n\x07\x64\x65\x66\x61ult\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x1d\n\x04type\x18\x04 \x01(\x0e\x32\x0f.TextInput.Type\x12\x11\n\tmax_chars\x18\x05 \x01(\r\x12\x0c\n\x04help\x18\x06 \x01(\t\x12\x0f\n\x07\x66orm_id\x18\x07 \x01(\t\x12\x12\n\x05value\x18\x08 \x01(\tH\x01\x88\x01\x01\x12\x11\n\tset_value\x18\t \x01(\x08\x12\x14\n\x0c\x61utocomplete\x18\n \x01(\t\x12\x13\n\x0bplaceholder\x18\x0b \x01(\t\x12\x10\n\x08\x64isabled\x18\x0c \x01(\x08\x12\x31\n\x10label_visibility\x18\r \x01(\x0b\x32\x17.LabelVisibilityMessage\"!\n\x04Type\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x0c\n\x08PASSWORD\x10\x01\x42\n\n\x08_defaultB\x08\n\x06_valueB.\n\x1c\x63om.snowflake.apps.streamlitB\x0eTextInputProtob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'streamlit.proto.TextInput_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034com.snowflake.apps.streamlitB\016TextInputProto'
  _TEXTINPUT._serialized_start=82
  _TEXTINPUT._serialized_end=431
  _TEXTINPUT_TYPE._serialized_start=376
  _TEXTINPUT_TYPE._serialized_end=409
# @@protoc_insertion_point(module_scope)
