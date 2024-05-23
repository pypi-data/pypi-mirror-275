# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/priv/datasphere/v2/nodedeployer/node_alias.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud.priv.datasphere.v2.nodedeployer import billing_spec_pb2 as yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_nodedeployer_dot_billing__spec__pb2
from yandex.cloud.priv import validation_pb2 as yandex_dot_cloud_dot_priv_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=yandex/cloud/priv/datasphere/v2/nodedeployer/node_alias.proto\x12,yandex.cloud.priv.datasphere.v2.nodedeployer\x1a\x1fgoogle/protobuf/timestamp.proto\x1a?yandex/cloud/priv/datasphere/v2/nodedeployer/billing_spec.proto\x1a\"yandex/cloud/priv/validation.proto\"\x95\x04\n\tNodeAlias\x12\x12\n\x04name\x18\x01 \x01(\tB\x04\xa8\x89\x31\x01\x12\x18\n\nproject_id\x18\x02 \x01(\tB\x04\xa8\x89\x31\x01\x12\x34\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xa8\x89\x31\x01\x12\x1b\n\rcreated_by_id\x18\x04 \x01(\tB\x04\xa8\x89\x31\x01\x12H\n\rexecution_acl\x18\x05 \x01(\x0b\x32\x31.yandex.cloud.priv.datasphere.v2.nodedeployer.ACL\x12S\n\x0eproxy_metadata\x18\x06 \x01(\x0b\x32;.yandex.cloud.priv.datasphere.v2.nodedeployer.ProxyMetadata\x12N\n\x08\x62\x61\x63kends\x18\x07 \x01(\x0b\x32\x36.yandex.cloud.priv.datasphere.v2.nodedeployer.BackendsB\x04\xa8\x89\x31\x01\x12O\n\x0c\x62illing_spec\x18\x08 \x01(\x0b\x32\x39.yandex.cloud.priv.datasphere.v2.nodedeployer.BillingSpec\x12.\n\nupdated_at\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x17\n\tfolder_id\x18\n \x01(\tB\x04\xa8\x89\x31\x01\")\n\x0e\x41\x43LFolderEntry\x12\x17\n\tfolder_id\x18\x01 \x01(\tB\x04\xa8\x89\x31\x01\"i\n\x08\x41\x43LEntry\x12T\n\x0c\x66older_entry\x18\x01 \x01(\x0b\x32<.yandex.cloud.priv.datasphere.v2.nodedeployer.ACLFolderEntryH\x00\x42\x07\n\x05\x65ntry\"u\n\x03\x41\x43L\x12G\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x36.yandex.cloud.priv.datasphere.v2.nodedeployer.ACLEntry\x12\x12\n\npermission\x18\x02 \x01(\t\x12\x11\n\tis_public\x18\x03 \x01(\x08\"1\n\x06Header\x12\x12\n\x04name\x18\x01 \x01(\tB\x04\xa8\x89\x31\x01\x12\x13\n\x05value\x18\x02 \x01(\tB\x04\xa8\x89\x31\x01\"V\n\rProxyMetadata\x12\x45\n\x07headers\x18\x01 \x03(\x0b\x32\x34.yandex.cloud.priv.datasphere.v2.nodedeployer.Header\";\n\x07\x42\x61\x63kend\x12\x15\n\x07node_id\x18\x01 \x01(\tB\x04\xa8\x89\x31\x01\x12\x19\n\x06weight\x18\x02 \x01(\x01\x42\t\xba\x89\x31\x05\x30-100\"[\n\x08\x42\x61\x63kends\x12O\n\x07\x62\x61\x63kend\x18\x01 \x03(\x0b\x32\x35.yandex.cloud.priv.datasphere.v2.nodedeployer.BackendB\x07\xc2\x89\x31\x03>=1B?\n\"yandex.cloud.priv.datasphere.v2ydsB\rNDNodeAliasV2Z\ndatasphereb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.priv.datasphere.v2.nodedeployer.node_alias_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"yandex.cloud.priv.datasphere.v2ydsB\rNDNodeAliasV2Z\ndatasphere'
  _globals['_NODEALIAS'].fields_by_name['name']._options = None
  _globals['_NODEALIAS'].fields_by_name['name']._serialized_options = b'\250\2111\001'
  _globals['_NODEALIAS'].fields_by_name['project_id']._options = None
  _globals['_NODEALIAS'].fields_by_name['project_id']._serialized_options = b'\250\2111\001'
  _globals['_NODEALIAS'].fields_by_name['created_at']._options = None
  _globals['_NODEALIAS'].fields_by_name['created_at']._serialized_options = b'\250\2111\001'
  _globals['_NODEALIAS'].fields_by_name['created_by_id']._options = None
  _globals['_NODEALIAS'].fields_by_name['created_by_id']._serialized_options = b'\250\2111\001'
  _globals['_NODEALIAS'].fields_by_name['backends']._options = None
  _globals['_NODEALIAS'].fields_by_name['backends']._serialized_options = b'\250\2111\001'
  _globals['_NODEALIAS'].fields_by_name['folder_id']._options = None
  _globals['_NODEALIAS'].fields_by_name['folder_id']._serialized_options = b'\250\2111\001'
  _globals['_ACLFOLDERENTRY'].fields_by_name['folder_id']._options = None
  _globals['_ACLFOLDERENTRY'].fields_by_name['folder_id']._serialized_options = b'\250\2111\001'
  _globals['_HEADER'].fields_by_name['name']._options = None
  _globals['_HEADER'].fields_by_name['name']._serialized_options = b'\250\2111\001'
  _globals['_HEADER'].fields_by_name['value']._options = None
  _globals['_HEADER'].fields_by_name['value']._serialized_options = b'\250\2111\001'
  _globals['_BACKEND'].fields_by_name['node_id']._options = None
  _globals['_BACKEND'].fields_by_name['node_id']._serialized_options = b'\250\2111\001'
  _globals['_BACKEND'].fields_by_name['weight']._options = None
  _globals['_BACKEND'].fields_by_name['weight']._serialized_options = b'\272\2111\0050-100'
  _globals['_BACKENDS'].fields_by_name['backend']._options = None
  _globals['_BACKENDS'].fields_by_name['backend']._serialized_options = b'\302\2111\003>=1'
  _globals['_NODEALIAS']._serialized_start=246
  _globals['_NODEALIAS']._serialized_end=779
  _globals['_ACLFOLDERENTRY']._serialized_start=781
  _globals['_ACLFOLDERENTRY']._serialized_end=822
  _globals['_ACLENTRY']._serialized_start=824
  _globals['_ACLENTRY']._serialized_end=929
  _globals['_ACL']._serialized_start=931
  _globals['_ACL']._serialized_end=1048
  _globals['_HEADER']._serialized_start=1050
  _globals['_HEADER']._serialized_end=1099
  _globals['_PROXYMETADATA']._serialized_start=1101
  _globals['_PROXYMETADATA']._serialized_end=1187
  _globals['_BACKEND']._serialized_start=1189
  _globals['_BACKEND']._serialized_end=1248
  _globals['_BACKENDS']._serialized_start=1250
  _globals['_BACKENDS']._serialized_end=1341
# @@protoc_insertion_point(module_scope)
