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
class QuotaLimit(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    QUOTA_ID_FIELD_NUMBER: builtins.int
    LIMIT_FIELD_NUMBER: builtins.int
    USAGE_FIELD_NUMBER: builtins.int
    quota_id: builtins.str
    """formatted as <domain>.<metric>.<unit>, e.g. mdb.hdd.size"""
    limit: builtins.float
    usage: builtins.float
    def __init__(
        self,
        *,
        quota_id: builtins.str = ...,
        limit: builtins.float = ...,
        usage: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["limit", b"limit", "quota_id", b"quota_id", "usage", b"usage"]) -> None: ...

global___QuotaLimit = QuotaLimit

@typing.final
class DesiredQuotaLimit(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    QUOTA_ID_FIELD_NUMBER: builtins.int
    LIMIT_FIELD_NUMBER: builtins.int
    quota_id: builtins.str
    limit: builtins.float
    def __init__(
        self,
        *,
        quota_id: builtins.str = ...,
        limit: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["limit", b"limit", "quota_id", b"quota_id"]) -> None: ...

global___DesiredQuotaLimit = DesiredQuotaLimit

@typing.final
class Resource(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_ID_FIELD_NUMBER: builtins.int
    RESOURCE_TYPE_FIELD_NUMBER: builtins.int
    resource_id: builtins.str
    resource_type: builtins.str
    def __init__(
        self,
        *,
        resource_id: builtins.str = ...,
        resource_type: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["resource_id", b"resource_id", "resource_type", b"resource_type"]) -> None: ...

global___Resource = Resource

@typing.final
class GetQuotaLimitRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_FIELD_NUMBER: builtins.int
    @property
    def resource(self) -> global___Resource: ...
    def __init__(
        self,
        *,
        resource: global___Resource | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["resource", b"resource"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["resource", b"resource"]) -> None: ...

global___GetQuotaLimitRequest = GetQuotaLimitRequest

@typing.final
class GetQuotaLimitResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_FIELD_NUMBER: builtins.int
    LIMITS_FIELD_NUMBER: builtins.int
    @property
    def resource(self) -> global___Resource: ...
    @property
    def limits(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___QuotaLimit]: ...
    def __init__(
        self,
        *,
        resource: global___Resource | None = ...,
        limits: collections.abc.Iterable[global___QuotaLimit] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["resource", b"resource"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["limits", b"limits", "resource", b"resource"]) -> None: ...

global___GetQuotaLimitResponse = GetQuotaLimitResponse

@typing.final
class GetDefaultQuotaLimitRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_TYPE_FIELD_NUMBER: builtins.int
    resource_type: builtins.str
    def __init__(
        self,
        *,
        resource_type: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["resource_type", b"resource_type"]) -> None: ...

global___GetDefaultQuotaLimitRequest = GetDefaultQuotaLimitRequest

@typing.final
class GetDefaultQuotaLimitResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_TYPE_FIELD_NUMBER: builtins.int
    LIMITS_FIELD_NUMBER: builtins.int
    resource_type: builtins.str
    @property
    def limits(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___QuotaLimit]: ...
    def __init__(
        self,
        *,
        resource_type: builtins.str = ...,
        limits: collections.abc.Iterable[global___QuotaLimit] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["limits", b"limits", "resource_type", b"resource_type"]) -> None: ...

global___GetDefaultQuotaLimitResponse = GetDefaultQuotaLimitResponse

@typing.final
class UpdateQuotaLimitRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_FIELD_NUMBER: builtins.int
    LIMIT_FIELD_NUMBER: builtins.int
    @property
    def resource(self) -> global___Resource: ...
    @property
    def limit(self) -> global___DesiredQuotaLimit: ...
    def __init__(
        self,
        *,
        resource: global___Resource | None = ...,
        limit: global___DesiredQuotaLimit | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["limit", b"limit", "resource", b"resource"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["limit", b"limit", "resource", b"resource"]) -> None: ...

global___UpdateQuotaLimitRequest = UpdateQuotaLimitRequest

@typing.final
class UpdateQuotaLimitMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_FIELD_NUMBER: builtins.int
    @property
    def resource(self) -> global___Resource: ...
    def __init__(
        self,
        *,
        resource: global___Resource | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["resource", b"resource"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["resource", b"resource"]) -> None: ...

global___UpdateQuotaLimitMetadata = UpdateQuotaLimitMetadata

@typing.final
class UpdateQuotaLimitResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_FIELD_NUMBER: builtins.int
    LIMIT_FIELD_NUMBER: builtins.int
    @property
    def resource(self) -> global___Resource: ...
    @property
    def limit(self) -> global___QuotaLimit: ...
    def __init__(
        self,
        *,
        resource: global___Resource | None = ...,
        limit: global___QuotaLimit | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["limit", b"limit", "resource", b"resource"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["limit", b"limit", "resource", b"resource"]) -> None: ...

global___UpdateQuotaLimitResponse = UpdateQuotaLimitResponse

@typing.final
class BatchUpdateQuotaLimitsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_FIELD_NUMBER: builtins.int
    LIMITS_FIELD_NUMBER: builtins.int
    @property
    def resource(self) -> global___Resource: ...
    @property
    def limits(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DesiredQuotaLimit]: ...
    def __init__(
        self,
        *,
        resource: global___Resource | None = ...,
        limits: collections.abc.Iterable[global___DesiredQuotaLimit] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["resource", b"resource"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["limits", b"limits", "resource", b"resource"]) -> None: ...

global___BatchUpdateQuotaLimitsRequest = BatchUpdateQuotaLimitsRequest

@typing.final
class BatchUpdateQuotaLimitsMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_FIELD_NUMBER: builtins.int
    @property
    def resource(self) -> global___Resource: ...
    def __init__(
        self,
        *,
        resource: global___Resource | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["resource", b"resource"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["resource", b"resource"]) -> None: ...

global___BatchUpdateQuotaLimitsMetadata = BatchUpdateQuotaLimitsMetadata

@typing.final
class BatchUpdateQuotaLimitsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_FIELD_NUMBER: builtins.int
    LIMITS_FIELD_NUMBER: builtins.int
    @property
    def resource(self) -> global___Resource: ...
    @property
    def limits(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___QuotaLimit]: ...
    def __init__(
        self,
        *,
        resource: global___Resource | None = ...,
        limits: collections.abc.Iterable[global___QuotaLimit] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["resource", b"resource"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["limits", b"limits", "resource", b"resource"]) -> None: ...

global___BatchUpdateQuotaLimitsResponse = BatchUpdateQuotaLimitsResponse
