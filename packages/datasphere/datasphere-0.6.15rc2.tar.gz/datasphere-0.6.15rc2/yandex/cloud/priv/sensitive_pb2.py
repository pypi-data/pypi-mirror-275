# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/priv/sensitive.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!yandex/cloud/priv/sensitive.proto\x12\x11yandex.cloud.priv\x1a google/protobuf/descriptor.proto*\xc1\x02\n\rSensitiveType\x12\x1e\n\x1aSENSITIVE_TYPE_UNSPECIFIED\x10\x00\x12\x11\n\rSENSITIVE_CRC\x10\x01\x12\x17\n\x13SENSITIVE_IAM_TOKEN\x10\x02\x12\x14\n\x10SENSITIVE_REMOVE\x10\x03\x12)\n%SENSITIVE_YANDEX_PASSPORT_OAUTH_TOKEN\x10\x04\x12\x18\n\x14SENSITIVE_IAM_COOKIE\x10\x05\x12\x1b\n\x17SENSITIVE_REFRESH_TOKEN\x10\x06\x12\x11\n\rSENSITIVE_JWT\x10\x07\x12\x1b\n\x17SENSITIVE_COOKIE_HEADER\x10\x08\x12\x1f\n\x1bSENSITIVE_SET_COOKIE_HEADER\x10\t\x12\x1b\n\x17SENSITIVE_SESSION_TOKEN\x10\n:2\n\tsensitive\x12\x1d.google.protobuf.FieldOptions\x18\xf9\x91\x06 \x01(\x08:Y\n\x0esensitive_type\x12\x1d.google.protobuf.FieldOptions\x18\xfa\x91\x06 \x01(\x0e\x32 .yandex.cloud.priv.SensitiveTypeB\x07Z\x05\x63loudb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.priv.sensitive_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\005cloud'
  _globals['_SENSITIVETYPE']._serialized_start=91
  _globals['_SENSITIVETYPE']._serialized_end=412
# @@protoc_insertion_point(module_scope)
