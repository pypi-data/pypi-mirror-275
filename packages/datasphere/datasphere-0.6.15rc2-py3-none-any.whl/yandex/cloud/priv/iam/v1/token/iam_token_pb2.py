# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/priv/iam/v1/token/iam_token.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud.priv import sensitive_pb2 as yandex_dot_cloud_dot_priv_dot_sensitive__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.yandex/cloud/priv/iam/v1/token/iam_token.proto\x12\x18yandex.cloud.priv.iam.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a!yandex/cloud/priv/sensitive.proto\"W\n\x08IamToken\x12\x1b\n\tiam_token\x18\x01 \x01(\tB\x08\xc8\x8f\x31\x01\xd0\x8f\x31\x02\x12.\n\nexpires_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\nB\x03PITZ\x03iamb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.priv.iam.v1.token.iam_token_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'B\003PITZ\003iam'
  _globals['_IAMTOKEN'].fields_by_name['iam_token']._options = None
  _globals['_IAMTOKEN'].fields_by_name['iam_token']._serialized_options = b'\310\2171\001\320\2171\002'
  _globals['_IAMTOKEN']._serialized_start=144
  _globals['_IAMTOKEN']._serialized_end=231
# @@protoc_insertion_point(module_scope)
