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

class _FileCompressionType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _FileCompressionTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_FileCompressionType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    FILE_COMPRESSION_TYPE_UNSPECIFIED: _FileCompressionType.ValueType  # 0
    NONE: _FileCompressionType.ValueType  # 1
    ZIP: _FileCompressionType.ValueType  # 2

class FileCompressionType(_FileCompressionType, metaclass=_FileCompressionTypeEnumTypeWrapper): ...

FILE_COMPRESSION_TYPE_UNSPECIFIED: FileCompressionType.ValueType  # 0
NONE: FileCompressionType.ValueType  # 1
ZIP: FileCompressionType.ValueType  # 2
global___FileCompressionType = FileCompressionType

class _S3MountMode:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _S3MountModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_S3MountMode.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    S3_MOUNT_MODE_UNSPECIFIED: _S3MountMode.ValueType  # 0
    READ_ONLY: _S3MountMode.ValueType  # 1
    READ_WRITE: _S3MountMode.ValueType  # 2

class S3MountMode(_S3MountMode, metaclass=_S3MountModeEnumTypeWrapper): ...

S3_MOUNT_MODE_UNSPECIFIED: S3MountMode.ValueType  # 0
READ_ONLY: S3MountMode.ValueType  # 1
READ_WRITE: S3MountMode.ValueType  # 2
global___S3MountMode = S3MountMode

class _S3Backend:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _S3BackendEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_S3Backend.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    S3_BACKEND_UNSPECIFIED: _S3Backend.ValueType  # 0
    DEFAULT: _S3Backend.ValueType  # 1
    GEESEFS: _S3Backend.ValueType  # 3

class S3Backend(_S3Backend, metaclass=_S3BackendEnumTypeWrapper): ...

S3_BACKEND_UNSPECIFIED: S3Backend.ValueType  # 0
DEFAULT: S3Backend.ValueType  # 1
GEESEFS: S3Backend.ValueType  # 3
global___S3Backend = S3Backend

class _JobStatus:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _JobStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_JobStatus.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    JOB_STATUS_UNSPECIFIED: _JobStatus.ValueType  # 0
    CREATING: _JobStatus.ValueType  # 1
    EXECUTING: _JobStatus.ValueType  # 2
    UPLOADING_OUTPUT: _JobStatus.ValueType  # 3
    SUCCESS: _JobStatus.ValueType  # 4
    ERROR: _JobStatus.ValueType  # 5
    CANCELLED: _JobStatus.ValueType  # 6

class JobStatus(_JobStatus, metaclass=_JobStatusEnumTypeWrapper): ...

JOB_STATUS_UNSPECIFIED: JobStatus.ValueType  # 0
CREATING: JobStatus.ValueType  # 1
EXECUTING: JobStatus.ValueType  # 2
UPLOADING_OUTPUT: JobStatus.ValueType  # 3
SUCCESS: JobStatus.ValueType  # 4
ERROR: JobStatus.ValueType  # 5
CANCELLED: JobStatus.ValueType  # 6
global___JobStatus = JobStatus

@typing.final
class JobParameters(google.protobuf.message.Message):
    """Scripting internal API"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INPUT_FILES_FIELD_NUMBER: builtins.int
    OUTPUT_FILES_FIELD_NUMBER: builtins.int
    S3_MOUNT_IDS_FIELD_NUMBER: builtins.int
    DATASET_IDS_FIELD_NUMBER: builtins.int
    CMD_FIELD_NUMBER: builtins.int
    ENV_FIELD_NUMBER: builtins.int
    ATTACH_PROJECT_DISK_FIELD_NUMBER: builtins.int
    CLOUD_INSTANCE_TYPES_FIELD_NUMBER: builtins.int
    EXTENDED_WORKING_STORAGE_FIELD_NUMBER: builtins.int
    ARGUMENTS_FIELD_NUMBER: builtins.int
    cmd: builtins.str
    attach_project_disk: builtins.bool
    @property
    def input_files(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___File]: ...
    @property
    def output_files(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___FileDesc]: ...
    @property
    def s3_mount_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def dataset_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def env(self) -> global___Environment: ...
    @property
    def cloud_instance_types(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CloudInstanceType]: ...
    @property
    def extended_working_storage(self) -> global___ExtendedWorkingStorage: ...
    @property
    def arguments(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Argument]: ...
    def __init__(
        self,
        *,
        input_files: collections.abc.Iterable[global___File] | None = ...,
        output_files: collections.abc.Iterable[global___FileDesc] | None = ...,
        s3_mount_ids: collections.abc.Iterable[builtins.str] | None = ...,
        dataset_ids: collections.abc.Iterable[builtins.str] | None = ...,
        cmd: builtins.str = ...,
        env: global___Environment | None = ...,
        attach_project_disk: builtins.bool = ...,
        cloud_instance_types: collections.abc.Iterable[global___CloudInstanceType] | None = ...,
        extended_working_storage: global___ExtendedWorkingStorage | None = ...,
        arguments: collections.abc.Iterable[global___Argument] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["env", b"env", "extended_working_storage", b"extended_working_storage"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["arguments", b"arguments", "attach_project_disk", b"attach_project_disk", "cloud_instance_types", b"cloud_instance_types", "cmd", b"cmd", "dataset_ids", b"dataset_ids", "env", b"env", "extended_working_storage", b"extended_working_storage", "input_files", b"input_files", "output_files", b"output_files", "s3_mount_ids", b"s3_mount_ids"]) -> None: ...

global___JobParameters = JobParameters

@typing.final
class CloudInstanceType(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Currently is DS pool name (g2.8, c1.4, ...). Additional spec providers can be added here in the future."""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["name", b"name"]) -> None: ...

global___CloudInstanceType = CloudInstanceType

@typing.final
class ExtendedWorkingStorage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _StorageType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StorageTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ExtendedWorkingStorage._StorageType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STORAGE_TYPE_UNSPECIFIED: ExtendedWorkingStorage._StorageType.ValueType  # 0
        SSD: ExtendedWorkingStorage._StorageType.ValueType  # 1

    class StorageType(_StorageType, metaclass=_StorageTypeEnumTypeWrapper): ...
    STORAGE_TYPE_UNSPECIFIED: ExtendedWorkingStorage.StorageType.ValueType  # 0
    SSD: ExtendedWorkingStorage.StorageType.ValueType  # 1

    TYPE_FIELD_NUMBER: builtins.int
    SIZE_GB_FIELD_NUMBER: builtins.int
    type: global___ExtendedWorkingStorage.StorageType.ValueType
    size_gb: builtins.int
    """>= 100Gb, <=10Tb, default=100Gb"""
    def __init__(
        self,
        *,
        type: global___ExtendedWorkingStorage.StorageType.ValueType = ...,
        size_gb: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["size_gb", b"size_gb", "type", b"type"]) -> None: ...

global___ExtendedWorkingStorage = ExtendedWorkingStorage

@typing.final
class Argument(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    name: builtins.str
    value: builtins.str
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        value: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["name", b"name", "value", b"value"]) -> None: ...

global___Argument = Argument

@typing.final
class File(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DESC_FIELD_NUMBER: builtins.int
    SHA256_FIELD_NUMBER: builtins.int
    SIZE_BYTES_FIELD_NUMBER: builtins.int
    COMPRESSION_TYPE_FIELD_NUMBER: builtins.int
    sha256: builtins.str
    size_bytes: builtins.int
    compression_type: global___FileCompressionType.ValueType
    @property
    def desc(self) -> global___FileDesc: ...
    def __init__(
        self,
        *,
        desc: global___FileDesc | None = ...,
        sha256: builtins.str = ...,
        size_bytes: builtins.int = ...,
        compression_type: global___FileCompressionType.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["desc", b"desc"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["compression_type", b"compression_type", "desc", b"desc", "sha256", b"sha256", "size_bytes", b"size_bytes"]) -> None: ...

global___File = File

@typing.final
class StorageFile(google.protobuf.message.Message):
    """File with its URL in storage."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FILE_FIELD_NUMBER: builtins.int
    URL_FIELD_NUMBER: builtins.int
    url: builtins.str
    @property
    def file(self) -> global___File: ...
    def __init__(
        self,
        *,
        file: global___File | None = ...,
        url: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["file", b"file"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["file", b"file", "url", b"url"]) -> None: ...

global___StorageFile = StorageFile

@typing.final
class FileDesc(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PATH_FIELD_NUMBER: builtins.int
    VAR_FIELD_NUMBER: builtins.int
    path: builtins.str
    """Path to file can be:
    - Hard-coded, only path, which can be only relative.
    - Variable, user will specify `var` for file besides path, this `var` will be in `cmd` template.
    """
    var: builtins.str
    def __init__(
        self,
        *,
        path: builtins.str = ...,
        var: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["path", b"path", "var", b"var"]) -> None: ...

global___FileDesc = FileDesc

@typing.final
class Environment(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class VarsEntry(google.protobuf.message.Message):
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

    VARS_FIELD_NUMBER: builtins.int
    DOCKER_IMAGE_RESOURCE_ID_FIELD_NUMBER: builtins.int
    DOCKER_IMAGE_SPEC_FIELD_NUMBER: builtins.int
    SYSTEM_DOCKER_IMAGE_FIELD_NUMBER: builtins.int
    PYTHON_ENV_FIELD_NUMBER: builtins.int
    docker_image_resource_id: builtins.str
    """Image associated with DS project."""
    system_docker_image: builtins.str
    @property
    def vars(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    @property
    def docker_image_spec(self) -> global___DockerImageSpec: ...
    @property
    def python_env(self) -> global___PythonEnv:
        """If not set, executing in bash env."""

    def __init__(
        self,
        *,
        vars: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        docker_image_resource_id: builtins.str = ...,
        docker_image_spec: global___DockerImageSpec | None = ...,
        system_docker_image: builtins.str = ...,
        python_env: global___PythonEnv | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["docker_image", b"docker_image", "docker_image_resource_id", b"docker_image_resource_id", "docker_image_spec", b"docker_image_spec", "python_env", b"python_env", "system_docker_image", b"system_docker_image"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["docker_image", b"docker_image", "docker_image_resource_id", b"docker_image_resource_id", "docker_image_spec", b"docker_image_spec", "python_env", b"python_env", "system_docker_image", b"system_docker_image", "vars", b"vars"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["docker_image", b"docker_image"]) -> typing.Literal["docker_image_resource_id", "docker_image_spec", "system_docker_image"] | None: ...

global___Environment = Environment

@typing.final
class DockerImageSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IMAGE_URL_FIELD_NUMBER: builtins.int
    USERNAME_FIELD_NUMBER: builtins.int
    PASSWORD_PLAIN_TEXT_FIELD_NUMBER: builtins.int
    PASSWORD_DS_SECRET_NAME_FIELD_NUMBER: builtins.int
    image_url: builtins.str
    """Just <image:tag> for image in Docker Hub or full URL with registry."""
    username: builtins.str
    """If not set, not logging in."""
    password_plain_text: builtins.str
    password_ds_secret_name: builtins.str
    def __init__(
        self,
        *,
        image_url: builtins.str = ...,
        username: builtins.str = ...,
        password_plain_text: builtins.str = ...,
        password_ds_secret_name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["password", b"password", "password_ds_secret_name", b"password_ds_secret_name", "password_plain_text", b"password_plain_text"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["image_url", b"image_url", "password", b"password", "password_ds_secret_name", b"password_ds_secret_name", "password_plain_text", b"password_plain_text", "username", b"username"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["password", b"password"]) -> typing.Literal["password_plain_text", "password_ds_secret_name"] | None: ...

global___DockerImageSpec = DockerImageSpec

@typing.final
class PythonEnv(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONDA_YAML_FIELD_NUMBER: builtins.int
    LOCAL_MODULES_FIELD_NUMBER: builtins.int
    conda_yaml: builtins.str
    """As in lzy now, for Conda."""
    @property
    def local_modules(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___File]: ...
    def __init__(
        self,
        *,
        conda_yaml: builtins.str = ...,
        local_modules: collections.abc.Iterable[global___File] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["conda_yaml", b"conda_yaml", "local_modules", b"local_modules"]) -> None: ...

global___PythonEnv = PythonEnv

@typing.final
class S3(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    ENDPOINT_FIELD_NUMBER: builtins.int
    BUCKET_FIELD_NUMBER: builtins.int
    MOUNT_PATH_FIELD_NUMBER: builtins.int
    ACCESS_KEY_ID_FIELD_NUMBER: builtins.int
    SECRET_ACCESS_KEY_DS_SECRET_NAME_FIELD_NUMBER: builtins.int
    S3_MOUNT_MODE_FIELD_NUMBER: builtins.int
    S3_BACKEND_FIELD_NUMBER: builtins.int
    id: builtins.str
    endpoint: builtins.str
    bucket: builtins.str
    mount_path: builtins.str
    access_key_id: builtins.str
    secret_access_key_ds_secret_name: builtins.str
    s3_mount_mode: global___S3MountMode.ValueType
    s3_backend: global___S3Backend.ValueType
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        endpoint: builtins.str = ...,
        bucket: builtins.str = ...,
        mount_path: builtins.str = ...,
        access_key_id: builtins.str = ...,
        secret_access_key_ds_secret_name: builtins.str = ...,
        s3_mount_mode: global___S3MountMode.ValueType = ...,
        s3_backend: global___S3Backend.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["access_key_id", b"access_key_id", "bucket", b"bucket", "endpoint", b"endpoint", "id", b"id", "mount_path", b"mount_path", "s3_backend", b"s3_backend", "s3_mount_mode", b"s3_mount_mode", "secret_access_key_ds_secret_name", b"secret_access_key_ds_secret_name"]) -> None: ...

global___S3 = S3

@typing.final
class Job(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    STARTED_AT_FIELD_NUMBER: builtins.int
    FINISHED_AT_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    STATUS_DETAILS_FIELD_NUMBER: builtins.int
    CONFIG_FIELD_NUMBER: builtins.int
    CREATED_BY_ID_FIELD_NUMBER: builtins.int
    PROJECT_ID_FIELD_NUMBER: builtins.int
    JOB_PARAMETERS_FIELD_NUMBER: builtins.int
    DATA_EXPIRES_AT_FIELD_NUMBER: builtins.int
    DATA_CLEARED_FIELD_NUMBER: builtins.int
    OUTPUT_FILES_FIELD_NUMBER: builtins.int
    LOG_FILES_FIELD_NUMBER: builtins.int
    DIAGNOSTIC_FILES_FIELD_NUMBER: builtins.int
    DATA_SIZE_BYTES_FIELD_NUMBER: builtins.int
    ACTUAL_CLOUD_INSTANCE_TYPE_FIELD_NUMBER: builtins.int
    PARENT_JOB_ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    name: builtins.str
    description: builtins.str
    status: global___JobStatus.ValueType
    status_details: builtins.str
    config: builtins.str
    """User config file as-is."""
    created_by_id: builtins.str
    project_id: builtins.str
    data_cleared: builtins.bool
    data_size_bytes: builtins.int
    parent_job_id: builtins.str
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def started_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def finished_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def job_parameters(self) -> global___JobParameters: ...
    @property
    def data_expires_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def output_files(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___File]: ...
    @property
    def log_files(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___File]: ...
    @property
    def diagnostic_files(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___File]: ...
    @property
    def actual_cloud_instance_type(self) -> global___CloudInstanceType: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        started_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        finished_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        status: global___JobStatus.ValueType = ...,
        status_details: builtins.str = ...,
        config: builtins.str = ...,
        created_by_id: builtins.str = ...,
        project_id: builtins.str = ...,
        job_parameters: global___JobParameters | None = ...,
        data_expires_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        data_cleared: builtins.bool = ...,
        output_files: collections.abc.Iterable[global___File] | None = ...,
        log_files: collections.abc.Iterable[global___File] | None = ...,
        diagnostic_files: collections.abc.Iterable[global___File] | None = ...,
        data_size_bytes: builtins.int = ...,
        actual_cloud_instance_type: global___CloudInstanceType | None = ...,
        parent_job_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["actual_cloud_instance_type", b"actual_cloud_instance_type", "created_at", b"created_at", "data_expires_at", b"data_expires_at", "finished_at", b"finished_at", "job_parameters", b"job_parameters", "started_at", b"started_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["actual_cloud_instance_type", b"actual_cloud_instance_type", "config", b"config", "created_at", b"created_at", "created_by_id", b"created_by_id", "data_cleared", b"data_cleared", "data_expires_at", b"data_expires_at", "data_size_bytes", b"data_size_bytes", "description", b"description", "diagnostic_files", b"diagnostic_files", "finished_at", b"finished_at", "id", b"id", "job_parameters", b"job_parameters", "log_files", b"log_files", "name", b"name", "output_files", b"output_files", "parent_job_id", b"parent_job_id", "project_id", b"project_id", "started_at", b"started_at", "status", b"status", "status_details", b"status_details"]) -> None: ...

global___Job = Job

@typing.final
class JobResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RETURN_CODE_FIELD_NUMBER: builtins.int
    return_code: builtins.int
    def __init__(
        self,
        *,
        return_code: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["return_code", b"return_code"]) -> None: ...

global___JobResult = JobResult
