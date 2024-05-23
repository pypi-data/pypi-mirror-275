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
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class RestrictionMeta(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _RestrictionValueType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _RestrictionValueTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[RestrictionMeta._RestrictionValueType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        RESTRICTION_VALUE_TYPE_UNSPECIFIED: RestrictionMeta._RestrictionValueType.ValueType  # 0
        BOOLEAN: RestrictionMeta._RestrictionValueType.ValueType  # 1
        LONG: RestrictionMeta._RestrictionValueType.ValueType  # 2
        STRING: RestrictionMeta._RestrictionValueType.ValueType  # 3

    class RestrictionValueType(_RestrictionValueType, metaclass=_RestrictionValueTypeEnumTypeWrapper): ...
    RESTRICTION_VALUE_TYPE_UNSPECIFIED: RestrictionMeta.RestrictionValueType.ValueType  # 0
    BOOLEAN: RestrictionMeta.RestrictionValueType.ValueType  # 1
    LONG: RestrictionMeta.RestrictionValueType.ValueType  # 2
    STRING: RestrictionMeta.RestrictionValueType.ValueType  # 3

    NAME_FIELD_NUMBER: builtins.int
    VALUE_TYPE_FIELD_NUMBER: builtins.int
    name: builtins.str
    value_type: global___RestrictionMeta.RestrictionValueType.ValueType
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        value_type: global___RestrictionMeta.RestrictionValueType.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["name", b"name", "value_type", b"value_type"]) -> None: ...

global___RestrictionMeta = RestrictionMeta

@typing.final
class Restriction(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    BOOL_VALUE_FIELD_NUMBER: builtins.int
    LONG_VALUE_FIELD_NUMBER: builtins.int
    STRING_VALUE_FIELD_NUMBER: builtins.int
    name: builtins.str
    @property
    def bool_value(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bool]: ...
    @property
    def long_value(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    @property
    def string_value(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        bool_value: collections.abc.Iterable[builtins.bool] | None = ...,
        long_value: collections.abc.Iterable[builtins.int] | None = ...,
        string_value: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["bool_value", b"bool_value", "long_value", b"long_value", "name", b"name", "string_value", b"string_value"]) -> None: ...

global___Restriction = Restriction

@typing.final
class GetRestrictionsMetaResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESTRICTIONS_META_FIELD_NUMBER: builtins.int
    @property
    def restrictions_meta(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___RestrictionMeta]: ...
    def __init__(
        self,
        *,
        restrictions_meta: collections.abc.Iterable[global___RestrictionMeta] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["restrictions_meta", b"restrictions_meta"]) -> None: ...

global___GetRestrictionsMetaResponse = GetRestrictionsMetaResponse

@typing.final
class RestrictionsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESTRICTIONS_FIELD_NUMBER: builtins.int
    @property
    def restrictions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Restriction]: ...
    def __init__(
        self,
        *,
        restrictions: collections.abc.Iterable[global___Restriction] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["restrictions", b"restrictions"]) -> None: ...

global___RestrictionsResponse = RestrictionsResponse
