# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hangups/test/test_pblite2.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='hangups/test/test_pblite2.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x1fhangups/test/test_pblite2.proto\"#\n\x0f\x45mbeddedMessage\x12\x10\n\x08test_int\x18\x01 \x01(\x05\"\x93\x01\n\x0bTestMessage\x12\x10\n\x08test_int\x18\x01 \x01(\x05\x12*\n\x10\x65mbedded_message\x18\x02 \x01(\x0b\x32\x10.EmbeddedMessage\x12\x15\n\rtest_int_list\x18\x03 \x03(\x05\x12/\n\x15\x65mbedded_message_list\x18\x04 \x03(\x0b\x32\x10.EmbeddedMessageb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_EMBEDDEDMESSAGE = _descriptor.Descriptor(
  name='EmbeddedMessage',
  full_name='EmbeddedMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='test_int', full_name='EmbeddedMessage.test_int', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=70,
)


_TESTMESSAGE = _descriptor.Descriptor(
  name='TestMessage',
  full_name='TestMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='test_int', full_name='TestMessage.test_int', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='embedded_message', full_name='TestMessage.embedded_message', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='test_int_list', full_name='TestMessage.test_int_list', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='embedded_message_list', full_name='TestMessage.embedded_message_list', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=73,
  serialized_end=220,
)

_TESTMESSAGE.fields_by_name['embedded_message'].message_type = _EMBEDDEDMESSAGE
_TESTMESSAGE.fields_by_name['embedded_message_list'].message_type = _EMBEDDEDMESSAGE
DESCRIPTOR.message_types_by_name['EmbeddedMessage'] = _EMBEDDEDMESSAGE
DESCRIPTOR.message_types_by_name['TestMessage'] = _TESTMESSAGE

EmbeddedMessage = _reflection.GeneratedProtocolMessageType('EmbeddedMessage', (_message.Message,), dict(
  DESCRIPTOR = _EMBEDDEDMESSAGE,
  __module__ = 'hangups.test.test_pblite2_pb2'
  # @@protoc_insertion_point(class_scope:EmbeddedMessage)
  ))
_sym_db.RegisterMessage(EmbeddedMessage)

TestMessage = _reflection.GeneratedProtocolMessageType('TestMessage', (_message.Message,), dict(
  DESCRIPTOR = _TESTMESSAGE,
  __module__ = 'hangups.test.test_pblite2_pb2'
  # @@protoc_insertion_point(class_scope:TestMessage)
  ))
_sym_db.RegisterMessage(TestMessage)


# @@protoc_insertion_point(module_scope)
