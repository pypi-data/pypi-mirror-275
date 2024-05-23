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
class Community(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _AccessType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _AccessTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Community._AccessType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        ACCESS_TYPE_UNSPECIFIED: Community._AccessType.ValueType  # 0
        PUBLIC: Community._AccessType.ValueType  # 1
        PRIVATE: Community._AccessType.ValueType  # 2

    class AccessType(_AccessType, metaclass=_AccessTypeEnumTypeWrapper): ...
    ACCESS_TYPE_UNSPECIFIED: Community.AccessType.ValueType  # 0
    PUBLIC: Community.AccessType.ValueType  # 1
    PRIVATE: Community.AccessType.ValueType  # 2

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Community._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: Community._Status.ValueType  # 0
        UNDEFINED: Community._Status.ValueType  # 1
        ACTIVE: Community._Status.ValueType  # 2
        BLOCKED_BY_BILLING: Community._Status.ValueType  # 3
        DELETING: Community._Status.ValueType  # 4

    class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...
    STATUS_UNSPECIFIED: Community.Status.ValueType  # 0
    UNDEFINED: Community.Status.ValueType  # 1
    ACTIVE: Community.Status.ValueType  # 2
    BLOCKED_BY_BILLING: Community.Status.ValueType  # 3
    DELETING: Community.Status.ValueType  # 4

    @typing.final
    class LabelsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    CREATED_BY_ID_FIELD_NUMBER: builtins.int
    ACCESS_TYPE_FIELD_NUMBER: builtins.int
    CHANNEL_FIELD_NUMBER: builtins.int
    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    BILLING_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    name: builtins.str
    description: builtins.str
    created_by_id: builtins.str
    access_type: global___Community.AccessType.ValueType
    organization_id: builtins.str
    status: global___Community.Status.ValueType
    billing_account_id: builtins.str
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    @property
    def channel(self) -> global___CommunicationChannel: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        created_by_id: builtins.str = ...,
        access_type: global___Community.AccessType.ValueType = ...,
        channel: global___CommunicationChannel | None = ...,
        organization_id: builtins.str = ...,
        status: global___Community.Status.ValueType = ...,
        billing_account_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["channel", b"channel", "created_at", b"created_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["access_type", b"access_type", "billing_account_id", b"billing_account_id", "channel", b"channel", "created_at", b"created_at", "created_by_id", b"created_by_id", "description", b"description", "id", b"id", "labels", b"labels", "name", b"name", "organization_id", b"organization_id", "status", b"status"]) -> None: ...

global___Community = Community

@typing.final
class CommunityAccessBinding(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _CommunityAccessBindingType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _CommunityAccessBindingTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[CommunityAccessBinding._CommunityAccessBindingType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        COMMUNITY_ACCESS_BINDING_TYPE_UNSPECIFIED: CommunityAccessBinding._CommunityAccessBindingType.ValueType  # 0
        ACCESS_ENABLED: CommunityAccessBinding._CommunityAccessBindingType.ValueType  # 1
        ACCESS_DISABLED: CommunityAccessBinding._CommunityAccessBindingType.ValueType  # 2

    class CommunityAccessBindingType(_CommunityAccessBindingType, metaclass=_CommunityAccessBindingTypeEnumTypeWrapper): ...
    COMMUNITY_ACCESS_BINDING_TYPE_UNSPECIFIED: CommunityAccessBinding.CommunityAccessBindingType.ValueType  # 0
    ACCESS_ENABLED: CommunityAccessBinding.CommunityAccessBindingType.ValueType  # 1
    ACCESS_DISABLED: CommunityAccessBinding.CommunityAccessBindingType.ValueType  # 2

    COMMUNITY_FIELD_NUMBER: builtins.int
    ACCESS_TYPE_FIELD_NUMBER: builtins.int
    access_type: global___CommunityAccessBinding.CommunityAccessBindingType.ValueType
    @property
    def community(self) -> global___Community: ...
    def __init__(
        self,
        *,
        community: global___Community | None = ...,
        access_type: global___CommunityAccessBinding.CommunityAccessBindingType.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["community", b"community"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["access_type", b"access_type", "community", b"community"]) -> None: ...

global___CommunityAccessBinding = CommunityAccessBinding

@typing.final
class CommunicationChannel(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Type:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[CommunicationChannel._Type.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        TYPE_UNSPECIFIED: CommunicationChannel._Type.ValueType  # 0
        TELEGRAM: CommunicationChannel._Type.ValueType  # 1
        SLACK: CommunicationChannel._Type.ValueType  # 2

    class Type(_Type, metaclass=_TypeEnumTypeWrapper): ...
    TYPE_UNSPECIFIED: CommunicationChannel.Type.ValueType  # 0
    TELEGRAM: CommunicationChannel.Type.ValueType  # 1
    SLACK: CommunicationChannel.Type.ValueType  # 2

    LINK_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    link: builtins.str
    type: global___CommunicationChannel.Type.ValueType
    name: builtins.str
    id: builtins.str
    def __init__(
        self,
        *,
        link: builtins.str = ...,
        type: global___CommunicationChannel.Type.ValueType = ...,
        name: builtins.str = ...,
        id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["id", b"id", "link", b"link", "name", b"name", "type", b"type"]) -> None: ...

global___CommunicationChannel = CommunicationChannel
