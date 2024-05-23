"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
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
class GetUserAccountRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    user_account_id: builtins.str
    def __init__(
        self,
        *,
        user_account_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["user_account_id", b"user_account_id"]) -> None: ...

global___GetUserAccountRequest = GetUserAccountRequest

@typing.final
class DeleteUserAccountRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBJECT_ID_FIELD_NUMBER: builtins.int
    subject_id: builtins.str
    def __init__(
        self,
        *,
        subject_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["subject_id", b"subject_id"]) -> None: ...

global___DeleteUserAccountRequest = DeleteUserAccountRequest

@typing.final
class DeleteUserAccountMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBJECT_ID_FIELD_NUMBER: builtins.int
    subject_id: builtins.str
    def __init__(
        self,
        *,
        subject_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["subject_id", b"subject_id"]) -> None: ...

global___DeleteUserAccountMetadata = DeleteUserAccountMetadata

@typing.final
class GetSettingsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESPONSE_JSON_PATH_FIELD_NUMBER: builtins.int
    SUBJECT_ID_FIELD_NUMBER: builtins.int
    subject_id: builtins.str
    """Optional - get specified subject user settings. By default equals to authenticated subject."""
    @property
    def response_json_path(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Empty list means full settings."""

    def __init__(
        self,
        *,
        response_json_path: collections.abc.Iterable[builtins.str] | None = ...,
        subject_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["response_json_path", b"response_json_path", "subject_id", b"subject_id"]) -> None: ...

global___GetSettingsRequest = GetSettingsRequest

@typing.final
class UserSettings(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JSON_FIELD_NUMBER: builtins.int
    json: builtins.str
    """JSON-serialized user-settings."""
    def __init__(
        self,
        *,
        json: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["json", b"json"]) -> None: ...

global___UserSettings = UserSettings

@typing.final
class UpdateSettingsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESPONSE_JSON_PATH_FIELD_NUMBER: builtins.int
    JSON_PATCH_FIELD_NUMBER: builtins.int
    SUBJECT_ID_FIELD_NUMBER: builtins.int
    json_patch: builtins.str
    """Serialized JSON Patch (https://tools.ietf.org/html/rfc6902)."""
    subject_id: builtins.str
    """Optional - update specified subject user settings. By default equals to authenticated subject."""
    @property
    def response_json_path(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Empty list means full settings."""

    def __init__(
        self,
        *,
        response_json_path: collections.abc.Iterable[builtins.str] | None = ...,
        json_patch: builtins.str = ...,
        subject_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["json_patch", b"json_patch", "response_json_path", b"response_json_path", "subject_id", b"subject_id"]) -> None: ...

global___UpdateSettingsRequest = UpdateSettingsRequest

@typing.final
class PresignUrlRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Version2Parameters(google.protobuf.message.Message):
        """https://docs.aws.amazon.com/general/latest/gr/signature-version-2.html"""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        class _SignatureMethod:
            ValueType = typing.NewType("ValueType", builtins.int)
            V: typing_extensions.TypeAlias = ValueType

        class _SignatureMethodEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[PresignUrlRequest.Version2Parameters._SignatureMethod.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            SIGNATURE_METHOD_UNSPECIFIED: PresignUrlRequest.Version2Parameters._SignatureMethod.ValueType  # 0
            HMAC_SHA1: PresignUrlRequest.Version2Parameters._SignatureMethod.ValueType  # 1
            HMAC_SHA256: PresignUrlRequest.Version2Parameters._SignatureMethod.ValueType  # 2

        class SignatureMethod(_SignatureMethod, metaclass=_SignatureMethodEnumTypeWrapper): ...
        SIGNATURE_METHOD_UNSPECIFIED: PresignUrlRequest.Version2Parameters.SignatureMethod.ValueType  # 0
        HMAC_SHA1: PresignUrlRequest.Version2Parameters.SignatureMethod.ValueType  # 1
        HMAC_SHA256: PresignUrlRequest.Version2Parameters.SignatureMethod.ValueType  # 2

        SIGNATURE_METHOD_FIELD_NUMBER: builtins.int
        signature_method: global___PresignUrlRequest.Version2Parameters.SignatureMethod.ValueType
        def __init__(
            self,
            *,
            signature_method: global___PresignUrlRequest.Version2Parameters.SignatureMethod.ValueType = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["signature_method", b"signature_method"]) -> None: ...

    @typing.final
    class Version4Parameters(google.protobuf.message.Message):
        """https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html"""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        SIGNED_AT_FIELD_NUMBER: builtins.int
        SERVICE_FIELD_NUMBER: builtins.int
        REGION_FIELD_NUMBER: builtins.int
        service: builtins.str
        region: builtins.str
        @property
        def signed_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
        def __init__(
            self,
            *,
            signed_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
            service: builtins.str = ...,
            region: builtins.str = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["signed_at", b"signed_at"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["region", b"region", "service", b"service", "signed_at", b"signed_at"]) -> None: ...

    SUBJECT_ID_FIELD_NUMBER: builtins.int
    STRINGS_TO_SIGN_FIELD_NUMBER: builtins.int
    V2_PARAMETERS_FIELD_NUMBER: builtins.int
    V4_PARAMETERS_FIELD_NUMBER: builtins.int
    subject_id: builtins.str
    @property
    def strings_to_sign(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """The formatted string to sign, see https://docs.aws.amazon.com/general/latest/gr/sigv4-create-string-to-sign.html"""

    @property
    def v2_parameters(self) -> global___PresignUrlRequest.Version2Parameters: ...
    @property
    def v4_parameters(self) -> global___PresignUrlRequest.Version4Parameters: ...
    def __init__(
        self,
        *,
        subject_id: builtins.str = ...,
        strings_to_sign: collections.abc.Iterable[builtins.str] | None = ...,
        v2_parameters: global___PresignUrlRequest.Version2Parameters | None = ...,
        v4_parameters: global___PresignUrlRequest.Version4Parameters | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["parameters", b"parameters", "v2_parameters", b"v2_parameters", "v4_parameters", b"v4_parameters"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["parameters", b"parameters", "strings_to_sign", b"strings_to_sign", "subject_id", b"subject_id", "v2_parameters", b"v2_parameters", "v4_parameters", b"v4_parameters"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["parameters", b"parameters"]) -> typing.Literal["v2_parameters", "v4_parameters"] | None: ...

global___PresignUrlRequest = PresignUrlRequest

@typing.final
class PresignUrlResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCESS_KEY_ID_FIELD_NUMBER: builtins.int
    SIGNED_STRINGS_FIELD_NUMBER: builtins.int
    access_key_id: builtins.str
    @property
    def signed_strings(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___SignedString]: ...
    def __init__(
        self,
        *,
        access_key_id: builtins.str = ...,
        signed_strings: collections.abc.Iterable[global___SignedString] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["access_key_id", b"access_key_id", "signed_strings", b"signed_strings"]) -> None: ...

global___PresignUrlResponse = PresignUrlResponse

@typing.final
class SignedString(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STRING_TO_SIGN_FIELD_NUMBER: builtins.int
    SIGNATURE_FIELD_NUMBER: builtins.int
    string_to_sign: builtins.str
    signature: builtins.str
    def __init__(
        self,
        *,
        string_to_sign: builtins.str = ...,
        signature: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["signature", b"signature", "string_to_sign", b"string_to_sign"]) -> None: ...

global___SignedString = SignedString
