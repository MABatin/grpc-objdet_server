# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protoc/object_detection/object_detection.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.protoc/object_detection/object_detection.proto\x12\x0fObjectDetection\"D\n\x10\x44\x65tectionRequest\x12\x10\n\x08\x66rame_id\x18\x01 \x01(\x05\x12\x0f\n\x07\x63lasses\x18\x02 \x03(\x05\x12\r\n\x05image\x18\x03 \x01(\x0c\"^\n\x11\x44\x65tectionResponse\x12\x10\n\x08\x66rame_id\x18\x01 \x01(\x05\x12(\n\x07results\x18\x02 \x03(\x0b\x32\x17.ObjectDetection.Result\x12\r\n\x05image\x18\x03 \x01(\x0c\"`\n\x06Result\x12\r\n\x05label\x18\x01 \x01(\t\x12\r\n\x05score\x18\x02 \x01(\x02\x12\x0c\n\x04xyxy\x18\x03 \x03(\x05\x12\r\n\x05xyxyn\x18\x04 \x03(\x02\x12\x0c\n\x04xywh\x18\x05 \x03(\x05\x12\r\n\x05xywhn\x18\x06 \x03(\x02\x32\xc6\x01\n\x0fObjectDetection\x12V\n\x0b\x44\x65tectImage\x12!.ObjectDetection.DetectionRequest\x1a\".ObjectDetection.DetectionResponse\"\x00\x12[\n\x0c\x44\x65tectStream\x12!.ObjectDetection.DetectionRequest\x1a\".ObjectDetection.DetectionResponse\"\x00(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protoc.object_detection.object_detection_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_DETECTIONREQUEST']._serialized_start=67
  _globals['_DETECTIONREQUEST']._serialized_end=135
  _globals['_DETECTIONRESPONSE']._serialized_start=137
  _globals['_DETECTIONRESPONSE']._serialized_end=231
  _globals['_RESULT']._serialized_start=233
  _globals['_RESULT']._serialized_end=329
  _globals['_OBJECTDETECTION']._serialized_start=332
  _globals['_OBJECTDETECTION']._serialized_end=530
# @@protoc_insertion_point(module_scope)
