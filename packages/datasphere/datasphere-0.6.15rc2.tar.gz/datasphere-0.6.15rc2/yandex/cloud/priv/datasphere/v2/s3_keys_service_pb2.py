# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/priv/datasphere/v2/s3_keys_service.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.priv import sensitive_pb2 as yandex_dot_cloud_dot_priv_dot_sensitive__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5yandex/cloud/priv/datasphere/v2/s3_keys_service.proto\x12\x1fyandex.cloud.priv.datasphere.v2\x1a!yandex/cloud/priv/sensitive.proto\"&\n\x10GetS3KeysRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\"M\n\x11GetS3KeysResponse\x12\x1b\n\rs3_access_key\x18\x01 \x01(\tB\x04\xc8\x8f\x31\x01\x12\x1b\n\rs3_secret_key\x18\x02 \x01(\tB\x04\xc8\x8f\x31\x01\x32\x83\x01\n\rS3KeysService\x12r\n\tGetS3Keys\x12\x31.yandex.cloud.priv.datasphere.v2.GetS3KeysRequest\x1a\x32.yandex.cloud.priv.datasphere.v2.GetS3KeysResponseB8\n\"yandex.cloud.priv.datasphere.v2ydsB\x06\x44SS3KSZ\ndatasphereb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.priv.datasphere.v2.s3_keys_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"yandex.cloud.priv.datasphere.v2ydsB\006DSS3KSZ\ndatasphere'
  _globals['_GETS3KEYSRESPONSE'].fields_by_name['s3_access_key']._options = None
  _globals['_GETS3KEYSRESPONSE'].fields_by_name['s3_access_key']._serialized_options = b'\310\2171\001'
  _globals['_GETS3KEYSRESPONSE'].fields_by_name['s3_secret_key']._options = None
  _globals['_GETS3KEYSRESPONSE'].fields_by_name['s3_secret_key']._serialized_options = b'\310\2171\001'
  _globals['_GETS3KEYSREQUEST']._serialized_start=125
  _globals['_GETS3KEYSREQUEST']._serialized_end=163
  _globals['_GETS3KEYSRESPONSE']._serialized_start=165
  _globals['_GETS3KEYSRESPONSE']._serialized_end=242
  _globals['_S3KEYSSERVICE']._serialized_start=245
  _globals['_S3KEYSSERVICE']._serialized_end=376
# @@protoc_insertion_point(module_scope)
