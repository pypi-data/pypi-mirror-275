# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/priv/iam/v1/mfa/operation_service.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.priv.operation import operation_pb2 as yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2
from yandex.cloud.priv import validation_pb2 as yandex_dot_cloud_dot_priv_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4yandex/cloud/priv/iam/v1/mfa/operation_service.proto\x12\x1cyandex.cloud.priv.iam.v1.mfa\x1a+yandex/cloud/priv/operation/operation.proto\x1a\"yandex/cloud/priv/validation.proto\"9\n\x13GetOperationRequest\x12\"\n\x0coperation_id\x18\x01 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=502v\n\x10OperationService\x12\x62\n\x03Get\x12\x31.yandex.cloud.priv.iam.v1.mfa.GetOperationRequest\x1a&.yandex.cloud.priv.operation.Operation\"\x00\x42\nB\x03POSZ\x03mfab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.priv.iam.v1.mfa.operation_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'B\003POSZ\003mfa'
  _globals['_GETOPERATIONREQUEST'].fields_by_name['operation_id']._options = None
  _globals['_GETOPERATIONREQUEST'].fields_by_name['operation_id']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_GETOPERATIONREQUEST']._serialized_start=167
  _globals['_GETOPERATIONREQUEST']._serialized_end=224
  _globals['_OPERATIONSERVICE']._serialized_start=226
  _globals['_OPERATIONSERVICE']._serialized_end=344
# @@protoc_insertion_point(module_scope)
