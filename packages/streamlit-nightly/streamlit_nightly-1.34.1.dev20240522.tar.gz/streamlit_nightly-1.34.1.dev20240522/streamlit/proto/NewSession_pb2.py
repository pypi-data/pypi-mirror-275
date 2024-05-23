# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streamlit/proto/NewSession.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from streamlit.proto import AppPage_pb2 as streamlit_dot_proto_dot_AppPage__pb2
from streamlit.proto import SessionStatus_pb2 as streamlit_dot_proto_dot_SessionStatus__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n streamlit/proto/NewSession.proto\x1a\x1dstreamlit/proto/AppPage.proto\x1a#streamlit/proto/SessionStatus.proto\"\x8b\x02\n\nNewSession\x12\x1f\n\ninitialize\x18\x01 \x01(\x0b\x32\x0b.Initialize\x12\x15\n\rscript_run_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x18\n\x10main_script_path\x18\x04 \x01(\t\x12\x17\n\x06\x63onfig\x18\x06 \x01(\x0b\x32\x07.Config\x12(\n\x0c\x63ustom_theme\x18\x07 \x01(\x0b\x32\x12.CustomThemeConfig\x12\x1b\n\tapp_pages\x18\x08 \x03(\x0b\x32\x08.AppPage\x12\x18\n\x10page_script_hash\x18\t \x01(\t\x12\x1d\n\x15\x66ragment_ids_this_run\x18\n \x03(\tJ\x04\x08\x05\x10\x06\"\xba\x01\n\nInitialize\x12\x1c\n\tuser_info\x18\x01 \x01(\x0b\x32\t.UserInfo\x12*\n\x10\x65nvironment_info\x18\x03 \x01(\x0b\x32\x10.EnvironmentInfo\x12&\n\x0esession_status\x18\x04 \x01(\x0b\x32\x0e.SessionStatus\x12\x14\n\x0c\x63ommand_line\x18\x05 \x01(\t\x12\x12\n\nsession_id\x18\x06 \x01(\t\x12\x10\n\x08is_hello\x18\x07 \x01(\x08\"\x97\x02\n\x06\x43onfig\x12\x1a\n\x12gather_usage_stats\x18\x02 \x01(\x08\x12\x1e\n\x16max_cached_message_age\x18\x03 \x01(\x05\x12\x14\n\x0cmapbox_token\x18\x04 \x01(\t\x12\x19\n\x11\x61llow_run_on_save\x18\x05 \x01(\x08\x12\x14\n\x0chide_top_bar\x18\x06 \x01(\x08\x12\x18\n\x10hide_sidebar_nav\x18\x07 \x01(\x08\x12)\n\x0ctoolbar_mode\x18\x08 \x01(\x0e\x32\x13.Config.ToolbarMode\"?\n\x0bToolbarMode\x12\x08\n\x04\x41UTO\x10\x00\x12\r\n\tDEVELOPER\x10\x01\x12\n\n\x06VIEWER\x10\x02\x12\x0b\n\x07MINIMAL\x10\x03J\x04\x08\x01\x10\x02\"\x8c\x04\n\x11\x43ustomThemeConfig\x12\x15\n\rprimary_color\x18\x01 \x01(\t\x12\"\n\x1asecondary_background_color\x18\x02 \x01(\t\x12\x18\n\x10\x62\x61\x63kground_color\x18\x03 \x01(\t\x12\x12\n\ntext_color\x18\x04 \x01(\t\x12+\n\x04\x66ont\x18\x05 \x01(\x0e\x32\x1d.CustomThemeConfig.FontFamily\x12*\n\x04\x62\x61se\x18\x06 \x01(\x0e\x32\x1c.CustomThemeConfig.BaseTheme\x12\x1f\n\x17widget_background_color\x18\x07 \x01(\t\x12\x1b\n\x13widget_border_color\x18\x08 \x01(\t\x12\x15\n\x05radii\x18\t \x01(\x0b\x32\x06.Radii\x12\x11\n\tbody_font\x18\r \x01(\t\x12\x11\n\tcode_font\x18\x0e \x01(\t\x12\x1d\n\nfont_faces\x18\x0f \x03(\x0b\x32\t.FontFace\x12\x1e\n\nfont_sizes\x18\x10 \x01(\x0b\x32\n.FontSizes\x12!\n\x19skeleton_background_color\x18\x11 \x01(\t\" \n\tBaseTheme\x12\t\n\x05LIGHT\x10\x00\x12\x08\n\x04\x44\x41RK\x10\x01\"6\n\nFontFamily\x12\x0e\n\nSANS_SERIF\x10\x00\x12\t\n\x05SERIF\x10\x01\x12\r\n\tMONOSPACE\x10\x02\"F\n\x08\x46ontFace\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x0e\n\x06\x66\x61mily\x18\x02 \x01(\t\x12\x0e\n\x06weight\x18\x03 \x01(\x05\x12\r\n\x05style\x18\x04 \x01(\t\"<\n\x05Radii\x12\x1a\n\x12\x62\x61se_widget_radius\x18\x01 \x01(\x05\x12\x17\n\x0f\x63heckbox_radius\x18\x02 \x01(\x05\"T\n\tFontSizes\x12\x16\n\x0etiny_font_size\x18\x01 \x01(\x05\x12\x17\n\x0fsmall_font_size\x18\x02 \x01(\x05\x12\x16\n\x0e\x62\x61se_font_size\x18\x03 \x01(\x05\"E\n\x08UserInfo\x12\x17\n\x0finstallation_id\x18\x01 \x01(\t\x12\x1a\n\x12installation_id_v3\x18\x05 \x01(\tJ\x04\x08\x02\x10\x03\"D\n\x0f\x45nvironmentInfo\x12\x19\n\x11streamlit_version\x18\x01 \x01(\t\x12\x16\n\x0epython_version\x18\x02 \x01(\tB/\n\x1c\x63om.snowflake.apps.streamlitB\x0fNewSessionProtob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'streamlit.proto.NewSession_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034com.snowflake.apps.streamlitB\017NewSessionProto'
  _NEWSESSION._serialized_start=105
  _NEWSESSION._serialized_end=372
  _INITIALIZE._serialized_start=375
  _INITIALIZE._serialized_end=561
  _CONFIG._serialized_start=564
  _CONFIG._serialized_end=843
  _CONFIG_TOOLBARMODE._serialized_start=774
  _CONFIG_TOOLBARMODE._serialized_end=837
  _CUSTOMTHEMECONFIG._serialized_start=846
  _CUSTOMTHEMECONFIG._serialized_end=1370
  _CUSTOMTHEMECONFIG_BASETHEME._serialized_start=1282
  _CUSTOMTHEMECONFIG_BASETHEME._serialized_end=1314
  _CUSTOMTHEMECONFIG_FONTFAMILY._serialized_start=1316
  _CUSTOMTHEMECONFIG_FONTFAMILY._serialized_end=1370
  _FONTFACE._serialized_start=1372
  _FONTFACE._serialized_end=1442
  _RADII._serialized_start=1444
  _RADII._serialized_end=1504
  _FONTSIZES._serialized_start=1506
  _FONTSIZES._serialized_end=1590
  _USERINFO._serialized_start=1592
  _USERINFO._serialized_end=1661
  _ENVIRONMENTINFO._serialized_start=1663
  _ENVIRONMENTINFO._serialized_end=1731
# @@protoc_insertion_point(module_scope)
