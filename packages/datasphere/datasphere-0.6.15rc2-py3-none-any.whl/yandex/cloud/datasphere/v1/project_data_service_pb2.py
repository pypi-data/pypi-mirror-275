# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/datasphere/v1/project_data_service.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5yandex/cloud/datasphere/v1/project_data_service.proto\x12\x1ayandex.cloud.datasphere.v1\x1a\x1dyandex/cloud/validation.proto\"S\n\x0c\x46ileMetadata\x12!\n\nproject_id\x18\x01 \x01(\tB\r\xe8\xc7\x31\x01\x8a\xc8\x31\x05<=200\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x12\n\nsize_bytes\x18\x03 \x01(\x03\"m\n\x11UploadFileRequest\x12<\n\x08metadata\x18\x01 \x01(\x0b\x32(.yandex.cloud.datasphere.v1.FileMetadataH\x00\x12\x0f\n\x05\x63hunk\x18\x02 \x01(\x0cH\x00\x42\t\n\x07message\"P\n\x12UploadFileResponse\x12:\n\x08metadata\x18\x01 \x01(\x0b\x32(.yandex.cloud.datasphere.v1.FileMetadata\"Q\n\x13\x44ownloadFileRequest\x12!\n\nproject_id\x18\x01 \x01(\tB\r\xe8\xc7\x31\x01\x8a\xc8\x31\x05<=200\x12\x17\n\tfile_path\x18\x02 \x01(\tB\x04\xe8\xc7\x31\x01\"p\n\x14\x44ownloadFileResponse\x12<\n\x08metadata\x18\x01 \x01(\x0b\x32(.yandex.cloud.datasphere.v1.FileMetadataH\x00\x12\x0f\n\x05\x63hunk\x18\x02 \x01(\x0cH\x00\x42\t\n\x07message2\xf8\x01\n\x12ProjectDataService\x12m\n\nUploadFile\x12-.yandex.cloud.datasphere.v1.UploadFileRequest\x1a..yandex.cloud.datasphere.v1.UploadFileResponse(\x01\x12s\n\x0c\x44ownloadFile\x12/.yandex.cloud.datasphere.v1.DownloadFileRequest\x1a\x30.yandex.cloud.datasphere.v1.DownloadFileResponse0\x01\x42,\n\x1eyandex.cloud.api.datasphere.v1Z\ndatasphereb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.datasphere.v1.project_data_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036yandex.cloud.api.datasphere.v1Z\ndatasphere'
  _globals['_FILEMETADATA'].fields_by_name['project_id']._options = None
  _globals['_FILEMETADATA'].fields_by_name['project_id']._serialized_options = b'\350\3071\001\212\3101\005<=200'
  _globals['_DOWNLOADFILEREQUEST'].fields_by_name['project_id']._options = None
  _globals['_DOWNLOADFILEREQUEST'].fields_by_name['project_id']._serialized_options = b'\350\3071\001\212\3101\005<=200'
  _globals['_DOWNLOADFILEREQUEST'].fields_by_name['file_path']._options = None
  _globals['_DOWNLOADFILEREQUEST'].fields_by_name['file_path']._serialized_options = b'\350\3071\001'
  _globals['_FILEMETADATA']._serialized_start=116
  _globals['_FILEMETADATA']._serialized_end=199
  _globals['_UPLOADFILEREQUEST']._serialized_start=201
  _globals['_UPLOADFILEREQUEST']._serialized_end=310
  _globals['_UPLOADFILERESPONSE']._serialized_start=312
  _globals['_UPLOADFILERESPONSE']._serialized_end=392
  _globals['_DOWNLOADFILEREQUEST']._serialized_start=394
  _globals['_DOWNLOADFILEREQUEST']._serialized_end=475
  _globals['_DOWNLOADFILERESPONSE']._serialized_start=477
  _globals['_DOWNLOADFILERESPONSE']._serialized_end=589
  _globals['_PROJECTDATASERVICE']._serialized_start=592
  _globals['_PROJECTDATASERVICE']._serialized_end=840
# @@protoc_insertion_point(module_scope)
