# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/priv/iam/v1/permission_stage.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.priv import validation_pb2 as yandex_dot_cloud_dot_priv_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/yandex/cloud/priv/iam/v1/permission_stage.proto\x12\x18yandex.cloud.priv.iam.v1\x1a\"yandex/cloud/priv/validation.proto\"2\n\x0fPermissionStage\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"B\n\x1dSetAllPermissionStagesRequest\x12!\n\x0bresource_id\x18\x01 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\"]\n\x1aSetPermissionStagesRequest\x12!\n\x0bresource_id\x18\x01 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\x12\x1c\n\x14permission_stage_ids\x18\x02 \x03(\t\"2\n\x1bSetPermissionStagesMetadata\x12\x13\n\x0bresource_id\x18\x01 \x01(\t\"\x89\x01\n\x1dUpdatePermissionStagesRequest\x12!\n\x0bresource_id\x18\x01 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\x12 \n\x18\x61\x64\x64_permission_stage_ids\x18\x02 \x03(\t\x12#\n\x1bremove_permission_stage_ids\x18\x03 \x03(\t\"5\n\x1eUpdatePermissionStagesMetadata\x12\x13\n\x0bresource_id\x18\x01 \x01(\tB\nB\x03PPSZ\x03iamb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.priv.iam.v1.permission_stage_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'B\003PPSZ\003iam'
  _globals['_SETALLPERMISSIONSTAGESREQUEST'].fields_by_name['resource_id']._options = None
  _globals['_SETALLPERMISSIONSTAGESREQUEST'].fields_by_name['resource_id']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_SETPERMISSIONSTAGESREQUEST'].fields_by_name['resource_id']._options = None
  _globals['_SETPERMISSIONSTAGESREQUEST'].fields_by_name['resource_id']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_UPDATEPERMISSIONSTAGESREQUEST'].fields_by_name['resource_id']._options = None
  _globals['_UPDATEPERMISSIONSTAGESREQUEST'].fields_by_name['resource_id']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_PERMISSIONSTAGE']._serialized_start=113
  _globals['_PERMISSIONSTAGE']._serialized_end=163
  _globals['_SETALLPERMISSIONSTAGESREQUEST']._serialized_start=165
  _globals['_SETALLPERMISSIONSTAGESREQUEST']._serialized_end=231
  _globals['_SETPERMISSIONSTAGESREQUEST']._serialized_start=233
  _globals['_SETPERMISSIONSTAGESREQUEST']._serialized_end=326
  _globals['_SETPERMISSIONSTAGESMETADATA']._serialized_start=328
  _globals['_SETPERMISSIONSTAGESMETADATA']._serialized_end=378
  _globals['_UPDATEPERMISSIONSTAGESREQUEST']._serialized_start=381
  _globals['_UPDATEPERMISSIONSTAGESREQUEST']._serialized_end=518
  _globals['_UPDATEPERMISSIONSTAGESMETADATA']._serialized_start=520
  _globals['_UPDATEPERMISSIONSTAGESMETADATA']._serialized_end=573
# @@protoc_insertion_point(module_scope)
