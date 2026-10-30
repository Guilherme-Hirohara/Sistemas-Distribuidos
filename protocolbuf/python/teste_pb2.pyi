from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RequestDoc(_message.Message):
    __slots__ = ("nome", "doc", "tipo")
    NOME_FIELD_NUMBER: _ClassVar[int]
    DOC_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    nome: str
    doc: str
    tipo: int
    def __init__(self, nome: _Optional[str] = ..., doc: _Optional[str] = ..., tipo: _Optional[int] = ...) -> None: ...

class ReplyDoc(_message.Message):
    __slots__ = ("nome", "tipo_erro", "mensagem")
    NOME_FIELD_NUMBER: _ClassVar[int]
    TIPO_ERRO_FIELD_NUMBER: _ClassVar[int]
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    nome: str
    tipo_erro: int
    mensagem: str
    def __init__(self, nome: _Optional[str] = ..., tipo_erro: _Optional[int] = ..., mensagem: _Optional[str] = ...) -> None: ...
