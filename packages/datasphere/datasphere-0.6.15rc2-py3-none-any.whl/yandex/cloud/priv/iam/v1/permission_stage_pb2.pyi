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
class PermissionStage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    id: builtins.str
    description: builtins.str
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        description: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["description", b"description", "id", b"id"]) -> None: ...

global___PermissionStage = PermissionStage

@typing.final
class SetAllPermissionStagesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_ID_FIELD_NUMBER: builtins.int
    resource_id: builtins.str
    def __init__(
        self,
        *,
        resource_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["resource_id", b"resource_id"]) -> None: ...

global___SetAllPermissionStagesRequest = SetAllPermissionStagesRequest

@typing.final
class SetPermissionStagesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_ID_FIELD_NUMBER: builtins.int
    PERMISSION_STAGE_IDS_FIELD_NUMBER: builtins.int
    resource_id: builtins.str
    @property
    def permission_stage_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        resource_id: builtins.str = ...,
        permission_stage_ids: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["permission_stage_ids", b"permission_stage_ids", "resource_id", b"resource_id"]) -> None: ...

global___SetPermissionStagesRequest = SetPermissionStagesRequest

@typing.final
class SetPermissionStagesMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_ID_FIELD_NUMBER: builtins.int
    resource_id: builtins.str
    def __init__(
        self,
        *,
        resource_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["resource_id", b"resource_id"]) -> None: ...

global___SetPermissionStagesMetadata = SetPermissionStagesMetadata

@typing.final
class UpdatePermissionStagesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_ID_FIELD_NUMBER: builtins.int
    ADD_PERMISSION_STAGE_IDS_FIELD_NUMBER: builtins.int
    REMOVE_PERMISSION_STAGE_IDS_FIELD_NUMBER: builtins.int
    resource_id: builtins.str
    @property
    def add_permission_stage_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def remove_permission_stage_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        resource_id: builtins.str = ...,
        add_permission_stage_ids: collections.abc.Iterable[builtins.str] | None = ...,
        remove_permission_stage_ids: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["add_permission_stage_ids", b"add_permission_stage_ids", "remove_permission_stage_ids", b"remove_permission_stage_ids", "resource_id", b"resource_id"]) -> None: ...

global___UpdatePermissionStagesRequest = UpdatePermissionStagesRequest

@typing.final
class UpdatePermissionStagesMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_ID_FIELD_NUMBER: builtins.int
    resource_id: builtins.str
    def __init__(
        self,
        *,
        resource_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["resource_id", b"resource_id"]) -> None: ...

global___UpdatePermissionStagesMetadata = UpdatePermissionStagesMetadata
