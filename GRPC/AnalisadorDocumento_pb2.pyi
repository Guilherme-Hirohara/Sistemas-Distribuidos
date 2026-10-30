from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RequisicaoDocumento(_message.Message):
    __slots__ = ("documento", "tipoDocumento")
    DOCUMENTO_FIELD_NUMBER: _ClassVar[int]
    TIPODOCUMENTO_FIELD_NUMBER: _ClassVar[int]
    documento: str
    tipoDocumento: int
    def __init__(self, documento: _Optional[str] = ..., tipoDocumento: _Optional[int] = ...) -> None: ...

class RespostaProtocolo(_message.Message):
    __slots__ = ("tipoResposta", "mensagem")
    TIPORESPOSTA_FIELD_NUMBER: _ClassVar[int]
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    tipoResposta: int
    mensagem: str
    def __init__(self, tipoResposta: _Optional[int] = ..., mensagem: _Optional[str] = ...) -> None: ...
