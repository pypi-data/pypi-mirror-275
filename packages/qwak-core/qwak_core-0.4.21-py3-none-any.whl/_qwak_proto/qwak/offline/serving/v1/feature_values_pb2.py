# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qwak/offline/serving/v1/feature_values.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,qwak/offline/serving/v1/feature_values.proto\x12%qwak.feature.store.offline.serving.v1\"D\n\x12\x46\x65\x61turesetFeatures\x12\x17\n\x0f\x66\x65\x61tureset_name\x18\x01 \x01(\t\x12\x15\n\rfeature_names\x18\x02 \x03(\tB&\n\"com.qwak.ai.offline.serving.api.v1P\x01\x62\x06proto3')



_FEATURESETFEATURES = DESCRIPTOR.message_types_by_name['FeaturesetFeatures']
FeaturesetFeatures = _reflection.GeneratedProtocolMessageType('FeaturesetFeatures', (_message.Message,), {
  'DESCRIPTOR' : _FEATURESETFEATURES,
  '__module__' : 'qwak.offline.serving.v1.feature_values_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.offline.serving.v1.FeaturesetFeatures)
  })
_sym_db.RegisterMessage(FeaturesetFeatures)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"com.qwak.ai.offline.serving.api.v1P\001'
  _FEATURESETFEATURES._serialized_start=87
  _FEATURESETFEATURES._serialized_end=155
# @@protoc_insertion_point(module_scope)
