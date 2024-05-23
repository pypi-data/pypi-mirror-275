# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/priv/iam/v1/inner/service_registry_service.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.priv.operation import operation_pb2 as yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.priv.iam.v1.inner import service_registry_pb2 as yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_inner_dot_service__registry__pb2
from yandex.cloud.priv import validation_pb2 as yandex_dot_cloud_dot_priv_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=yandex/cloud/priv/iam/v1/inner/service_registry_service.proto\x12\x1eyandex.cloud.priv.iam.v1.inner\x1a google/protobuf/field_mask.proto\x1a+yandex/cloud/priv/operation/operation.proto\x1a yandex/cloud/api/operation.proto\x1a\x35yandex/cloud/priv/iam/v1/inner/service_registry.proto\x1a\"yandex/cloud/priv/validation.proto\"Z\n\x11GetServiceRequest\x12 \n\nservice_id\x18\x01 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\x12#\n\rresource_type\x18\x02 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\"\xfb\x01\n\x14\x43reateServiceRequest\x12 \n\nservice_id\x18\x01 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\x12#\n\rresource_type\x18\x02 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\x12\x1d\n\x07version\x18\x03 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\xca\x89\x31\x05<=255\x12\x1f\n\rgizmo_service\x18\x05 \x01(\tB\x08\xca\x89\x31\x04<=50\x12\x12\n\nis_default\x18\x06 \x01(\x08\x12\x12\n\nis_visible\x18\x07 \x01(\x08\x12\x14\n\x0cuser_managed\x18\x08 \x01(\x08\"\xa8\x02\n\x14UpdateServiceRequest\x12 \n\nservice_id\x18\x01 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\x12#\n\rresource_type\x18\x02 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x19\n\x07version\x18\x04 \x01(\tB\x08\xca\x89\x31\x04<=50\x12\x1e\n\x0b\x64\x65scription\x18\x05 \x01(\tB\t\xca\x89\x31\x05<=255\x12\x1f\n\rgizmo_service\x18\x06 \x01(\tB\x08\xca\x89\x31\x04<=50\x12\x12\n\nis_default\x18\x07 \x01(\x08\x12\x12\n\nis_visible\x18\x08 \x01(\x08\x12\x14\n\x0cuser_managed\x18\t \x01(\x08\"]\n\x14\x44\x65leteServiceRequest\x12 \n\nservice_id\x18\x01 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\x12#\n\rresource_type\x18\x02 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\"\x80\x01\n\x18GetServiceVersionRequest\x12 \n\nservice_id\x18\x01 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\x12#\n\rresource_type\x18\x02 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\x12\x1d\n\x07version\x18\x03 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\"\xd3\x01\n\x1b\x43reateServiceVersionRequest\x12 \n\nservice_id\x18\x01 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\x12#\n\rresource_type\x18\x02 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\x12\x1d\n\x07version\x18\x03 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\x12N\n\rmicroservices\x18\x04 \x03(\x0b\x32,.yandex.cloud.priv.iam.v1.inner.MicroserviceB\t\xc2\x89\x31\x05<=100\"\x83\x01\n\x1b\x44\x65leteServiceVersionRequest\x12 \n\nservice_id\x18\x01 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\x12#\n\rresource_type\x18\x02 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\x12\x1d\n\x07version\x18\x03 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\"B\n\x15\x43reateServiceMetadata\x12\x12\n\nservice_id\x18\x01 \x01(\t\x12\x15\n\rresource_type\x18\x02 \x01(\t\"B\n\x15UpdateServiceMetadata\x12\x12\n\nservice_id\x18\x01 \x01(\t\x12\x15\n\rresource_type\x18\x02 \x01(\t\"B\n\x15\x44\x65leteServiceMetadata\x12\x12\n\nservice_id\x18\x01 \x01(\t\x12\x15\n\rresource_type\x18\x02 \x01(\t\"Z\n\x1c\x43reateServiceVersionMetadata\x12\x12\n\nservice_id\x18\x01 \x01(\t\x12\x15\n\rresource_type\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\"Z\n\x1c\x44\x65leteServiceVersionMetadata\x12\x12\n\nservice_id\x18\x01 \x01(\t\x12\x15\n\rresource_type\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t2\x8b\x08\n\x16ServiceRegistryService\x12\x61\n\x03Get\x12\x31.yandex.cloud.priv.iam.v1.inner.GetServiceRequest\x1a\'.yandex.cloud.priv.iam.v1.inner.Service\x12\x8c\x01\n\x06\x43reate\x12\x34.yandex.cloud.priv.iam.v1.inner.CreateServiceRequest\x1a&.yandex.cloud.priv.operation.Operation\"$\xb2\xd2* \n\x15\x43reateServiceMetadata\x12\x07Service\x12\x8c\x01\n\x06Update\x12\x34.yandex.cloud.priv.iam.v1.inner.UpdateServiceRequest\x1a&.yandex.cloud.priv.operation.Operation\"$\xb2\xd2* \n\x15UpdateServiceMetadata\x12\x07Service\x12\x9a\x01\n\x06\x44\x65lete\x12\x34.yandex.cloud.priv.iam.v1.inner.DeleteServiceRequest\x1a&.yandex.cloud.priv.operation.Operation\"2\xb2\xd2*.\n\x15\x44\x65leteServiceMetadata\x12\x15google.protobuf.Empty\x12v\n\nGetVersion\x12\x38.yandex.cloud.priv.iam.v1.inner.GetServiceVersionRequest\x1a..yandex.cloud.priv.iam.v1.inner.ServiceVersion\x12\xa8\x01\n\rCreateVersion\x12;.yandex.cloud.priv.iam.v1.inner.CreateServiceVersionRequest\x1a&.yandex.cloud.priv.operation.Operation\"2\xb2\xd2*.\n\x1c\x43reateServiceVersionMetadata\x12\x0eServiceVersion\x12\xaf\x01\n\rDeleteVersion\x12;.yandex.cloud.priv.iam.v1.inner.DeleteServiceVersionRequest\x1a&.yandex.cloud.priv.operation.Operation\"9\xb2\xd2*5\n\x1c\x44\x65leteServiceVersionMetadata\x12\x15google.protobuf.EmptyB\x11\x42\x04PSRSZ\tiam_innerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.priv.iam.v1.inner.service_registry_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'B\004PSRSZ\tiam_inner'
  _globals['_GETSERVICEREQUEST'].fields_by_name['service_id']._options = None
  _globals['_GETSERVICEREQUEST'].fields_by_name['service_id']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_GETSERVICEREQUEST'].fields_by_name['resource_type']._options = None
  _globals['_GETSERVICEREQUEST'].fields_by_name['resource_type']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_CREATESERVICEREQUEST'].fields_by_name['service_id']._options = None
  _globals['_CREATESERVICEREQUEST'].fields_by_name['service_id']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_CREATESERVICEREQUEST'].fields_by_name['resource_type']._options = None
  _globals['_CREATESERVICEREQUEST'].fields_by_name['resource_type']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_CREATESERVICEREQUEST'].fields_by_name['version']._options = None
  _globals['_CREATESERVICEREQUEST'].fields_by_name['version']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_CREATESERVICEREQUEST'].fields_by_name['description']._options = None
  _globals['_CREATESERVICEREQUEST'].fields_by_name['description']._serialized_options = b'\312\2111\005<=255'
  _globals['_CREATESERVICEREQUEST'].fields_by_name['gizmo_service']._options = None
  _globals['_CREATESERVICEREQUEST'].fields_by_name['gizmo_service']._serialized_options = b'\312\2111\004<=50'
  _globals['_UPDATESERVICEREQUEST'].fields_by_name['service_id']._options = None
  _globals['_UPDATESERVICEREQUEST'].fields_by_name['service_id']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_UPDATESERVICEREQUEST'].fields_by_name['resource_type']._options = None
  _globals['_UPDATESERVICEREQUEST'].fields_by_name['resource_type']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_UPDATESERVICEREQUEST'].fields_by_name['version']._options = None
  _globals['_UPDATESERVICEREQUEST'].fields_by_name['version']._serialized_options = b'\312\2111\004<=50'
  _globals['_UPDATESERVICEREQUEST'].fields_by_name['description']._options = None
  _globals['_UPDATESERVICEREQUEST'].fields_by_name['description']._serialized_options = b'\312\2111\005<=255'
  _globals['_UPDATESERVICEREQUEST'].fields_by_name['gizmo_service']._options = None
  _globals['_UPDATESERVICEREQUEST'].fields_by_name['gizmo_service']._serialized_options = b'\312\2111\004<=50'
  _globals['_DELETESERVICEREQUEST'].fields_by_name['service_id']._options = None
  _globals['_DELETESERVICEREQUEST'].fields_by_name['service_id']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_DELETESERVICEREQUEST'].fields_by_name['resource_type']._options = None
  _globals['_DELETESERVICEREQUEST'].fields_by_name['resource_type']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_GETSERVICEVERSIONREQUEST'].fields_by_name['service_id']._options = None
  _globals['_GETSERVICEVERSIONREQUEST'].fields_by_name['service_id']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_GETSERVICEVERSIONREQUEST'].fields_by_name['resource_type']._options = None
  _globals['_GETSERVICEVERSIONREQUEST'].fields_by_name['resource_type']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_GETSERVICEVERSIONREQUEST'].fields_by_name['version']._options = None
  _globals['_GETSERVICEVERSIONREQUEST'].fields_by_name['version']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_CREATESERVICEVERSIONREQUEST'].fields_by_name['service_id']._options = None
  _globals['_CREATESERVICEVERSIONREQUEST'].fields_by_name['service_id']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_CREATESERVICEVERSIONREQUEST'].fields_by_name['resource_type']._options = None
  _globals['_CREATESERVICEVERSIONREQUEST'].fields_by_name['resource_type']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_CREATESERVICEVERSIONREQUEST'].fields_by_name['version']._options = None
  _globals['_CREATESERVICEVERSIONREQUEST'].fields_by_name['version']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_CREATESERVICEVERSIONREQUEST'].fields_by_name['microservices']._options = None
  _globals['_CREATESERVICEVERSIONREQUEST'].fields_by_name['microservices']._serialized_options = b'\302\2111\005<=100'
  _globals['_DELETESERVICEVERSIONREQUEST'].fields_by_name['service_id']._options = None
  _globals['_DELETESERVICEVERSIONREQUEST'].fields_by_name['service_id']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_DELETESERVICEVERSIONREQUEST'].fields_by_name['resource_type']._options = None
  _globals['_DELETESERVICEVERSIONREQUEST'].fields_by_name['resource_type']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_DELETESERVICEVERSIONREQUEST'].fields_by_name['version']._options = None
  _globals['_DELETESERVICEVERSIONREQUEST'].fields_by_name['version']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_SERVICEREGISTRYSERVICE'].methods_by_name['Create']._options = None
  _globals['_SERVICEREGISTRYSERVICE'].methods_by_name['Create']._serialized_options = b'\262\322* \n\025CreateServiceMetadata\022\007Service'
  _globals['_SERVICEREGISTRYSERVICE'].methods_by_name['Update']._options = None
  _globals['_SERVICEREGISTRYSERVICE'].methods_by_name['Update']._serialized_options = b'\262\322* \n\025UpdateServiceMetadata\022\007Service'
  _globals['_SERVICEREGISTRYSERVICE'].methods_by_name['Delete']._options = None
  _globals['_SERVICEREGISTRYSERVICE'].methods_by_name['Delete']._serialized_options = b'\262\322*.\n\025DeleteServiceMetadata\022\025google.protobuf.Empty'
  _globals['_SERVICEREGISTRYSERVICE'].methods_by_name['CreateVersion']._options = None
  _globals['_SERVICEREGISTRYSERVICE'].methods_by_name['CreateVersion']._serialized_options = b'\262\322*.\n\034CreateServiceVersionMetadata\022\016ServiceVersion'
  _globals['_SERVICEREGISTRYSERVICE'].methods_by_name['DeleteVersion']._options = None
  _globals['_SERVICEREGISTRYSERVICE'].methods_by_name['DeleteVersion']._serialized_options = b'\262\322*5\n\034DeleteServiceVersionMetadata\022\025google.protobuf.Empty'
  _globals['_GETSERVICEREQUEST']._serialized_start=301
  _globals['_GETSERVICEREQUEST']._serialized_end=391
  _globals['_CREATESERVICEREQUEST']._serialized_start=394
  _globals['_CREATESERVICEREQUEST']._serialized_end=645
  _globals['_UPDATESERVICEREQUEST']._serialized_start=648
  _globals['_UPDATESERVICEREQUEST']._serialized_end=944
  _globals['_DELETESERVICEREQUEST']._serialized_start=946
  _globals['_DELETESERVICEREQUEST']._serialized_end=1039
  _globals['_GETSERVICEVERSIONREQUEST']._serialized_start=1042
  _globals['_GETSERVICEVERSIONREQUEST']._serialized_end=1170
  _globals['_CREATESERVICEVERSIONREQUEST']._serialized_start=1173
  _globals['_CREATESERVICEVERSIONREQUEST']._serialized_end=1384
  _globals['_DELETESERVICEVERSIONREQUEST']._serialized_start=1387
  _globals['_DELETESERVICEVERSIONREQUEST']._serialized_end=1518
  _globals['_CREATESERVICEMETADATA']._serialized_start=1520
  _globals['_CREATESERVICEMETADATA']._serialized_end=1586
  _globals['_UPDATESERVICEMETADATA']._serialized_start=1588
  _globals['_UPDATESERVICEMETADATA']._serialized_end=1654
  _globals['_DELETESERVICEMETADATA']._serialized_start=1656
  _globals['_DELETESERVICEMETADATA']._serialized_end=1722
  _globals['_CREATESERVICEVERSIONMETADATA']._serialized_start=1724
  _globals['_CREATESERVICEVERSIONMETADATA']._serialized_end=1814
  _globals['_DELETESERVICEVERSIONMETADATA']._serialized_start=1816
  _globals['_DELETESERVICEVERSIONMETADATA']._serialized_end=1906
  _globals['_SERVICEREGISTRYSERVICE']._serialized_start=1909
  _globals['_SERVICEREGISTRYSERVICE']._serialized_end=2944
# @@protoc_insertion_point(module_scope)
