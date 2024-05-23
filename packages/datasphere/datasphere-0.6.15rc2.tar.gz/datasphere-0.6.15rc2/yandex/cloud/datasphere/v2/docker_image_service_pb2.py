# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/datasphere/v2/docker_image_service.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5yandex/cloud/datasphere/v2/docker_image_service.proto\x12\x1ayandex.cloud.datasphere.v2\x1a\x1cgoogle/api/annotations.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"_\n\x1a\x41\x63tivateDockerImageRequest\x12 \n\nproject_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1f\n\tdocker_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=502\xc2\x01\n\x12\x44ockerImageService\x12\xab\x01\n\x08\x41\x63tivate\x12\x36.yandex.cloud.datasphere.v2.ActivateDockerImageRequest\x1a!.yandex.cloud.operation.Operation\"D\xb2\xd2*\x17\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02#\"\x1e/datasphere/v2/docker/activate:\x01*B,\n\x1eyandex.cloud.api.datasphere.v2Z\ndatasphereb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.datasphere.v2.docker_image_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036yandex.cloud.api.datasphere.v2Z\ndatasphere'
  _globals['_ACTIVATEDOCKERIMAGEREQUEST'].fields_by_name['project_id']._options = None
  _globals['_ACTIVATEDOCKERIMAGEREQUEST'].fields_by_name['project_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_ACTIVATEDOCKERIMAGEREQUEST'].fields_by_name['docker_id']._options = None
  _globals['_ACTIVATEDOCKERIMAGEREQUEST'].fields_by_name['docker_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_DOCKERIMAGESERVICE'].methods_by_name['Activate']._options = None
  _globals['_DOCKERIMAGESERVICE'].methods_by_name['Activate']._serialized_options = b'\262\322*\027\022\025google.protobuf.Empty\202\323\344\223\002#\"\036/datasphere/v2/docker/activate:\001*'
  _globals['_ACTIVATEDOCKERIMAGEREQUEST']._serialized_start=220
  _globals['_ACTIVATEDOCKERIMAGEREQUEST']._serialized_end=315
  _globals['_DOCKERIMAGESERVICE']._serialized_start=318
  _globals['_DOCKERIMAGESERVICE']._serialized_end=512
# @@protoc_insertion_point(module_scope)
