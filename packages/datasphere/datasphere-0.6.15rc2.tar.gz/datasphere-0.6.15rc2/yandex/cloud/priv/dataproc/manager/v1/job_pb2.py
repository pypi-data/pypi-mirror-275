# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/priv/dataproc/manager/v1/job.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/yandex/cloud/priv/dataproc/manager/v1/job.proto\x12%yandex.cloud.priv.dataproc.manager.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\x9e\x06\n\x03Job\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ncluster_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nstarted_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x66inished_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x12\n\ncreated_by\x18\x0c \x01(\t\x12\x41\n\x06status\x18\x07 \x01(\x0e\x32\x31.yandex.cloud.priv.dataproc.manager.v1.Job.Status\x12L\n\rmapreduce_job\x18\x08 \x01(\x0b\x32\x33.yandex.cloud.priv.dataproc.manager.v1.MapreduceJobH\x00\x12\x44\n\tspark_job\x18\t \x01(\x0b\x32/.yandex.cloud.priv.dataproc.manager.v1.SparkJobH\x00\x12H\n\x0bpyspark_job\x18\n \x01(\x0b\x32\x31.yandex.cloud.priv.dataproc.manager.v1.PysparkJobH\x00\x12\x42\n\x08hive_job\x18\x0b \x01(\x0b\x32..yandex.cloud.priv.dataproc.manager.v1.HiveJobH\x00\x12P\n\x10\x61pplication_info\x18\r \x01(\x0b\x32\x36.yandex.cloud.priv.dataproc.manager.v1.ApplicationInfo\"\x80\x01\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x10\n\x0cPROVISIONING\x10\x01\x12\x0b\n\x07PENDING\x10\x02\x12\x0b\n\x07RUNNING\x10\x03\x12\t\n\x05\x45RROR\x10\x04\x12\x08\n\x04\x44ONE\x10\x05\x12\r\n\tCANCELLED\x10\x06\x12\x0e\n\nCANCELLING\x10\x07\x42\n\n\x08job_spec\"9\n\x12\x41pplicationAttempt\x12\n\n\x02id\x18\x01 \x01(\t\x12\x17\n\x0f\x61m_container_id\x18\x02 \x01(\t\"v\n\x0f\x41pplicationInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12W\n\x14\x61pplication_attempts\x18\x02 \x03(\x0b\x32\x39.yandex.cloud.priv.dataproc.manager.v1.ApplicationAttempt\"\xa5\x02\n\x0cMapreduceJob\x12\x0c\n\x04\x61rgs\x18\x01 \x03(\t\x12\x15\n\rjar_file_uris\x18\x02 \x03(\t\x12\x11\n\tfile_uris\x18\x03 \x03(\t\x12\x14\n\x0c\x61rchive_uris\x18\x04 \x03(\t\x12W\n\nproperties\x18\x05 \x03(\x0b\x32\x43.yandex.cloud.priv.dataproc.manager.v1.MapreduceJob.PropertiesEntry\x12\x1b\n\x11main_jar_file_uri\x18\x06 \x01(\tH\x00\x12\x14\n\nmain_class\x18\x07 \x01(\tH\x00\x1a\x31\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x08\n\x06\x64river\"\xd1\x02\n\x08SparkJob\x12\x0c\n\x04\x61rgs\x18\x01 \x03(\t\x12\x15\n\rjar_file_uris\x18\x02 \x03(\t\x12\x11\n\tfile_uris\x18\x03 \x03(\t\x12\x14\n\x0c\x61rchive_uris\x18\x04 \x03(\t\x12S\n\nproperties\x18\x05 \x03(\x0b\x32?.yandex.cloud.priv.dataproc.manager.v1.SparkJob.PropertiesEntry\x12\x19\n\x11main_jar_file_uri\x18\x06 \x01(\t\x12\x12\n\nmain_class\x18\x07 \x01(\t\x12\x10\n\x08packages\x18\x08 \x03(\t\x12\x14\n\x0crepositories\x18\t \x03(\t\x12\x18\n\x10\x65xclude_packages\x18\n \x03(\t\x1a\x31\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xde\x02\n\nPysparkJob\x12\x0c\n\x04\x61rgs\x18\x01 \x03(\t\x12\x15\n\rjar_file_uris\x18\x02 \x03(\t\x12\x11\n\tfile_uris\x18\x03 \x03(\t\x12\x14\n\x0c\x61rchive_uris\x18\x04 \x03(\t\x12U\n\nproperties\x18\x05 \x03(\x0b\x32\x41.yandex.cloud.priv.dataproc.manager.v1.PysparkJob.PropertiesEntry\x12\x1c\n\x14main_python_file_uri\x18\x06 \x01(\t\x12\x18\n\x10python_file_uris\x18\x07 \x03(\t\x12\x10\n\x08packages\x18\x08 \x03(\t\x12\x14\n\x0crepositories\x18\t \x03(\t\x12\x18\n\x10\x65xclude_packages\x18\n \x03(\t\x1a\x31\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x1c\n\tQueryList\x12\x0f\n\x07queries\x18\x01 \x03(\t\"\xcb\x03\n\x07HiveJob\x12R\n\nproperties\x18\x01 \x03(\x0b\x32>.yandex.cloud.priv.dataproc.manager.v1.HiveJob.PropertiesEntry\x12\x1b\n\x13\x63ontinue_on_failure\x18\x02 \x01(\x08\x12]\n\x10script_variables\x18\x03 \x03(\x0b\x32\x43.yandex.cloud.priv.dataproc.manager.v1.HiveJob.ScriptVariablesEntry\x12\x15\n\rjar_file_uris\x18\x04 \x03(\t\x12\x18\n\x0equery_file_uri\x18\x05 \x01(\tH\x00\x12\x46\n\nquery_list\x18\x06 \x01(\x0b\x32\x30.yandex.cloud.priv.dataproc.manager.v1.QueryListH\x00\x1a\x31\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x36\n\x14ScriptVariablesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x0c\n\nquery_type\"\xbc\x03\n\nSupportJob\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ncluster_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nstarted_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x66inished_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12H\n\x06status\x18\x06 \x01(\x0e\x32\x38.yandex.cloud.priv.dataproc.manager.v1.SupportJob.Status\x12\x0b\n\x03\x63md\x18\x07 \x01(\t\x12\x0f\n\x07timeout\x18\x08 \x01(\x03\x12\x12\n\ncreated_by\x18\t \x01(\t\"\x80\x01\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x10\n\x0cPROVISIONING\x10\x01\x12\x0b\n\x07PENDING\x10\x02\x12\x0b\n\x07RUNNING\x10\x03\x12\t\n\x05\x45RROR\x10\x04\x12\x08\n\x04\x44ONE\x10\x05\x12\r\n\tCANCELLED\x10\x06\x12\x0e\n\nCANCELLING\x10\x07\x42\x17\x42\x03PHJZ\x10\x64\x61taproc_managerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.priv.dataproc.manager.v1.job_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'B\003PHJZ\020dataproc_manager'
  _globals['_MAPREDUCEJOB_PROPERTIESENTRY']._options = None
  _globals['_MAPREDUCEJOB_PROPERTIESENTRY']._serialized_options = b'8\001'
  _globals['_SPARKJOB_PROPERTIESENTRY']._options = None
  _globals['_SPARKJOB_PROPERTIESENTRY']._serialized_options = b'8\001'
  _globals['_PYSPARKJOB_PROPERTIESENTRY']._options = None
  _globals['_PYSPARKJOB_PROPERTIESENTRY']._serialized_options = b'8\001'
  _globals['_HIVEJOB_PROPERTIESENTRY']._options = None
  _globals['_HIVEJOB_PROPERTIESENTRY']._serialized_options = b'8\001'
  _globals['_HIVEJOB_SCRIPTVARIABLESENTRY']._options = None
  _globals['_HIVEJOB_SCRIPTVARIABLESENTRY']._serialized_options = b'8\001'
  _globals['_JOB']._serialized_start=124
  _globals['_JOB']._serialized_end=922
  _globals['_JOB_STATUS']._serialized_start=782
  _globals['_JOB_STATUS']._serialized_end=910
  _globals['_APPLICATIONATTEMPT']._serialized_start=924
  _globals['_APPLICATIONATTEMPT']._serialized_end=981
  _globals['_APPLICATIONINFO']._serialized_start=983
  _globals['_APPLICATIONINFO']._serialized_end=1101
  _globals['_MAPREDUCEJOB']._serialized_start=1104
  _globals['_MAPREDUCEJOB']._serialized_end=1397
  _globals['_MAPREDUCEJOB_PROPERTIESENTRY']._serialized_start=1338
  _globals['_MAPREDUCEJOB_PROPERTIESENTRY']._serialized_end=1387
  _globals['_SPARKJOB']._serialized_start=1400
  _globals['_SPARKJOB']._serialized_end=1737
  _globals['_SPARKJOB_PROPERTIESENTRY']._serialized_start=1338
  _globals['_SPARKJOB_PROPERTIESENTRY']._serialized_end=1387
  _globals['_PYSPARKJOB']._serialized_start=1740
  _globals['_PYSPARKJOB']._serialized_end=2090
  _globals['_PYSPARKJOB_PROPERTIESENTRY']._serialized_start=1338
  _globals['_PYSPARKJOB_PROPERTIESENTRY']._serialized_end=1387
  _globals['_QUERYLIST']._serialized_start=2092
  _globals['_QUERYLIST']._serialized_end=2120
  _globals['_HIVEJOB']._serialized_start=2123
  _globals['_HIVEJOB']._serialized_end=2582
  _globals['_HIVEJOB_PROPERTIESENTRY']._serialized_start=1338
  _globals['_HIVEJOB_PROPERTIESENTRY']._serialized_end=1387
  _globals['_HIVEJOB_SCRIPTVARIABLESENTRY']._serialized_start=2514
  _globals['_HIVEJOB_SCRIPTVARIABLESENTRY']._serialized_end=2568
  _globals['_SUPPORTJOB']._serialized_start=2585
  _globals['_SUPPORTJOB']._serialized_end=3029
  _globals['_SUPPORTJOB_STATUS']._serialized_start=782
  _globals['_SUPPORTJOB_STATUS']._serialized_end=910
# @@protoc_insertion_point(module_scope)
