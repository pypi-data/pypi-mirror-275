# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/priv/iam/v1/awscompatibility/delegation_key_service.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.priv.operation import operation_pb2 as yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2
from yandex.cloud.priv import validation_pb2 as yandex_dot_cloud_dot_priv_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nFyandex/cloud/priv/iam/v1/awscompatibility/delegation_key_service.proto\x12)yandex.cloud.priv.iam.v1.awscompatibility\x1a yandex/cloud/api/operation.proto\x1a+yandex/cloud/priv/operation/operation.proto\x1a\"yandex/cloud/priv/validation.proto\"0\n\x0cGetIdRequest\x12 \n\nsubject_id\x18\x01 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\"=\n\x19GetKeyIdForSubjectRequest\x12 \n\nsubject_id\x18\x01 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\"0\n\x1aGetKeyIdForSubjectMetadata\x12\x12\n\nsubject_id\x18\x01 \x01(\t\",\n\x1aGetKeyIdForSubjectResponse\x12\x0e\n\x06key_id\x18\x01 \x01(\t2\xd9\x01\n\x14\x44\x65legationKeyService\x12\xc0\x01\n\x12GetKeyIdForSubject\x12\x44.yandex.cloud.priv.iam.v1.awscompatibility.GetKeyIdForSubjectRequest\x1a&.yandex.cloud.priv.operation.Operation\"<\xb2\xd2*8\n\x1aGetKeyIdForSubjectMetadata\x12\x1aGetKeyIdForSubjectResponseB\x18\x42\x04PDKSZ\x10\x61wscompatibilityb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.priv.iam.v1.awscompatibility.delegation_key_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'B\004PDKSZ\020awscompatibility'
  _globals['_GETIDREQUEST'].fields_by_name['subject_id']._options = None
  _globals['_GETIDREQUEST'].fields_by_name['subject_id']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_GETKEYIDFORSUBJECTREQUEST'].fields_by_name['subject_id']._options = None
  _globals['_GETKEYIDFORSUBJECTREQUEST'].fields_by_name['subject_id']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_DELEGATIONKEYSERVICE'].methods_by_name['GetKeyIdForSubject']._options = None
  _globals['_DELEGATIONKEYSERVICE'].methods_by_name['GetKeyIdForSubject']._serialized_options = b'\262\322*8\n\032GetKeyIdForSubjectMetadata\022\032GetKeyIdForSubjectResponse'
  _globals['_GETIDREQUEST']._serialized_start=232
  _globals['_GETIDREQUEST']._serialized_end=280
  _globals['_GETKEYIDFORSUBJECTREQUEST']._serialized_start=282
  _globals['_GETKEYIDFORSUBJECTREQUEST']._serialized_end=343
  _globals['_GETKEYIDFORSUBJECTMETADATA']._serialized_start=345
  _globals['_GETKEYIDFORSUBJECTMETADATA']._serialized_end=393
  _globals['_GETKEYIDFORSUBJECTRESPONSE']._serialized_start=395
  _globals['_GETKEYIDFORSUBJECTRESPONSE']._serialized_end=439
  _globals['_DELEGATIONKEYSERVICE']._serialized_start=442
  _globals['_DELEGATIONKEYSERVICE']._serialized_end=659
# @@protoc_insertion_point(module_scope)
