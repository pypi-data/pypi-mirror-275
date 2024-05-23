"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.priv.dataproc.v1.job_operation.operation_service_pb2
import yandex.cloud.priv.operation.operation_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class OperationServiceStub:
    """A set of methods for managing operations that are asynchronous API requests."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.dataproc.v1.job_operation.operation_service_pb2.GetOperationRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]
    """Returns the specified operation."""

class OperationServiceAsyncStub:
    """A set of methods for managing operations that are asynchronous API requests."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.dataproc.v1.job_operation.operation_service_pb2.GetOperationRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]
    """Returns the specified operation."""

class OperationServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing operations that are asynchronous API requests."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.priv.dataproc.v1.job_operation.operation_service_pb2.GetOperationRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.priv.operation.operation_pb2.Operation]]:
        """Returns the specified operation."""

def add_OperationServiceServicer_to_server(servicer: OperationServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
