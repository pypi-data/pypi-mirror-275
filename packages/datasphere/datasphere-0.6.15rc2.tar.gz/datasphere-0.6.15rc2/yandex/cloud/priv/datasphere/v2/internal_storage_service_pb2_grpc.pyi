"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.priv.datasphere.v2.internal_storage_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class InternalStorageServiceStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    GenerateJobPresignedUrls: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.datasphere.v2.internal_storage_service_pb2.GenerateJobPresignedUrlsRequest,
        yandex.cloud.priv.datasphere.v2.internal_storage_service_pb2.GenerateJobPresignedUrlsResponse,
    ]

class InternalStorageServiceAsyncStub:
    GenerateJobPresignedUrls: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.datasphere.v2.internal_storage_service_pb2.GenerateJobPresignedUrlsRequest,
        yandex.cloud.priv.datasphere.v2.internal_storage_service_pb2.GenerateJobPresignedUrlsResponse,
    ]

class InternalStorageServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GenerateJobPresignedUrls(
        self,
        request: yandex.cloud.priv.datasphere.v2.internal_storage_service_pb2.GenerateJobPresignedUrlsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.datasphere.v2.internal_storage_service_pb2.GenerateJobPresignedUrlsResponse, collections.abc.Awaitable[yandex.cloud.priv.datasphere.v2.internal_storage_service_pb2.GenerateJobPresignedUrlsResponse]]: ...

def add_InternalStorageServiceServicer_to_server(servicer: InternalStorageServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
