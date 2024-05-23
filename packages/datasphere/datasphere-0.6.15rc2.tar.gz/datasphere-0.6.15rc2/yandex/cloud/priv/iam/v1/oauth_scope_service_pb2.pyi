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
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class ListOAuthScopesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    page_size: builtins.int
    page_token: builtins.str
    def __init__(
        self,
        *,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListOAuthScopesRequest = ListOAuthScopesRequest

@typing.final
class ListOAuthScopesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OAUTH_SCOPES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    @property
    def oauth_scopes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___OAuthScopeListView]: ...
    def __init__(
        self,
        *,
        oauth_scopes: collections.abc.Iterable[global___OAuthScopeListView] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "oauth_scopes", b"oauth_scopes"]) -> None: ...

global___ListOAuthScopesResponse = ListOAuthScopesResponse

@typing.final
class GetOAuthScopeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OAUTH_SCOPE_ID_FIELD_NUMBER: builtins.int
    oauth_scope_id: builtins.str
    def __init__(
        self,
        *,
        oauth_scope_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["oauth_scope_id", b"oauth_scope_id"]) -> None: ...

global___GetOAuthScopeRequest = GetOAuthScopeRequest

@typing.final
class OAuthScopeListView(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    IS_SYSTEM_FIELD_NUMBER: builtins.int
    SERVICE_FIELD_NUMBER: builtins.int
    id: builtins.str
    is_system: builtins.bool
    service: builtins.str
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        is_system: builtins.bool = ...,
        service: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["id", b"id", "is_system", b"is_system", "service", b"service"]) -> None: ...

global___OAuthScopeListView = OAuthScopeListView

@typing.final
class CreateOAuthScopeMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OAUTH_SCOPE_ID_FIELD_NUMBER: builtins.int
    oauth_scope_id: builtins.str
    def __init__(
        self,
        *,
        oauth_scope_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["oauth_scope_id", b"oauth_scope_id"]) -> None: ...

global___CreateOAuthScopeMetadata = CreateOAuthScopeMetadata

@typing.final
class UpdateOAuthScopeMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OAUTH_SCOPE_ID_FIELD_NUMBER: builtins.int
    oauth_scope_id: builtins.str
    def __init__(
        self,
        *,
        oauth_scope_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["oauth_scope_id", b"oauth_scope_id"]) -> None: ...

global___UpdateOAuthScopeMetadata = UpdateOAuthScopeMetadata

@typing.final
class DeleteOAuthScopeMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OAUTH_SCOPE_ID_FIELD_NUMBER: builtins.int
    oauth_scope_id: builtins.str
    def __init__(
        self,
        *,
        oauth_scope_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["oauth_scope_id", b"oauth_scope_id"]) -> None: ...

global___DeleteOAuthScopeMetadata = DeleteOAuthScopeMetadata

@typing.final
class CreateOAuthScopeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OAUTH_SCOPE_ID_FIELD_NUMBER: builtins.int
    IS_SYSTEM_FIELD_NUMBER: builtins.int
    SERVICE_FIELD_NUMBER: builtins.int
    PERMISSION_IDS_FIELD_NUMBER: builtins.int
    oauth_scope_id: builtins.str
    is_system: builtins.bool
    service: builtins.str
    @property
    def permission_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        oauth_scope_id: builtins.str = ...,
        is_system: builtins.bool = ...,
        service: builtins.str = ...,
        permission_ids: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["is_system", b"is_system", "oauth_scope_id", b"oauth_scope_id", "permission_ids", b"permission_ids", "service", b"service"]) -> None: ...

global___CreateOAuthScopeRequest = CreateOAuthScopeRequest

@typing.final
class UpdateOAuthScopeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OAUTH_SCOPE_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    IS_SYSTEM_FIELD_NUMBER: builtins.int
    SERVICE_FIELD_NUMBER: builtins.int
    PERMISSION_IDS_FIELD_NUMBER: builtins.int
    oauth_scope_id: builtins.str
    is_system: builtins.bool
    service: builtins.str
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask: ...
    @property
    def permission_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        oauth_scope_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        is_system: builtins.bool = ...,
        service: builtins.str = ...,
        permission_ids: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["is_system", b"is_system", "oauth_scope_id", b"oauth_scope_id", "permission_ids", b"permission_ids", "service", b"service", "update_mask", b"update_mask"]) -> None: ...

global___UpdateOAuthScopeRequest = UpdateOAuthScopeRequest

@typing.final
class DeleteOAuthScopeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OAUTH_SCOPE_ID_FIELD_NUMBER: builtins.int
    oauth_scope_id: builtins.str
    def __init__(
        self,
        *,
        oauth_scope_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["oauth_scope_id", b"oauth_scope_id"]) -> None: ...

global___DeleteOAuthScopeRequest = DeleteOAuthScopeRequest
