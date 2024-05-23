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
import yandex.cloud.priv.datasphere.v2.data_proc_template_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetDataProcTemplateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_PROC_TEMPLATE_ID_FIELD_NUMBER: builtins.int
    data_proc_template_id: builtins.str
    def __init__(
        self,
        *,
        data_proc_template_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["data_proc_template_id", b"data_proc_template_id"]) -> None: ...

global___GetDataProcTemplateRequest = GetDataProcTemplateRequest

@typing.final
class CreateDataProcTemplateRequest(google.protobuf.message.Message):
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
    CLUSTER_SPEC_NAME_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    name: builtins.str
    description: builtins.str
    cluster_spec_name: builtins.str
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        cluster_spec_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_spec_name", b"cluster_spec_name", "description", b"description", "labels", b"labels", "name", b"name", "project_id", b"project_id"]) -> None: ...

global___CreateDataProcTemplateRequest = CreateDataProcTemplateRequest

@typing.final
class CreateDataProcTemplateMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_PROC_TEMPLATE_ID_FIELD_NUMBER: builtins.int
    data_proc_template_id: builtins.str
    def __init__(
        self,
        *,
        data_proc_template_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["data_proc_template_id", b"data_proc_template_id"]) -> None: ...

global___CreateDataProcTemplateMetadata = CreateDataProcTemplateMetadata

@typing.final
class UpdateDataProcTemplateRequest(google.protobuf.message.Message):
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

    DATA_PROC_TEMPLATE_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    CLUSTER_SPEC_NAME_FIELD_NUMBER: builtins.int
    data_proc_template_id: builtins.str
    name: builtins.str
    description: builtins.str
    cluster_spec_name: builtins.str
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask: ...
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    def __init__(
        self,
        *,
        data_proc_template_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        cluster_spec_name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cluster_spec_name", b"cluster_spec_name", "data_proc_template_id", b"data_proc_template_id", "description", b"description", "labels", b"labels", "name", b"name", "update_mask", b"update_mask"]) -> None: ...

global___UpdateDataProcTemplateRequest = UpdateDataProcTemplateRequest

@typing.final
class UpdateDataProcTemplateMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_PROC_TEMPLATE_ID_FIELD_NUMBER: builtins.int
    data_proc_template_id: builtins.str
    def __init__(
        self,
        *,
        data_proc_template_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["data_proc_template_id", b"data_proc_template_id"]) -> None: ...

global___UpdateDataProcTemplateMetadata = UpdateDataProcTemplateMetadata

@typing.final
class DeleteDataProcTemplateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_PROC_TEMPLATE_ID_FIELD_NUMBER: builtins.int
    data_proc_template_id: builtins.str
    def __init__(
        self,
        *,
        data_proc_template_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["data_proc_template_id", b"data_proc_template_id"]) -> None: ...

global___DeleteDataProcTemplateRequest = DeleteDataProcTemplateRequest

@typing.final
class DeleteDataProcTemplateMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_PROC_TEMPLATE_ID_FIELD_NUMBER: builtins.int
    data_proc_template_id: builtins.str
    def __init__(
        self,
        *,
        data_proc_template_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["data_proc_template_id", b"data_proc_template_id"]) -> None: ...

global___DeleteDataProcTemplateMetadata = DeleteDataProcTemplateMetadata

@typing.final
class ActivateDataProcTemplateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_PROC_TEMPLATE_ID_FIELD_NUMBER: builtins.int
    PROJECT_ID_FIELD_NUMBER: builtins.int
    data_proc_template_id: builtins.str
    project_id: builtins.str
    def __init__(
        self,
        *,
        data_proc_template_id: builtins.str = ...,
        project_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["data_proc_template_id", b"data_proc_template_id", "project_id", b"project_id"]) -> None: ...

global___ActivateDataProcTemplateRequest = ActivateDataProcTemplateRequest

@typing.final
class DeactivateDataProcTemplateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_PROC_TEMPLATE_ID_FIELD_NUMBER: builtins.int
    PROJECT_ID_FIELD_NUMBER: builtins.int
    data_proc_template_id: builtins.str
    project_id: builtins.str
    def __init__(
        self,
        *,
        data_proc_template_id: builtins.str = ...,
        project_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["data_proc_template_id", b"data_proc_template_id", "project_id", b"project_id"]) -> None: ...

global___DeactivateDataProcTemplateRequest = DeactivateDataProcTemplateRequest

@typing.final
class GetDataProcTemplateActivationStatusRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_PROC_TEMPLATE_ID_FIELD_NUMBER: builtins.int
    PROJECT_ID_FIELD_NUMBER: builtins.int
    data_proc_template_id: builtins.str
    project_id: builtins.str
    def __init__(
        self,
        *,
        data_proc_template_id: builtins.str = ...,
        project_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["data_proc_template_id", b"data_proc_template_id", "project_id", b"project_id"]) -> None: ...

global___GetDataProcTemplateActivationStatusRequest = GetDataProcTemplateActivationStatusRequest

@typing.final
class GetDataProcTemplateActivationStatusResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_PROC_TEMPLATE_STATUS_FIELD_NUMBER: builtins.int
    @property
    def data_proc_template_status(self) -> yandex.cloud.priv.datasphere.v2.data_proc_template_pb2.DataProcTemplateStatus: ...
    def __init__(
        self,
        *,
        data_proc_template_status: yandex.cloud.priv.datasphere.v2.data_proc_template_pb2.DataProcTemplateStatus | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["data_proc_template_status", b"data_proc_template_status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["data_proc_template_status", b"data_proc_template_status"]) -> None: ...

global___GetDataProcTemplateActivationStatusResponse = GetDataProcTemplateActivationStatusResponse

@typing.final
class ListAvailableDataProcClusterSpecsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ListAvailableDataProcClusterSpecsRequest = ListAvailableDataProcClusterSpecsRequest

@typing.final
class ListAvailableDataProcClusterSpecsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_SPECS_FIELD_NUMBER: builtins.int
    @property
    def cluster_specs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.priv.datasphere.v2.data_proc_template_pb2.DataProcClusterSpec]: ...
    def __init__(
        self,
        *,
        cluster_specs: collections.abc.Iterable[yandex.cloud.priv.datasphere.v2.data_proc_template_pb2.DataProcClusterSpec] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_specs", b"cluster_specs"]) -> None: ...

global___ListAvailableDataProcClusterSpecsResponse = ListAvailableDataProcClusterSpecsResponse

@typing.final
class ListDataProcClustersRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_ID_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["project_id", b"project_id"]) -> None: ...

global___ListDataProcClustersRequest = ListDataProcClustersRequest

@typing.final
class ListDataProcClustersResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTERS_FIELD_NUMBER: builtins.int
    @property
    def clusters(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.priv.datasphere.v2.data_proc_template_pb2.DataProcCluster]: ...
    def __init__(
        self,
        *,
        clusters: collections.abc.Iterable[yandex.cloud.priv.datasphere.v2.data_proc_template_pb2.DataProcCluster] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["clusters", b"clusters"]) -> None: ...

global___ListDataProcClustersResponse = ListDataProcClustersResponse
