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
class Job(google.protobuf.message.Message):
    """Dataproc job."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Job._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: Job._Status.ValueType  # 0
        PROVISIONING: Job._Status.ValueType  # 1
        """Job created in metadb and is waiting agent to acquire."""
        PENDING: Job._Status.ValueType  # 2
        """Job acquired by agent and is waiting for execution."""
        RUNNING: Job._Status.ValueType  # 3
        """Job is running."""
        ERROR: Job._Status.ValueType  # 4
        """Job failed."""
        DONE: Job._Status.ValueType  # 5
        """Job finished."""
        CANCELLED: Job._Status.ValueType  # 6
        """Job cancelled."""
        CANCELLING: Job._Status.ValueType  # 7
        """Job is waiting for cancellation."""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...
    STATUS_UNSPECIFIED: Job.Status.ValueType  # 0
    PROVISIONING: Job.Status.ValueType  # 1
    """Job created in metadb and is waiting agent to acquire."""
    PENDING: Job.Status.ValueType  # 2
    """Job acquired by agent and is waiting for execution."""
    RUNNING: Job.Status.ValueType  # 3
    """Job is running."""
    ERROR: Job.Status.ValueType  # 4
    """Job failed."""
    DONE: Job.Status.ValueType  # 5
    """Job finished."""
    CANCELLED: Job.Status.ValueType  # 6
    """Job cancelled."""
    CANCELLING: Job.Status.ValueType  # 7
    """Job is waiting for cancellation."""

    ID_FIELD_NUMBER: builtins.int
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    STARTED_AT_FIELD_NUMBER: builtins.int
    FINISHED_AT_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    CREATED_BY_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    MAPREDUCE_JOB_FIELD_NUMBER: builtins.int
    SPARK_JOB_FIELD_NUMBER: builtins.int
    PYSPARK_JOB_FIELD_NUMBER: builtins.int
    HIVE_JOB_FIELD_NUMBER: builtins.int
    APPLICATION_INFO_FIELD_NUMBER: builtins.int
    id: builtins.str
    """Required. Unique ID of the Dataproc job.
    This ID is assigned by MDB in the process of creating Dataproc job.
    """
    cluster_id: builtins.str
    """Required. Unique ID of the Dataproc cluster."""
    name: builtins.str
    """Name of the Dataproc job."""
    created_by: builtins.str
    """The id of the user who created the job"""
    status: global___Job.Status.ValueType
    """Status."""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The time when the Dataproc job was created."""

    @property
    def started_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The time when the Dataproc job was started."""

    @property
    def finished_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The time when the Dataproc job was finished."""

    @property
    def mapreduce_job(self) -> global___MapreduceJob: ...
    @property
    def spark_job(self) -> global___SparkJob: ...
    @property
    def pyspark_job(self) -> global___PysparkJob: ...
    @property
    def hive_job(self) -> global___HiveJob: ...
    @property
    def application_info(self) -> global___ApplicationInfo:
        """Attributes of YARN application."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        cluster_id: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        started_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        finished_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        name: builtins.str = ...,
        created_by: builtins.str = ...,
        status: global___Job.Status.ValueType = ...,
        mapreduce_job: global___MapreduceJob | None = ...,
        spark_job: global___SparkJob | None = ...,
        pyspark_job: global___PysparkJob | None = ...,
        hive_job: global___HiveJob | None = ...,
        application_info: global___ApplicationInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["application_info", b"application_info", "created_at", b"created_at", "finished_at", b"finished_at", "hive_job", b"hive_job", "job_spec", b"job_spec", "mapreduce_job", b"mapreduce_job", "pyspark_job", b"pyspark_job", "spark_job", b"spark_job", "started_at", b"started_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["application_info", b"application_info", "cluster_id", b"cluster_id", "created_at", b"created_at", "created_by", b"created_by", "finished_at", b"finished_at", "hive_job", b"hive_job", "id", b"id", "job_spec", b"job_spec", "mapreduce_job", b"mapreduce_job", "name", b"name", "pyspark_job", b"pyspark_job", "spark_job", b"spark_job", "started_at", b"started_at", "status", b"status"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["job_spec", b"job_spec"]) -> typing.Literal["mapreduce_job", "spark_job", "pyspark_job", "hive_job"] | None: ...

global___Job = Job

@typing.final
class ApplicationAttempt(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    AM_CONTAINER_ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of YARN application attempt"""
    am_container_id: builtins.str
    """ID of YARN Application Master container"""
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        am_container_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["am_container_id", b"am_container_id", "id", b"id"]) -> None: ...

global___ApplicationAttempt = ApplicationAttempt

@typing.final
class ApplicationInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    APPLICATION_ATTEMPTS_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of YARN application"""
    @property
    def application_attempts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ApplicationAttempt]:
        """YARN application attempts"""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        application_attempts: collections.abc.Iterable[global___ApplicationAttempt] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["application_attempts", b"application_attempts", "id", b"id"]) -> None: ...

global___ApplicationInfo = ApplicationInfo

@typing.final
class MapreduceJob(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class PropertiesEntry(google.protobuf.message.Message):
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

    ARGS_FIELD_NUMBER: builtins.int
    JAR_FILE_URIS_FIELD_NUMBER: builtins.int
    FILE_URIS_FIELD_NUMBER: builtins.int
    ARCHIVE_URIS_FIELD_NUMBER: builtins.int
    PROPERTIES_FIELD_NUMBER: builtins.int
    MAIN_JAR_FILE_URI_FIELD_NUMBER: builtins.int
    MAIN_CLASS_FIELD_NUMBER: builtins.int
    main_jar_file_uri: builtins.str
    """The HCFS URI of the jar file containing the main class."""
    main_class: builtins.str
    """The name of the driver's main class."""
    @property
    def args(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Optional arguments to the driver."""

    @property
    def jar_file_uris(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """URIs of file to run."""

    @property
    def file_uris(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """URIs of files to be copied to the working directory of Dataproc drivers and distributed tasks."""

    @property
    def archive_uris(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """URIs of archives to be extracted in the working directory of Dataproc drivers and tasks."""

    @property
    def properties(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """A mapping of property names to values, used to configure Dataproc."""

    def __init__(
        self,
        *,
        args: collections.abc.Iterable[builtins.str] | None = ...,
        jar_file_uris: collections.abc.Iterable[builtins.str] | None = ...,
        file_uris: collections.abc.Iterable[builtins.str] | None = ...,
        archive_uris: collections.abc.Iterable[builtins.str] | None = ...,
        properties: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        main_jar_file_uri: builtins.str = ...,
        main_class: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["driver", b"driver", "main_class", b"main_class", "main_jar_file_uri", b"main_jar_file_uri"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["archive_uris", b"archive_uris", "args", b"args", "driver", b"driver", "file_uris", b"file_uris", "jar_file_uris", b"jar_file_uris", "main_class", b"main_class", "main_jar_file_uri", b"main_jar_file_uri", "properties", b"properties"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["driver", b"driver"]) -> typing.Literal["main_jar_file_uri", "main_class"] | None: ...

global___MapreduceJob = MapreduceJob

@typing.final
class SparkJob(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class PropertiesEntry(google.protobuf.message.Message):
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

    ARGS_FIELD_NUMBER: builtins.int
    JAR_FILE_URIS_FIELD_NUMBER: builtins.int
    FILE_URIS_FIELD_NUMBER: builtins.int
    ARCHIVE_URIS_FIELD_NUMBER: builtins.int
    PROPERTIES_FIELD_NUMBER: builtins.int
    MAIN_JAR_FILE_URI_FIELD_NUMBER: builtins.int
    MAIN_CLASS_FIELD_NUMBER: builtins.int
    PACKAGES_FIELD_NUMBER: builtins.int
    REPOSITORIES_FIELD_NUMBER: builtins.int
    EXCLUDE_PACKAGES_FIELD_NUMBER: builtins.int
    main_jar_file_uri: builtins.str
    """The HCFS URI of the jar file containing the main class."""
    main_class: builtins.str
    """The name of the driver's main class."""
    @property
    def args(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Optional arguments to the driver."""

    @property
    def jar_file_uris(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Jar file URIs to add to the CLASSPATHs of the Dataproc driver and tasks."""

    @property
    def file_uris(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """URIs of files to be copied to the working directory of Dataproc drivers and distributed tasks."""

    @property
    def archive_uris(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """URIs of archives to be extracted in the working directory of Dataproc drivers and tasks."""

    @property
    def properties(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """A mapping of property names to values, used to configure Dataproc."""

    @property
    def packages(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of maven coordinates of jars to include on the driver and executor classpaths."""

    @property
    def repositories(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of additional remote repositories to search for the maven coordinates given with --packages."""

    @property
    def exclude_packages(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of groupId:artifactId, to exclude while resolving the dependencies provided in --packages to avoid dependency conflicts."""

    def __init__(
        self,
        *,
        args: collections.abc.Iterable[builtins.str] | None = ...,
        jar_file_uris: collections.abc.Iterable[builtins.str] | None = ...,
        file_uris: collections.abc.Iterable[builtins.str] | None = ...,
        archive_uris: collections.abc.Iterable[builtins.str] | None = ...,
        properties: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        main_jar_file_uri: builtins.str = ...,
        main_class: builtins.str = ...,
        packages: collections.abc.Iterable[builtins.str] | None = ...,
        repositories: collections.abc.Iterable[builtins.str] | None = ...,
        exclude_packages: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["archive_uris", b"archive_uris", "args", b"args", "exclude_packages", b"exclude_packages", "file_uris", b"file_uris", "jar_file_uris", b"jar_file_uris", "main_class", b"main_class", "main_jar_file_uri", b"main_jar_file_uri", "packages", b"packages", "properties", b"properties", "repositories", b"repositories"]) -> None: ...

global___SparkJob = SparkJob

@typing.final
class PysparkJob(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class PropertiesEntry(google.protobuf.message.Message):
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

    ARGS_FIELD_NUMBER: builtins.int
    JAR_FILE_URIS_FIELD_NUMBER: builtins.int
    FILE_URIS_FIELD_NUMBER: builtins.int
    ARCHIVE_URIS_FIELD_NUMBER: builtins.int
    PROPERTIES_FIELD_NUMBER: builtins.int
    MAIN_PYTHON_FILE_URI_FIELD_NUMBER: builtins.int
    PYTHON_FILE_URIS_FIELD_NUMBER: builtins.int
    PACKAGES_FIELD_NUMBER: builtins.int
    REPOSITORIES_FIELD_NUMBER: builtins.int
    EXCLUDE_PACKAGES_FIELD_NUMBER: builtins.int
    main_python_file_uri: builtins.str
    """URI of the main Python file to use as the driver. Must be a .py file."""
    @property
    def args(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Optional arguments to the driver."""

    @property
    def jar_file_uris(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Jar file URIs to add to the CLASSPATHs of the Dataproc driver and tasks."""

    @property
    def file_uris(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """URIs of files to be copied to the working directory of Dataproc drivers and distributed tasks."""

    @property
    def archive_uris(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """URIs of archives to be extracted in the working directory of Dataproc drivers and tasks."""

    @property
    def properties(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """A mapping of property names to values, used to configure Dataproc."""

    @property
    def python_file_uris(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """URIs of Python files to pass to the PySpark framework."""

    @property
    def packages(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of maven coordinates of jars to include on the driver and executor classpaths."""

    @property
    def repositories(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of additional remote repositories to search for the maven coordinates given with --packages."""

    @property
    def exclude_packages(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of groupId:artifactId, to exclude while resolving the dependencies provided in --packages to avoid dependency conflicts."""

    def __init__(
        self,
        *,
        args: collections.abc.Iterable[builtins.str] | None = ...,
        jar_file_uris: collections.abc.Iterable[builtins.str] | None = ...,
        file_uris: collections.abc.Iterable[builtins.str] | None = ...,
        archive_uris: collections.abc.Iterable[builtins.str] | None = ...,
        properties: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        main_python_file_uri: builtins.str = ...,
        python_file_uris: collections.abc.Iterable[builtins.str] | None = ...,
        packages: collections.abc.Iterable[builtins.str] | None = ...,
        repositories: collections.abc.Iterable[builtins.str] | None = ...,
        exclude_packages: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["archive_uris", b"archive_uris", "args", b"args", "exclude_packages", b"exclude_packages", "file_uris", b"file_uris", "jar_file_uris", b"jar_file_uris", "main_python_file_uri", b"main_python_file_uri", "packages", b"packages", "properties", b"properties", "python_file_uris", b"python_file_uris", "repositories", b"repositories"]) -> None: ...

global___PysparkJob = PysparkJob

@typing.final
class QueryList(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    QUERIES_FIELD_NUMBER: builtins.int
    @property
    def queries(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        queries: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["queries", b"queries"]) -> None: ...

global___QueryList = QueryList

@typing.final
class HiveJob(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class PropertiesEntry(google.protobuf.message.Message):
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

    @typing.final
    class ScriptVariablesEntry(google.protobuf.message.Message):
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

    PROPERTIES_FIELD_NUMBER: builtins.int
    CONTINUE_ON_FAILURE_FIELD_NUMBER: builtins.int
    SCRIPT_VARIABLES_FIELD_NUMBER: builtins.int
    JAR_FILE_URIS_FIELD_NUMBER: builtins.int
    QUERY_FILE_URI_FIELD_NUMBER: builtins.int
    QUERY_LIST_FIELD_NUMBER: builtins.int
    continue_on_failure: builtins.bool
    """Whether to continue executing queries if a query fails."""
    query_file_uri: builtins.str
    """URI of the script that contains Hive queries."""
    @property
    def properties(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """A mapping of property names to values, used to configure Hive."""

    @property
    def script_variables(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Mapping of query variable names to values."""

    @property
    def jar_file_uris(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Jar file URIs to add to the CLASSPATHs of the Hive driver and tasks."""

    @property
    def query_list(self) -> global___QueryList: ...
    def __init__(
        self,
        *,
        properties: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        continue_on_failure: builtins.bool = ...,
        script_variables: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        jar_file_uris: collections.abc.Iterable[builtins.str] | None = ...,
        query_file_uri: builtins.str = ...,
        query_list: global___QueryList | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["query_file_uri", b"query_file_uri", "query_list", b"query_list", "query_type", b"query_type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["continue_on_failure", b"continue_on_failure", "jar_file_uris", b"jar_file_uris", "properties", b"properties", "query_file_uri", b"query_file_uri", "query_list", b"query_list", "query_type", b"query_type", "script_variables", b"script_variables"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["query_type", b"query_type"]) -> typing.Literal["query_file_uri", "query_list"] | None: ...

global___HiveJob = HiveJob

@typing.final
class SupportJob(google.protobuf.message.Message):
    """Dataproc support job."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[SupportJob._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: SupportJob._Status.ValueType  # 0
        PROVISIONING: SupportJob._Status.ValueType  # 1
        """Job created in metadb and is waiting agent to acquire."""
        PENDING: SupportJob._Status.ValueType  # 2
        """Job acquired by agent and is waiting for execution."""
        RUNNING: SupportJob._Status.ValueType  # 3
        """Job is running."""
        ERROR: SupportJob._Status.ValueType  # 4
        """Job failed."""
        DONE: SupportJob._Status.ValueType  # 5
        """Job finished."""
        CANCELLED: SupportJob._Status.ValueType  # 6
        """Job cancelled."""
        CANCELLING: SupportJob._Status.ValueType  # 7
        """Job is waiting for cancellation."""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...
    STATUS_UNSPECIFIED: SupportJob.Status.ValueType  # 0
    PROVISIONING: SupportJob.Status.ValueType  # 1
    """Job created in metadb and is waiting agent to acquire."""
    PENDING: SupportJob.Status.ValueType  # 2
    """Job acquired by agent and is waiting for execution."""
    RUNNING: SupportJob.Status.ValueType  # 3
    """Job is running."""
    ERROR: SupportJob.Status.ValueType  # 4
    """Job failed."""
    DONE: SupportJob.Status.ValueType  # 5
    """Job finished."""
    CANCELLED: SupportJob.Status.ValueType  # 6
    """Job cancelled."""
    CANCELLING: SupportJob.Status.ValueType  # 7
    """Job is waiting for cancellation."""

    ID_FIELD_NUMBER: builtins.int
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    STARTED_AT_FIELD_NUMBER: builtins.int
    FINISHED_AT_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    CMD_FIELD_NUMBER: builtins.int
    TIMEOUT_FIELD_NUMBER: builtins.int
    CREATED_BY_FIELD_NUMBER: builtins.int
    id: builtins.str
    """Required. Unique ID of the Dataproc job.
    This ID is assigned by MDB in the process of creating Dataproc job.
    """
    cluster_id: builtins.str
    """Required. Unique ID of the Dataproc cluster."""
    status: global___SupportJob.Status.ValueType
    """Status."""
    cmd: builtins.str
    """Command."""
    timeout: builtins.int
    """Execution timeout in seconds."""
    created_by: builtins.str
    """The id of the user who created the job"""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The time when the Dataproc job was created."""

    @property
    def started_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The time when the Dataproc job was started."""

    @property
    def finished_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The time when the Dataproc job was finished."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        cluster_id: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        started_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        finished_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        status: global___SupportJob.Status.ValueType = ...,
        cmd: builtins.str = ...,
        timeout: builtins.int = ...,
        created_by: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at", "finished_at", b"finished_at", "started_at", b"started_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "cmd", b"cmd", "created_at", b"created_at", "created_by", b"created_by", "finished_at", b"finished_at", "id", b"id", "started_at", b"started_at", "status", b"status", "timeout", b"timeout"]) -> None: ...

global___SupportJob = SupportJob
