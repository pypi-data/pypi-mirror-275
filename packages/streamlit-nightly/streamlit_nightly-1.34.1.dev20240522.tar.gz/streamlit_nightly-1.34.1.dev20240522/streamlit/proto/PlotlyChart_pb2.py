# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streamlit/proto/PlotlyChart.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!streamlit/proto/PlotlyChart.proto\"\x98\x02\n\x0bPlotlyChart\x12\x1b\n\x13use_container_width\x18\x05 \x01(\x08\x12\r\n\x05theme\x18\x06 \x01(\t\x12\n\n\x02id\x18\x07 \x01(\t\x12\x32\n\x0eselection_mode\x18\x08 \x03(\x0e\x32\x1a.PlotlyChart.SelectionMode\x12\x0f\n\x07\x66orm_id\x18\t \x01(\t\x12\x0c\n\x04spec\x18\n \x01(\t\x12\x0e\n\x06\x63onfig\x18\x0b \x01(\t\x12\r\n\x03url\x18\x01 \x01(\tH\x00\x12\x19\n\x06\x66igure\x18\x02 \x01(\x0b\x32\x07.FigureH\x00\"/\n\rSelectionMode\x12\n\n\x06POINTS\x10\x00\x12\x07\n\x03\x42OX\x10\x01\x12\t\n\x05LASSO\x10\x02\x42\x07\n\x05\x63hartJ\x04\x08\x03\x10\x04J\x04\x08\x04\x10\x05\"&\n\x06\x46igure\x12\x0c\n\x04spec\x18\x01 \x01(\t\x12\x0e\n\x06\x63onfig\x18\x02 \x01(\tB0\n\x1c\x63om.snowflake.apps.streamlitB\x10PlotlyChartProtob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'streamlit.proto.PlotlyChart_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034com.snowflake.apps.streamlitB\020PlotlyChartProto'
  _PLOTLYCHART._serialized_start=38
  _PLOTLYCHART._serialized_end=318
  _PLOTLYCHART_SELECTIONMODE._serialized_start=250
  _PLOTLYCHART_SELECTIONMODE._serialized_end=297
  _FIGURE._serialized_start=320
  _FIGURE._serialized_end=358
# @@protoc_insertion_point(module_scope)
