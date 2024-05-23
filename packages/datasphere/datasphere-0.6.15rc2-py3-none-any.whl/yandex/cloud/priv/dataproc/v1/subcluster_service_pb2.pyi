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
import yandex.cloud.priv.dataproc.v1.common_pb2
import yandex.cloud.priv.dataproc.v1.subcluster_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetSubclusterRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    SUBCLUSTER_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Hadoop cluster to get subcluster from."""
    subcluster_id: builtins.str
    """Required. ID of the Hadoop subcluster to return."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        subcluster_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "subcluster_id", b"subcluster_id"]) -> None: ...

global___GetSubclusterRequest = GetSubclusterRequest

@typing.final
class GetSubclusterAtRevisionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    SUBCLUSTER_ID_FIELD_NUMBER: builtins.int
    REVISION_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Dataproc cluster to return.
    To get the cluster ID use a [ClusterService.List] request.
    """
    subcluster_id: builtins.str
    """Required. ID of the Dataproc subcluster to return."""
    revision: builtins.int
    """Cluster revision"""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        subcluster_id: builtins.str = ...,
        revision: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "revision", b"revision", "subcluster_id", b"subcluster_id"]) -> None: ...

global___GetSubclusterAtRevisionRequest = GetSubclusterAtRevisionRequest

@typing.final
class ListSubclustersRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """Required. ID of the cluster to list Hadoop subclusters of."""
    page_size: builtins.int
    """The maximum number of results per page that should be returned. If the number of available
    results is larger than `page_size`, the service returns a `next_page_token` that can be used
    to get the next page of results in subsequent ListSubclusters requests.
    Acceptable values are 0 to 1000, inclusive. Default value: 100.
    """
    page_token: builtins.str
    """Page token. Set `page_token` to the `next_page_token` returned by a previous ListSubclusters
    request to get the next page of results.
    """
    filter: builtins.str
    """String that describes a display filter."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "filter", b"filter", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListSubclustersRequest = ListSubclustersRequest

@typing.final
class ListSubclustersResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBCLUSTERS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for ListSubclusters requests,
    if the number of results is larger than `page_size` specified in the request.
    To get the next page, specify the value of `next_page_token` as a value for
    the `page_token` parameter in the next ListClusters request. Subsequent ListClusters
    requests will have their own `next_page_token` to continue paging through the results.
    """
    @property
    def subclusters(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.priv.dataproc.v1.subcluster_pb2.Subcluster]:
        """Requested list of Hadoop subclusters."""

    def __init__(
        self,
        *,
        subclusters: collections.abc.Iterable[yandex.cloud.priv.dataproc.v1.subcluster_pb2.Subcluster] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "subclusters", b"subclusters"]) -> None: ...

global___ListSubclustersResponse = ListSubclustersResponse

@typing.final
class CreateSubclusterRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    ROLE_FIELD_NUMBER: builtins.int
    RESOURCES_FIELD_NUMBER: builtins.int
    SUBNET_ID_FIELD_NUMBER: builtins.int
    HOSTS_COUNT_FIELD_NUMBER: builtins.int
    AUTOSCALING_CONFIG_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """Required. ID of the cluster to create Hadoop subcluster in."""
    name: builtins.str
    """Required. Name of the Hadoop subcluster. The name must be unique within the cluster.
    The name must be 1-63 characters long and match the regular expression `^[a-z]([-a-z0-9]{,61}[a-z0-9])?$`.
    The name can't be changed after the Hadoop subcluster is created.
    """
    role: yandex.cloud.priv.dataproc.v1.subcluster_pb2.Role.ValueType
    """Role of hosts in subcluster"""
    subnet_id: builtins.str
    hosts_count: builtins.int
    """Number of hosts in subcluster"""
    @property
    def resources(self) -> yandex.cloud.priv.dataproc.v1.common_pb2.Resources:
        """Recource configuration for hosts in subcluster"""

    @property
    def autoscaling_config(self) -> yandex.cloud.priv.dataproc.v1.subcluster_pb2.AutoscalingConfig:
        """Configuration for instance group based subclusters"""

    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        name: builtins.str = ...,
        role: yandex.cloud.priv.dataproc.v1.subcluster_pb2.Role.ValueType = ...,
        resources: yandex.cloud.priv.dataproc.v1.common_pb2.Resources | None = ...,
        subnet_id: builtins.str = ...,
        hosts_count: builtins.int = ...,
        autoscaling_config: yandex.cloud.priv.dataproc.v1.subcluster_pb2.AutoscalingConfig | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["autoscaling_config", b"autoscaling_config", "resources", b"resources"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["autoscaling_config", b"autoscaling_config", "cluster_id", b"cluster_id", "hosts_count", b"hosts_count", "name", b"name", "resources", b"resources", "role", b"role", "subnet_id", b"subnet_id"]) -> None: ...

global___CreateSubclusterRequest = CreateSubclusterRequest

@typing.final
class CreateSubclusterMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    SUBCLUSTER_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """Required. ID of the Hadoop cluster for creating subcluster."""
    subcluster_id: builtins.str
    """Required. ID of the creating Hadoop subcluster."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        subcluster_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "subcluster_id", b"subcluster_id"]) -> None: ...

global___CreateSubclusterMetadata = CreateSubclusterMetadata

@typing.final
class UpdateSubclusterRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    SUBCLUSTER_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    RESOURCES_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    HOSTS_COUNT_FIELD_NUMBER: builtins.int
    ASSIGN_PUBLIC_IP_FIELD_NUMBER: builtins.int
    DECOMMISSION_TIMEOUT_FIELD_NUMBER: builtins.int
    AUTOSCALING_CONFIG_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Hadoop cluster to update subcluster to.
    To get the Hadoop cluster ID, use a [ClusterService.List] request.
    """
    subcluster_id: builtins.str
    """Required. ID of the Hadoop subcluster."""
    name: builtins.str
    hosts_count: builtins.int
    """Number of hosts in subcluster"""
    assign_public_ip: builtins.bool
    """Assign public ip addresses for all hosts in subcluter."""
    decommission_timeout: builtins.int
    """Timeout to gracefully decommission nodes. In seconds. Default value: 0"""
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask: ...
    @property
    def resources(self) -> yandex.cloud.priv.dataproc.v1.common_pb2.Resources: ...
    @property
    def autoscaling_config(self) -> yandex.cloud.priv.dataproc.v1.subcluster_pb2.AutoscalingConfig:
        """Configuration for instance group based subclusters"""

    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        subcluster_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        resources: yandex.cloud.priv.dataproc.v1.common_pb2.Resources | None = ...,
        name: builtins.str = ...,
        hosts_count: builtins.int = ...,
        assign_public_ip: builtins.bool = ...,
        decommission_timeout: builtins.int = ...,
        autoscaling_config: yandex.cloud.priv.dataproc.v1.subcluster_pb2.AutoscalingConfig | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["autoscaling_config", b"autoscaling_config", "resources", b"resources", "update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["assign_public_ip", b"assign_public_ip", "autoscaling_config", b"autoscaling_config", "cluster_id", b"cluster_id", "decommission_timeout", b"decommission_timeout", "hosts_count", b"hosts_count", "name", b"name", "resources", b"resources", "subcluster_id", b"subcluster_id", "update_mask", b"update_mask"]) -> None: ...

global___UpdateSubclusterRequest = UpdateSubclusterRequest

@typing.final
class UpdateSubclusterMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    SUBCLUSTER_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """Required. ID of the Hadoop cluster."""
    subcluster_id: builtins.str
    """Required. ID of the Hadoop subcluster to update."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        subcluster_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "subcluster_id", b"subcluster_id"]) -> None: ...

global___UpdateSubclusterMetadata = UpdateSubclusterMetadata

@typing.final
class DeleteSubclusterRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    SUBCLUSTER_ID_FIELD_NUMBER: builtins.int
    DECOMMISSION_TIMEOUT_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Hadoop cluster to delete subcluster from.
    To get the Hadoop cluster ID, use a [ClusterService.List] request.
    """
    subcluster_id: builtins.str
    """Required. ID of the Hadoop subcluster to delete."""
    decommission_timeout: builtins.int
    """Timeout to gracefully decommission nodes. In seconds. Default value: 0"""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        subcluster_id: builtins.str = ...,
        decommission_timeout: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "decommission_timeout", b"decommission_timeout", "subcluster_id", b"subcluster_id"]) -> None: ...

global___DeleteSubclusterRequest = DeleteSubclusterRequest

@typing.final
class DeleteSubclusterMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    SUBCLUSTER_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """Required. ID of the Hadoop cluster."""
    subcluster_id: builtins.str
    """Required. ID of the deleting Hadoop subcluster."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        subcluster_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "subcluster_id", b"subcluster_id"]) -> None: ...

global___DeleteSubclusterMetadata = DeleteSubclusterMetadata
