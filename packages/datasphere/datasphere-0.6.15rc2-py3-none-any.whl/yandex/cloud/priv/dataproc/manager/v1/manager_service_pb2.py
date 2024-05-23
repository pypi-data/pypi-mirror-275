# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/priv/dataproc/manager/v1/manager_service.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;yandex/cloud/priv/dataproc/manager/v1/manager_service.proto\x12%yandex.cloud.priv.dataproc.manager.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"_\n\rHbaseNodeInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08requests\x18\x02 \x01(\x03\x12\x14\n\x0cheap_size_mb\x18\x03 \x01(\x03\x12\x18\n\x10max_heap_size_mb\x18\x04 \x01(\x03\"\xeb\x01\n\tHbaseInfo\x12\x11\n\tavailable\x18\x01 \x01(\x08\x12\x0f\n\x07regions\x18\x02 \x01(\x03\x12\x10\n\x08requests\x18\x03 \x01(\x03\x12\x14\n\x0c\x61verage_load\x18\x04 \x01(\x01\x12H\n\nlive_nodes\x18\x05 \x03(\x0b\x32\x34.yandex.cloud.priv.dataproc.manager.v1.HbaseNodeInfo\x12H\n\ndead_nodes\x18\x06 \x03(\x0b\x32\x34.yandex.cloud.priv.dataproc.manager.v1.HbaseNodeInfo\"r\n\x0cHDFSNodeInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04used\x18\x02 \x01(\x03\x12\x11\n\tremaining\x18\x03 \x01(\x03\x12\x10\n\x08\x63\x61pacity\x18\x04 \x01(\x03\x12\x12\n\nnum_blocks\x18\x05 \x01(\x03\x12\r\n\x05state\x18\x06 \x01(\t\"\x9d\x04\n\x08HDFSInfo\x12\x11\n\tavailable\x18\x01 \x01(\x08\x12\x19\n\x11percent_remaining\x18\x02 \x01(\x01\x12\x0c\n\x04used\x18\x03 \x01(\x03\x12\x0c\n\x04\x66ree\x18\x04 \x01(\x03\x12\x14\n\x0ctotal_blocks\x18\x05 \x01(\x03\x12\x16\n\x0emissing_blocks\x18\x06 \x01(\x03\x12\"\n\x1amissing_blocks_replica_one\x18\x07 \x01(\x03\x12G\n\nlive_nodes\x18\x08 \x03(\x0b\x32\x33.yandex.cloud.priv.dataproc.manager.v1.HDFSNodeInfo\x12G\n\ndead_nodes\x18\t \x03(\x0b\x32\x33.yandex.cloud.priv.dataproc.manager.v1.HDFSNodeInfo\x12\x10\n\x08safemode\x18\x0b \x01(\t\x12R\n\x15\x64\x65\x63ommissioning_nodes\x18\x0c \x03(\x0b\x32\x33.yandex.cloud.priv.dataproc.manager.v1.HDFSNodeInfo\x12Q\n\x14\x64\x65\x63ommissioned_nodes\x18\r \x03(\x0b\x32\x33.yandex.cloud.priv.dataproc.manager.v1.HDFSNodeInfo\x12$\n\x1crequested_decommission_hosts\x18\x0e \x03(\tJ\x04\x08\n\x10\x0b\"\x9b\x01\n\x08HiveInfo\x12\x11\n\tavailable\x18\x01 \x01(\x08\x12\x19\n\x11queries_succeeded\x18\x02 \x01(\x03\x12\x16\n\x0equeries_failed\x18\x03 \x01(\x03\x12\x19\n\x11queries_executing\x18\x04 \x01(\x03\x12\x15\n\rsessions_open\x18\x05 \x01(\x03\x12\x17\n\x0fsessions_active\x18\x06 \x01(\x03\"\x8d\x01\n\x0cYarnNodeInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05state\x18\x02 \x01(\t\x12\x16\n\x0enum_containers\x18\x03 \x01(\x03\x12\x16\n\x0eused_memory_mb\x18\x04 \x01(\x03\x12\x1b\n\x13\x61vailable_memory_mb\x18\x05 \x01(\x03\x12\x13\n\x0bupdate_time\x18\x06 \x01(\x03\"\x8c\x01\n\x08YarnInfo\x12\x11\n\tavailable\x18\x01 \x01(\x08\x12G\n\nlive_nodes\x18\x02 \x03(\x0b\x32\x33.yandex.cloud.priv.dataproc.manager.v1.YarnNodeInfo\x12$\n\x1crequested_decommission_hosts\x18\x03 \x03(\t\"\x1e\n\rZookeeperInfo\x12\r\n\x05\x61live\x18\x01 \x01(\x08\"\x1a\n\tOozieInfo\x12\r\n\x05\x61live\x18\x01 \x01(\x08\"\x19\n\x08LivyInfo\x12\r\n\x05\x61live\x18\x01 \x01(\x08\"^\n\x08InitActs\x12\x43\n\x05state\x18\x01 \x01(\x0e\x32\x34.yandex.cloud.priv.dataproc.manager.v1.InitActsState\x12\r\n\x05\x66qdns\x18\x02 \x03(\t\"\xa7\x04\n\x04Info\x12=\n\x04hdfs\x18\x01 \x01(\x0b\x32/.yandex.cloud.priv.dataproc.manager.v1.HDFSInfo\x12=\n\x04yarn\x18\x02 \x01(\x0b\x32/.yandex.cloud.priv.dataproc.manager.v1.YarnInfo\x12=\n\x04hive\x18\x03 \x01(\x0b\x32/.yandex.cloud.priv.dataproc.manager.v1.HiveInfo\x12G\n\tzookeeper\x18\x04 \x01(\x0b\x32\x34.yandex.cloud.priv.dataproc.manager.v1.ZookeeperInfo\x12?\n\x05hbase\x18\x05 \x01(\x0b\x32\x30.yandex.cloud.priv.dataproc.manager.v1.HbaseInfo\x12?\n\x05oozie\x18\x06 \x01(\x0b\x32\x30.yandex.cloud.priv.dataproc.manager.v1.OozieInfo\x12\x14\n\x0creport_count\x18\x07 \x01(\x03\x12=\n\x04livy\x18\x08 \x01(\x0b\x32/.yandex.cloud.priv.dataproc.manager.v1.LivyInfo\x12\x42\n\tinit_acts\x18\t \x01(\x0b\x32/.yandex.cloud.priv.dataproc.manager.v1.InitActs\"\xa4\x01\n\rReportRequest\x12\x0b\n\x03\x63id\x18\x01 \x01(\t\x12\x19\n\x11topology_revision\x18\x02 \x01(\x03\x12\x39\n\x04info\x18\x03 \x01(\x0b\x32+.yandex.cloud.priv.dataproc.manager.v1.Info\x12\x30\n\x0c\x63ollected_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"s\n\x0bReportReply\x12\x1c\n\x14\x64\x65\x63ommission_timeout\x18\x01 \x01(\x03\x12\"\n\x1ayarn_hosts_to_decommission\x18\x02 \x03(\t\x12\"\n\x1ahdfs_hosts_to_decommission\x18\x03 \x03(\t\"#\n\x14\x43lusterHealthRequest\x12\x0b\n\x03\x63id\x18\x01 \x01(\t\"\xb9\x01\n\rServiceHealth\x12?\n\x07service\x18\x01 \x01(\x0e\x32..yandex.cloud.priv.dataproc.manager.v1.Service\x12=\n\x06health\x18\x02 \x01(\x0e\x32-.yandex.cloud.priv.dataproc.manager.v1.Health\x12\x13\n\x0b\x65xplanation\x18\x03 \x01(\t\x12\x13\n\x0bupdate_time\x18\x04 \x01(\x03\"\xe7\x02\n\x12\x43lusterHealthReply\x12\x0b\n\x03\x63id\x18\x01 \x01(\t\x12=\n\x06health\x18\x02 \x01(\x0e\x32-.yandex.cloud.priv.dataproc.manager.v1.Health\x12L\n\x0eservice_health\x18\x03 \x03(\x0b\x32\x34.yandex.cloud.priv.dataproc.manager.v1.ServiceHealth\x12\x13\n\x0b\x65xplanation\x18\x04 \x01(\t\x12\x18\n\x10hdfs_in_safemode\x18\x05 \x01(\x08\x12\x14\n\x0creport_count\x18\x06 \x01(\x03\x12\x13\n\x0bupdate_time\x18\x07 \x01(\x03\x12\x42\n\tinit_acts\x18\x08 \x01(\x0b\x32/.yandex.cloud.priv.dataproc.manager.v1.InitActs\x12\x19\n\x11topology_revision\x18\t \x01(\x03\"0\n\x12HostsHealthRequest\x12\x0b\n\x03\x63id\x18\x01 \x01(\t\x12\r\n\x05\x66qdns\x18\x02 \x03(\t\"\xa7\x01\n\nHostHealth\x12\x0c\n\x04\x66qdn\x18\x01 \x01(\t\x12=\n\x06health\x18\x02 \x01(\x0e\x32-.yandex.cloud.priv.dataproc.manager.v1.Health\x12L\n\x0eservice_health\x18\x03 \x03(\x0b\x32\x34.yandex.cloud.priv.dataproc.manager.v1.ServiceHealth\"[\n\x10HostsHealthReply\x12G\n\x0chosts_health\x18\x01 \x03(\x0b\x32\x31.yandex.cloud.priv.dataproc.manager.v1.HostHealth\"\xe2\x01\n\x17MetricsAgentStatusReply\x12\x62\n\rhealth_status\x18\x01 \x01(\x0e\x32K.yandex.cloud.priv.dataproc.manager.v1.MetricsAgentStatusReply.HealthStatus\x12\x0f\n\x07message\x18\x02 \x01(\t\"R\n\x0cHealthStatus\x12\x1d\n\x19HEALTH_STATUS_UNSPECIFIED\x10\x00\x12\x0b\n\x07HEALTHY\x10\x01\x12\x0b\n\x07WARNING\x10\x02\x12\t\n\x05\x45RROR\x10\x03\"\x1b\n\x19MetricsAgentStatusRequest\"[\n\x13\x44\x65\x63ommissionRequest\x12\x0b\n\x03\x63id\x18\x01 \x01(\t\x12\x0f\n\x07timeout\x18\x02 \x01(\x03\x12\x12\n\nyarn_hosts\x18\x03 \x03(\t\x12\x12\n\nhdfs_hosts\x18\x04 \x03(\t\"\x13\n\x11\x44\x65\x63ommissionReply\"(\n\x19\x44\x65\x63ommissionStatusRequest\x12\x0b\n\x03\x63id\x18\x01 \x01(\t\"o\n\x17\x44\x65\x63ommissionStatusReply\x12)\n!yarn_requested_decommission_hosts\x18\x01 \x03(\t\x12)\n!hdfs_requested_decommission_hosts\x18\x02 \x03(\t*]\n\rInitActsState\x12\x1f\n\x1bINIT_ACTS_STATE_UNSPECIFIED\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01\x12\x0e\n\nSUCCESSFUL\x10\x02\x12\x0f\n\x0bIN_PROGRESS\x10\x03*l\n\x06Health\x12\x16\n\x12HEALTH_UNSPECIFIED\x10\x00\x12\t\n\x05\x41LIVE\x10\x01\x12\x08\n\x04\x44\x45\x41\x44\x10\x02\x12\x0c\n\x08\x44\x45GRADED\x10\x03\x12\x13\n\x0f\x44\x45\x43OMMISSIONING\x10\x04\x12\x12\n\x0e\x44\x45\x43OMMISSIONED\x10\x05*\xb6\x01\n\x07Service\x12\x17\n\x13SERVICE_UNSPECIFIED\x10\x00\x12\x08\n\x04HDFS\x10\x01\x12\x08\n\x04YARN\x10\x02\x12\r\n\tMAPREDUCE\x10\x03\x12\x08\n\x04HIVE\x10\x04\x12\x07\n\x03TEZ\x10\x05\x12\r\n\tZOOKEEPER\x10\x06\x12\t\n\x05HBASE\x10\x07\x12\t\n\x05SQOOP\x10\x08\x12\t\n\x05\x46LUME\x10\t\x12\t\n\x05SPARK\x10\n\x12\x0c\n\x08ZEPPELIN\x10\x0b\x12\t\n\x05OOZIE\x10\x0c\x12\x08\n\x04LIVY\x10\r2\xdf\x06\n\x16\x44\x61taprocManagerService\x12t\n\x06Report\x12\x34.yandex.cloud.priv.dataproc.manager.v1.ReportRequest\x1a\x32.yandex.cloud.priv.dataproc.manager.v1.ReportReply\"\x00\x12\x89\x01\n\rClusterHealth\x12;.yandex.cloud.priv.dataproc.manager.v1.ClusterHealthRequest\x1a\x39.yandex.cloud.priv.dataproc.manager.v1.ClusterHealthReply\"\x00\x12\x83\x01\n\x0bHostsHealth\x12\x39.yandex.cloud.priv.dataproc.manager.v1.HostsHealthRequest\x1a\x37.yandex.cloud.priv.dataproc.manager.v1.HostsHealthReply\"\x00\x12\x86\x01\n\x0c\x44\x65\x63ommission\x12:.yandex.cloud.priv.dataproc.manager.v1.DecommissionRequest\x1a\x38.yandex.cloud.priv.dataproc.manager.v1.DecommissionReply\"\x00\x12\x98\x01\n\x12\x44\x65\x63ommissionStatus\x12@.yandex.cloud.priv.dataproc.manager.v1.DecommissionStatusRequest\x1a>.yandex.cloud.priv.dataproc.manager.v1.DecommissionStatusReply\"\x00\x12\x98\x01\n\x12MetricsAgentStatus\x12@.yandex.cloud.priv.dataproc.manager.v1.MetricsAgentStatusRequest\x1a>.yandex.cloud.priv.dataproc.manager.v1.MetricsAgentStatusReply\"\x00\x42\x12Z\x10\x64\x61taproc_managerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.priv.dataproc.manager.v1.manager_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\020dataproc_manager'
  _globals['_INITACTSSTATE']._serialized_start=4023
  _globals['_INITACTSSTATE']._serialized_end=4116
  _globals['_HEALTH']._serialized_start=4118
  _globals['_HEALTH']._serialized_end=4226
  _globals['_SERVICE']._serialized_start=4229
  _globals['_SERVICE']._serialized_end=4411
  _globals['_HBASENODEINFO']._serialized_start=135
  _globals['_HBASENODEINFO']._serialized_end=230
  _globals['_HBASEINFO']._serialized_start=233
  _globals['_HBASEINFO']._serialized_end=468
  _globals['_HDFSNODEINFO']._serialized_start=470
  _globals['_HDFSNODEINFO']._serialized_end=584
  _globals['_HDFSINFO']._serialized_start=587
  _globals['_HDFSINFO']._serialized_end=1128
  _globals['_HIVEINFO']._serialized_start=1131
  _globals['_HIVEINFO']._serialized_end=1286
  _globals['_YARNNODEINFO']._serialized_start=1289
  _globals['_YARNNODEINFO']._serialized_end=1430
  _globals['_YARNINFO']._serialized_start=1433
  _globals['_YARNINFO']._serialized_end=1573
  _globals['_ZOOKEEPERINFO']._serialized_start=1575
  _globals['_ZOOKEEPERINFO']._serialized_end=1605
  _globals['_OOZIEINFO']._serialized_start=1607
  _globals['_OOZIEINFO']._serialized_end=1633
  _globals['_LIVYINFO']._serialized_start=1635
  _globals['_LIVYINFO']._serialized_end=1660
  _globals['_INITACTS']._serialized_start=1662
  _globals['_INITACTS']._serialized_end=1756
  _globals['_INFO']._serialized_start=1759
  _globals['_INFO']._serialized_end=2310
  _globals['_REPORTREQUEST']._serialized_start=2313
  _globals['_REPORTREQUEST']._serialized_end=2477
  _globals['_REPORTREPLY']._serialized_start=2479
  _globals['_REPORTREPLY']._serialized_end=2594
  _globals['_CLUSTERHEALTHREQUEST']._serialized_start=2596
  _globals['_CLUSTERHEALTHREQUEST']._serialized_end=2631
  _globals['_SERVICEHEALTH']._serialized_start=2634
  _globals['_SERVICEHEALTH']._serialized_end=2819
  _globals['_CLUSTERHEALTHREPLY']._serialized_start=2822
  _globals['_CLUSTERHEALTHREPLY']._serialized_end=3181
  _globals['_HOSTSHEALTHREQUEST']._serialized_start=3183
  _globals['_HOSTSHEALTHREQUEST']._serialized_end=3231
  _globals['_HOSTHEALTH']._serialized_start=3234
  _globals['_HOSTHEALTH']._serialized_end=3401
  _globals['_HOSTSHEALTHREPLY']._serialized_start=3403
  _globals['_HOSTSHEALTHREPLY']._serialized_end=3494
  _globals['_METRICSAGENTSTATUSREPLY']._serialized_start=3497
  _globals['_METRICSAGENTSTATUSREPLY']._serialized_end=3723
  _globals['_METRICSAGENTSTATUSREPLY_HEALTHSTATUS']._serialized_start=3641
  _globals['_METRICSAGENTSTATUSREPLY_HEALTHSTATUS']._serialized_end=3723
  _globals['_METRICSAGENTSTATUSREQUEST']._serialized_start=3725
  _globals['_METRICSAGENTSTATUSREQUEST']._serialized_end=3752
  _globals['_DECOMMISSIONREQUEST']._serialized_start=3754
  _globals['_DECOMMISSIONREQUEST']._serialized_end=3845
  _globals['_DECOMMISSIONREPLY']._serialized_start=3847
  _globals['_DECOMMISSIONREPLY']._serialized_end=3866
  _globals['_DECOMMISSIONSTATUSREQUEST']._serialized_start=3868
  _globals['_DECOMMISSIONSTATUSREQUEST']._serialized_end=3908
  _globals['_DECOMMISSIONSTATUSREPLY']._serialized_start=3910
  _globals['_DECOMMISSIONSTATUSREPLY']._serialized_end=4021
  _globals['_DATAPROCMANAGERSERVICE']._serialized_start=4414
  _globals['_DATAPROCMANAGERSERVICE']._serialized_end=5277
# @@protoc_insertion_point(module_scope)
