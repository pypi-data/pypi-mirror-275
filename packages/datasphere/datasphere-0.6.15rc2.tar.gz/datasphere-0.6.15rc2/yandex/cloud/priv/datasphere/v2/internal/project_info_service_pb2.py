# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/priv/datasphere/v2/internal/project_info_service.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.priv.datasphere.v2.internal import project_info_pb2 as yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_internal_dot_project__info__pb2
from yandex.cloud.priv.datasphere.v2 import restrictions_pb2 as yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_restrictions__pb2
from yandex.cloud.priv.operation import operation_pb2 as yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2
from yandex.cloud.priv import validation_pb2 as yandex_dot_cloud_dot_priv_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCyandex/cloud/priv/datasphere/v2/internal/project_info_service.proto\x12(yandex.cloud.priv.datasphere.v2.internal\x1a yandex/cloud/api/operation.proto\x1a;yandex/cloud/priv/datasphere/v2/internal/project_info.proto\x1a\x32yandex/cloud/priv/datasphere/v2/restrictions.proto\x1a+yandex/cloud/priv/operation/operation.proto\x1a\"yandex/cloud/priv/validation.proto\">\n\x1aGetProjectAuthModelRequest\x12 \n\nproject_id\x18\x01 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\"=\n\x19GetProjectFullInfoRequest\x12 \n\nproject_id\x18\x01 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\"=\n\x19GetProjectIdeModelRequest\x12 \n\nproject_id\x18\x01 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=502\xc7\x03\n\x12ProjectInfoService\x12\x90\x01\n\x0cGetAuthModel\x12\x44.yandex.cloud.priv.datasphere.v2.internal.GetProjectAuthModelRequest\x1a:.yandex.cloud.priv.datasphere.v2.internal.ProjectAuthModel\x12\x8d\x01\n\x0bGetFullInfo\x12\x43.yandex.cloud.priv.datasphere.v2.internal.GetProjectFullInfoRequest\x1a\x39.yandex.cloud.priv.datasphere.v2.internal.ProjectFullInfo\x12\x8d\x01\n\x0bGetIdeModel\x12\x43.yandex.cloud.priv.datasphere.v2.internal.GetProjectIdeModelRequest\x1a\x39.yandex.cloud.priv.datasphere.v2.internal.ProjectIdeModelB8\n\"yandex.cloud.priv.datasphere.v2ydsB\x06\x44SPRISZ\ndatasphereb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.priv.datasphere.v2.internal.project_info_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"yandex.cloud.priv.datasphere.v2ydsB\006DSPRISZ\ndatasphere'
  _globals['_GETPROJECTAUTHMODELREQUEST'].fields_by_name['project_id']._options = None
  _globals['_GETPROJECTAUTHMODELREQUEST'].fields_by_name['project_id']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_GETPROJECTFULLINFOREQUEST'].fields_by_name['project_id']._options = None
  _globals['_GETPROJECTFULLINFOREQUEST'].fields_by_name['project_id']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_GETPROJECTIDEMODELREQUEST'].fields_by_name['project_id']._options = None
  _globals['_GETPROJECTIDEMODELREQUEST'].fields_by_name['project_id']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_GETPROJECTAUTHMODELREQUEST']._serialized_start=341
  _globals['_GETPROJECTAUTHMODELREQUEST']._serialized_end=403
  _globals['_GETPROJECTFULLINFOREQUEST']._serialized_start=405
  _globals['_GETPROJECTFULLINFOREQUEST']._serialized_end=466
  _globals['_GETPROJECTIDEMODELREQUEST']._serialized_start=468
  _globals['_GETPROJECTIDEMODELREQUEST']._serialized_end=529
  _globals['_PROJECTINFOSERVICE']._serialized_start=532
  _globals['_PROJECTINFOSERVICE']._serialized_end=987
# @@protoc_insertion_point(module_scope)
