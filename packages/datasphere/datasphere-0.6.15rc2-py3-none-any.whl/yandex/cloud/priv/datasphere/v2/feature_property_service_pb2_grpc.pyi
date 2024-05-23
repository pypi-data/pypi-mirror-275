"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import google.protobuf.empty_pb2
import grpc
import grpc.aio
import typing
import yandex.cloud.priv.datasphere.v2.feature_property_pb2
import yandex.cloud.priv.datasphere.v2.feature_property_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class FeaturePropertyServiceStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    ListFeatureProperties: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.datasphere.v2.feature_property_service_pb2.ListFeaturePropertiesRequest,
        yandex.cloud.priv.datasphere.v2.feature_property_service_pb2.ListFeaturePropertiesResponse,
    ]

    SetFeatureProperty: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.datasphere.v2.feature_property_service_pb2.SetFeaturePropertyRequest,
        yandex.cloud.priv.datasphere.v2.feature_property_pb2.PropertyValue,
    ]

    DeleteFeatureProperty: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.datasphere.v2.feature_property_service_pb2.DeleteFeaturePropertyRequest,
        google.protobuf.empty_pb2.Empty,
    ]

    SetBillingAccountPreset: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.datasphere.v2.feature_property_service_pb2.SetBillingAccountPresetRequest,
        google.protobuf.empty_pb2.Empty,
    ]

    DeleteBillingAccountPreset: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.datasphere.v2.feature_property_service_pb2.DeleteBillingAccountPresetRequest,
        google.protobuf.empty_pb2.Empty,
    ]

class FeaturePropertyServiceAsyncStub:
    ListFeatureProperties: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.datasphere.v2.feature_property_service_pb2.ListFeaturePropertiesRequest,
        yandex.cloud.priv.datasphere.v2.feature_property_service_pb2.ListFeaturePropertiesResponse,
    ]

    SetFeatureProperty: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.datasphere.v2.feature_property_service_pb2.SetFeaturePropertyRequest,
        yandex.cloud.priv.datasphere.v2.feature_property_pb2.PropertyValue,
    ]

    DeleteFeatureProperty: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.datasphere.v2.feature_property_service_pb2.DeleteFeaturePropertyRequest,
        google.protobuf.empty_pb2.Empty,
    ]

    SetBillingAccountPreset: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.datasphere.v2.feature_property_service_pb2.SetBillingAccountPresetRequest,
        google.protobuf.empty_pb2.Empty,
    ]

    DeleteBillingAccountPreset: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.datasphere.v2.feature_property_service_pb2.DeleteBillingAccountPresetRequest,
        google.protobuf.empty_pb2.Empty,
    ]

class FeaturePropertyServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def ListFeatureProperties(
        self,
        request: yandex.cloud.priv.datasphere.v2.feature_property_service_pb2.ListFeaturePropertiesRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.datasphere.v2.feature_property_service_pb2.ListFeaturePropertiesResponse, collections.abc.Awaitable[yandex.cloud.priv.datasphere.v2.feature_property_service_pb2.ListFeaturePropertiesResponse]]: ...

    @abc.abstractmethod
    def SetFeatureProperty(
        self,
        request: yandex.cloud.priv.datasphere.v2.feature_property_service_pb2.SetFeaturePropertyRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.datasphere.v2.feature_property_pb2.PropertyValue, collections.abc.Awaitable[yandex.cloud.priv.datasphere.v2.feature_property_pb2.PropertyValue]]: ...

    @abc.abstractmethod
    def DeleteFeatureProperty(
        self,
        request: yandex.cloud.priv.datasphere.v2.feature_property_service_pb2.DeleteFeaturePropertyRequest,
        context: _ServicerContext,
    ) -> typing.Union[google.protobuf.empty_pb2.Empty, collections.abc.Awaitable[google.protobuf.empty_pb2.Empty]]: ...

    @abc.abstractmethod
    def SetBillingAccountPreset(
        self,
        request: yandex.cloud.priv.datasphere.v2.feature_property_service_pb2.SetBillingAccountPresetRequest,
        context: _ServicerContext,
    ) -> typing.Union[google.protobuf.empty_pb2.Empty, collections.abc.Awaitable[google.protobuf.empty_pb2.Empty]]: ...

    @abc.abstractmethod
    def DeleteBillingAccountPreset(
        self,
        request: yandex.cloud.priv.datasphere.v2.feature_property_service_pb2.DeleteBillingAccountPresetRequest,
        context: _ServicerContext,
    ) -> typing.Union[google.protobuf.empty_pb2.Empty, collections.abc.Awaitable[google.protobuf.empty_pb2.Empty]]: ...

def add_FeaturePropertyServiceServicer_to_server(servicer: FeaturePropertyServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
