# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spelling_bee_game.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='spelling_bee_game.proto',
  package='app',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17spelling_bee_game.proto\x12\x03\x61pp\"1\n\x0bGameRequest\x12\x10\n\x08userName\x18\x01 \x01(\t\x12\x10\n\x08gameType\x18\x02 \x01(\t\"3\n\x0cGameResponse\x12\x0e\n\x06gameId\x18\x01 \x01(\t\x12\x13\n\x0bplayerIndex\x18\x02 \x01(\x05\"3\n\x0fRegisterRequest\x12\x0e\n\x06gameId\x18\x01 \x01(\t\x12\x10\n\x08userName\x18\x02 \x01(\t\"\'\n\x10RegisterResponse\x12\x13\n\x0bplayerIndex\x18\x01 \x01(\x05\"!\n\x0f\x46inalizeRequest\x12\x0e\n\x06gameId\x18\x01 \x01(\t\"\x12\n\x10\x46inalizeResponse\"\x14\n\x04Word\x12\x0c\n\x04word\x18\x01 \x01(\t\"W\n\x11SuggestionRequest\x12\x0e\n\x06gameId\x18\x01 \x01(\t\x12\x13\n\x0bplayerIndex\x18\x02 \x01(\x05\x12\x1d\n\nsuggestion\x18\x03 \x01(\x0b\x32\t.app.Word\"5\n\x12SuggestionResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x1f\n\rStatusRequest\x12\x0e\n\x06gameId\x18\x01 \x01(\t\"F\n\x0eStatusResponse\x12\x13\n\x0bplayerCount\x18\x01 \x01(\x05\x12\x0f\n\x07pangram\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\x08\x32\xc7\x02\n\x0fSpellingBeeGame\x12\x33\n\nCreateGame\x12\x10.app.GameRequest\x1a\x11.app.GameResponse\"\x00\x12?\n\x0eRegisterPlayer\x12\x14.app.RegisterRequest\x1a\x15.app.RegisterResponse\"\x00\x12=\n\x0c\x46inalizeGame\x12\x14.app.FinalizeRequest\x1a\x15.app.FinalizeResponse\"\x00\x12\x46\n\x11ProcessSuggestion\x12\x16.app.SuggestionRequest\x1a\x17.app.SuggestionResponse\"\x00\x12\x37\n\nGameStatus\x12\x12.app.StatusRequest\x1a\x13.app.StatusResponse\"\x00\x62\x06proto3'
)




_GAMEREQUEST = _descriptor.Descriptor(
  name='GameRequest',
  full_name='app.GameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userName', full_name='app.GameRequest.userName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gameType', full_name='app.GameRequest.gameType', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=81,
)


_GAMERESPONSE = _descriptor.Descriptor(
  name='GameResponse',
  full_name='app.GameResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='gameId', full_name='app.GameResponse.gameId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='playerIndex', full_name='app.GameResponse.playerIndex', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=83,
  serialized_end=134,
)


_REGISTERREQUEST = _descriptor.Descriptor(
  name='RegisterRequest',
  full_name='app.RegisterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='gameId', full_name='app.RegisterRequest.gameId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userName', full_name='app.RegisterRequest.userName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=136,
  serialized_end=187,
)


_REGISTERRESPONSE = _descriptor.Descriptor(
  name='RegisterResponse',
  full_name='app.RegisterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='playerIndex', full_name='app.RegisterResponse.playerIndex', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=189,
  serialized_end=228,
)


_FINALIZEREQUEST = _descriptor.Descriptor(
  name='FinalizeRequest',
  full_name='app.FinalizeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='gameId', full_name='app.FinalizeRequest.gameId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=230,
  serialized_end=263,
)


_FINALIZERESPONSE = _descriptor.Descriptor(
  name='FinalizeResponse',
  full_name='app.FinalizeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=265,
  serialized_end=283,
)


_WORD = _descriptor.Descriptor(
  name='Word',
  full_name='app.Word',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='word', full_name='app.Word.word', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=285,
  serialized_end=305,
)


_SUGGESTIONREQUEST = _descriptor.Descriptor(
  name='SuggestionRequest',
  full_name='app.SuggestionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='gameId', full_name='app.SuggestionRequest.gameId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='playerIndex', full_name='app.SuggestionRequest.playerIndex', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='suggestion', full_name='app.SuggestionRequest.suggestion', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=307,
  serialized_end=394,
)


_SUGGESTIONRESPONSE = _descriptor.Descriptor(
  name='SuggestionResponse',
  full_name='app.SuggestionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='app.SuggestionResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='app.SuggestionResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=396,
  serialized_end=449,
)


_STATUSREQUEST = _descriptor.Descriptor(
  name='StatusRequest',
  full_name='app.StatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='gameId', full_name='app.StatusRequest.gameId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=451,
  serialized_end=482,
)


_STATUSRESPONSE = _descriptor.Descriptor(
  name='StatusResponse',
  full_name='app.StatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='playerCount', full_name='app.StatusResponse.playerCount', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pangram', full_name='app.StatusResponse.pangram', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='app.StatusResponse.status', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=484,
  serialized_end=554,
)

_SUGGESTIONREQUEST.fields_by_name['suggestion'].message_type = _WORD
DESCRIPTOR.message_types_by_name['GameRequest'] = _GAMEREQUEST
DESCRIPTOR.message_types_by_name['GameResponse'] = _GAMERESPONSE
DESCRIPTOR.message_types_by_name['RegisterRequest'] = _REGISTERREQUEST
DESCRIPTOR.message_types_by_name['RegisterResponse'] = _REGISTERRESPONSE
DESCRIPTOR.message_types_by_name['FinalizeRequest'] = _FINALIZEREQUEST
DESCRIPTOR.message_types_by_name['FinalizeResponse'] = _FINALIZERESPONSE
DESCRIPTOR.message_types_by_name['Word'] = _WORD
DESCRIPTOR.message_types_by_name['SuggestionRequest'] = _SUGGESTIONREQUEST
DESCRIPTOR.message_types_by_name['SuggestionResponse'] = _SUGGESTIONRESPONSE
DESCRIPTOR.message_types_by_name['StatusRequest'] = _STATUSREQUEST
DESCRIPTOR.message_types_by_name['StatusResponse'] = _STATUSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GameRequest = _reflection.GeneratedProtocolMessageType('GameRequest', (_message.Message,), {
  'DESCRIPTOR' : _GAMEREQUEST,
  '__module__' : 'spelling_bee_game_pb2'
  # @@protoc_insertion_point(class_scope:app.GameRequest)
  })
_sym_db.RegisterMessage(GameRequest)

GameResponse = _reflection.GeneratedProtocolMessageType('GameResponse', (_message.Message,), {
  'DESCRIPTOR' : _GAMERESPONSE,
  '__module__' : 'spelling_bee_game_pb2'
  # @@protoc_insertion_point(class_scope:app.GameResponse)
  })
_sym_db.RegisterMessage(GameResponse)

RegisterRequest = _reflection.GeneratedProtocolMessageType('RegisterRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERREQUEST,
  '__module__' : 'spelling_bee_game_pb2'
  # @@protoc_insertion_point(class_scope:app.RegisterRequest)
  })
_sym_db.RegisterMessage(RegisterRequest)

RegisterResponse = _reflection.GeneratedProtocolMessageType('RegisterResponse', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERRESPONSE,
  '__module__' : 'spelling_bee_game_pb2'
  # @@protoc_insertion_point(class_scope:app.RegisterResponse)
  })
_sym_db.RegisterMessage(RegisterResponse)

FinalizeRequest = _reflection.GeneratedProtocolMessageType('FinalizeRequest', (_message.Message,), {
  'DESCRIPTOR' : _FINALIZEREQUEST,
  '__module__' : 'spelling_bee_game_pb2'
  # @@protoc_insertion_point(class_scope:app.FinalizeRequest)
  })
_sym_db.RegisterMessage(FinalizeRequest)

FinalizeResponse = _reflection.GeneratedProtocolMessageType('FinalizeResponse', (_message.Message,), {
  'DESCRIPTOR' : _FINALIZERESPONSE,
  '__module__' : 'spelling_bee_game_pb2'
  # @@protoc_insertion_point(class_scope:app.FinalizeResponse)
  })
_sym_db.RegisterMessage(FinalizeResponse)

Word = _reflection.GeneratedProtocolMessageType('Word', (_message.Message,), {
  'DESCRIPTOR' : _WORD,
  '__module__' : 'spelling_bee_game_pb2'
  # @@protoc_insertion_point(class_scope:app.Word)
  })
_sym_db.RegisterMessage(Word)

SuggestionRequest = _reflection.GeneratedProtocolMessageType('SuggestionRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUGGESTIONREQUEST,
  '__module__' : 'spelling_bee_game_pb2'
  # @@protoc_insertion_point(class_scope:app.SuggestionRequest)
  })
_sym_db.RegisterMessage(SuggestionRequest)

SuggestionResponse = _reflection.GeneratedProtocolMessageType('SuggestionResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUGGESTIONRESPONSE,
  '__module__' : 'spelling_bee_game_pb2'
  # @@protoc_insertion_point(class_scope:app.SuggestionResponse)
  })
_sym_db.RegisterMessage(SuggestionResponse)

StatusRequest = _reflection.GeneratedProtocolMessageType('StatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _STATUSREQUEST,
  '__module__' : 'spelling_bee_game_pb2'
  # @@protoc_insertion_point(class_scope:app.StatusRequest)
  })
_sym_db.RegisterMessage(StatusRequest)

StatusResponse = _reflection.GeneratedProtocolMessageType('StatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _STATUSRESPONSE,
  '__module__' : 'spelling_bee_game_pb2'
  # @@protoc_insertion_point(class_scope:app.StatusResponse)
  })
_sym_db.RegisterMessage(StatusResponse)



_SPELLINGBEEGAME = _descriptor.ServiceDescriptor(
  name='SpellingBeeGame',
  full_name='app.SpellingBeeGame',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=557,
  serialized_end=884,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateGame',
    full_name='app.SpellingBeeGame.CreateGame',
    index=0,
    containing_service=None,
    input_type=_GAMEREQUEST,
    output_type=_GAMERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RegisterPlayer',
    full_name='app.SpellingBeeGame.RegisterPlayer',
    index=1,
    containing_service=None,
    input_type=_REGISTERREQUEST,
    output_type=_REGISTERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='FinalizeGame',
    full_name='app.SpellingBeeGame.FinalizeGame',
    index=2,
    containing_service=None,
    input_type=_FINALIZEREQUEST,
    output_type=_FINALIZERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ProcessSuggestion',
    full_name='app.SpellingBeeGame.ProcessSuggestion',
    index=3,
    containing_service=None,
    input_type=_SUGGESTIONREQUEST,
    output_type=_SUGGESTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GameStatus',
    full_name='app.SpellingBeeGame.GameStatus',
    index=4,
    containing_service=None,
    input_type=_STATUSREQUEST,
    output_type=_STATUSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SPELLINGBEEGAME)

DESCRIPTOR.services_by_name['SpellingBeeGame'] = _SPELLINGBEEGAME

# @@protoc_insertion_point(module_scope)
