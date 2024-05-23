"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.priv.iam.v1.oauth_scope_pb2
import yandex.cloud.priv.iam.v1.oauth_scope_service_pb2
import yandex.cloud.priv.operation.operation_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class OAuthScopeServiceStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.oauth_scope_service_pb2.GetOAuthScopeRequest,
        yandex.cloud.priv.iam.v1.oauth_scope_pb2.OAuthScope,
    ]

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.oauth_scope_service_pb2.ListOAuthScopesRequest,
        yandex.cloud.priv.iam.v1.oauth_scope_service_pb2.ListOAuthScopesResponse,
    ]

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.oauth_scope_service_pb2.CreateOAuthScopeRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.oauth_scope_service_pb2.UpdateOAuthScopeRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.oauth_scope_service_pb2.DeleteOAuthScopeRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

class OAuthScopeServiceAsyncStub:
    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.oauth_scope_service_pb2.GetOAuthScopeRequest,
        yandex.cloud.priv.iam.v1.oauth_scope_pb2.OAuthScope,
    ]

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.oauth_scope_service_pb2.ListOAuthScopesRequest,
        yandex.cloud.priv.iam.v1.oauth_scope_service_pb2.ListOAuthScopesResponse,
    ]

    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.oauth_scope_service_pb2.CreateOAuthScopeRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

    Update: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.oauth_scope_service_pb2.UpdateOAuthScopeRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.oauth_scope_service_pb2.DeleteOAuthScopeRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

class OAuthScopeServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.priv.iam.v1.oauth_scope_service_pb2.GetOAuthScopeRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.iam.v1.oauth_scope_pb2.OAuthScope, collections.abc.Awaitable[yandex.cloud.priv.iam.v1.oauth_scope_pb2.OAuthScope]]: ...

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.priv.iam.v1.oauth_scope_service_pb2.ListOAuthScopesRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.iam.v1.oauth_scope_service_pb2.ListOAuthScopesResponse, collections.abc.Awaitable[yandex.cloud.priv.iam.v1.oauth_scope_service_pb2.ListOAuthScopesResponse]]: ...

    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.priv.iam.v1.oauth_scope_service_pb2.CreateOAuthScopeRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.priv.operation.operation_pb2.Operation]]: ...

    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.priv.iam.v1.oauth_scope_service_pb2.UpdateOAuthScopeRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.priv.operation.operation_pb2.Operation]]: ...

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.priv.iam.v1.oauth_scope_service_pb2.DeleteOAuthScopeRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.priv.operation.operation_pb2.Operation]]: ...

def add_OAuthScopeServiceServicer_to_server(servicer: OAuthScopeServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
