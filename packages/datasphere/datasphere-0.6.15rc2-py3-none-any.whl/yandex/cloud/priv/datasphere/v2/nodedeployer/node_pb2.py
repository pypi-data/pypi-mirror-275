# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/priv/datasphere/v2/nodedeployer/node.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud.priv.datasphere.v2.nodedeployer import node_spec_pb2 as yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_nodedeployer_dot_node__spec__pb2
from yandex.cloud.priv import validation_pb2 as yandex_dot_cloud_dot_priv_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7yandex/cloud/priv/datasphere/v2/nodedeployer/node.proto\x12,yandex.cloud.priv.datasphere.v2.nodedeployer\x1a\x1fgoogle/protobuf/timestamp.proto\x1a<yandex/cloud/priv/datasphere/v2/nodedeployer/node_spec.proto\x1a\"yandex/cloud/priv/validation.proto\"\xa7\x02\n\x04Node\x12\x10\n\x02id\x18\x01 \x01(\tB\x04\xa8\x89\x31\x01\x12\x18\n\nproject_id\x18\x02 \x01(\tB\x04\xa8\x89\x31\x01\x12\x17\n\tfolder_id\x18\x03 \x01(\tB\x04\xa8\x89\x31\x01\x12\x34\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xa8\x89\x31\x01\x12\x15\n\rcreated_by_id\x18\x05 \x01(\t\x12O\n\tnode_spec\x18\x06 \x01(\x0b\x32\x36.yandex.cloud.priv.datasphere.v2.nodedeployer.NodeSpecB\x04\xa8\x89\x31\x01\x12\x0c\n\x04tags\x18\x07 \x03(\t\x12.\n\nupdated_at\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp*\x94\x01\n\nNodeStatus\x12\x1b\n\x17NODE_STATUS_UNSPECIFIED\x10\x00\x12\x19\n\x15NODE_STATUS_SUSPENDED\x10\x01\x12\x1a\n\x16NODE_STATUS_DESTROYING\x10\x02\x12\x17\n\x13NODE_STATUS_HEALTHY\x10\x03\x12\x19\n\x15NODE_STATUS_UNHEALTHY\x10\x04\x42:\n\"yandex.cloud.priv.datasphere.v2ydsB\x08NDNodeV2Z\ndatasphereb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.priv.datasphere.v2.nodedeployer.node_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"yandex.cloud.priv.datasphere.v2ydsB\010NDNodeV2Z\ndatasphere'
  _globals['_NODE'].fields_by_name['id']._options = None
  _globals['_NODE'].fields_by_name['id']._serialized_options = b'\250\2111\001'
  _globals['_NODE'].fields_by_name['project_id']._options = None
  _globals['_NODE'].fields_by_name['project_id']._serialized_options = b'\250\2111\001'
  _globals['_NODE'].fields_by_name['folder_id']._options = None
  _globals['_NODE'].fields_by_name['folder_id']._serialized_options = b'\250\2111\001'
  _globals['_NODE'].fields_by_name['created_at']._options = None
  _globals['_NODE'].fields_by_name['created_at']._serialized_options = b'\250\2111\001'
  _globals['_NODE'].fields_by_name['node_spec']._options = None
  _globals['_NODE'].fields_by_name['node_spec']._serialized_options = b'\250\2111\001'
  _globals['_NODESTATUS']._serialized_start=535
  _globals['_NODESTATUS']._serialized_end=683
  _globals['_NODE']._serialized_start=237
  _globals['_NODE']._serialized_end=532
# @@protoc_insertion_point(module_scope)
