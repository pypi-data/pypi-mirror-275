"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetUserMetadataRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ORG_ID_FIELD_NUMBER: builtins.int
    USER_ID_FIELD_NUMBER: builtins.int
    org_id: builtins.str
    user_id: builtins.str
    def __init__(
        self,
        *,
        org_id: builtins.str = ...,
        user_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["org_id", b"org_id", "user_id", b"user_id"]) -> None: ...

global___GetUserMetadataRequest = GetUserMetadataRequest

@typing.final
class GetUserMetadataResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    METADATA_FIELD_NUMBER: builtins.int
    metadata: builtins.str
    def __init__(
        self,
        *,
        metadata: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["metadata", b"metadata"]) -> None: ...

global___GetUserMetadataResponse = GetUserMetadataResponse

@typing.final
class SetUserMetadataRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ORG_ID_FIELD_NUMBER: builtins.int
    USER_ID_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    org_id: builtins.str
    user_id: builtins.str
    metadata: builtins.str
    def __init__(
        self,
        *,
        org_id: builtins.str = ...,
        user_id: builtins.str = ...,
        metadata: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["metadata", b"metadata", "org_id", b"org_id", "user_id", b"user_id"]) -> None: ...

global___SetUserMetadataRequest = SetUserMetadataRequest

@typing.final
class SetUserMetadataResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STATUS_FIELD_NUMBER: builtins.int
    status: builtins.str
    def __init__(
        self,
        *,
        status: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["status", b"status"]) -> None: ...

global___SetUserMetadataResponse = SetUserMetadataResponse

@typing.final
class GetPassportUserRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBJECT_ID_FIELD_NUMBER: builtins.int
    subject_id: builtins.str
    def __init__(
        self,
        *,
        subject_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["subject_id", b"subject_id"]) -> None: ...

global___GetPassportUserRequest = GetPassportUserRequest

@typing.final
class GetPassportUserResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PASSPORT_UID_FIELD_NUMBER: builtins.int
    passport_uid: builtins.str
    def __init__(
        self,
        *,
        passport_uid: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["passport_uid", b"passport_uid"]) -> None: ...

global___GetPassportUserResponse = GetPassportUserResponse

@typing.final
class ListUsersRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLOUD_ID_FIELD_NUMBER: builtins.int
    cloud_id: builtins.str
    def __init__(
        self,
        *,
        cloud_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cloud_id", b"cloud_id"]) -> None: ...

global___ListUsersRequest = ListUsersRequest

@typing.final
class ListUsersResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class User(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        ID_FIELD_NUMBER: builtins.int
        LOGIN_FIELD_NUMBER: builtins.int
        FIRST_NAME_FIELD_NUMBER: builtins.int
        LAST_NAME_FIELD_NUMBER: builtins.int
        AVATAR_FIELD_NUMBER: builtins.int
        id: builtins.str
        login: builtins.str
        first_name: builtins.str
        last_name: builtins.str
        avatar: builtins.str
        def __init__(
            self,
            *,
            id: builtins.str = ...,
            login: builtins.str = ...,
            first_name: builtins.str = ...,
            last_name: builtins.str = ...,
            avatar: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["avatar", b"avatar", "first_name", b"first_name", "id", b"id", "last_name", b"last_name", "login", b"login"]) -> None: ...

    USERS_FIELD_NUMBER: builtins.int
    @property
    def users(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ListUsersResponse.User]: ...
    def __init__(
        self,
        *,
        users: collections.abc.Iterable[global___ListUsersResponse.User] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["users", b"users"]) -> None: ...

global___ListUsersResponse = ListUsersResponse

@typing.final
class GetCurrentSubjectResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    CLOUD_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    SUBJECT_TYPE_FIELD_NUMBER: builtins.int
    LOGIN_FIELD_NUMBER: builtins.int
    EMAIL_FIELD_NUMBER: builtins.int
    REFERENCE_FIELD_NUMBER: builtins.int
    DELETED_FIELD_NUMBER: builtins.int
    id: builtins.str
    cloud_id: builtins.str
    subject_type: builtins.str
    login: builtins.str
    email: builtins.str
    reference: builtins.str
    deleted: builtins.int
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        cloud_id: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        subject_type: builtins.str = ...,
        login: builtins.str = ...,
        email: builtins.str = ...,
        reference: builtins.str = ...,
        deleted: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cloud_id", b"cloud_id", "created_at", b"created_at", "deleted", b"deleted", "email", b"email", "id", b"id", "login", b"login", "reference", b"reference", "subject_type", b"subject_type"]) -> None: ...

global___GetCurrentSubjectResponse = GetCurrentSubjectResponse
