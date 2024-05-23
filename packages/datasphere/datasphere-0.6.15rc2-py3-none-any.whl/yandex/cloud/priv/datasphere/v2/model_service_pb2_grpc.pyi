"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.priv.datasphere.v2.model_service_pb2
import yandex.cloud.priv.operation.operation_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class ModelServiceStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.datasphere.v2.model_service_pb2.GetModelRequest,
        yandex.cloud.priv.datasphere.v2.model_service_pb2.GetModelResponse,
    ]

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.datasphere.v2.model_service_pb2.ListModelsRequest,
        yandex.cloud.priv.datasphere.v2.model_service_pb2.ListModelsResponse,
    ]

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.datasphere.v2.model_service_pb2.CreateModelRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.datasphere.v2.model_service_pb2.UpdateModelRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.datasphere.v2.model_service_pb2.DeleteModelRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

    ListPythonVariables: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.datasphere.v2.model_service_pb2.ListPythonVariablesRequest,
        yandex.cloud.priv.datasphere.v2.model_service_pb2.ListPythonVariablesResponse,
    ]

    Load: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.datasphere.v2.model_service_pb2.LoadModelRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

class ModelServiceAsyncStub:
    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.datasphere.v2.model_service_pb2.GetModelRequest,
        yandex.cloud.priv.datasphere.v2.model_service_pb2.GetModelResponse,
    ]

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.datasphere.v2.model_service_pb2.ListModelsRequest,
        yandex.cloud.priv.datasphere.v2.model_service_pb2.ListModelsResponse,
    ]

    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.datasphere.v2.model_service_pb2.CreateModelRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

    Update: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.datasphere.v2.model_service_pb2.UpdateModelRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.datasphere.v2.model_service_pb2.DeleteModelRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

    ListPythonVariables: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.datasphere.v2.model_service_pb2.ListPythonVariablesRequest,
        yandex.cloud.priv.datasphere.v2.model_service_pb2.ListPythonVariablesResponse,
    ]

    Load: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.datasphere.v2.model_service_pb2.LoadModelRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

class ModelServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.priv.datasphere.v2.model_service_pb2.GetModelRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.datasphere.v2.model_service_pb2.GetModelResponse, collections.abc.Awaitable[yandex.cloud.priv.datasphere.v2.model_service_pb2.GetModelResponse]]: ...

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.priv.datasphere.v2.model_service_pb2.ListModelsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.datasphere.v2.model_service_pb2.ListModelsResponse, collections.abc.Awaitable[yandex.cloud.priv.datasphere.v2.model_service_pb2.ListModelsResponse]]: ...

    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.priv.datasphere.v2.model_service_pb2.CreateModelRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.priv.operation.operation_pb2.Operation]]: ...

    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.priv.datasphere.v2.model_service_pb2.UpdateModelRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.priv.operation.operation_pb2.Operation]]: ...

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.priv.datasphere.v2.model_service_pb2.DeleteModelRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.priv.operation.operation_pb2.Operation]]: ...

    @abc.abstractmethod
    def ListPythonVariables(
        self,
        request: yandex.cloud.priv.datasphere.v2.model_service_pb2.ListPythonVariablesRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.datasphere.v2.model_service_pb2.ListPythonVariablesResponse, collections.abc.Awaitable[yandex.cloud.priv.datasphere.v2.model_service_pb2.ListPythonVariablesResponse]]: ...

    @abc.abstractmethod
    def Load(
        self,
        request: yandex.cloud.priv.datasphere.v2.model_service_pb2.LoadModelRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.priv.operation.operation_pb2.Operation]]: ...

def add_ModelServiceServicer_to_server(servicer: ModelServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
