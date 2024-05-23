# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/priv/iam/v1/iam_token_service.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud.priv import validation_pb2 as yandex_dot_cloud_dot_priv_dot_validation__pb2
from yandex.cloud.priv import sensitive_pb2 as yandex_dot_cloud_dot_priv_dot_sensitive__pb2
from yandex.cloud.priv.iam.v1.ts import iam_token_service_subject_pb2 as yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_ts_dot_iam__token__service__subject__pb2
from yandex.cloud.priv.iam.v1 import yandex_passport_cookie_pb2 as yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_yandex__passport__cookie__pb2
from yandex.cloud.priv.oauth.v1 import oauth_request_pb2 as yandex_dot_cloud_dot_priv_dot_oauth_dot_v1_dot_oauth__request__pb2
from yandex.cloud.priv.iam.v1 import revoked_credential_pb2 as yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_revoked__credential__pb2
from yandex.cloud.priv.iam.v1 import resource_boundary_pb2 as yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_resource__boundary__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0yandex/cloud/priv/iam/v1/iam_token_service.proto\x12\x18yandex.cloud.priv.iam.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\"yandex/cloud/priv/validation.proto\x1a!yandex/cloud/priv/sensitive.proto\x1a;yandex/cloud/priv/iam/v1/ts/iam_token_service_subject.proto\x1a\x35yandex/cloud/priv/iam/v1/yandex_passport_cookie.proto\x1a.yandex/cloud/priv/oauth/v1/oauth_request.proto\x1a\x31yandex/cloud/priv/iam/v1/revoked_credential.proto\x1a\x30yandex/cloud/priv/iam/v1/resource_boundary.proto\"\xfb\x01\n\x15\x43reateIamTokenRequest\x12\x39\n\x1byandex_passport_oauth_token\x18\x01 \x01(\tB\x12\xca\x89\x31\x06<=4000\xc8\x8f\x31\x01\xd0\x8f\x31\x04H\x00\x12!\n\x03jwt\x18\x02 \x01(\tB\x12\xca\x89\x31\x06<=8000\xc8\x8f\x31\x01\xd0\x8f\x31\x07H\x00\x12\x1e\n\niam_cookie\x18\x03 \x01(\tB\x08\xc8\x8f\x31\x01\xd0\x8f\x31\x05H\x00\x12R\n\x17yandex_passport_cookies\x18\x04 \x01(\x0b\x32/.yandex.cloud.priv.iam.v1.YandexPassportCookiesH\x00\x42\x10\n\x08identity\x12\x04\x80\x83\x31\x01\"\xbc\x01\n\x1f\x43reateIamTokenForSubjectRequest\x12 \n\nsubject_id\x18\x01 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\x12?\n\roauth_request\x18\x02 \x01(\x0b\x32(.yandex.cloud.priv.oauth.v1.OAuthRequest\x12\x12\n\nsession_id\x18\x03 \x01(\t\x12\"\n\x10refresh_token_id\x18\x04 \x01(\tB\x08\xca\x89\x31\x04<=50\"\xfc\x01\n!CreateIamTokenForAccessKeyRequest\x12\x45\n\tsignature\x18\x01 \x01(\x0b\x32,.yandex.cloud.priv.iam.v1.AccessKeySignatureB\x04\xa8\x89\x31\x01\x12&\n\x03ttl\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x1f\n\tclient_id\x18\x03 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\x12G\n\x13resource_boundaries\x18\x04 \x03(\x0b\x32*.yandex.cloud.priv.iam.v1.ResourceBoundary\"r\n&CreateIamTokenForServiceAccountRequest\x12(\n\x12service_account_id\x18\x01 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\x12\x1e\n\x04path\x18\x02 \x03(\tB\x10\xc2\x89\x31\x04<=10\xca\x89\x31\x04<=50\"\xdb\x01\n\x1f\x43reateIamTokenForServiceRequest\x12 \n\nservice_id\x18\x01 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\x12!\n\x0fmicroservice_id\x18\x02 \x01(\tB\x08\xca\x89\x31\x04<=50\x12!\n\x0bresource_id\x18\x03 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\x12#\n\rresource_type\x18\x04 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\x12+\n\x19target_service_account_id\x18\x05 \x01(\tB\x08\xca\x89\x31\x04<=50\"v\n\'CreateIamTokenForComputeInstanceRequest\x12(\n\x12service_account_id\x18\x01 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\x12!\n\x0binstance_id\x18\x02 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\"\xcb\x01\n\x16\x43reateIamTokenResponse\x12\x1b\n\tiam_token\x18\x01 \x01(\tB\x08\xc8\x8f\x31\x01\xd0\x8f\x31\x02\x12-\n\tissued_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nexpires_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x35\n\x07subject\x18\x03 \x01(\x0b\x32$.yandex.cloud.priv.iam.v1.ts.Subject\"8\n\x15RevokeIamTokenRequest\x12\x1f\n\tiam_token\x18\x01 \x01(\tB\x0c\xa8\x89\x31\x01\xc8\x8f\x31\x01\xd0\x8f\x31\x02\"u\n\x16RevokeIamTokenResponse\x12\x12\n\nsubject_id\x18\x01 \x01(\t\x12G\n\x12revoked_credential\x18\x02 \x01(\x0b\x32+.yandex.cloud.priv.iam.v1.RevokedCredential\"\xe2\x05\n\x12\x41\x63\x63\x65ssKeySignature\x12#\n\raccess_key_id\x18\x01 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\x12&\n\x0estring_to_sign\x18\x02 \x01(\tB\x0e\xa8\x89\x31\x01\xca\x89\x31\x06<=8192\x12(\n\tsignature\x18\x03 \x01(\tB\x15\xa8\x89\x31\x01\xca\x89\x31\x05<=128\xc8\x8f\x31\x01\xd0\x8f\x31\x01\x12X\n\rv2_parameters\x18\x04 \x01(\x0b\x32?.yandex.cloud.priv.iam.v1.AccessKeySignature.Version2ParametersH\x00\x12X\n\rv4_parameters\x18\x05 \x01(\x0b\x32?.yandex.cloud.priv.iam.v1.AccessKeySignature.Version4ParametersH\x00\x12-\n\rsession_token\x18\x06 \x01(\tB\x16\xa8\x89\x31\x00\xca\x89\x31\x06<=4096\xc8\x8f\x31\x01\xd0\x8f\x31\n\x1a\xd4\x01\n\x12Version2Parameters\x12i\n\x10signature_method\x18\x01 \x01(\x0e\x32O.yandex.cloud.priv.iam.v1.AccessKeySignature.Version2Parameters.SignatureMethod\"S\n\x0fSignatureMethod\x12 \n\x1cSIGNATURE_METHOD_UNSPECIFIED\x10\x00\x12\r\n\tHMAC_SHA1\x10\x01\x12\x0f\n\x0bHMAC_SHA256\x10\x02\x1a\x86\x01\n\x12Version4Parameters\x12\x33\n\tsigned_at\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xa8\x89\x31\x01\x12\x1d\n\x07service\x18\x02 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=64\x12\x1c\n\x06region\x18\x03 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=32B\x12\n\nparameters\x12\x04\x80\x83\x31\x01\"\x8a\x01\n\x17\x45xchangeIamTokenRequest\x12&\n\x03ttl\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration\x12G\n\x13resource_boundaries\x18\x02 \x03(\x0b\x32*.yandex.cloud.priv.iam.v1.ResourceBoundary\"\xcd\x01\n\x18\x45xchangeIamTokenResponse\x12\x1b\n\tiam_token\x18\x01 \x01(\tB\x08\xc8\x8f\x31\x01\xd0\x8f\x31\x02\x12-\n\tissued_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nexpires_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x35\n\x07subject\x18\x04 \x01(\x0b\x32$.yandex.cloud.priv.iam.v1.ts.Subject2\xaf\t\n\x0fIamTokenService\x12\x86\x01\n\x06\x43reate\x12/.yandex.cloud.priv.iam.v1.CreateIamTokenRequest\x1a\x30.yandex.cloud.priv.iam.v1.CreateIamTokenResponse\"\x19\x82\xd3\xe4\x93\x02\x13\"\x0e/iam/v1/tokens:\x01*\x12\x83\x01\n\x12\x43reateForAccessKey\x12;.yandex.cloud.priv.iam.v1.CreateIamTokenForAccessKeyRequest\x1a\x30.yandex.cloud.priv.iam.v1.CreateIamTokenResponse\x12\x8d\x01\n\x17\x43reateForServiceAccount\x12@.yandex.cloud.priv.iam.v1.CreateIamTokenForServiceAccountRequest\x1a\x30.yandex.cloud.priv.iam.v1.CreateIamTokenResponse\x12\x7f\n\x10\x43reateForService\x12\x39.yandex.cloud.priv.iam.v1.CreateIamTokenForServiceRequest\x1a\x30.yandex.cloud.priv.iam.v1.CreateIamTokenResponse\x12\x8f\x01\n\x18\x43reateForComputeInstance\x12\x41.yandex.cloud.priv.iam.v1.CreateIamTokenForComputeInstanceRequest\x1a\x30.yandex.cloud.priv.iam.v1.CreateIamTokenResponse\x12\x88\x01\n\x14\x43reateForUserAccount\x12\x39.yandex.cloud.priv.iam.v1.CreateIamTokenForSubjectRequest\x1a\x30.yandex.cloud.priv.iam.v1.CreateIamTokenResponse\"\x03\x88\x02\x01\x12\x7f\n\x10\x43reateForSubject\x12\x39.yandex.cloud.priv.iam.v1.CreateIamTokenForSubjectRequest\x1a\x30.yandex.cloud.priv.iam.v1.CreateIamTokenResponse\x12k\n\x06Revoke\x12/.yandex.cloud.priv.iam.v1.RevokeIamTokenRequest\x1a\x30.yandex.cloud.priv.iam.v1.RevokeIamTokenResponse\x12q\n\x08\x45xchange\x12\x31.yandex.cloud.priv.iam.v1.ExchangeIamTokenRequest\x1a\x32.yandex.cloud.priv.iam.v1.ExchangeIamTokenResponseB\x0b\x42\x04PITSZ\x03iamb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.priv.iam.v1.iam_token_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'B\004PITSZ\003iam'
  _globals['_CREATEIAMTOKENREQUEST'].oneofs_by_name['identity']._options = None
  _globals['_CREATEIAMTOKENREQUEST'].oneofs_by_name['identity']._serialized_options = b'\200\2031\001'
  _globals['_CREATEIAMTOKENREQUEST'].fields_by_name['yandex_passport_oauth_token']._options = None
  _globals['_CREATEIAMTOKENREQUEST'].fields_by_name['yandex_passport_oauth_token']._serialized_options = b'\312\2111\006<=4000\310\2171\001\320\2171\004'
  _globals['_CREATEIAMTOKENREQUEST'].fields_by_name['jwt']._options = None
  _globals['_CREATEIAMTOKENREQUEST'].fields_by_name['jwt']._serialized_options = b'\312\2111\006<=8000\310\2171\001\320\2171\007'
  _globals['_CREATEIAMTOKENREQUEST'].fields_by_name['iam_cookie']._options = None
  _globals['_CREATEIAMTOKENREQUEST'].fields_by_name['iam_cookie']._serialized_options = b'\310\2171\001\320\2171\005'
  _globals['_CREATEIAMTOKENFORSUBJECTREQUEST'].fields_by_name['subject_id']._options = None
  _globals['_CREATEIAMTOKENFORSUBJECTREQUEST'].fields_by_name['subject_id']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_CREATEIAMTOKENFORSUBJECTREQUEST'].fields_by_name['refresh_token_id']._options = None
  _globals['_CREATEIAMTOKENFORSUBJECTREQUEST'].fields_by_name['refresh_token_id']._serialized_options = b'\312\2111\004<=50'
  _globals['_CREATEIAMTOKENFORACCESSKEYREQUEST'].fields_by_name['signature']._options = None
  _globals['_CREATEIAMTOKENFORACCESSKEYREQUEST'].fields_by_name['signature']._serialized_options = b'\250\2111\001'
  _globals['_CREATEIAMTOKENFORACCESSKEYREQUEST'].fields_by_name['client_id']._options = None
  _globals['_CREATEIAMTOKENFORACCESSKEYREQUEST'].fields_by_name['client_id']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_CREATEIAMTOKENFORSERVICEACCOUNTREQUEST'].fields_by_name['service_account_id']._options = None
  _globals['_CREATEIAMTOKENFORSERVICEACCOUNTREQUEST'].fields_by_name['service_account_id']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_CREATEIAMTOKENFORSERVICEACCOUNTREQUEST'].fields_by_name['path']._options = None
  _globals['_CREATEIAMTOKENFORSERVICEACCOUNTREQUEST'].fields_by_name['path']._serialized_options = b'\302\2111\004<=10\312\2111\004<=50'
  _globals['_CREATEIAMTOKENFORSERVICEREQUEST'].fields_by_name['service_id']._options = None
  _globals['_CREATEIAMTOKENFORSERVICEREQUEST'].fields_by_name['service_id']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_CREATEIAMTOKENFORSERVICEREQUEST'].fields_by_name['microservice_id']._options = None
  _globals['_CREATEIAMTOKENFORSERVICEREQUEST'].fields_by_name['microservice_id']._serialized_options = b'\312\2111\004<=50'
  _globals['_CREATEIAMTOKENFORSERVICEREQUEST'].fields_by_name['resource_id']._options = None
  _globals['_CREATEIAMTOKENFORSERVICEREQUEST'].fields_by_name['resource_id']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_CREATEIAMTOKENFORSERVICEREQUEST'].fields_by_name['resource_type']._options = None
  _globals['_CREATEIAMTOKENFORSERVICEREQUEST'].fields_by_name['resource_type']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_CREATEIAMTOKENFORSERVICEREQUEST'].fields_by_name['target_service_account_id']._options = None
  _globals['_CREATEIAMTOKENFORSERVICEREQUEST'].fields_by_name['target_service_account_id']._serialized_options = b'\312\2111\004<=50'
  _globals['_CREATEIAMTOKENFORCOMPUTEINSTANCEREQUEST'].fields_by_name['service_account_id']._options = None
  _globals['_CREATEIAMTOKENFORCOMPUTEINSTANCEREQUEST'].fields_by_name['service_account_id']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_CREATEIAMTOKENFORCOMPUTEINSTANCEREQUEST'].fields_by_name['instance_id']._options = None
  _globals['_CREATEIAMTOKENFORCOMPUTEINSTANCEREQUEST'].fields_by_name['instance_id']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_CREATEIAMTOKENRESPONSE'].fields_by_name['iam_token']._options = None
  _globals['_CREATEIAMTOKENRESPONSE'].fields_by_name['iam_token']._serialized_options = b'\310\2171\001\320\2171\002'
  _globals['_REVOKEIAMTOKENREQUEST'].fields_by_name['iam_token']._options = None
  _globals['_REVOKEIAMTOKENREQUEST'].fields_by_name['iam_token']._serialized_options = b'\250\2111\001\310\2171\001\320\2171\002'
  _globals['_ACCESSKEYSIGNATURE_VERSION4PARAMETERS'].fields_by_name['signed_at']._options = None
  _globals['_ACCESSKEYSIGNATURE_VERSION4PARAMETERS'].fields_by_name['signed_at']._serialized_options = b'\250\2111\001'
  _globals['_ACCESSKEYSIGNATURE_VERSION4PARAMETERS'].fields_by_name['service']._options = None
  _globals['_ACCESSKEYSIGNATURE_VERSION4PARAMETERS'].fields_by_name['service']._serialized_options = b'\250\2111\001\312\2111\004<=64'
  _globals['_ACCESSKEYSIGNATURE_VERSION4PARAMETERS'].fields_by_name['region']._options = None
  _globals['_ACCESSKEYSIGNATURE_VERSION4PARAMETERS'].fields_by_name['region']._serialized_options = b'\250\2111\001\312\2111\004<=32'
  _globals['_ACCESSKEYSIGNATURE'].oneofs_by_name['parameters']._options = None
  _globals['_ACCESSKEYSIGNATURE'].oneofs_by_name['parameters']._serialized_options = b'\200\2031\001'
  _globals['_ACCESSKEYSIGNATURE'].fields_by_name['access_key_id']._options = None
  _globals['_ACCESSKEYSIGNATURE'].fields_by_name['access_key_id']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_ACCESSKEYSIGNATURE'].fields_by_name['string_to_sign']._options = None
  _globals['_ACCESSKEYSIGNATURE'].fields_by_name['string_to_sign']._serialized_options = b'\250\2111\001\312\2111\006<=8192'
  _globals['_ACCESSKEYSIGNATURE'].fields_by_name['signature']._options = None
  _globals['_ACCESSKEYSIGNATURE'].fields_by_name['signature']._serialized_options = b'\250\2111\001\312\2111\005<=128\310\2171\001\320\2171\001'
  _globals['_ACCESSKEYSIGNATURE'].fields_by_name['session_token']._options = None
  _globals['_ACCESSKEYSIGNATURE'].fields_by_name['session_token']._serialized_options = b'\250\2111\000\312\2111\006<=4096\310\2171\001\320\2171\n'
  _globals['_EXCHANGEIAMTOKENRESPONSE'].fields_by_name['iam_token']._options = None
  _globals['_EXCHANGEIAMTOKENRESPONSE'].fields_by_name['iam_token']._serialized_options = b'\310\2171\001\320\2171\002'
  _globals['_IAMTOKENSERVICE'].methods_by_name['Create']._options = None
  _globals['_IAMTOKENSERVICE'].methods_by_name['Create']._serialized_options = b'\202\323\344\223\002\023\"\016/iam/v1/tokens:\001*'
  _globals['_IAMTOKENSERVICE'].methods_by_name['CreateForUserAccount']._options = None
  _globals['_IAMTOKENSERVICE'].methods_by_name['CreateForUserAccount']._serialized_options = b'\210\002\001'
  _globals['_CREATEIAMTOKENREQUEST']._serialized_start=510
  _globals['_CREATEIAMTOKENREQUEST']._serialized_end=761
  _globals['_CREATEIAMTOKENFORSUBJECTREQUEST']._serialized_start=764
  _globals['_CREATEIAMTOKENFORSUBJECTREQUEST']._serialized_end=952
  _globals['_CREATEIAMTOKENFORACCESSKEYREQUEST']._serialized_start=955
  _globals['_CREATEIAMTOKENFORACCESSKEYREQUEST']._serialized_end=1207
  _globals['_CREATEIAMTOKENFORSERVICEACCOUNTREQUEST']._serialized_start=1209
  _globals['_CREATEIAMTOKENFORSERVICEACCOUNTREQUEST']._serialized_end=1323
  _globals['_CREATEIAMTOKENFORSERVICEREQUEST']._serialized_start=1326
  _globals['_CREATEIAMTOKENFORSERVICEREQUEST']._serialized_end=1545
  _globals['_CREATEIAMTOKENFORCOMPUTEINSTANCEREQUEST']._serialized_start=1547
  _globals['_CREATEIAMTOKENFORCOMPUTEINSTANCEREQUEST']._serialized_end=1665
  _globals['_CREATEIAMTOKENRESPONSE']._serialized_start=1668
  _globals['_CREATEIAMTOKENRESPONSE']._serialized_end=1871
  _globals['_REVOKEIAMTOKENREQUEST']._serialized_start=1873
  _globals['_REVOKEIAMTOKENREQUEST']._serialized_end=1929
  _globals['_REVOKEIAMTOKENRESPONSE']._serialized_start=1931
  _globals['_REVOKEIAMTOKENRESPONSE']._serialized_end=2048
  _globals['_ACCESSKEYSIGNATURE']._serialized_start=2051
  _globals['_ACCESSKEYSIGNATURE']._serialized_end=2789
  _globals['_ACCESSKEYSIGNATURE_VERSION2PARAMETERS']._serialized_start=2420
  _globals['_ACCESSKEYSIGNATURE_VERSION2PARAMETERS']._serialized_end=2632
  _globals['_ACCESSKEYSIGNATURE_VERSION2PARAMETERS_SIGNATUREMETHOD']._serialized_start=2549
  _globals['_ACCESSKEYSIGNATURE_VERSION2PARAMETERS_SIGNATUREMETHOD']._serialized_end=2632
  _globals['_ACCESSKEYSIGNATURE_VERSION4PARAMETERS']._serialized_start=2635
  _globals['_ACCESSKEYSIGNATURE_VERSION4PARAMETERS']._serialized_end=2769
  _globals['_EXCHANGEIAMTOKENREQUEST']._serialized_start=2792
  _globals['_EXCHANGEIAMTOKENREQUEST']._serialized_end=2930
  _globals['_EXCHANGEIAMTOKENRESPONSE']._serialized_start=2933
  _globals['_EXCHANGEIAMTOKENRESPONSE']._serialized_end=3138
  _globals['_IAMTOKENSERVICE']._serialized_start=3141
  _globals['_IAMTOKENSERVICE']._serialized_end=4340
# @@protoc_insertion_point(module_scope)
