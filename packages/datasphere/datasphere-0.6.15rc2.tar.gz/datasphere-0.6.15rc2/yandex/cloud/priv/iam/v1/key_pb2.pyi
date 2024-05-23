"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Key(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Algorithm:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _AlgorithmEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Key._Algorithm.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        ALGORITHM_UNSPECIFIED: Key._Algorithm.ValueType  # 0
        RSA_2048: Key._Algorithm.ValueType  # 1
        RSA_4096: Key._Algorithm.ValueType  # 2

    class Algorithm(_Algorithm, metaclass=_AlgorithmEnumTypeWrapper): ...
    ALGORITHM_UNSPECIFIED: Key.Algorithm.ValueType  # 0
    RSA_2048: Key.Algorithm.ValueType  # 1
    RSA_4096: Key.Algorithm.ValueType  # 2

    ID_FIELD_NUMBER: builtins.int
    USER_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    SERVICE_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    KEY_ALGORITHM_FIELD_NUMBER: builtins.int
    PUBLIC_KEY_FIELD_NUMBER: builtins.int
    FINGERPRINT_FIELD_NUMBER: builtins.int
    LAST_USED_AT_FIELD_NUMBER: builtins.int
    id: builtins.str
    user_account_id: builtins.str
    service_account_id: builtins.str
    description: builtins.str
    key_algorithm: global___Key.Algorithm.ValueType
    public_key: builtins.str
    """This field does not contain sensitive data,
    but such data also does not contain useful information.
    At the same time, these bits are difficult to compress.
    That's why we don't log this field.
    Use the fingerprint value to identify the key.
    """
    fingerprint: builtins.str
    """Base64-encoded (no padding) sha256 hash of DER-encoded RSA public key in SubjectPublicKeyInfo format."""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def last_used_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        user_account_id: builtins.str = ...,
        service_account_id: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        description: builtins.str = ...,
        key_algorithm: global___Key.Algorithm.ValueType = ...,
        public_key: builtins.str = ...,
        fingerprint: builtins.str = ...,
        last_used_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at", "last_used_at", b"last_used_at", "service_account_id", b"service_account_id", "subject", b"subject", "user_account_id", b"user_account_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["created_at", b"created_at", "description", b"description", "fingerprint", b"fingerprint", "id", b"id", "key_algorithm", b"key_algorithm", "last_used_at", b"last_used_at", "public_key", b"public_key", "service_account_id", b"service_account_id", "subject", b"subject", "user_account_id", b"user_account_id"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["subject", b"subject"]) -> typing.Literal["user_account_id", "service_account_id"] | None: ...

global___Key = Key
