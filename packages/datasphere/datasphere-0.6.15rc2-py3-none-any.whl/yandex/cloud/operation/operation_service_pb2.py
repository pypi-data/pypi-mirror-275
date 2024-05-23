# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/operation/operation_service.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.api.tools import options_pb2 as yandex_dot_cloud_dot_api_dot_tools_dot_options__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.yandex/cloud/operation/operation_service.proto\x12\x16yandex.cloud.operation\x1a\x1cgoogle/api/annotations.proto\x1a$yandex/cloud/api/tools/options.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"1\n\x13GetOperationRequest\x12\x1a\n\x0coperation_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"4\n\x16\x43\x61ncelOperationRequest\x12\x1a\n\x0coperation_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x32\x9e\x02\n\x10OperationService\x12y\n\x03Get\x12+.yandex.cloud.operation.GetOperationRequest\x1a!.yandex.cloud.operation.Operation\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/operations/{operation_id}\x12\x8e\x01\n\x06\x43\x61ncel\x12..yandex.cloud.operation.CancelOperationRequest\x1a!.yandex.cloud.operation.Operation\"1\xca\xef \x04\n\x02(\x01\x82\xd3\xe4\x93\x02#\x12!/operations/{operation_id}:cancelB\'\n\x1ayandex.cloud.api.operationZ\toperationb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.operation.operation_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032yandex.cloud.api.operationZ\toperation'
  _globals['_GETOPERATIONREQUEST'].fields_by_name['operation_id']._options = None
  _globals['_GETOPERATIONREQUEST'].fields_by_name['operation_id']._serialized_options = b'\350\3071\001'
  _globals['_CANCELOPERATIONREQUEST'].fields_by_name['operation_id']._options = None
  _globals['_CANCELOPERATIONREQUEST'].fields_by_name['operation_id']._serialized_options = b'\350\3071\001'
  _globals['_OPERATIONSERVICE'].methods_by_name['Get']._options = None
  _globals['_OPERATIONSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\034\022\032/operations/{operation_id}'
  _globals['_OPERATIONSERVICE'].methods_by_name['Cancel']._options = None
  _globals['_OPERATIONSERVICE'].methods_by_name['Cancel']._serialized_options = b'\312\357 \004\n\002(\001\202\323\344\223\002#\022!/operations/{operation_id}:cancel'
  _globals['_GETOPERATIONREQUEST']._serialized_start=213
  _globals['_GETOPERATIONREQUEST']._serialized_end=262
  _globals['_CANCELOPERATIONREQUEST']._serialized_start=264
  _globals['_CANCELOPERATIONREQUEST']._serialized_end=316
  _globals['_OPERATIONSERVICE']._serialized_start=319
  _globals['_OPERATIONSERVICE']._serialized_end=605
# @@protoc_insertion_point(module_scope)
