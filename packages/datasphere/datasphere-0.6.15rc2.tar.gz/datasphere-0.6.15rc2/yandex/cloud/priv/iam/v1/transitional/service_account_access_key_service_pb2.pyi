"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class PresignUrlRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_ID_FIELD_NUMBER: builtins.int
    STRING_TO_SIGN_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    REGION_FIELD_NUMBER: builtins.int
    SERVICE_FIELD_NUMBER: builtins.int
    key_id: builtins.str
    """TODO not cloud ID"""
    string_to_sign: builtins.str
    version: builtins.str
    """TODO enum"""
    region: builtins.str
    service: builtins.str
    def __init__(
        self,
        *,
        key_id: builtins.str = ...,
        string_to_sign: builtins.str = ...,
        version: builtins.str = ...,
        region: builtins.str = ...,
        service: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["key_id", b"key_id", "region", b"region", "service", b"service", "string_to_sign", b"string_to_sign", "version", b"version"]) -> None: ...

global___PresignUrlRequest = PresignUrlRequest

@typing.final
class PresignUrlResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESULT_FIELD_NUMBER: builtins.int
    SIGNATURE_FIELD_NUMBER: builtins.int
    KEY_ID_FIELD_NUMBER: builtins.int
    result: builtins.str
    signature: builtins.str
    key_id: builtins.str
    def __init__(
        self,
        *,
        result: builtins.str = ...,
        signature: builtins.str = ...,
        key_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["key_id", b"key_id", "result", b"result", "signature", b"signature"]) -> None: ...

global___PresignUrlResponse = PresignUrlResponse

@typing.final
class PresignUrlsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_ID_FIELD_NUMBER: builtins.int
    STRINGS_TO_SIGN_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    REGION_FIELD_NUMBER: builtins.int
    SERVICE_FIELD_NUMBER: builtins.int
    key_id: builtins.str
    """TODO not cloud ID"""
    version: builtins.str
    """TODO enum"""
    region: builtins.str
    service: builtins.str
    @property
    def strings_to_sign(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        key_id: builtins.str = ...,
        strings_to_sign: collections.abc.Iterable[builtins.str] | None = ...,
        version: builtins.str = ...,
        region: builtins.str = ...,
        service: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["key_id", b"key_id", "region", b"region", "service", b"service", "strings_to_sign", b"strings_to_sign", "version", b"version"]) -> None: ...

global___PresignUrlsRequest = PresignUrlsRequest

@typing.final
class PresignUrlsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_ID_FIELD_NUMBER: builtins.int
    SIGNATURES_FIELD_NUMBER: builtins.int
    key_id: builtins.str
    @property
    def signatures(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        key_id: builtins.str = ...,
        signatures: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["key_id", b"key_id", "signatures", b"signatures"]) -> None: ...

global___PresignUrlsResponse = PresignUrlsResponse

@typing.final
class PresignKey(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_ID_FIELD_NUMBER: builtins.int
    key_id: builtins.str
    def __init__(
        self,
        *,
        key_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["key_id", b"key_id"]) -> None: ...

global___PresignKey = PresignKey
