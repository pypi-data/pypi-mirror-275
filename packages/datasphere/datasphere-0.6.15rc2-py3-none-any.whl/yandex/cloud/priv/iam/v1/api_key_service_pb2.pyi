"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import yandex.cloud.priv.iam.v1.api_key_pb2
import yandex.cloud.priv.operation.operation_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetApiKeyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    API_KEY_ID_FIELD_NUMBER: builtins.int
    api_key_id: builtins.str
    def __init__(
        self,
        *,
        api_key_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["api_key_id", b"api_key_id"]) -> None: ...

global___GetApiKeyRequest = GetApiKeyRequest

@typing.final
class ListApiKeysRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVICE_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    service_account_id: builtins.str
    """use current subject identity if this not set"""
    page_size: builtins.int
    page_token: builtins.str
    def __init__(
        self,
        *,
        service_account_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["page_size", b"page_size", "page_token", b"page_token", "service_account_id", b"service_account_id"]) -> None: ...

global___ListApiKeysRequest = ListApiKeysRequest

@typing.final
class ListApiKeysResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    API_KEYS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    @property
    def api_keys(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.priv.iam.v1.api_key_pb2.ApiKey]: ...
    def __init__(
        self,
        *,
        api_keys: collections.abc.Iterable[yandex.cloud.priv.iam.v1.api_key_pb2.ApiKey] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["api_keys", b"api_keys", "next_page_token", b"next_page_token"]) -> None: ...

global___ListApiKeysResponse = ListApiKeysResponse

@typing.final
class CreateApiKeyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    API_KEY_ID_FIELD_NUMBER: builtins.int
    SERVICE_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    SCOPE_FIELD_NUMBER: builtins.int
    EXPIRES_AT_FIELD_NUMBER: builtins.int
    api_key_id: builtins.str
    service_account_id: builtins.str
    """use current subject identity if this not set"""
    description: builtins.str
    scope: builtins.str
    @property
    def expires_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(
        self,
        *,
        api_key_id: builtins.str = ...,
        service_account_id: builtins.str = ...,
        description: builtins.str = ...,
        scope: builtins.str = ...,
        expires_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["expires_at", b"expires_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["api_key_id", b"api_key_id", "description", b"description", "expires_at", b"expires_at", "scope", b"scope", "service_account_id", b"service_account_id"]) -> None: ...

global___CreateApiKeyRequest = CreateApiKeyRequest

@typing.final
class CreateApiKeyResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    API_KEY_FIELD_NUMBER: builtins.int
    SECRET_FIELD_NUMBER: builtins.int
    secret: builtins.str
    @property
    def api_key(self) -> yandex.cloud.priv.iam.v1.api_key_pb2.ApiKey: ...
    def __init__(
        self,
        *,
        api_key: yandex.cloud.priv.iam.v1.api_key_pb2.ApiKey | None = ...,
        secret: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["api_key", b"api_key"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["api_key", b"api_key", "secret", b"secret"]) -> None: ...

global___CreateApiKeyResponse = CreateApiKeyResponse

@typing.final
class UpdateApiKeyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    API_KEY_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    api_key_id: builtins.str
    description: builtins.str
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask: ...
    def __init__(
        self,
        *,
        api_key_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        description: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["api_key_id", b"api_key_id", "description", b"description", "update_mask", b"update_mask"]) -> None: ...

global___UpdateApiKeyRequest = UpdateApiKeyRequest

@typing.final
class UpdateApiKeyMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    API_KEY_ID_FIELD_NUMBER: builtins.int
    api_key_id: builtins.str
    def __init__(
        self,
        *,
        api_key_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["api_key_id", b"api_key_id"]) -> None: ...

global___UpdateApiKeyMetadata = UpdateApiKeyMetadata

@typing.final
class DeleteApiKeyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    API_KEY_ID_FIELD_NUMBER: builtins.int
    api_key_id: builtins.str
    def __init__(
        self,
        *,
        api_key_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["api_key_id", b"api_key_id"]) -> None: ...

global___DeleteApiKeyRequest = DeleteApiKeyRequest

@typing.final
class DeleteApiKeyMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    API_KEY_ID_FIELD_NUMBER: builtins.int
    api_key_id: builtins.str
    def __init__(
        self,
        *,
        api_key_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["api_key_id", b"api_key_id"]) -> None: ...

global___DeleteApiKeyMetadata = DeleteApiKeyMetadata

@typing.final
class ListApiKeyOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    API_KEY_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    api_key_id: builtins.str
    page_size: builtins.int
    page_token: builtins.str
    def __init__(
        self,
        *,
        api_key_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["api_key_id", b"api_key_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListApiKeyOperationsRequest = ListApiKeyOperationsRequest

@typing.final
class ListApiKeyOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.priv.operation.operation_pb2.Operation]: ...
    def __init__(
        self,
        *,
        operations: collections.abc.Iterable[yandex.cloud.priv.operation.operation_pb2.Operation] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "operations", b"operations"]) -> None: ...

global___ListApiKeyOperationsResponse = ListApiKeyOperationsResponse
