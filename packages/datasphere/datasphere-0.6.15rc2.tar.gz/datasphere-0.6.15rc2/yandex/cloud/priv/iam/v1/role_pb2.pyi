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
class Role(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    PERMISSION_IDS_FIELD_NUMBER: builtins.int
    IS_SYSTEM_FIELD_NUMBER: builtins.int
    CATEGORY_IDS_FIELD_NUMBER: builtins.int
    id: builtins.str
    description: builtins.str
    is_system: builtins.bool
    @property
    def permission_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def category_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        description: builtins.str = ...,
        permission_ids: collections.abc.Iterable[builtins.str] | None = ...,
        is_system: builtins.bool = ...,
        category_ids: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["category_ids", b"category_ids", "description", b"description", "id", b"id", "is_system", b"is_system", "permission_ids", b"permission_ids"]) -> None: ...

global___Role = Role

@typing.final
class RoleCategory(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    id: builtins.str
    name: builtins.str
    description: builtins.str
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["description", b"description", "id", b"id", "name", b"name"]) -> None: ...

global___RoleCategory = RoleCategory
