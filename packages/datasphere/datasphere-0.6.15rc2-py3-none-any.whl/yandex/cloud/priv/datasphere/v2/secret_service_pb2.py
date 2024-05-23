# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/priv/datasphere/v2/secret_service.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.priv.datasphere.v2 import secret_pb2 as yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_secret__pb2
from yandex.cloud.priv import validation_pb2 as yandex_dot_cloud_dot_priv_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4yandex/cloud/priv/datasphere/v2/secret_service.proto\x12\x1fyandex.cloud.priv.datasphere.v2\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a,yandex/cloud/priv/datasphere/v2/secret.proto\x1a\"yandex/cloud/priv/validation.proto\"\xa4\x03\n\x13\x43reateSecretRequest\x12 \n\nproject_id\x18\x01 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\x12\x44\n\x04name\x18\x02 \x01(\tB6\xa8\x89\x31\x01\xb2\x89\x31&[a-zA-Z][-_a-zA-Z0-9]{1,61}[a-zA-Z0-9]\xca\x89\x31\x04<=63\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\xca\x89\x31\x05<=256\x12\x8d\x01\n\x06labels\x18\x04 \x03(\x0b\x32@.yandex.cloud.priv.datasphere.v2.CreateSecretRequest.LabelsEntryB;\xb2\x89\x31\x0b[-_0-9a-z]*\xc2\x89\x31\x04<=64\xca\x89\x31\x04<=63\xf2\x89\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04\x31-63\x12\x0f\n\x07\x63ontent\x18\x05 \x01(\t\x12\x35\n\x05scope\x18\x06 \x01(\x0e\x32&.yandex.cloud.priv.datasphere.v2.Scope\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xc8\x03\n\x13UpdateSecretRequest\x12\x17\n\tsecret_id\x18\x01 \x01(\tB\x04\xa8\x89\x31\x01\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12@\n\x04name\x18\x03 \x01(\tB2\xb2\x89\x31&[a-zA-Z][-_a-zA-Z0-9]{1,61}[a-zA-Z0-9]\xca\x89\x31\x04<=63\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\xca\x89\x31\x05<=256\x12\x8d\x01\n\x06labels\x18\x05 \x03(\x0b\x32@.yandex.cloud.priv.datasphere.v2.UpdateSecretRequest.LabelsEntryB;\xb2\x89\x31\x0b[-_0-9a-z]*\xc2\x89\x31\x04<=64\xca\x89\x31\x04<=63\xf2\x89\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04\x31-63\x12\x0f\n\x07\x63ontent\x18\x06 \x01(\t\x12\x35\n\x05scope\x18\x07 \x01(\x0e\x32&.yandex.cloud.priv.datasphere.v2.Scope\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"3\n\x10GetSecretRequest\x12\x1f\n\tsecret_id\x18\x01 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\"6\n\x13\x44\x65leteSecretRequest\x12\x1f\n\tsecret_id\x18\x01 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\"7\n\x14\x44\x65\x63ryptSecretRequest\x12\x1f\n\tsecret_id\x18\x01 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\"=\n\x19ListProjectSecretsRequest\x12 \n\nproject_id\x18\x01 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\"V\n\x1aListProjectSecretsResponse\x12\x38\n\x07secrets\x18\x01 \x03(\x0b\x32\'.yandex.cloud.priv.datasphere.v2.Secret\"9\n\x17ListSpaceSecretsRequest\x12\x1e\n\x08space_id\x18\x01 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\"T\n\x18ListSpaceSecretsResponse\x12\x38\n\x07secrets\x18\x01 \x03(\x0b\x32\'.yandex.cloud.priv.datasphere.v2.Secret2\xbb\x07\n\rSecretService\x12g\n\x06\x43reate\x12\x34.yandex.cloud.priv.datasphere.v2.CreateSecretRequest\x1a\'.yandex.cloud.priv.datasphere.v2.Secret\x12\x61\n\x03Get\x12\x31.yandex.cloud.priv.datasphere.v2.GetSecretRequest\x1a\'.yandex.cloud.priv.datasphere.v2.Secret\x12g\n\x06Update\x12\x34.yandex.cloud.priv.datasphere.v2.UpdateSecretRequest\x1a\'.yandex.cloud.priv.datasphere.v2.Secret\x12V\n\x06\x44\x65lete\x12\x34.yandex.cloud.priv.datasphere.v2.DeleteSecretRequest\x1a\x16.google.protobuf.Empty\x12r\n\x07\x44\x65\x63rypt\x12\x35.yandex.cloud.priv.datasphere.v2.DecryptSecretRequest\x1a\x30.yandex.cloud.priv.datasphere.v2.DecryptedSecret\x12\x8b\x01\n\x0bListProject\x12:.yandex.cloud.priv.datasphere.v2.ListProjectSecretsRequest\x1a;.yandex.cloud.priv.datasphere.v2.ListProjectSecretsResponse\"\x03\x88\x02\x01\x12\x92\x01\n\x12ListProjectSecrets\x12:.yandex.cloud.priv.datasphere.v2.ListProjectSecretsRequest\x1a;.yandex.cloud.priv.datasphere.v2.ListProjectSecretsResponse\"\x03\x88\x02\x01\x12\x85\x01\n\tListSpace\x12\x38.yandex.cloud.priv.datasphere.v2.ListSpaceSecretsRequest\x1a\x39.yandex.cloud.priv.datasphere.v2.ListSpaceSecretsResponse\"\x03\x88\x02\x01\x42\x37\n\"yandex.cloud.priv.datasphere.v2ydsB\x05\x44SSCSZ\ndatasphereb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.priv.datasphere.v2.secret_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"yandex.cloud.priv.datasphere.v2ydsB\005DSSCSZ\ndatasphere'
  _globals['_CREATESECRETREQUEST_LABELSENTRY']._options = None
  _globals['_CREATESECRETREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_CREATESECRETREQUEST'].fields_by_name['project_id']._options = None
  _globals['_CREATESECRETREQUEST'].fields_by_name['project_id']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_CREATESECRETREQUEST'].fields_by_name['name']._options = None
  _globals['_CREATESECRETREQUEST'].fields_by_name['name']._serialized_options = b'\250\2111\001\262\2111&[a-zA-Z][-_a-zA-Z0-9]{1,61}[a-zA-Z0-9]\312\2111\004<=63'
  _globals['_CREATESECRETREQUEST'].fields_by_name['description']._options = None
  _globals['_CREATESECRETREQUEST'].fields_by_name['description']._serialized_options = b'\312\2111\005<=256'
  _globals['_CREATESECRETREQUEST'].fields_by_name['labels']._options = None
  _globals['_CREATESECRETREQUEST'].fields_by_name['labels']._serialized_options = b'\262\2111\013[-_0-9a-z]*\302\2111\004<=64\312\2111\004<=63\362\2111\030\022\020[a-z][-_0-9a-z]*\032\0041-63'
  _globals['_UPDATESECRETREQUEST_LABELSENTRY']._options = None
  _globals['_UPDATESECRETREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_UPDATESECRETREQUEST'].fields_by_name['secret_id']._options = None
  _globals['_UPDATESECRETREQUEST'].fields_by_name['secret_id']._serialized_options = b'\250\2111\001'
  _globals['_UPDATESECRETREQUEST'].fields_by_name['name']._options = None
  _globals['_UPDATESECRETREQUEST'].fields_by_name['name']._serialized_options = b'\262\2111&[a-zA-Z][-_a-zA-Z0-9]{1,61}[a-zA-Z0-9]\312\2111\004<=63'
  _globals['_UPDATESECRETREQUEST'].fields_by_name['description']._options = None
  _globals['_UPDATESECRETREQUEST'].fields_by_name['description']._serialized_options = b'\312\2111\005<=256'
  _globals['_UPDATESECRETREQUEST'].fields_by_name['labels']._options = None
  _globals['_UPDATESECRETREQUEST'].fields_by_name['labels']._serialized_options = b'\262\2111\013[-_0-9a-z]*\302\2111\004<=64\312\2111\004<=63\362\2111\030\022\020[a-z][-_0-9a-z]*\032\0041-63'
  _globals['_GETSECRETREQUEST'].fields_by_name['secret_id']._options = None
  _globals['_GETSECRETREQUEST'].fields_by_name['secret_id']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_DELETESECRETREQUEST'].fields_by_name['secret_id']._options = None
  _globals['_DELETESECRETREQUEST'].fields_by_name['secret_id']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_DECRYPTSECRETREQUEST'].fields_by_name['secret_id']._options = None
  _globals['_DECRYPTSECRETREQUEST'].fields_by_name['secret_id']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_LISTPROJECTSECRETSREQUEST'].fields_by_name['project_id']._options = None
  _globals['_LISTPROJECTSECRETSREQUEST'].fields_by_name['project_id']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_LISTSPACESECRETSREQUEST'].fields_by_name['space_id']._options = None
  _globals['_LISTSPACESECRETSREQUEST'].fields_by_name['space_id']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_SECRETSERVICE'].methods_by_name['ListProject']._options = None
  _globals['_SECRETSERVICE'].methods_by_name['ListProject']._serialized_options = b'\210\002\001'
  _globals['_SECRETSERVICE'].methods_by_name['ListProjectSecrets']._options = None
  _globals['_SECRETSERVICE'].methods_by_name['ListProjectSecrets']._serialized_options = b'\210\002\001'
  _globals['_SECRETSERVICE'].methods_by_name['ListSpace']._options = None
  _globals['_SECRETSERVICE'].methods_by_name['ListSpace']._serialized_options = b'\210\002\001'
  _globals['_CREATESECRETREQUEST']._serialized_start=235
  _globals['_CREATESECRETREQUEST']._serialized_end=655
  _globals['_CREATESECRETREQUEST_LABELSENTRY']._serialized_start=610
  _globals['_CREATESECRETREQUEST_LABELSENTRY']._serialized_end=655
  _globals['_UPDATESECRETREQUEST']._serialized_start=658
  _globals['_UPDATESECRETREQUEST']._serialized_end=1114
  _globals['_UPDATESECRETREQUEST_LABELSENTRY']._serialized_start=610
  _globals['_UPDATESECRETREQUEST_LABELSENTRY']._serialized_end=655
  _globals['_GETSECRETREQUEST']._serialized_start=1116
  _globals['_GETSECRETREQUEST']._serialized_end=1167
  _globals['_DELETESECRETREQUEST']._serialized_start=1169
  _globals['_DELETESECRETREQUEST']._serialized_end=1223
  _globals['_DECRYPTSECRETREQUEST']._serialized_start=1225
  _globals['_DECRYPTSECRETREQUEST']._serialized_end=1280
  _globals['_LISTPROJECTSECRETSREQUEST']._serialized_start=1282
  _globals['_LISTPROJECTSECRETSREQUEST']._serialized_end=1343
  _globals['_LISTPROJECTSECRETSRESPONSE']._serialized_start=1345
  _globals['_LISTPROJECTSECRETSRESPONSE']._serialized_end=1431
  _globals['_LISTSPACESECRETSREQUEST']._serialized_start=1433
  _globals['_LISTSPACESECRETSREQUEST']._serialized_end=1490
  _globals['_LISTSPACESECRETSRESPONSE']._serialized_start=1492
  _globals['_LISTSPACESECRETSRESPONSE']._serialized_end=1576
  _globals['_SECRETSERVICE']._serialized_start=1579
  _globals['_SECRETSERVICE']._serialized_end=2534
# @@protoc_insertion_point(module_scope)
