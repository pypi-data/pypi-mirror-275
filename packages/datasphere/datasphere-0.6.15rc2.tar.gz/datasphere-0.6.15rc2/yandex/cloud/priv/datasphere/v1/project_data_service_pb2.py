# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/priv/datasphere/v1/project_data_service.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.priv import validation_pb2 as yandex_dot_cloud_dot_priv_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:yandex/cloud/priv/datasphere/v1/project_data_service.proto\x12\x1fyandex.cloud.priv.datasphere.v1\x1a\"yandex/cloud/priv/validation.proto\"S\n\x0c\x46ileMetadata\x12!\n\nproject_id\x18\x01 \x01(\tB\r\xa8\x89\x31\x01\xca\x89\x31\x05<=200\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x12\n\nsize_bytes\x18\x03 \x01(\x03\"r\n\x11UploadFileRequest\x12\x41\n\x08metadata\x18\x01 \x01(\x0b\x32-.yandex.cloud.priv.datasphere.v1.FileMetadataH\x00\x12\x0f\n\x05\x63hunk\x18\x02 \x01(\x0cH\x00\x42\t\n\x07message\"U\n\x12UploadFileResponse\x12?\n\x08metadata\x18\x01 \x01(\x0b\x32-.yandex.cloud.priv.datasphere.v1.FileMetadata\"Q\n\x13\x44ownloadFileRequest\x12!\n\nproject_id\x18\x01 \x01(\tB\r\xa8\x89\x31\x01\xca\x89\x31\x05<=200\x12\x17\n\tfile_path\x18\x02 \x01(\tB\x04\xa8\x89\x31\x01\"u\n\x14\x44ownloadFileResponse\x12\x41\n\x08metadata\x18\x01 \x01(\x0b\x32-.yandex.cloud.priv.datasphere.v1.FileMetadataH\x00\x12\x0f\n\x05\x63hunk\x18\x02 \x01(\x0cH\x00\x42\t\n\x07message2\x8c\x02\n\x12ProjectDataService\x12w\n\nUploadFile\x12\x32.yandex.cloud.priv.datasphere.v1.UploadFileRequest\x1a\x33.yandex.cloud.priv.datasphere.v1.UploadFileResponse(\x01\x12}\n\x0c\x44ownloadFile\x12\x34.yandex.cloud.priv.datasphere.v1.DownloadFileRequest\x1a\x35.yandex.cloud.priv.datasphere.v1.DownloadFileResponse0\x01\x42\x13\x42\x05\x44SPDSZ\ndatasphereb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.priv.datasphere.v1.project_data_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'B\005DSPDSZ\ndatasphere'
  _globals['_FILEMETADATA'].fields_by_name['project_id']._options = None
  _globals['_FILEMETADATA'].fields_by_name['project_id']._serialized_options = b'\250\2111\001\312\2111\005<=200'
  _globals['_DOWNLOADFILEREQUEST'].fields_by_name['project_id']._options = None
  _globals['_DOWNLOADFILEREQUEST'].fields_by_name['project_id']._serialized_options = b'\250\2111\001\312\2111\005<=200'
  _globals['_DOWNLOADFILEREQUEST'].fields_by_name['file_path']._options = None
  _globals['_DOWNLOADFILEREQUEST'].fields_by_name['file_path']._serialized_options = b'\250\2111\001'
  _globals['_FILEMETADATA']._serialized_start=131
  _globals['_FILEMETADATA']._serialized_end=214
  _globals['_UPLOADFILEREQUEST']._serialized_start=216
  _globals['_UPLOADFILEREQUEST']._serialized_end=330
  _globals['_UPLOADFILERESPONSE']._serialized_start=332
  _globals['_UPLOADFILERESPONSE']._serialized_end=417
  _globals['_DOWNLOADFILEREQUEST']._serialized_start=419
  _globals['_DOWNLOADFILEREQUEST']._serialized_end=500
  _globals['_DOWNLOADFILERESPONSE']._serialized_start=502
  _globals['_DOWNLOADFILERESPONSE']._serialized_end=619
  _globals['_PROJECTDATASERVICE']._serialized_start=622
  _globals['_PROJECTDATASERVICE']._serialized_end=890
# @@protoc_insertion_point(module_scope)
