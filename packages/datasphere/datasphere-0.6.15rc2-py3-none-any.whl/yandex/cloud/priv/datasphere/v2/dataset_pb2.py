# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/priv/datasphere/v2/dataset.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-yandex/cloud/priv/datasphere/v2/dataset.proto\x12\x1fyandex.cloud.priv.datasphere.v2\x1a\x1fgoogle/protobuf/timestamp.proto\"\xe6\x02\n\x07\x44\x61taset\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x44\n\x06labels\x18\x06 \x03(\x0b\x32\x34.yandex.cloud.priv.datasphere.v2.Dataset.LabelsEntry\x12\x15\n\rcreated_by_id\x18\x07 \x01(\t\x12\x0c\n\x04\x63ode\x18\x08 \x01(\t\x12\x0f\n\x07size_gb\x18\t \x01(\x03\x12\x10\n\x08zone_ids\x18\n \x03(\t\x12\x12\n\nmount_path\x18\x0b \x01(\t\x12\x17\n\x0f\x64\x61ta_capsule_id\x18\x0c \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xdd\x02\n\rDatasetStatus\x12T\n\rstatus_active\x18\x01 \x01(\x0b\x32;.yandex.cloud.priv.datasphere.v2.DatasetStatus.StatusActiveH\x00\x12X\n\x0fstatus_inactive\x18\x02 \x01(\x0b\x32=.yandex.cloud.priv.datasphere.v2.DatasetStatus.StatusInactiveH\x00\x12R\n\x0cstatus_error\x18\x03 \x01(\x0b\x32:.yandex.cloud.priv.datasphere.v2.DatasetStatus.StatusErrorH\x00\x1a\x0e\n\x0cStatusActive\x1a\x10\n\x0eStatusInactive\x1a\x1c\n\x0bStatusError\x12\r\n\x05\x65rror\x18\x01 \x01(\tB\x08\n\x06statusB6\n\"yandex.cloud.priv.datasphere.v2ydsB\x04\x44SDSZ\ndatasphereb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.priv.datasphere.v2.dataset_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"yandex.cloud.priv.datasphere.v2ydsB\004DSDSZ\ndatasphere'
  _globals['_DATASET_LABELSENTRY']._options = None
  _globals['_DATASET_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_DATASET']._serialized_start=116
  _globals['_DATASET']._serialized_end=474
  _globals['_DATASET_LABELSENTRY']._serialized_start=429
  _globals['_DATASET_LABELSENTRY']._serialized_end=474
  _globals['_DATASETSTATUS']._serialized_start=477
  _globals['_DATASETSTATUS']._serialized_end=826
  _globals['_DATASETSTATUS_STATUSACTIVE']._serialized_start=754
  _globals['_DATASETSTATUS_STATUSACTIVE']._serialized_end=768
  _globals['_DATASETSTATUS_STATUSINACTIVE']._serialized_start=770
  _globals['_DATASETSTATUS_STATUSINACTIVE']._serialized_end=786
  _globals['_DATASETSTATUS_STATUSERROR']._serialized_start=788
  _globals['_DATASETSTATUS_STATUSERROR']._serialized_end=816
# @@protoc_insertion_point(module_scope)
