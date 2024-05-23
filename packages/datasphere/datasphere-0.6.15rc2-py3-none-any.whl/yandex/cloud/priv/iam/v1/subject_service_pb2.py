# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/priv/iam/v1/subject_service.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.priv.iam.v1 import subject_pb2 as yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_subject__pb2
from yandex.cloud.priv.operation import operation_pb2 as yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2
from yandex.cloud.priv import validation_pb2 as yandex_dot_cloud_dot_priv_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.yandex/cloud/priv/iam/v1/subject_service.proto\x12\x18yandex.cloud.priv.iam.v1\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/priv/iam/v1/subject.proto\x1a+yandex/cloud/priv/operation/operation.proto\x1a\"yandex/cloud/priv/validation.proto\"\xe9\x01\n\x19GetOrCreateSubjectRequest\x12 \n\nsubject_id\x18\x01 \x01(\tB\x0c\xa8\x89\x31\x00\xca\x89\x31\x04<=50\x12#\n\x0csubject_type\x18\x02 \x01(\tB\r\xa8\x89\x31\x01\xca\x89\x31\x05<=256\x12\"\n\x0b\x65xternal_id\x18\x03 \x01(\tB\r\xa8\x89\x31\x01\xca\x89\x31\x05\x33-256\x12 \n\nattributes\x18\x04 \x01(\tB\x0c\xca\x89\x31\x08<=262144\x12\x1e\n\x08settings\x18\x05 \x01(\tB\x0c\xca\x89\x31\x08<=262144\x12\x1f\n\rfederation_id\x18\x06 \x01(\tB\x08\xca\x89\x31\x04<=50\"\xdd\x01\n\x1aGetOrCreateSubjectResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0csubject_type\x18\x02 \x01(\t\x12\x13\n\x0b\x65xternal_id\x18\x03 \x01(\t\x12\x12\n\nattributes\x18\x04 \x01(\t\x12\x10\n\x08settings\x18\x05 \x01(\t\x12.\n\ncreated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x15\n\rfederation_id\x18\x07 \x01(\t\x12\x1b\n\x13new_subject_created\x18\x08 \x01(\x08\"]\n\x14MergeSubjectsRequest\x12\x1f\n\x11source_subject_id\x18\x01 \x01(\tB\x04\xa8\x89\x31\x01\x12$\n\x16\x64\x65stination_subject_id\x18\x02 \x01(\tB\x04\xa8\x89\x31\x01\"R\n\x15MergeSubjectsMetadata\x12\x19\n\x11source_subject_id\x18\x01 \x01(\t\x12\x1e\n\x16\x64\x65stination_subject_id\x18\x02 \x01(\t\"8\n\x14\x44\x65leteSubjectRequest\x12 \n\nsubject_id\x18\x01 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\"+\n\x15\x44\x65leteSubjectMetadata\x12\x12\n\nsubject_id\x18\x01 \x01(\t\"c\n\x17SubjectExternalIdentity\x12#\n\x0b\x65xternal_id\x18\x01 \x01(\tB\x0e\xa8\x89\x31\x01\xca\x89\x31\x06<=1024\x12#\n\rfederation_id\x18\x02 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\"\xa1\x01\n\x0fSubjectIdentity\x12\x1c\n\nsubject_id\x18\x01 \x01(\tB\x08\xca\x89\x31\x04<=50\x12L\n\x11\x65xternal_identity\x18\x02 \x01(\x0b\x32\x31.yandex.cloud.priv.iam.v1.SubjectExternalIdentity\x12\"\n\x0csubject_type\x18\x03 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\"a\n\x11SubjectDefinition\x12&\n\x10\x61ttributes_patch\x18\x03 \x01(\tB\x0c\xca\x89\x31\x08<=262144\x12$\n\x0esettings_patch\x18\x04 \x01(\tB\x0c\xca\x89\x31\x08<=262144\"\xa0\x01\n\x1aSubjectModificationRequest\x12\x41\n\x08identity\x18\x01 \x01(\x0b\x32).yandex.cloud.priv.iam.v1.SubjectIdentityB\x04\xa8\x89\x31\x01\x12?\n\ndefinition\x18\x02 \x01(\x0b\x32+.yandex.cloud.priv.iam.v1.SubjectDefinition\"\xb5\x02\n\x1e\x42ulkGetOrCreateSubjectsRequest\x12R\n\x08requests\x18\x01 \x03(\x0b\x32\x34.yandex.cloud.priv.iam.v1.SubjectModificationRequestB\n\xc2\x89\x31\x06\x31-1000\x12\x82\x01\n\x15per_federation_quotas\x18\x02 \x03(\x0b\x32Q.yandex.cloud.priv.iam.v1.BulkGetOrCreateSubjectsRequest.PerFederationQuotasEntryB\x10\xba\x89\x31\x02>0\xc2\x89\x31\x06<=1000\x1a:\n\x18PerFederationQuotasEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\"\xa0\x01\n\x1f\x42ulkGetOrCreateSubjectsResponse\x12>\n\x11\x65xisting_subjects\x18\x01 \x03(\x0b\x32#.yandex.cloud.priv.iam.v1.SubjectV2\x12=\n\x10\x63reated_subjects\x18\x02 \x03(\x0b\x32#.yandex.cloud.priv.iam.v1.SubjectV2\"6\n\x1f\x42ulkGetOrCreateSubjectsMetadata\x12\x13\n\x0bsubject_ids\x18\x01 \x03(\t\"\xa0\x01\n\x19\x42ulkUpdateSubjectsRequest\x12R\n\x08requests\x18\x01 \x03(\x0b\x32\x34.yandex.cloud.priv.iam.v1.SubjectModificationRequestB\n\xc2\x89\x31\x06\x31-1000\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"[\n\x1a\x42ulkUpdateSubjectsResponse\x12=\n\x10updated_subjects\x18\x01 \x03(\x0b\x32#.yandex.cloud.priv.iam.v1.SubjectV2\"1\n\x1a\x42ulkUpdateSubjectsMetadata\x12\x13\n\x0bsubject_ids\x18\x01 \x03(\t\"\xec\x02\n!BulkCreateOrUpdateSubjectsRequest\x12R\n\x08requests\x18\x01 \x03(\x0b\x32\x34.yandex.cloud.priv.iam.v1.SubjectModificationRequestB\n\xc2\x89\x31\x06\x31-1000\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x85\x01\n\x15per_federation_quotas\x18\x03 \x03(\x0b\x32T.yandex.cloud.priv.iam.v1.BulkCreateOrUpdateSubjectsRequest.PerFederationQuotasEntryB\x10\xba\x89\x31\x02>0\xc2\x89\x31\x06<=1000\x1a:\n\x18PerFederationQuotasEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\"\xa2\x01\n\"BulkCreateOrUpdateSubjectsResponse\x12=\n\x10\x63reated_subjects\x18\x01 \x03(\x0b\x32#.yandex.cloud.priv.iam.v1.SubjectV2\x12=\n\x10updated_subjects\x18\x02 \x03(\x0b\x32#.yandex.cloud.priv.iam.v1.SubjectV2\"9\n\"BulkCreateOrUpdateSubjectsMetadata\x12\x13\n\x0bsubject_ids\x18\x01 \x03(\t\"f\n\x19\x42ulkDeleteSubjectsRequest\x12I\n\nidentities\x18\x01 \x03(\x0b\x32).yandex.cloud.priv.iam.v1.SubjectIdentityB\n\xc2\x89\x31\x06\x31-1000\"[\n\x1a\x42ulkDeleteSubjectsResponse\x12=\n\x10\x64\x65leted_subjects\x18\x01 \x03(\x0b\x32#.yandex.cloud.priv.iam.v1.SubjectV2\"1\n\x1a\x42ulkDeleteSubjectsMetadata\x12\x13\n\x0bsubject_ids\x18\x01 \x03(\t\"\xb5\x01\n\x18\x42ulkMergeSubjectsRequest\x12I\n\nidentities\x18\x01 \x03(\x0b\x32).yandex.cloud.priv.iam.v1.SubjectIdentityB\n\xc2\x89\x31\x06\x31-1000\x12N\n\nmerge_into\x18\x02 \x01(\x0b\x32\x34.yandex.cloud.priv.iam.v1.SubjectModificationRequestB\x04\xa8\x89\x31\x01\"X\n\x19\x42ulkMergeSubjectsResponse\x12;\n\x0emerged_subject\x18\x01 \x01(\x0b\x32#.yandex.cloud.priv.iam.v1.SubjectV2\"0\n\x19\x42ulkMergeSubjectsMetadata\x12\x13\n\x0bsubject_ids\x18\x01 \x03(\t2\xb9\n\n\x0eSubjectService\x12x\n\x0bGetOrCreate\x12\x33.yandex.cloud.priv.iam.v1.GetOrCreateSubjectRequest\x1a\x34.yandex.cloud.priv.iam.v1.GetOrCreateSubjectResponse\x12\x93\x01\n\x05Merge\x12..yandex.cloud.priv.iam.v1.MergeSubjectsRequest\x1a&.yandex.cloud.priv.operation.Operation\"2\xb2\xd2*.\n\x15MergeSubjectsMetadata\x12\x15google.protobuf.Empty\x12\x94\x01\n\x06\x44\x65lete\x12..yandex.cloud.priv.iam.v1.DeleteSubjectRequest\x1a&.yandex.cloud.priv.operation.Operation\"2\xb2\xd2*.\n\x15\x44\x65leteSubjectMetadata\x12\x15google.protobuf.Empty\x12\xbb\x01\n\x0f\x42ulkGetOrCreate\x12\x38.yandex.cloud.priv.iam.v1.BulkGetOrCreateSubjectsRequest\x1a&.yandex.cloud.priv.operation.Operation\"F\xb2\xd2*B\n\x1f\x42ulkGetOrCreateSubjectsMetadata\x12\x1f\x42ulkGetOrCreateSubjectsResponse\x12\xa7\x01\n\nBulkUpdate\x12\x33.yandex.cloud.priv.iam.v1.BulkUpdateSubjectsRequest\x1a&.yandex.cloud.priv.operation.Operation\"<\xb2\xd2*8\n\x1a\x42ulkUpdateSubjectsMetadata\x12\x1a\x42ulkUpdateSubjectsResponse\x12\xc7\x01\n\x12\x42ulkCreateOrUpdate\x12;.yandex.cloud.priv.iam.v1.BulkCreateOrUpdateSubjectsRequest\x1a&.yandex.cloud.priv.operation.Operation\"L\xb2\xd2*H\n\"BulkCreateOrUpdateSubjectsMetadata\x12\"BulkCreateOrUpdateSubjectsResponse\x12\xa7\x01\n\nBulkDelete\x12\x33.yandex.cloud.priv.iam.v1.BulkDeleteSubjectsRequest\x1a&.yandex.cloud.priv.operation.Operation\"<\xb2\xd2*8\n\x1a\x42ulkDeleteSubjectsMetadata\x12\x1a\x42ulkDeleteSubjectsResponse\x12\xa3\x01\n\tBulkMerge\x12\x32.yandex.cloud.priv.iam.v1.BulkMergeSubjectsRequest\x1a&.yandex.cloud.priv.operation.Operation\":\xb2\xd2*6\n\x19\x42ulkMergeSubjectsMetadata\x12\x19\x42ulkMergeSubjectsResponseB\nB\x03PSSZ\x03iamb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.priv.iam.v1.subject_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'B\003PSSZ\003iam'
  _globals['_GETORCREATESUBJECTREQUEST'].fields_by_name['subject_id']._options = None
  _globals['_GETORCREATESUBJECTREQUEST'].fields_by_name['subject_id']._serialized_options = b'\250\2111\000\312\2111\004<=50'
  _globals['_GETORCREATESUBJECTREQUEST'].fields_by_name['subject_type']._options = None
  _globals['_GETORCREATESUBJECTREQUEST'].fields_by_name['subject_type']._serialized_options = b'\250\2111\001\312\2111\005<=256'
  _globals['_GETORCREATESUBJECTREQUEST'].fields_by_name['external_id']._options = None
  _globals['_GETORCREATESUBJECTREQUEST'].fields_by_name['external_id']._serialized_options = b'\250\2111\001\312\2111\0053-256'
  _globals['_GETORCREATESUBJECTREQUEST'].fields_by_name['attributes']._options = None
  _globals['_GETORCREATESUBJECTREQUEST'].fields_by_name['attributes']._serialized_options = b'\312\2111\010<=262144'
  _globals['_GETORCREATESUBJECTREQUEST'].fields_by_name['settings']._options = None
  _globals['_GETORCREATESUBJECTREQUEST'].fields_by_name['settings']._serialized_options = b'\312\2111\010<=262144'
  _globals['_GETORCREATESUBJECTREQUEST'].fields_by_name['federation_id']._options = None
  _globals['_GETORCREATESUBJECTREQUEST'].fields_by_name['federation_id']._serialized_options = b'\312\2111\004<=50'
  _globals['_MERGESUBJECTSREQUEST'].fields_by_name['source_subject_id']._options = None
  _globals['_MERGESUBJECTSREQUEST'].fields_by_name['source_subject_id']._serialized_options = b'\250\2111\001'
  _globals['_MERGESUBJECTSREQUEST'].fields_by_name['destination_subject_id']._options = None
  _globals['_MERGESUBJECTSREQUEST'].fields_by_name['destination_subject_id']._serialized_options = b'\250\2111\001'
  _globals['_DELETESUBJECTREQUEST'].fields_by_name['subject_id']._options = None
  _globals['_DELETESUBJECTREQUEST'].fields_by_name['subject_id']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_SUBJECTEXTERNALIDENTITY'].fields_by_name['external_id']._options = None
  _globals['_SUBJECTEXTERNALIDENTITY'].fields_by_name['external_id']._serialized_options = b'\250\2111\001\312\2111\006<=1024'
  _globals['_SUBJECTEXTERNALIDENTITY'].fields_by_name['federation_id']._options = None
  _globals['_SUBJECTEXTERNALIDENTITY'].fields_by_name['federation_id']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_SUBJECTIDENTITY'].fields_by_name['subject_id']._options = None
  _globals['_SUBJECTIDENTITY'].fields_by_name['subject_id']._serialized_options = b'\312\2111\004<=50'
  _globals['_SUBJECTIDENTITY'].fields_by_name['subject_type']._options = None
  _globals['_SUBJECTIDENTITY'].fields_by_name['subject_type']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _globals['_SUBJECTDEFINITION'].fields_by_name['attributes_patch']._options = None
  _globals['_SUBJECTDEFINITION'].fields_by_name['attributes_patch']._serialized_options = b'\312\2111\010<=262144'
  _globals['_SUBJECTDEFINITION'].fields_by_name['settings_patch']._options = None
  _globals['_SUBJECTDEFINITION'].fields_by_name['settings_patch']._serialized_options = b'\312\2111\010<=262144'
  _globals['_SUBJECTMODIFICATIONREQUEST'].fields_by_name['identity']._options = None
  _globals['_SUBJECTMODIFICATIONREQUEST'].fields_by_name['identity']._serialized_options = b'\250\2111\001'
  _globals['_BULKGETORCREATESUBJECTSREQUEST_PERFEDERATIONQUOTASENTRY']._options = None
  _globals['_BULKGETORCREATESUBJECTSREQUEST_PERFEDERATIONQUOTASENTRY']._serialized_options = b'8\001'
  _globals['_BULKGETORCREATESUBJECTSREQUEST'].fields_by_name['requests']._options = None
  _globals['_BULKGETORCREATESUBJECTSREQUEST'].fields_by_name['requests']._serialized_options = b'\302\2111\0061-1000'
  _globals['_BULKGETORCREATESUBJECTSREQUEST'].fields_by_name['per_federation_quotas']._options = None
  _globals['_BULKGETORCREATESUBJECTSREQUEST'].fields_by_name['per_federation_quotas']._serialized_options = b'\272\2111\002>0\302\2111\006<=1000'
  _globals['_BULKUPDATESUBJECTSREQUEST'].fields_by_name['requests']._options = None
  _globals['_BULKUPDATESUBJECTSREQUEST'].fields_by_name['requests']._serialized_options = b'\302\2111\0061-1000'
  _globals['_BULKCREATEORUPDATESUBJECTSREQUEST_PERFEDERATIONQUOTASENTRY']._options = None
  _globals['_BULKCREATEORUPDATESUBJECTSREQUEST_PERFEDERATIONQUOTASENTRY']._serialized_options = b'8\001'
  _globals['_BULKCREATEORUPDATESUBJECTSREQUEST'].fields_by_name['requests']._options = None
  _globals['_BULKCREATEORUPDATESUBJECTSREQUEST'].fields_by_name['requests']._serialized_options = b'\302\2111\0061-1000'
  _globals['_BULKCREATEORUPDATESUBJECTSREQUEST'].fields_by_name['per_federation_quotas']._options = None
  _globals['_BULKCREATEORUPDATESUBJECTSREQUEST'].fields_by_name['per_federation_quotas']._serialized_options = b'\272\2111\002>0\302\2111\006<=1000'
  _globals['_BULKDELETESUBJECTSREQUEST'].fields_by_name['identities']._options = None
  _globals['_BULKDELETESUBJECTSREQUEST'].fields_by_name['identities']._serialized_options = b'\302\2111\0061-1000'
  _globals['_BULKMERGESUBJECTSREQUEST'].fields_by_name['identities']._options = None
  _globals['_BULKMERGESUBJECTSREQUEST'].fields_by_name['identities']._serialized_options = b'\302\2111\0061-1000'
  _globals['_BULKMERGESUBJECTSREQUEST'].fields_by_name['merge_into']._options = None
  _globals['_BULKMERGESUBJECTSREQUEST'].fields_by_name['merge_into']._serialized_options = b'\250\2111\001'
  _globals['_SUBJECTSERVICE'].methods_by_name['Merge']._options = None
  _globals['_SUBJECTSERVICE'].methods_by_name['Merge']._serialized_options = b'\262\322*.\n\025MergeSubjectsMetadata\022\025google.protobuf.Empty'
  _globals['_SUBJECTSERVICE'].methods_by_name['Delete']._options = None
  _globals['_SUBJECTSERVICE'].methods_by_name['Delete']._serialized_options = b'\262\322*.\n\025DeleteSubjectMetadata\022\025google.protobuf.Empty'
  _globals['_SUBJECTSERVICE'].methods_by_name['BulkGetOrCreate']._options = None
  _globals['_SUBJECTSERVICE'].methods_by_name['BulkGetOrCreate']._serialized_options = b'\262\322*B\n\037BulkGetOrCreateSubjectsMetadata\022\037BulkGetOrCreateSubjectsResponse'
  _globals['_SUBJECTSERVICE'].methods_by_name['BulkUpdate']._options = None
  _globals['_SUBJECTSERVICE'].methods_by_name['BulkUpdate']._serialized_options = b'\262\322*8\n\032BulkUpdateSubjectsMetadata\022\032BulkUpdateSubjectsResponse'
  _globals['_SUBJECTSERVICE'].methods_by_name['BulkCreateOrUpdate']._options = None
  _globals['_SUBJECTSERVICE'].methods_by_name['BulkCreateOrUpdate']._serialized_options = b'\262\322*H\n\"BulkCreateOrUpdateSubjectsMetadata\022\"BulkCreateOrUpdateSubjectsResponse'
  _globals['_SUBJECTSERVICE'].methods_by_name['BulkDelete']._options = None
  _globals['_SUBJECTSERVICE'].methods_by_name['BulkDelete']._serialized_options = b'\262\322*8\n\032BulkDeleteSubjectsMetadata\022\032BulkDeleteSubjectsResponse'
  _globals['_SUBJECTSERVICE'].methods_by_name['BulkMerge']._options = None
  _globals['_SUBJECTSERVICE'].methods_by_name['BulkMerge']._serialized_options = b'\262\322*6\n\031BulkMergeSubjectsMetadata\022\031BulkMergeSubjectsResponse'
  _globals['_GETORCREATESUBJECTREQUEST']._serialized_start=299
  _globals['_GETORCREATESUBJECTREQUEST']._serialized_end=532
  _globals['_GETORCREATESUBJECTRESPONSE']._serialized_start=535
  _globals['_GETORCREATESUBJECTRESPONSE']._serialized_end=756
  _globals['_MERGESUBJECTSREQUEST']._serialized_start=758
  _globals['_MERGESUBJECTSREQUEST']._serialized_end=851
  _globals['_MERGESUBJECTSMETADATA']._serialized_start=853
  _globals['_MERGESUBJECTSMETADATA']._serialized_end=935
  _globals['_DELETESUBJECTREQUEST']._serialized_start=937
  _globals['_DELETESUBJECTREQUEST']._serialized_end=993
  _globals['_DELETESUBJECTMETADATA']._serialized_start=995
  _globals['_DELETESUBJECTMETADATA']._serialized_end=1038
  _globals['_SUBJECTEXTERNALIDENTITY']._serialized_start=1040
  _globals['_SUBJECTEXTERNALIDENTITY']._serialized_end=1139
  _globals['_SUBJECTIDENTITY']._serialized_start=1142
  _globals['_SUBJECTIDENTITY']._serialized_end=1303
  _globals['_SUBJECTDEFINITION']._serialized_start=1305
  _globals['_SUBJECTDEFINITION']._serialized_end=1402
  _globals['_SUBJECTMODIFICATIONREQUEST']._serialized_start=1405
  _globals['_SUBJECTMODIFICATIONREQUEST']._serialized_end=1565
  _globals['_BULKGETORCREATESUBJECTSREQUEST']._serialized_start=1568
  _globals['_BULKGETORCREATESUBJECTSREQUEST']._serialized_end=1877
  _globals['_BULKGETORCREATESUBJECTSREQUEST_PERFEDERATIONQUOTASENTRY']._serialized_start=1819
  _globals['_BULKGETORCREATESUBJECTSREQUEST_PERFEDERATIONQUOTASENTRY']._serialized_end=1877
  _globals['_BULKGETORCREATESUBJECTSRESPONSE']._serialized_start=1880
  _globals['_BULKGETORCREATESUBJECTSRESPONSE']._serialized_end=2040
  _globals['_BULKGETORCREATESUBJECTSMETADATA']._serialized_start=2042
  _globals['_BULKGETORCREATESUBJECTSMETADATA']._serialized_end=2096
  _globals['_BULKUPDATESUBJECTSREQUEST']._serialized_start=2099
  _globals['_BULKUPDATESUBJECTSREQUEST']._serialized_end=2259
  _globals['_BULKUPDATESUBJECTSRESPONSE']._serialized_start=2261
  _globals['_BULKUPDATESUBJECTSRESPONSE']._serialized_end=2352
  _globals['_BULKUPDATESUBJECTSMETADATA']._serialized_start=2354
  _globals['_BULKUPDATESUBJECTSMETADATA']._serialized_end=2403
  _globals['_BULKCREATEORUPDATESUBJECTSREQUEST']._serialized_start=2406
  _globals['_BULKCREATEORUPDATESUBJECTSREQUEST']._serialized_end=2770
  _globals['_BULKCREATEORUPDATESUBJECTSREQUEST_PERFEDERATIONQUOTASENTRY']._serialized_start=1819
  _globals['_BULKCREATEORUPDATESUBJECTSREQUEST_PERFEDERATIONQUOTASENTRY']._serialized_end=1877
  _globals['_BULKCREATEORUPDATESUBJECTSRESPONSE']._serialized_start=2773
  _globals['_BULKCREATEORUPDATESUBJECTSRESPONSE']._serialized_end=2935
  _globals['_BULKCREATEORUPDATESUBJECTSMETADATA']._serialized_start=2937
  _globals['_BULKCREATEORUPDATESUBJECTSMETADATA']._serialized_end=2994
  _globals['_BULKDELETESUBJECTSREQUEST']._serialized_start=2996
  _globals['_BULKDELETESUBJECTSREQUEST']._serialized_end=3098
  _globals['_BULKDELETESUBJECTSRESPONSE']._serialized_start=3100
  _globals['_BULKDELETESUBJECTSRESPONSE']._serialized_end=3191
  _globals['_BULKDELETESUBJECTSMETADATA']._serialized_start=3193
  _globals['_BULKDELETESUBJECTSMETADATA']._serialized_end=3242
  _globals['_BULKMERGESUBJECTSREQUEST']._serialized_start=3245
  _globals['_BULKMERGESUBJECTSREQUEST']._serialized_end=3426
  _globals['_BULKMERGESUBJECTSRESPONSE']._serialized_start=3428
  _globals['_BULKMERGESUBJECTSRESPONSE']._serialized_end=3516
  _globals['_BULKMERGESUBJECTSMETADATA']._serialized_start=3518
  _globals['_BULKMERGESUBJECTSMETADATA']._serialized_end=3566
  _globals['_SUBJECTSERVICE']._serialized_start=3569
  _globals['_SUBJECTSERVICE']._serialized_end=4906
# @@protoc_insertion_point(module_scope)
