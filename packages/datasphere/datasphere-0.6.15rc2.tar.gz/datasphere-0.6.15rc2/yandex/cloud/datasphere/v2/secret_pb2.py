# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/datasphere/v2/secret.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'yandex/cloud/datasphere/v2/secret.proto\x12\x1ayandex.cloud.datasphere.v2\x1a\x1fgoogle/protobuf/timestamp.proto\"\xbd\x02\n\x06Secret\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12>\n\x06labels\x18\x06 \x03(\x0b\x32..yandex.cloud.datasphere.v2.Secret.LabelsEntry\x12\x15\n\rcreated_by_id\x18\x07 \x01(\t\x12.\n\nupdated_at\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01J\x04\x08\x08\x10\tJ\x04\x08\n\x10\x0b\"V\n\x0f\x44\x65\x63ryptedSecret\x12\x32\n\x06secret\x18\x01 \x01(\x0b\x32\".yandex.cloud.datasphere.v2.Secret\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\tB,\n\x1eyandex.cloud.api.datasphere.v2Z\ndatasphereb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.datasphere.v2.secret_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036yandex.cloud.api.datasphere.v2Z\ndatasphere'
  _globals['_SECRET_LABELSENTRY']._options = None
  _globals['_SECRET_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_SECRET']._serialized_start=105
  _globals['_SECRET']._serialized_end=422
  _globals['_SECRET_LABELSENTRY']._serialized_start=365
  _globals['_SECRET_LABELSENTRY']._serialized_end=410
  _globals['_DECRYPTEDSECRET']._serialized_start=424
  _globals['_DECRYPTEDSECRET']._serialized_end=510
# @@protoc_insertion_point(module_scope)
