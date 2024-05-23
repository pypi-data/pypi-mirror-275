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
import google.protobuf.wrappers_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Project(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Settings(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        class _CommitMode:
            ValueType = typing.NewType("ValueType", builtins.int)
            V: typing_extensions.TypeAlias = ValueType

        class _CommitModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Project.Settings._CommitMode.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            COMMIT_MODE_UNSPECIFIED: Project.Settings._CommitMode.ValueType  # 0
            STANDARD: Project.Settings._CommitMode.ValueType  # 1
            AUTO: Project.Settings._CommitMode.ValueType  # 2

        class CommitMode(_CommitMode, metaclass=_CommitModeEnumTypeWrapper): ...
        COMMIT_MODE_UNSPECIFIED: Project.Settings.CommitMode.ValueType  # 0
        STANDARD: Project.Settings.CommitMode.ValueType  # 1
        AUTO: Project.Settings.CommitMode.ValueType  # 2

        class _Ide:
            ValueType = typing.NewType("ValueType", builtins.int)
            V: typing_extensions.TypeAlias = ValueType

        class _IdeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Project.Settings._Ide.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            IDE_UNSPECIFIED: Project.Settings._Ide.ValueType  # 0
            JUPYTER_LAB: Project.Settings._Ide.ValueType  # 1
            VS_CODE: Project.Settings._Ide.ValueType  # 2

        class Ide(_Ide, metaclass=_IdeEnumTypeWrapper): ...
        IDE_UNSPECIFIED: Project.Settings.Ide.ValueType  # 0
        JUPYTER_LAB: Project.Settings.Ide.ValueType  # 1
        VS_CODE: Project.Settings.Ide.ValueType  # 2

        class _StaleExecutionTimeoutMode:
            ValueType = typing.NewType("ValueType", builtins.int)
            V: typing_extensions.TypeAlias = ValueType

        class _StaleExecutionTimeoutModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Project.Settings._StaleExecutionTimeoutMode.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            STALE_EXECUTION_TIMEOUT_MODE_UNSPECIFIED: Project.Settings._StaleExecutionTimeoutMode.ValueType  # 0
            ONE_HOUR: Project.Settings._StaleExecutionTimeoutMode.ValueType  # 1
            THREE_HOURS: Project.Settings._StaleExecutionTimeoutMode.ValueType  # 2
            NO_TIMEOUT: Project.Settings._StaleExecutionTimeoutMode.ValueType  # 3

        class StaleExecutionTimeoutMode(_StaleExecutionTimeoutMode, metaclass=_StaleExecutionTimeoutModeEnumTypeWrapper): ...
        STALE_EXECUTION_TIMEOUT_MODE_UNSPECIFIED: Project.Settings.StaleExecutionTimeoutMode.ValueType  # 0
        ONE_HOUR: Project.Settings.StaleExecutionTimeoutMode.ValueType  # 1
        THREE_HOURS: Project.Settings.StaleExecutionTimeoutMode.ValueType  # 2
        NO_TIMEOUT: Project.Settings.StaleExecutionTimeoutMode.ValueType  # 3

        class _IdeExecutionMode:
            ValueType = typing.NewType("ValueType", builtins.int)
            V: typing_extensions.TypeAlias = ValueType

        class _IdeExecutionModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Project.Settings._IdeExecutionMode.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            IDE_EXECUTION_MODE_UNSPECIFIED: Project.Settings._IdeExecutionMode.ValueType  # 0
            SERVERLESS: Project.Settings._IdeExecutionMode.ValueType  # 1
            DEDICATED: Project.Settings._IdeExecutionMode.ValueType  # 2

        class IdeExecutionMode(_IdeExecutionMode, metaclass=_IdeExecutionModeEnumTypeWrapper): ...
        IDE_EXECUTION_MODE_UNSPECIFIED: Project.Settings.IdeExecutionMode.ValueType  # 0
        SERVERLESS: Project.Settings.IdeExecutionMode.ValueType  # 1
        DEDICATED: Project.Settings.IdeExecutionMode.ValueType  # 2

        SERVICE_ACCOUNT_ID_FIELD_NUMBER: builtins.int
        SUBNET_ID_FIELD_NUMBER: builtins.int
        DATA_PROC_CLUSTER_ID_FIELD_NUMBER: builtins.int
        COMMIT_MODE_FIELD_NUMBER: builtins.int
        SECURITY_GROUP_IDS_FIELD_NUMBER: builtins.int
        IDE_FIELD_NUMBER: builtins.int
        DEFAULT_FOLDER_ID_FIELD_NUMBER: builtins.int
        STALE_EXEC_TIMEOUT_MODE_FIELD_NUMBER: builtins.int
        IDE_EXECUTION_MODE_FIELD_NUMBER: builtins.int
        service_account_id: builtins.str
        subnet_id: builtins.str
        data_proc_cluster_id: builtins.str
        commit_mode: global___Project.Settings.CommitMode.ValueType
        ide: global___Project.Settings.Ide.ValueType
        default_folder_id: builtins.str
        stale_exec_timeout_mode: global___Project.Settings.StaleExecutionTimeoutMode.ValueType
        ide_execution_mode: global___Project.Settings.IdeExecutionMode.ValueType
        @property
        def security_group_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
        def __init__(
            self,
            *,
            service_account_id: builtins.str = ...,
            subnet_id: builtins.str = ...,
            data_proc_cluster_id: builtins.str = ...,
            commit_mode: global___Project.Settings.CommitMode.ValueType = ...,
            security_group_ids: collections.abc.Iterable[builtins.str] | None = ...,
            ide: global___Project.Settings.Ide.ValueType = ...,
            default_folder_id: builtins.str = ...,
            stale_exec_timeout_mode: global___Project.Settings.StaleExecutionTimeoutMode.ValueType = ...,
            ide_execution_mode: global___Project.Settings.IdeExecutionMode.ValueType = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["commit_mode", b"commit_mode", "data_proc_cluster_id", b"data_proc_cluster_id", "default_folder_id", b"default_folder_id", "ide", b"ide", "ide_execution_mode", b"ide_execution_mode", "security_group_ids", b"security_group_ids", "service_account_id", b"service_account_id", "stale_exec_timeout_mode", b"stale_exec_timeout_mode", "subnet_id", b"subnet_id"]) -> None: ...

    @typing.final
    class Limits(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        MAX_UNITS_PER_HOUR_FIELD_NUMBER: builtins.int
        MAX_UNITS_PER_EXECUTION_FIELD_NUMBER: builtins.int
        @property
        def max_units_per_hour(self) -> google.protobuf.wrappers_pb2.Int64Value: ...
        @property
        def max_units_per_execution(self) -> google.protobuf.wrappers_pb2.Int64Value: ...
        def __init__(
            self,
            *,
            max_units_per_hour: google.protobuf.wrappers_pb2.Int64Value | None = ...,
            max_units_per_execution: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["max_units_per_execution", b"max_units_per_execution", "max_units_per_hour", b"max_units_per_hour"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["max_units_per_execution", b"max_units_per_execution", "max_units_per_hour", b"max_units_per_hour"]) -> None: ...

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
    FOLDER_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    SETTINGS_FIELD_NUMBER: builtins.int
    LIMITS_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    id: builtins.str
    folder_id: builtins.str
    name: builtins.str
    description: builtins.str
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def settings(self) -> global___Project.Settings: ...
    @property
    def limits(self) -> global___Project.Limits: ...
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        folder_id: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        settings: global___Project.Settings | None = ...,
        limits: global___Project.Limits | None = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at", "limits", b"limits", "settings", b"settings"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["created_at", b"created_at", "description", b"description", "folder_id", b"folder_id", "id", b"id", "labels", b"labels", "limits", b"limits", "name", b"name", "settings", b"settings"]) -> None: ...

global___Project = Project
