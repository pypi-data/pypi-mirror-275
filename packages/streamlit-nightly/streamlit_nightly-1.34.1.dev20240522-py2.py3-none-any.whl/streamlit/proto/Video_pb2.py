# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streamlit/proto/Video.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bstreamlit/proto/Video.proto\"+\n\rSubtitleTrack\x12\r\n\x05label\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\"\x87\x02\n\x05Video\x12\x0b\n\x03url\x18\x06 \x01(\t\x12\x12\n\nstart_time\x18\x03 \x01(\x05\x12\x19\n\x04type\x18\x05 \x01(\x0e\x32\x0b.Video.Type\x12!\n\tsubtitles\x18\x07 \x03(\x0b\x32\x0e.SubtitleTrack\x12\x10\n\x08\x65nd_time\x18\x08 \x01(\x05\x12\x0c\n\x04loop\x18\t \x01(\x08\x12\x10\n\x08\x61utoplay\x18\n \x01(\x08\x12\r\n\x05muted\x18\x0b \x01(\x08\x12\n\n\x02id\x18\x0c \x01(\t\"2\n\x04Type\x12\n\n\x06UNUSED\x10\x00\x12\n\n\x06NATIVE\x10\x01\x12\x12\n\x0eYOUTUBE_IFRAME\x10\x02J\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03J\x04\x08\x04\x10\x05R\x06\x66ormatR\x04\x64\x61taB*\n\x1c\x63om.snowflake.apps.streamlitB\nVideoProtob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'streamlit.proto.Video_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034com.snowflake.apps.streamlitB\nVideoProto'
  _SUBTITLETRACK._serialized_start=31
  _SUBTITLETRACK._serialized_end=74
  _VIDEO._serialized_start=77
  _VIDEO._serialized_end=340
  _VIDEO_TYPE._serialized_start=258
  _VIDEO_TYPE._serialized_end=308
# @@protoc_insertion_point(module_scope)
