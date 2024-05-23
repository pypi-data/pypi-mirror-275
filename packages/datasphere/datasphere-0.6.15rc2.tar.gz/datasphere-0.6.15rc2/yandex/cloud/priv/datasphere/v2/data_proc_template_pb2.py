# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/priv/datasphere/v2/data_proc_template.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8yandex/cloud/priv/datasphere/v2/data_proc_template.proto\x12\x1fyandex.cloud.priv.datasphere.v2\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xe3\x02\n\x10\x44\x61taProcTemplate\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12M\n\x06labels\x18\x06 \x03(\x0b\x32=.yandex.cloud.priv.datasphere.v2.DataProcTemplate.LabelsEntry\x12\x12\n\ncreated_by\x18\x07 \x01(\t\x12J\n\x0c\x63luster_spec\x18\t \x01(\x0b\x32\x34.yandex.cloud.priv.datasphere.v2.DataProcClusterSpec\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xc4\x03\n\x16\x44\x61taProcTemplateStatus\x12]\n\rstatus_active\x18\x01 \x01(\x0b\x32\x44.yandex.cloud.priv.datasphere.v2.DataProcTemplateStatus.StatusActiveH\x00\x12\x61\n\x0fstatus_inactive\x18\x02 \x01(\x0b\x32\x46.yandex.cloud.priv.datasphere.v2.DataProcTemplateStatus.StatusInactiveH\x00\x12[\n\x0cstatus_error\x18\x03 \x01(\x0b\x32\x43.yandex.cloud.priv.datasphere.v2.DataProcTemplateStatus.StatusErrorH\x00\x1aQ\n\x0cStatusActive\x12\x41\n\x07\x63luster\x18\x01 \x01(\x0b\x32\x30.yandex.cloud.priv.datasphere.v2.DataProcCluster\x1a\x10\n\x0eStatusInactive\x1a\x1c\n\x0bStatusError\x12\r\n\x05\x65rror\x18\x01 \x01(\tB\x08\n\x06status\"\x9d\x04\n\x0f\x44\x61taProcCluster\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12G\n\x06status\x18\x03 \x01(\x0e\x32\x37.yandex.cloud.priv.datasphere.v2.DataProcCluster.Status\x12[\n\x14\x64\x61tasphere_data_proc\x18\x04 \x01(\x0b\x32;.yandex.cloud.priv.datasphere.v2.DataProcCluster.DataSphereH\x00\x12\x31\n\x0f\x63loud_data_proc\x18\x05 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00\x1aw\n\nDataSphere\x12\x1d\n\x15\x64\x61ta_proc_template_id\x18\x01 \x01(\t\x12J\n\x0c\x63luster_spec\x18\x02 \x01(\x0b\x32\x34.yandex.cloud.priv.datasphere.v2.DataProcClusterSpec\"\x94\x01\n\x06Status\x12(\n$DATA_PROC_CLUSTER_STATUS_UNSPECIFIED\x10\x00\x12\x1d\n\x19\x44\x41TA_PROC_CLUSTER_RUNNING\x10\x01\x12!\n\x1d\x44\x41TA_PROC_CLUSTER_NOT_RUNNING\x10\x02\x12\x1e\n\x1a\x44\x41TA_PROC_CLUSTER_STARTING\x10\x03\x42\x07\n\x05owner\"\x86\x02\n\x13\x44\x61taProcClusterSpec\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nnode_count\x18\x02 \x01(\x03\x12\x10\n\x08node_cpu\x18\x03 \x01(\x03\x12\x13\n\x0bnode_ram_gb\x18\x04 \x01(\x03\x12\x16\n\x0enode_disk_size\x18\x05 \x01(\x03\x12U\n\x0enode_disk_type\x18\x06 \x01(\x0e\x32=.yandex.cloud.priv.datasphere.v2.DataProcClusterSpec.DiskType\"7\n\x08\x44iskType\x12\x19\n\x15\x44ISK_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03HDD\x10\x01\x12\x07\n\x03SSD\x10\x02\x42\x36\n\"yandex.cloud.priv.datasphere.v2ydsB\x04\x44SDPZ\ndatasphereb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.priv.datasphere.v2.data_proc_template_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"yandex.cloud.priv.datasphere.v2ydsB\004DSDPZ\ndatasphere'
  _globals['_DATAPROCTEMPLATE_LABELSENTRY']._options = None
  _globals['_DATAPROCTEMPLATE_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_DATAPROCTEMPLATE']._serialized_start=156
  _globals['_DATAPROCTEMPLATE']._serialized_end=511
  _globals['_DATAPROCTEMPLATE_LABELSENTRY']._serialized_start=466
  _globals['_DATAPROCTEMPLATE_LABELSENTRY']._serialized_end=511
  _globals['_DATAPROCTEMPLATESTATUS']._serialized_start=514
  _globals['_DATAPROCTEMPLATESTATUS']._serialized_end=966
  _globals['_DATAPROCTEMPLATESTATUS_STATUSACTIVE']._serialized_start=827
  _globals['_DATAPROCTEMPLATESTATUS_STATUSACTIVE']._serialized_end=908
  _globals['_DATAPROCTEMPLATESTATUS_STATUSINACTIVE']._serialized_start=910
  _globals['_DATAPROCTEMPLATESTATUS_STATUSINACTIVE']._serialized_end=926
  _globals['_DATAPROCTEMPLATESTATUS_STATUSERROR']._serialized_start=928
  _globals['_DATAPROCTEMPLATESTATUS_STATUSERROR']._serialized_end=956
  _globals['_DATAPROCCLUSTER']._serialized_start=969
  _globals['_DATAPROCCLUSTER']._serialized_end=1510
  _globals['_DATAPROCCLUSTER_DATASPHERE']._serialized_start=1231
  _globals['_DATAPROCCLUSTER_DATASPHERE']._serialized_end=1350
  _globals['_DATAPROCCLUSTER_STATUS']._serialized_start=1353
  _globals['_DATAPROCCLUSTER_STATUS']._serialized_end=1501
  _globals['_DATAPROCCLUSTERSPEC']._serialized_start=1513
  _globals['_DATAPROCCLUSTERSPEC']._serialized_end=1775
  _globals['_DATAPROCCLUSTERSPEC_DISKTYPE']._serialized_start=1720
  _globals['_DATAPROCCLUSTERSPEC_DISKTYPE']._serialized_end=1775
# @@protoc_insertion_point(module_scope)
