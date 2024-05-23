# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/priv/iam/v1/mfa/totp_profile_service.proto
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
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.priv.iam.v1.mfa import totp_profile_pb2 as yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_mfa_dot_totp__profile__pb2
from yandex.cloud.priv.operation import operation_pb2 as yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2
from yandex.cloud.priv import sensitive_pb2 as yandex_dot_cloud_dot_priv_dot_sensitive__pb2
from yandex.cloud.priv import validation_pb2 as yandex_dot_cloud_dot_priv_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7yandex/cloud/priv/iam/v1/mfa/totp_profile_service.proto\x12\x1cyandex.cloud.priv.iam.v1.mfa\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a yandex/cloud/api/operation.proto\x1a/yandex/cloud/priv/iam/v1/mfa/totp_profile.proto\x1a+yandex/cloud/priv/operation/operation.proto\x1a!yandex/cloud/priv/sensitive.proto\x1a\"yandex/cloud/priv/validation.proto\"\xba\x01\n\x18\x43reateTotpProfileRequest\x12>\n\talgorithm\x18\x01 \x01(\x0e\x32+.yandex.cloud.priv.iam.v1.mfa.HashAlgorithm\x12\x1b\n\x06\x64igits\x18\x02 \x01(\x03\x42\x0b\xba\x89\x31\x07\x30,6,7,8\x12\x41\n\x07options\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.priv.iam.v1.mfa.TotpProfileOptions\"/\n\x19\x43reateTotpProfileMetadata\x12\x12\n\nsubject_id\x18\x01 \x01(\t\"\x82\x01\n\x19\x43reateTotpProfileResponse\x12\x14\n\x06secret\x18\x01 \x01(\tB\x04\xc8\x8f\x31\x01\x12\x0e\n\x06issuer\x18\x02 \x01(\t\x12?\n\x0ctotp_profile\x18\x03 \x01(\x0b\x32).yandex.cloud.priv.iam.v1.mfa.TotpProfile\";\n\x1fGetTotpProfileForSubjectRequest\x12\x18\n\nsubject_id\x18\x01 \x01(\tB\x04\xa8\x89\x31\x01\"8\n\x18\x44\x65leteTotpProfileRequest\x12\x1c\n\x04\x63ode\x18\x01 \x01(\x03\x42\x0e\xba\x89\x31\x02>0\xc8\x8f\x31\x01\xd0\x8f\x31\x03\">\n\"DeleteTotpProfileForSubjectRequest\x12\x18\n\nsubject_id\x18\x01 \x01(\tB\x04\xa8\x89\x31\x01\"/\n\x19\x44\x65leteTotpProfileMetadata\x12\x12\n\nsubject_id\x18\x01 \x01(\t\"9\n#DeleteTotpProfileForSubjectMetadata\x12\x12\n\nsubject_id\x18\x01 \x01(\t\"a\n ListTotpProfileOperationsRequest\x12\x1d\n\tpage_size\x18\x01 \x01(\x03\x42\n\xba\x89\x31\x06\x30-1000\x12\x1e\n\npage_token\x18\x02 \x01(\tB\n\xca\x89\x31\x06<=2000\"x\n!ListTotpProfileOperationsResponse\x12:\n\noperations\x18\x01 \x03(\x0b\x32&.yandex.cloud.priv.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"1\n\x11VerifyTotpRequest\x12\x1c\n\x04\x63ode\x18\x01 \x01(\x03\x42\x0e\xba\x89\x31\x02>0\xc8\x8f\x31\x01\xd0\x8f\x31\x03\"\xa9\x01\n\x12VerifyTotpResponse\x12@\n\x06result\x18\x01 \x01(\x0e\x32\x30.yandex.cloud.priv.iam.v1.mfa.VerificationResult\x12#\n\x11set_cookie_header\x18\x02 \x03(\tB\x08\xc8\x8f\x31\x01\xd0\x8f\x31\t\x12,\n\x08retry_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp2\xed\x07\n\x12TotpProfileService\x12J\n\x03Get\x12\x16.google.protobuf.Empty\x1a).yandex.cloud.priv.iam.v1.mfa.TotpProfile\"\x00\x12\xa4\x01\n\x06\x43reate\x12\x36.yandex.cloud.priv.iam.v1.mfa.CreateTotpProfileRequest\x1a&.yandex.cloud.priv.operation.Operation\":\xb2\xd2*6\n\x19\x43reateTotpProfileMetadata\x12\x19\x43reateTotpProfileResponse\x12\xa0\x01\n\x06\x44\x65lete\x12\x36.yandex.cloud.priv.iam.v1.mfa.DeleteTotpProfileRequest\x1a&.yandex.cloud.priv.operation.Operation\"6\xb2\xd2*2\n\x19\x44\x65leteTotpProfileMetadata\x12\x15google.protobuf.Empty\x12\x93\x01\n\x0eListOperations\x12>.yandex.cloud.priv.iam.v1.mfa.ListTotpProfileOperationsRequest\x1a?.yandex.cloud.priv.iam.v1.mfa.ListTotpProfileOperationsResponse\"\x00\x12m\n\x06Verify\x12/.yandex.cloud.priv.iam.v1.mfa.VerifyTotpRequest\x1a\x30.yandex.cloud.priv.iam.v1.mfa.VerifyTotpResponse\"\x00\x12{\n\rGetForSubject\x12=.yandex.cloud.priv.iam.v1.mfa.GetTotpProfileForSubjectRequest\x1a).yandex.cloud.priv.iam.v1.mfa.TotpProfile\"\x00\x12\xbe\x01\n\x10\x44\x65leteForSubject\x12@.yandex.cloud.priv.iam.v1.mfa.DeleteTotpProfileForSubjectRequest\x1a&.yandex.cloud.priv.operation.Operation\"@\xb2\xd2*<\n#DeleteTotpProfileForSubjectMetadata\x12\x15google.protobuf.EmptyB\x0b\x42\x04PTPSZ\x03mfab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.priv.iam.v1.mfa.totp_profile_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'B\004PTPSZ\003mfa'
  _globals['_CREATETOTPPROFILEREQUEST'].fields_by_name['digits']._options = None
  _globals['_CREATETOTPPROFILEREQUEST'].fields_by_name['digits']._serialized_options = b'\272\2111\0070,6,7,8'
  _globals['_CREATETOTPPROFILERESPONSE'].fields_by_name['secret']._options = None
  _globals['_CREATETOTPPROFILERESPONSE'].fields_by_name['secret']._serialized_options = b'\310\2171\001'
  _globals['_GETTOTPPROFILEFORSUBJECTREQUEST'].fields_by_name['subject_id']._options = None
  _globals['_GETTOTPPROFILEFORSUBJECTREQUEST'].fields_by_name['subject_id']._serialized_options = b'\250\2111\001'
  _globals['_DELETETOTPPROFILEREQUEST'].fields_by_name['code']._options = None
  _globals['_DELETETOTPPROFILEREQUEST'].fields_by_name['code']._serialized_options = b'\272\2111\002>0\310\2171\001\320\2171\003'
  _globals['_DELETETOTPPROFILEFORSUBJECTREQUEST'].fields_by_name['subject_id']._options = None
  _globals['_DELETETOTPPROFILEFORSUBJECTREQUEST'].fields_by_name['subject_id']._serialized_options = b'\250\2111\001'
  _globals['_LISTTOTPPROFILEOPERATIONSREQUEST'].fields_by_name['page_size']._options = None
  _globals['_LISTTOTPPROFILEOPERATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\272\2111\0060-1000'
  _globals['_LISTTOTPPROFILEOPERATIONSREQUEST'].fields_by_name['page_token']._options = None
  _globals['_LISTTOTPPROFILEOPERATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\312\2111\006<=2000'
  _globals['_VERIFYTOTPREQUEST'].fields_by_name['code']._options = None
  _globals['_VERIFYTOTPREQUEST'].fields_by_name['code']._serialized_options = b'\272\2111\002>0\310\2171\001\320\2171\003'
  _globals['_VERIFYTOTPRESPONSE'].fields_by_name['set_cookie_header']._options = None
  _globals['_VERIFYTOTPRESPONSE'].fields_by_name['set_cookie_header']._serialized_options = b'\310\2171\001\320\2171\t'
  _globals['_TOTPPROFILESERVICE'].methods_by_name['Create']._options = None
  _globals['_TOTPPROFILESERVICE'].methods_by_name['Create']._serialized_options = b'\262\322*6\n\031CreateTotpProfileMetadata\022\031CreateTotpProfileResponse'
  _globals['_TOTPPROFILESERVICE'].methods_by_name['Delete']._options = None
  _globals['_TOTPPROFILESERVICE'].methods_by_name['Delete']._serialized_options = b'\262\322*2\n\031DeleteTotpProfileMetadata\022\025google.protobuf.Empty'
  _globals['_TOTPPROFILESERVICE'].methods_by_name['DeleteForSubject']._options = None
  _globals['_TOTPPROFILESERVICE'].methods_by_name['DeleteForSubject']._serialized_options = b'\262\322*<\n#DeleteTotpProfileForSubjectMetadata\022\025google.protobuf.Empty'
  _globals['_CREATETOTPPROFILEREQUEST']._serialized_start=351
  _globals['_CREATETOTPPROFILEREQUEST']._serialized_end=537
  _globals['_CREATETOTPPROFILEMETADATA']._serialized_start=539
  _globals['_CREATETOTPPROFILEMETADATA']._serialized_end=586
  _globals['_CREATETOTPPROFILERESPONSE']._serialized_start=589
  _globals['_CREATETOTPPROFILERESPONSE']._serialized_end=719
  _globals['_GETTOTPPROFILEFORSUBJECTREQUEST']._serialized_start=721
  _globals['_GETTOTPPROFILEFORSUBJECTREQUEST']._serialized_end=780
  _globals['_DELETETOTPPROFILEREQUEST']._serialized_start=782
  _globals['_DELETETOTPPROFILEREQUEST']._serialized_end=838
  _globals['_DELETETOTPPROFILEFORSUBJECTREQUEST']._serialized_start=840
  _globals['_DELETETOTPPROFILEFORSUBJECTREQUEST']._serialized_end=902
  _globals['_DELETETOTPPROFILEMETADATA']._serialized_start=904
  _globals['_DELETETOTPPROFILEMETADATA']._serialized_end=951
  _globals['_DELETETOTPPROFILEFORSUBJECTMETADATA']._serialized_start=953
  _globals['_DELETETOTPPROFILEFORSUBJECTMETADATA']._serialized_end=1010
  _globals['_LISTTOTPPROFILEOPERATIONSREQUEST']._serialized_start=1012
  _globals['_LISTTOTPPROFILEOPERATIONSREQUEST']._serialized_end=1109
  _globals['_LISTTOTPPROFILEOPERATIONSRESPONSE']._serialized_start=1111
  _globals['_LISTTOTPPROFILEOPERATIONSRESPONSE']._serialized_end=1231
  _globals['_VERIFYTOTPREQUEST']._serialized_start=1233
  _globals['_VERIFYTOTPREQUEST']._serialized_end=1282
  _globals['_VERIFYTOTPRESPONSE']._serialized_start=1285
  _globals['_VERIFYTOTPRESPONSE']._serialized_end=1454
  _globals['_TOTPPROFILESERVICE']._serialized_start=1457
  _globals['_TOTPPROFILESERVICE']._serialized_end=2462
# @@protoc_insertion_point(module_scope)
