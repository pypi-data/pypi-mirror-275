# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: JobState.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Log_pb2 as Log__pb2
import JobStatus_pb2 as JobStatus__pb2
import JobResult_pb2 as JobResult__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eJobState.proto\x1a\tLog.proto\x1a\x0fJobStatus.proto\x1a\x0fJobResult.proto\"\xa9\x01\n\x08JobState\x12\x12\n\nacceptedAt\x18\r \x01(\x04\x12\x12\n\nacceptedBy\x18\x0e \x01(\t\x12\x1a\n\x06status\x18\x0f \x01(\x0e\x32\n.JobStatus\x12\x12\n\x04logs\x18\x11 \x03(\x0b\x32\x04.Log\x12\x11\n\ttimestamp\x18\x12 \x01(\x04\x12\x1a\n\x06result\x18\x13 \x01(\x0b\x32\n.JobResult\x12\x16\n\x0e\x61\x63\x63\x65ptedByNode\x18\x14 \x01(\tB.\xca\x02\x0e\x41pp\\Grpc\\nostr\xe2\x02\x1a\x41pp\\Grpc\\nostr\\GPBMetadatab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'JobState_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\312\002\016App\\Grpc\\nostr\342\002\032App\\Grpc\\nostr\\GPBMetadata'
  _globals['_JOBSTATE']._serialized_start=64
  _globals['_JOBSTATE']._serialized_end=233
# @@protoc_insertion_point(module_scope)
