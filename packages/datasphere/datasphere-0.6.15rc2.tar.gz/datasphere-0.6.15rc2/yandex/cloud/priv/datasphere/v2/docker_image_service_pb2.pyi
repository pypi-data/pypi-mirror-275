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
import yandex.cloud.priv.datasphere.v2.docker_image_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class BuildDockerRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

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

    PROJECT_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    BUILD_PATH_FIELD_NUMBER: builtins.int
    REPOSITORY_FIELD_NUMBER: builtins.int
    TAG_FIELD_NUMBER: builtins.int
    TEMPLATE_NAME_FIELD_NUMBER: builtins.int
    CODE_FIELD_NUMBER: builtins.int
    AUTH_CREDENTIALS_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    name: builtins.str
    description: builtins.str
    build_path: builtins.str
    repository: builtins.str
    tag: builtins.str
    template_name: builtins.str
    code: builtins.str
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    @property
    def auth_credentials(self) -> global___BuildDockerCredentials: ...
    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        build_path: builtins.str = ...,
        repository: builtins.str = ...,
        tag: builtins.str = ...,
        template_name: builtins.str = ...,
        code: builtins.str = ...,
        auth_credentials: global___BuildDockerCredentials | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["auth_credentials", b"auth_credentials"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["auth_credentials", b"auth_credentials", "build_path", b"build_path", "code", b"code", "description", b"description", "labels", b"labels", "name", b"name", "project_id", b"project_id", "repository", b"repository", "tag", b"tag", "template_name", b"template_name"]) -> None: ...

global___BuildDockerRequest = BuildDockerRequest

@typing.final
class BuildDockerCredentials(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USERNAME_FIELD_NUMBER: builtins.int
    PASSWORD_SECRET_ID_FIELD_NUMBER: builtins.int
    username: builtins.str
    password_secret_id: builtins.str
    def __init__(
        self,
        *,
        username: builtins.str = ...,
        password_secret_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["password_secret_id", b"password_secret_id", "username", b"username"]) -> None: ...

global___BuildDockerCredentials = BuildDockerCredentials

@typing.final
class BuildDockerResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DOCKER_ID_FIELD_NUMBER: builtins.int
    docker_id: builtins.str
    def __init__(
        self,
        *,
        docker_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["docker_id", b"docker_id"]) -> None: ...

global___BuildDockerResponse = BuildDockerResponse

@typing.final
class BuildDockerLogsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DOCKER_ID_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    docker_id: builtins.str
    page_token: builtins.str
    def __init__(
        self,
        *,
        docker_id: builtins.str = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["docker_id", b"docker_id", "page_token", b"page_token"]) -> None: ...

global___BuildDockerLogsRequest = BuildDockerLogsRequest

@typing.final
class BuildDockerLog(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOG_FIELD_NUMBER: builtins.int
    log: builtins.str
    def __init__(
        self,
        *,
        log: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["log", b"log"]) -> None: ...

global___BuildDockerLog = BuildDockerLog

@typing.final
class BuildDockerLogsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOGS_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    page_token: builtins.str
    @property
    def logs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___BuildDockerLog]: ...
    def __init__(
        self,
        *,
        logs: collections.abc.Iterable[global___BuildDockerLog] | None = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["logs", b"logs", "page_token", b"page_token"]) -> None: ...

global___BuildDockerLogsResponse = BuildDockerLogsResponse

@typing.final
class CreateDockerRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

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

    PROJECT_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    BUILD_PATH_FIELD_NUMBER: builtins.int
    REPOSITORY_FIELD_NUMBER: builtins.int
    TAG_FIELD_NUMBER: builtins.int
    TEMPLATE_NAME_FIELD_NUMBER: builtins.int
    CODE_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    name: builtins.str
    description: builtins.str
    build_path: builtins.str
    repository: builtins.str
    tag: builtins.str
    template_name: builtins.str
    code: builtins.str
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        build_path: builtins.str = ...,
        repository: builtins.str = ...,
        tag: builtins.str = ...,
        template_name: builtins.str = ...,
        code: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["build_path", b"build_path", "code", b"code", "description", b"description", "labels", b"labels", "name", b"name", "project_id", b"project_id", "repository", b"repository", "tag", b"tag", "template_name", b"template_name"]) -> None: ...

global___CreateDockerRequest = CreateDockerRequest

@typing.final
class UpdateDockerRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

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

    DOCKER_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    BUILD_PATH_FIELD_NUMBER: builtins.int
    REPOSITORY_FIELD_NUMBER: builtins.int
    TAG_FIELD_NUMBER: builtins.int
    TEMPLATE_NAME_FIELD_NUMBER: builtins.int
    CODE_FIELD_NUMBER: builtins.int
    DATA_CAPSULE_ID_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    docker_id: builtins.str
    name: builtins.str
    description: builtins.str
    build_path: builtins.str
    repository: builtins.str
    tag: builtins.str
    template_name: builtins.str
    code: builtins.str
    data_capsule_id: builtins.str
    status: yandex.cloud.priv.datasphere.v2.docker_image_pb2.DockerImage.BuildStatus.ValueType
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask: ...
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    def __init__(
        self,
        *,
        docker_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        build_path: builtins.str = ...,
        repository: builtins.str = ...,
        tag: builtins.str = ...,
        template_name: builtins.str = ...,
        code: builtins.str = ...,
        data_capsule_id: builtins.str = ...,
        status: yandex.cloud.priv.datasphere.v2.docker_image_pb2.DockerImage.BuildStatus.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["build_path", b"build_path", "code", b"code", "data_capsule_id", b"data_capsule_id", "description", b"description", "docker_id", b"docker_id", "labels", b"labels", "name", b"name", "repository", b"repository", "status", b"status", "tag", b"tag", "template_name", b"template_name", "update_mask", b"update_mask"]) -> None: ...

global___UpdateDockerRequest = UpdateDockerRequest

@typing.final
class UpdateDockerStatusRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DOCKER_ID_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    docker_id: builtins.str
    status: yandex.cloud.priv.datasphere.v2.docker_image_pb2.DockerImage.BuildStatus.ValueType
    def __init__(
        self,
        *,
        docker_id: builtins.str = ...,
        status: yandex.cloud.priv.datasphere.v2.docker_image_pb2.DockerImage.BuildStatus.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["docker_id", b"docker_id", "status", b"status"]) -> None: ...

global___UpdateDockerStatusRequest = UpdateDockerStatusRequest

@typing.final
class GetDockerRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DOCKER_ID_FIELD_NUMBER: builtins.int
    docker_id: builtins.str
    def __init__(
        self,
        *,
        docker_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["docker_id", b"docker_id"]) -> None: ...

global___GetDockerRequest = GetDockerRequest

@typing.final
class DeleteDockerRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DOCKER_ID_FIELD_NUMBER: builtins.int
    docker_id: builtins.str
    def __init__(
        self,
        *,
        docker_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["docker_id", b"docker_id"]) -> None: ...

global___DeleteDockerRequest = DeleteDockerRequest

@typing.final
class ActivateDockerRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_ID_FIELD_NUMBER: builtins.int
    DOCKER_ID_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    docker_id: builtins.str
    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
        docker_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["docker_id", b"docker_id", "project_id", b"project_id"]) -> None: ...

global___ActivateDockerRequest = ActivateDockerRequest

@typing.final
class GetDockerActivationStatusRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DOCKER_ID_FIELD_NUMBER: builtins.int
    PROJECT_ID_FIELD_NUMBER: builtins.int
    docker_id: builtins.str
    project_id: builtins.str
    def __init__(
        self,
        *,
        docker_id: builtins.str = ...,
        project_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["docker_id", b"docker_id", "project_id", b"project_id"]) -> None: ...

global___GetDockerActivationStatusRequest = GetDockerActivationStatusRequest

@typing.final
class GetDockerActivationStatusResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class StatusActive(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        def __init__(
            self,
        ) -> None: ...

    @typing.final
    class StatusInactive(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        def __init__(
            self,
        ) -> None: ...

    STATUS_ACTIVE_FIELD_NUMBER: builtins.int
    STATUS_INACTIVE_FIELD_NUMBER: builtins.int
    @property
    def status_active(self) -> global___GetDockerActivationStatusResponse.StatusActive: ...
    @property
    def status_inactive(self) -> global___GetDockerActivationStatusResponse.StatusInactive: ...
    def __init__(
        self,
        *,
        status_active: global___GetDockerActivationStatusResponse.StatusActive | None = ...,
        status_inactive: global___GetDockerActivationStatusResponse.StatusInactive | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["status", b"status", "status_active", b"status_active", "status_inactive", b"status_inactive"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["status", b"status", "status_active", b"status_active", "status_inactive", b"status_inactive"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["status", b"status"]) -> typing.Literal["status_active", "status_inactive"] | None: ...

global___GetDockerActivationStatusResponse = GetDockerActivationStatusResponse

@typing.final
class ListProjectDockersRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_ID_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["project_id", b"project_id"]) -> None: ...

global___ListProjectDockersRequest = ListProjectDockersRequest

@typing.final
class ListProjectDockersResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IMAGES_FIELD_NUMBER: builtins.int
    @property
    def images(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.priv.datasphere.v2.docker_image_pb2.DockerImage]: ...
    def __init__(
        self,
        *,
        images: collections.abc.Iterable[yandex.cloud.priv.datasphere.v2.docker_image_pb2.DockerImage] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["images", b"images"]) -> None: ...

global___ListProjectDockersResponse = ListProjectDockersResponse

@typing.final
class ListSpaceDockersRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SPACE_ID_FIELD_NUMBER: builtins.int
    space_id: builtins.str
    def __init__(
        self,
        *,
        space_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["space_id", b"space_id"]) -> None: ...

global___ListSpaceDockersRequest = ListSpaceDockersRequest

@typing.final
class ListSpaceDockersResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IMAGES_FIELD_NUMBER: builtins.int
    @property
    def images(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.priv.datasphere.v2.docker_image_pb2.DockerImage]: ...
    def __init__(
        self,
        *,
        images: collections.abc.Iterable[yandex.cloud.priv.datasphere.v2.docker_image_pb2.DockerImage] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["images", b"images"]) -> None: ...

global___ListSpaceDockersResponse = ListSpaceDockersResponse

@typing.final
class DeleteDockerMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DOCKER_ID_FIELD_NUMBER: builtins.int
    docker_id: builtins.str
    def __init__(
        self,
        *,
        docker_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["docker_id", b"docker_id"]) -> None: ...

global___DeleteDockerMetadata = DeleteDockerMetadata

@typing.final
class CheckDockerInProjectRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_ID_FIELD_NUMBER: builtins.int
    DOCKER_ID_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    docker_id: builtins.str
    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
        docker_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["docker_id", b"docker_id", "project_id", b"project_id"]) -> None: ...

global___CheckDockerInProjectRequest = CheckDockerInProjectRequest

@typing.final
class CheckDockerInProjectResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IN_PROJECT_FIELD_NUMBER: builtins.int
    in_project: builtins.bool
    def __init__(
        self,
        *,
        in_project: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["in_project", b"in_project"]) -> None: ...

global___CheckDockerInProjectResponse = CheckDockerInProjectResponse

@typing.final
class DeactivateDockerRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_ID_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["project_id", b"project_id"]) -> None: ...

global___DeactivateDockerRequest = DeactivateDockerRequest
