# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/priv/iam/v1/iam_credential_service.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud.priv import validation_pb2 as yandex_dot_cloud_dot_priv_dot_validation__pb2
from yandex.cloud.priv.iam.v1 import revoked_credential_pb2 as yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_revoked__credential__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5yandex/cloud/priv/iam/v1/iam_credential_service.proto\x12\x18yandex.cloud.priv.iam.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\"yandex/cloud/priv/validation.proto\x1a\x31yandex/cloud/priv/iam/v1/revoked_credential.proto\"\xba\x01\n\x17RevokeCredentialRequest\x12)\n\x11\x61uthorized_key_id\x18\x01 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50H\x00\x12(\n\x10refresh_token_id\x18\x02 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50H\x00\x12\x30\n\x0c\x64\x65lete_after\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x18\n\x10revoke_condition\x12\x04\x80\x83\x31\x01\x32\x80\x01\n\x14IamCredentialService\x12h\n\x06Revoke\x12\x31.yandex.cloud.priv.iam.v1.RevokeCredentialRequest\x1a+.yandex.cloud.priv.iam.v1.RevokedCredentialB\x0c\x42\x05PICRSZ\x03iamb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.priv.iam.v1.iam_credential_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'B\005PICRSZ\003iam'
  _globals['_REVOKECREDENTIALREQUEST'].oneofs_by_name['revoke_condition']._options = None
  _globals['_REVOKECREDENTIALREQUEST'].oneofs_by_name['revoke_condition']._serialized_options = b'\200\2031\001'
  _globals['_REVOKECREDENTIALREQUEST'].fields_by_name['authorized_key_id']._options = None
  _globals['_REVOKECREDENTIALREQUEST'].fields_by_name['authorized_key_id']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_REVOKECREDENTIALREQUEST'].fields_by_name['refresh_token_id']._options = None
  _globals['_REVOKECREDENTIALREQUEST'].fields_by_name['refresh_token_id']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_REVOKECREDENTIALREQUEST']._serialized_start=204
  _globals['_REVOKECREDENTIALREQUEST']._serialized_end=390
  _globals['_IAMCREDENTIALSERVICE']._serialized_start=393
  _globals['_IAMCREDENTIALSERVICE']._serialized_end=521
# @@protoc_insertion_point(module_scope)
