# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/iam/v1/saml/federation_service.proto
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
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.iam.v1 import user_account_pb2 as yandex_dot_cloud_dot_iam_dot_v1_dot_user__account__pb2
from yandex.cloud.iam.v1.saml import federation_pb2 as yandex_dot_cloud_dot_iam_dot_v1_dot_saml_dot_federation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1yandex/cloud/iam/v1/saml/federation_service.proto\x12\x18yandex.cloud.iam.v1.saml\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/iam/v1/user_account.proto\x1a)yandex/cloud/iam/v1/saml/federation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"7\n\x14GetFederationRequest\x12\x1f\n\rfederation_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\"\xb9\x01\n\x16ListFederationsRequest\x12\x1c\n\x08\x63loud_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50H\x00\x12\x1d\n\tfolder_id\x18\x02 \x01(\tB\x08\x8a\xc8\x31\x04<=50H\x00\x12\x1d\n\tpage_size\x18\x03 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1e\n\npage_token\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=2000\x12\x1a\n\x06\x66ilter\x18\x05 \x01(\tB\n\x8a\xc8\x31\x06<=1000B\x07\n\x05scope\"m\n\x17ListFederationsResponse\x12\x39\n\x0b\x66\x65\x64\x65rations\x18\x01 \x03(\x0b\x32$.yandex.cloud.iam.v1.saml.Federation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xe0\x03\n\x17\x43reateFederationRequest\x12\x1b\n\tfolder_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x31\n\x04name\x18\x02 \x01(\tB#\xf2\xc7\x31\x1f[a-z]([-a-z0-9]{0,61}[a-z0-9])?\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12>\n\x0e\x63ookie_max_age\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationB\x0b\xfa\xc7\x31\x07\x31\x30m-12h\x12$\n\x1c\x61uto_create_account_on_login\x18\x05 \x01(\x08\x12\x1e\n\x06issuer\x18\x06 \x01(\tB\x0e\xe8\xc7\x31\x01\x8a\xc8\x31\x06<=8000\x12:\n\x0bsso_binding\x18\x07 \x01(\x0e\x32%.yandex.cloud.iam.v1.saml.BindingType\x12\x1f\n\x07sso_url\x18\x08 \x01(\tB\x0e\xe8\xc7\x31\x01\x8a\xc8\x31\x06<=8000\x12O\n\x11security_settings\x18\t \x01(\x0b\x32\x34.yandex.cloud.iam.v1.saml.FederationSecuritySettings\x12!\n\x19\x63\x61se_insensitive_name_ids\x18\n \x01(\x08\"1\n\x18\x43reateFederationMetadata\x12\x15\n\rfederation_id\x18\x01 \x01(\t\"\x96\x04\n\x17UpdateFederationRequest\x12\x1f\n\rfederation_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x32\n\x04name\x18\x03 \x01(\tB$\xf2\xc7\x31 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12>\n\x0e\x63ookie_max_age\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationB\x0b\xfa\xc7\x31\x07\x31\x30m-12h\x12$\n\x1c\x61uto_create_account_on_login\x18\x06 \x01(\x08\x12\x1e\n\x06issuer\x18\x07 \x01(\tB\x0e\xe8\xc7\x31\x01\x8a\xc8\x31\x06<=8000\x12:\n\x0bsso_binding\x18\x08 \x01(\x0e\x32%.yandex.cloud.iam.v1.saml.BindingType\x12\x1f\n\x07sso_url\x18\t \x01(\tB\x0e\xe8\xc7\x31\x01\x8a\xc8\x31\x06<=8000\x12O\n\x11security_settings\x18\n \x01(\x0b\x32\x34.yandex.cloud.iam.v1.saml.FederationSecuritySettings\x12!\n\x19\x63\x61se_insensitive_name_ids\x18\x0c \x01(\x08\"1\n\x18UpdateFederationMetadata\x12\x15\n\rfederation_id\x18\x01 \x01(\t\":\n\x17\x44\x65leteFederationRequest\x12\x1f\n\rfederation_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\"1\n\x18\x44\x65leteFederationMetadata\x12\x15\n\rfederation_id\x18\x01 \x01(\t\"`\n\x1f\x41\x64\x64\x46\x65\x64\x65ratedUserAccountsRequest\x12\x1f\n\rfederation_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x1c\n\x08name_ids\x18\x02 \x03(\tB\n\x8a\xc8\x31\x06<=1000\"9\n AddFederatedUserAccountsMetadata\x12\x15\n\rfederation_id\x18\x01 \x01(\t\"[\n AddFederatedUserAccountsResponse\x12\x37\n\ruser_accounts\x18\x01 \x03(\x0b\x32 .yandex.cloud.iam.v1.UserAccount\"\x86\x01\n ListFederatedUserAccountsRequest\x12#\n\rfederation_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1e\n\npage_token\x18\x03 \x01(\tB\n\x8a\xc8\x31\x06<=2000\"u\n!ListFederatedUserAccountsResponse\x12\x37\n\ruser_accounts\x18\x01 \x03(\x0b\x32 .yandex.cloud.iam.v1.UserAccount\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x81\x01\n\x1fListFederationOperationsRequest\x12\x1f\n\rfederation_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1e\n\npage_token\x18\x03 \x01(\tB\n\x8a\xc8\x31\x06<=2000\"r\n ListFederationOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\x83\x0c\n\x11\x46\x65\x64\x65rationService\x12\x8d\x01\n\x03Get\x12..yandex.cloud.iam.v1.saml.GetFederationRequest\x1a$.yandex.cloud.iam.v1.saml.Federation\"0\x82\xd3\xe4\x93\x02*\x12(/iam/v1/saml/federations/{federation_id}\x12\x8d\x01\n\x04List\x12\x30.yandex.cloud.iam.v1.saml.ListFederationsRequest\x1a\x31.yandex.cloud.iam.v1.saml.ListFederationsResponse\" \x82\xd3\xe4\x93\x02\x1a\x12\x18/iam/v1/saml/federations\x12\xad\x01\n\x06\x43reate\x12\x31.yandex.cloud.iam.v1.saml.CreateFederationRequest\x1a!.yandex.cloud.operation.Operation\"M\xb2\xd2*&\n\x18\x43reateFederationMetadata\x12\nFederation\x82\xd3\xe4\x93\x02\x1d\"\x18/iam/v1/saml/federations:\x01*\x12\xbd\x01\n\x06Update\x12\x31.yandex.cloud.iam.v1.saml.UpdateFederationRequest\x1a!.yandex.cloud.operation.Operation\"]\xb2\xd2*&\n\x18UpdateFederationMetadata\x12\nFederation\x82\xd3\xe4\x93\x02-2(/iam/v1/saml/federations/{federation_id}:\x01*\x12\xc5\x01\n\x06\x44\x65lete\x12\x31.yandex.cloud.iam.v1.saml.DeleteFederationRequest\x1a!.yandex.cloud.operation.Operation\"e\xb2\xd2*1\n\x18\x44\x65leteFederationMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02**(/iam/v1/saml/federations/{federation_id}\x12\xfd\x01\n\x0f\x41\x64\x64UserAccounts\x12\x39.yandex.cloud.iam.v1.saml.AddFederatedUserAccountsRequest\x1a!.yandex.cloud.operation.Operation\"\x8b\x01\xb2\xd2*D\n AddFederatedUserAccountsMetadata\x12 AddFederatedUserAccountsResponse\x82\xd3\xe4\x93\x02=\"8/iam/v1/saml/federations/{federation_id}:addUserAccounts:\x01*\x12\xce\x01\n\x10ListUserAccounts\x12:.yandex.cloud.iam.v1.saml.ListFederatedUserAccountsRequest\x1a;.yandex.cloud.iam.v1.saml.ListFederatedUserAccountsResponse\"A\x82\xd3\xe4\x93\x02;\x12\x39/iam/v1/saml/federations/{federation_id}:listUserAccounts\x12\xc4\x01\n\x0eListOperations\x12\x39.yandex.cloud.iam.v1.saml.ListFederationOperationsRequest\x1a:.yandex.cloud.iam.v1.saml.ListFederationOperationsResponse\";\x82\xd3\xe4\x93\x02\x35\x12\x33/iam/v1/saml/federations/{federation_id}/operationsB$\n\x1cyandex.cloud.api.iam.v1.samlZ\x04samlb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.iam.v1.saml.federation_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034yandex.cloud.api.iam.v1.samlZ\004saml'
  _globals['_GETFEDERATIONREQUEST'].fields_by_name['federation_id']._options = None
  _globals['_GETFEDERATIONREQUEST'].fields_by_name['federation_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_LISTFEDERATIONSREQUEST'].fields_by_name['cloud_id']._options = None
  _globals['_LISTFEDERATIONSREQUEST'].fields_by_name['cloud_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_LISTFEDERATIONSREQUEST'].fields_by_name['folder_id']._options = None
  _globals['_LISTFEDERATIONSREQUEST'].fields_by_name['folder_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_LISTFEDERATIONSREQUEST'].fields_by_name['page_size']._options = None
  _globals['_LISTFEDERATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _globals['_LISTFEDERATIONSREQUEST'].fields_by_name['page_token']._options = None
  _globals['_LISTFEDERATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\006<=2000'
  _globals['_LISTFEDERATIONSREQUEST'].fields_by_name['filter']._options = None
  _globals['_LISTFEDERATIONSREQUEST'].fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _globals['_CREATEFEDERATIONREQUEST'].fields_by_name['folder_id']._options = None
  _globals['_CREATEFEDERATIONREQUEST'].fields_by_name['folder_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_CREATEFEDERATIONREQUEST'].fields_by_name['name']._options = None
  _globals['_CREATEFEDERATIONREQUEST'].fields_by_name['name']._serialized_options = b'\362\3071\037[a-z]([-a-z0-9]{0,61}[a-z0-9])?'
  _globals['_CREATEFEDERATIONREQUEST'].fields_by_name['description']._options = None
  _globals['_CREATEFEDERATIONREQUEST'].fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _globals['_CREATEFEDERATIONREQUEST'].fields_by_name['cookie_max_age']._options = None
  _globals['_CREATEFEDERATIONREQUEST'].fields_by_name['cookie_max_age']._serialized_options = b'\372\3071\00710m-12h'
  _globals['_CREATEFEDERATIONREQUEST'].fields_by_name['issuer']._options = None
  _globals['_CREATEFEDERATIONREQUEST'].fields_by_name['issuer']._serialized_options = b'\350\3071\001\212\3101\006<=8000'
  _globals['_CREATEFEDERATIONREQUEST'].fields_by_name['sso_url']._options = None
  _globals['_CREATEFEDERATIONREQUEST'].fields_by_name['sso_url']._serialized_options = b'\350\3071\001\212\3101\006<=8000'
  _globals['_UPDATEFEDERATIONREQUEST'].fields_by_name['federation_id']._options = None
  _globals['_UPDATEFEDERATIONREQUEST'].fields_by_name['federation_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_UPDATEFEDERATIONREQUEST'].fields_by_name['name']._options = None
  _globals['_UPDATEFEDERATIONREQUEST'].fields_by_name['name']._serialized_options = b'\362\3071 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?'
  _globals['_UPDATEFEDERATIONREQUEST'].fields_by_name['description']._options = None
  _globals['_UPDATEFEDERATIONREQUEST'].fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _globals['_UPDATEFEDERATIONREQUEST'].fields_by_name['cookie_max_age']._options = None
  _globals['_UPDATEFEDERATIONREQUEST'].fields_by_name['cookie_max_age']._serialized_options = b'\372\3071\00710m-12h'
  _globals['_UPDATEFEDERATIONREQUEST'].fields_by_name['issuer']._options = None
  _globals['_UPDATEFEDERATIONREQUEST'].fields_by_name['issuer']._serialized_options = b'\350\3071\001\212\3101\006<=8000'
  _globals['_UPDATEFEDERATIONREQUEST'].fields_by_name['sso_url']._options = None
  _globals['_UPDATEFEDERATIONREQUEST'].fields_by_name['sso_url']._serialized_options = b'\350\3071\001\212\3101\006<=8000'
  _globals['_DELETEFEDERATIONREQUEST'].fields_by_name['federation_id']._options = None
  _globals['_DELETEFEDERATIONREQUEST'].fields_by_name['federation_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_ADDFEDERATEDUSERACCOUNTSREQUEST'].fields_by_name['federation_id']._options = None
  _globals['_ADDFEDERATEDUSERACCOUNTSREQUEST'].fields_by_name['federation_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_ADDFEDERATEDUSERACCOUNTSREQUEST'].fields_by_name['name_ids']._options = None
  _globals['_ADDFEDERATEDUSERACCOUNTSREQUEST'].fields_by_name['name_ids']._serialized_options = b'\212\3101\006<=1000'
  _globals['_LISTFEDERATEDUSERACCOUNTSREQUEST'].fields_by_name['federation_id']._options = None
  _globals['_LISTFEDERATEDUSERACCOUNTSREQUEST'].fields_by_name['federation_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTFEDERATEDUSERACCOUNTSREQUEST'].fields_by_name['page_size']._options = None
  _globals['_LISTFEDERATEDUSERACCOUNTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _globals['_LISTFEDERATEDUSERACCOUNTSREQUEST'].fields_by_name['page_token']._options = None
  _globals['_LISTFEDERATEDUSERACCOUNTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\006<=2000'
  _globals['_LISTFEDERATIONOPERATIONSREQUEST'].fields_by_name['federation_id']._options = None
  _globals['_LISTFEDERATIONOPERATIONSREQUEST'].fields_by_name['federation_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_LISTFEDERATIONOPERATIONSREQUEST'].fields_by_name['page_size']._options = None
  _globals['_LISTFEDERATIONOPERATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _globals['_LISTFEDERATIONOPERATIONSREQUEST'].fields_by_name['page_token']._options = None
  _globals['_LISTFEDERATIONOPERATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\006<=2000'
  _globals['_FEDERATIONSERVICE'].methods_by_name['Get']._options = None
  _globals['_FEDERATIONSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002*\022(/iam/v1/saml/federations/{federation_id}'
  _globals['_FEDERATIONSERVICE'].methods_by_name['List']._options = None
  _globals['_FEDERATIONSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002\032\022\030/iam/v1/saml/federations'
  _globals['_FEDERATIONSERVICE'].methods_by_name['Create']._options = None
  _globals['_FEDERATIONSERVICE'].methods_by_name['Create']._serialized_options = b'\262\322*&\n\030CreateFederationMetadata\022\nFederation\202\323\344\223\002\035\"\030/iam/v1/saml/federations:\001*'
  _globals['_FEDERATIONSERVICE'].methods_by_name['Update']._options = None
  _globals['_FEDERATIONSERVICE'].methods_by_name['Update']._serialized_options = b'\262\322*&\n\030UpdateFederationMetadata\022\nFederation\202\323\344\223\002-2(/iam/v1/saml/federations/{federation_id}:\001*'
  _globals['_FEDERATIONSERVICE'].methods_by_name['Delete']._options = None
  _globals['_FEDERATIONSERVICE'].methods_by_name['Delete']._serialized_options = b'\262\322*1\n\030DeleteFederationMetadata\022\025google.protobuf.Empty\202\323\344\223\002**(/iam/v1/saml/federations/{federation_id}'
  _globals['_FEDERATIONSERVICE'].methods_by_name['AddUserAccounts']._options = None
  _globals['_FEDERATIONSERVICE'].methods_by_name['AddUserAccounts']._serialized_options = b'\262\322*D\n AddFederatedUserAccountsMetadata\022 AddFederatedUserAccountsResponse\202\323\344\223\002=\"8/iam/v1/saml/federations/{federation_id}:addUserAccounts:\001*'
  _globals['_FEDERATIONSERVICE'].methods_by_name['ListUserAccounts']._options = None
  _globals['_FEDERATIONSERVICE'].methods_by_name['ListUserAccounts']._serialized_options = b'\202\323\344\223\002;\0229/iam/v1/saml/federations/{federation_id}:listUserAccounts'
  _globals['_FEDERATIONSERVICE'].methods_by_name['ListOperations']._options = None
  _globals['_FEDERATIONSERVICE'].methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\0025\0223/iam/v1/saml/federations/{federation_id}/operations'
  _globals['_GETFEDERATIONREQUEST']._serialized_start=363
  _globals['_GETFEDERATIONREQUEST']._serialized_end=418
  _globals['_LISTFEDERATIONSREQUEST']._serialized_start=421
  _globals['_LISTFEDERATIONSREQUEST']._serialized_end=606
  _globals['_LISTFEDERATIONSRESPONSE']._serialized_start=608
  _globals['_LISTFEDERATIONSRESPONSE']._serialized_end=717
  _globals['_CREATEFEDERATIONREQUEST']._serialized_start=720
  _globals['_CREATEFEDERATIONREQUEST']._serialized_end=1200
  _globals['_CREATEFEDERATIONMETADATA']._serialized_start=1202
  _globals['_CREATEFEDERATIONMETADATA']._serialized_end=1251
  _globals['_UPDATEFEDERATIONREQUEST']._serialized_start=1254
  _globals['_UPDATEFEDERATIONREQUEST']._serialized_end=1788
  _globals['_UPDATEFEDERATIONMETADATA']._serialized_start=1790
  _globals['_UPDATEFEDERATIONMETADATA']._serialized_end=1839
  _globals['_DELETEFEDERATIONREQUEST']._serialized_start=1841
  _globals['_DELETEFEDERATIONREQUEST']._serialized_end=1899
  _globals['_DELETEFEDERATIONMETADATA']._serialized_start=1901
  _globals['_DELETEFEDERATIONMETADATA']._serialized_end=1950
  _globals['_ADDFEDERATEDUSERACCOUNTSREQUEST']._serialized_start=1952
  _globals['_ADDFEDERATEDUSERACCOUNTSREQUEST']._serialized_end=2048
  _globals['_ADDFEDERATEDUSERACCOUNTSMETADATA']._serialized_start=2050
  _globals['_ADDFEDERATEDUSERACCOUNTSMETADATA']._serialized_end=2107
  _globals['_ADDFEDERATEDUSERACCOUNTSRESPONSE']._serialized_start=2109
  _globals['_ADDFEDERATEDUSERACCOUNTSRESPONSE']._serialized_end=2200
  _globals['_LISTFEDERATEDUSERACCOUNTSREQUEST']._serialized_start=2203
  _globals['_LISTFEDERATEDUSERACCOUNTSREQUEST']._serialized_end=2337
  _globals['_LISTFEDERATEDUSERACCOUNTSRESPONSE']._serialized_start=2339
  _globals['_LISTFEDERATEDUSERACCOUNTSRESPONSE']._serialized_end=2456
  _globals['_LISTFEDERATIONOPERATIONSREQUEST']._serialized_start=2459
  _globals['_LISTFEDERATIONOPERATIONSREQUEST']._serialized_end=2588
  _globals['_LISTFEDERATIONOPERATIONSRESPONSE']._serialized_start=2590
  _globals['_LISTFEDERATIONOPERATIONSRESPONSE']._serialized_end=2704
  _globals['_FEDERATIONSERVICE']._serialized_start=2707
  _globals['_FEDERATIONSERVICE']._serialized_end=4246
# @@protoc_insertion_point(module_scope)
