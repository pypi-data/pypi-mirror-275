"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _RestrictionKind:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _RestrictionKindEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_RestrictionKind.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    RESTRICTION_KIND_UNSPECIFIED: _RestrictionKind.ValueType  # 0
    BLOCK_PERMISSIONS: _RestrictionKind.ValueType  # 1

class RestrictionKind(_RestrictionKind, metaclass=_RestrictionKindEnumTypeWrapper): ...

RESTRICTION_KIND_UNSPECIFIED: RestrictionKind.ValueType  # 0
BLOCK_PERMISSIONS: RestrictionKind.ValueType  # 1
global___RestrictionKind = RestrictionKind

@typing.final
class RestrictionType(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class BlockPermissions(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        ROLE_MASK_FIELD_NUMBER: builtins.int
        DIRECT_MASK_FIELD_NUMBER: builtins.int
        SERVICES_TO_STOP_FIELD_NUMBER: builtins.int
        RESOURCES_TO_STOP_FIELD_NUMBER: builtins.int
        STOP_DELAY_FIELD_NUMBER: builtins.int
        DELETION_INITIATION_INTERVAL_FIELD_NUMBER: builtins.int
        DELETION_DELAY_FIELD_NUMBER: builtins.int
        role_mask: builtins.str
        direct_mask: builtins.bool
        @property
        def services_to_stop(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
        @property
        def resources_to_stop(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
        @property
        def stop_delay(self) -> google.protobuf.duration_pb2.Duration: ...
        @property
        def deletion_initiation_interval(self) -> google.protobuf.duration_pb2.Duration: ...
        @property
        def deletion_delay(self) -> google.protobuf.duration_pb2.Duration: ...
        def __init__(
            self,
            *,
            role_mask: builtins.str = ...,
            direct_mask: builtins.bool = ...,
            services_to_stop: collections.abc.Iterable[builtins.str] | None = ...,
            resources_to_stop: collections.abc.Iterable[builtins.str] | None = ...,
            stop_delay: google.protobuf.duration_pb2.Duration | None = ...,
            deletion_initiation_interval: google.protobuf.duration_pb2.Duration | None = ...,
            deletion_delay: google.protobuf.duration_pb2.Duration | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["deletion_delay", b"deletion_delay", "deletion_initiation_interval", b"deletion_initiation_interval", "stop_delay", b"stop_delay"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["deletion_delay", b"deletion_delay", "deletion_initiation_interval", b"deletion_initiation_interval", "direct_mask", b"direct_mask", "resources_to_stop", b"resources_to_stop", "role_mask", b"role_mask", "services_to_stop", b"services_to_stop", "stop_delay", b"stop_delay"]) -> None: ...

    ID_FIELD_NUMBER: builtins.int
    RESTRICTION_KIND_FIELD_NUMBER: builtins.int
    BLOCK_PERMISSIONS_FIELD_NUMBER: builtins.int
    id: builtins.str
    restriction_kind: global___RestrictionKind.ValueType
    @property
    def block_permissions(self) -> global___RestrictionType.BlockPermissions: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        restriction_kind: global___RestrictionKind.ValueType = ...,
        block_permissions: global___RestrictionType.BlockPermissions | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["block_permissions", b"block_permissions", "type", b"type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["block_permissions", b"block_permissions", "id", b"id", "restriction_kind", b"restriction_kind", "type", b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["type", b"type"]) -> typing.Literal["block_permissions"] | None: ...

global___RestrictionType = RestrictionType
