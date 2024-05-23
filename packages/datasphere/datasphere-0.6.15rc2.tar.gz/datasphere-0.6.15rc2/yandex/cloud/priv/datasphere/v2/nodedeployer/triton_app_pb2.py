# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/priv/datasphere/v2/nodedeployer/triton_app.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.priv.datasphere.v2.nodedeployer import runtime_options_pb2 as yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_nodedeployer_dot_runtime__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=yandex/cloud/priv/datasphere/v2/nodedeployer/triton_app.proto\x12,yandex.cloud.priv.datasphere.v2.nodedeployer\x1a\x42yandex/cloud/priv/datasphere/v2/nodedeployer/runtime_options.proto\"\xad\x01\n\tTritonApp\x12I\n\x06models\x18\x01 \x03(\x0b\x32\x39.yandex.cloud.priv.datasphere.v2.nodedeployer.TritonModel\x12U\n\x0fruntime_options\x18\x02 \x01(\x0b\x32<.yandex.cloud.priv.datasphere.v2.nodedeployer.RuntimeOptions\"q\n\x0bTritonModel\x12\n\n\x02id\x18\x01 \x01(\t\x12V\n\x13triton_model_config\x18\x02 \x01(\x0b\x32\x39.yandex.cloud.priv.datasphere.v2.nodedeployer.ModelConfig\"\xa8\x05\n\x0bModelConfig\x12S\n\x05input\x18\x01 \x03(\x0b\x32\x44.yandex.cloud.priv.datasphere.v2.nodedeployer.ModelConfig.ModelInput\x12U\n\x06output\x18\x02 \x03(\x0b\x32\x45.yandex.cloud.priv.datasphere.v2.nodedeployer.ModelConfig.ModelOutput\x1a\x7f\n\nModelInput\x12\x0c\n\x04name\x18\x01 \x01(\t\x12U\n\tdata_type\x18\x02 \x01(\x0e\x32\x42.yandex.cloud.priv.datasphere.v2.nodedeployer.ModelConfig.DataType\x12\x0c\n\x04\x64ims\x18\x03 \x03(\x03\x1a\x80\x01\n\x0bModelOutput\x12\x0c\n\x04name\x18\x01 \x01(\t\x12U\n\tdata_type\x18\x02 \x01(\x0e\x32\x42.yandex.cloud.priv.datasphere.v2.nodedeployer.ModelConfig.DataType\x12\x0c\n\x04\x64ims\x18\x03 \x03(\x03\"\xe8\x01\n\x08\x44\x61taType\x12\r\n\tTYPE_BOOL\x10\x00\x12\x0e\n\nTYPE_UINT8\x10\x01\x12\x0f\n\x0bTYPE_UINT16\x10\x02\x12\x0f\n\x0bTYPE_UINT32\x10\x03\x12\x0f\n\x0bTYPE_UINT64\x10\x04\x12\r\n\tTYPE_INT8\x10\x05\x12\x0e\n\nTYPE_INT16\x10\x06\x12\x0e\n\nTYPE_INT32\x10\x07\x12\x0e\n\nTYPE_INT64\x10\x08\x12\r\n\tTYPE_FP16\x10\t\x12\r\n\tTYPE_FP32\x10\n\x12\r\n\tTYPE_FP64\x10\x0b\x12\x0f\n\x0bTYPE_STRING\x10\x0c\x12\r\n\tTYPE_BF16\x10\rB?\n\"yandex.cloud.priv.datasphere.v2ydsB\rNDTritonAppV2Z\ndatasphereb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.priv.datasphere.v2.nodedeployer.triton_app_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"yandex.cloud.priv.datasphere.v2ydsB\rNDTritonAppV2Z\ndatasphere'
  _globals['_TRITONAPP']._serialized_start=180
  _globals['_TRITONAPP']._serialized_end=353
  _globals['_TRITONMODEL']._serialized_start=355
  _globals['_TRITONMODEL']._serialized_end=468
  _globals['_MODELCONFIG']._serialized_start=471
  _globals['_MODELCONFIG']._serialized_end=1151
  _globals['_MODELCONFIG_MODELINPUT']._serialized_start=658
  _globals['_MODELCONFIG_MODELINPUT']._serialized_end=785
  _globals['_MODELCONFIG_MODELOUTPUT']._serialized_start=788
  _globals['_MODELCONFIG_MODELOUTPUT']._serialized_end=916
  _globals['_MODELCONFIG_DATATYPE']._serialized_start=919
  _globals['_MODELCONFIG_DATATYPE']._serialized_end=1151
# @@protoc_insertion_point(module_scope)
