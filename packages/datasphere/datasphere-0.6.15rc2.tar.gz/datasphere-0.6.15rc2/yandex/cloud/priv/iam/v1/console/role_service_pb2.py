# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/priv/iam/v1/console/role_service.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.priv import validation_pb2 as yandex_dot_cloud_dot_priv_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3yandex/cloud/priv/iam/v1/console/role_service.proto\x12 yandex.cloud.priv.iam.v1.console\x1a\"yandex/cloud/priv/validation.proto\"Q\n\x10ListRolesRequest\x12\x1d\n\tpage_size\x18\x01 \x01(\x03\x42\n\xba\x89\x31\x06\x30-1000\x12\x1e\n\npage_token\x18\x02 \x01(\tB\n\xca\x89\x31\x06<=2000\"c\n\x11ListRolesResponse\x12\x35\n\x05roles\x18\x01 \x03(\x0b\x32&.yandex.cloud.priv.iam.v1.console.Role\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"=\n\x04Role\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x14\n\x0c\x63\x61tegory_ids\x18\x03 \x03(\t\"V\n\x15ListCategoriesRequest\x12\x1d\n\tpage_size\x18\x01 \x01(\x03\x42\n\xba\x89\x31\x06\x30-1000\x12\x1e\n\npage_token\x18\x02 \x01(\tB\n\xca\x89\x31\x06<=2000\"q\n\x16ListCategoriesResponse\x12>\n\ncategories\x18\x01 \x03(\x0b\x32*.yandex.cloud.priv.iam.v1.console.Category\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"$\n\x08\x43\x61tegory\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t2\x84\x02\n\x0bRoleService\x12o\n\x04List\x12\x32.yandex.cloud.priv.iam.v1.console.ListRolesRequest\x1a\x33.yandex.cloud.priv.iam.v1.console.ListRolesResponse\x12\x83\x01\n\x0eListCategories\x12\x37.yandex.cloud.priv.iam.v1.console.ListCategoriesRequest\x1a\x38.yandex.cloud.priv.iam.v1.console.ListCategoriesResponseB\x13\x42\x04PCRSZ\x0biam_consoleb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.priv.iam.v1.console.role_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'B\004PCRSZ\013iam_console'
  _globals['_LISTROLESREQUEST'].fields_by_name['page_size']._options = None
  _globals['_LISTROLESREQUEST'].fields_by_name['page_size']._serialized_options = b'\272\2111\0060-1000'
  _globals['_LISTROLESREQUEST'].fields_by_name['page_token']._options = None
  _globals['_LISTROLESREQUEST'].fields_by_name['page_token']._serialized_options = b'\312\2111\006<=2000'
  _globals['_LISTCATEGORIESREQUEST'].fields_by_name['page_size']._options = None
  _globals['_LISTCATEGORIESREQUEST'].fields_by_name['page_size']._serialized_options = b'\272\2111\0060-1000'
  _globals['_LISTCATEGORIESREQUEST'].fields_by_name['page_token']._options = None
  _globals['_LISTCATEGORIESREQUEST'].fields_by_name['page_token']._serialized_options = b'\312\2111\006<=2000'
  _globals['_LISTROLESREQUEST']._serialized_start=125
  _globals['_LISTROLESREQUEST']._serialized_end=206
  _globals['_LISTROLESRESPONSE']._serialized_start=208
  _globals['_LISTROLESRESPONSE']._serialized_end=307
  _globals['_ROLE']._serialized_start=309
  _globals['_ROLE']._serialized_end=370
  _globals['_LISTCATEGORIESREQUEST']._serialized_start=372
  _globals['_LISTCATEGORIESREQUEST']._serialized_end=458
  _globals['_LISTCATEGORIESRESPONSE']._serialized_start=460
  _globals['_LISTCATEGORIESRESPONSE']._serialized_end=573
  _globals['_CATEGORY']._serialized_start=575
  _globals['_CATEGORY']._serialized_end=611
  _globals['_ROLESERVICE']._serialized_start=614
  _globals['_ROLESERVICE']._serialized_end=874
# @@protoc_insertion_point(module_scope)
