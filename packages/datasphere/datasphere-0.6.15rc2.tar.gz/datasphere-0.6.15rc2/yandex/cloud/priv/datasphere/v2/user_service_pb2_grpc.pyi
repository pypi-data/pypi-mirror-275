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
import yandex.cloud.priv.datasphere.v2.user_pb2
import yandex.cloud.priv.datasphere.v2.user_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class UserServiceStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    GetCurrent: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.datasphere.v2.user_service_pb2.GetCurrentUserRequest,
        yandex.cloud.priv.datasphere.v2.user_pb2.User,
    ]

    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.datasphere.v2.user_service_pb2.GetUsersRequest,
        yandex.cloud.priv.datasphere.v2.user_service_pb2.GetUsersResponse,
    ]

    SetChat: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.datasphere.v2.user_service_pb2.SetChatRequest,
        google.protobuf.empty_pb2.Empty,
    ]

    GetByChat: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.datasphere.v2.user_service_pb2.GetUserByChatRequest,
        yandex.cloud.priv.datasphere.v2.user_service_pb2.GetUserByChatResponse,
    ]

class UserServiceAsyncStub:
    GetCurrent: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.datasphere.v2.user_service_pb2.GetCurrentUserRequest,
        yandex.cloud.priv.datasphere.v2.user_pb2.User,
    ]

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.datasphere.v2.user_service_pb2.GetUsersRequest,
        yandex.cloud.priv.datasphere.v2.user_service_pb2.GetUsersResponse,
    ]

    SetChat: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.datasphere.v2.user_service_pb2.SetChatRequest,
        google.protobuf.empty_pb2.Empty,
    ]

    GetByChat: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.datasphere.v2.user_service_pb2.GetUserByChatRequest,
        yandex.cloud.priv.datasphere.v2.user_service_pb2.GetUserByChatResponse,
    ]

class UserServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetCurrent(
        self,
        request: yandex.cloud.priv.datasphere.v2.user_service_pb2.GetCurrentUserRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.datasphere.v2.user_pb2.User, collections.abc.Awaitable[yandex.cloud.priv.datasphere.v2.user_pb2.User]]: ...

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.priv.datasphere.v2.user_service_pb2.GetUsersRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.datasphere.v2.user_service_pb2.GetUsersResponse, collections.abc.Awaitable[yandex.cloud.priv.datasphere.v2.user_service_pb2.GetUsersResponse]]: ...

    @abc.abstractmethod
    def SetChat(
        self,
        request: yandex.cloud.priv.datasphere.v2.user_service_pb2.SetChatRequest,
        context: _ServicerContext,
    ) -> typing.Union[google.protobuf.empty_pb2.Empty, collections.abc.Awaitable[google.protobuf.empty_pb2.Empty]]: ...

    @abc.abstractmethod
    def GetByChat(
        self,
        request: yandex.cloud.priv.datasphere.v2.user_service_pb2.GetUserByChatRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.datasphere.v2.user_service_pb2.GetUserByChatResponse, collections.abc.Awaitable[yandex.cloud.priv.datasphere.v2.user_service_pb2.GetUserByChatResponse]]: ...

def add_UserServiceServicer_to_server(servicer: UserServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
