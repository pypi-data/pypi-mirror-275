"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.priv.iam.v1.compute.os_login_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class OsLoginServiceStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    GetUserInfo: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.compute.os_login_service_pb2.GetUserInfoRequest,
        yandex.cloud.priv.iam.v1.compute.os_login_service_pb2.GetUserInfoResponse,
    ]
    """DEPRECATED"""

    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.compute.os_login_service_pb2.GetOsLoginRequest,
        yandex.cloud.priv.iam.v1.compute.os_login_service_pb2.GetOsLoginResponse,
    ]

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.compute.os_login_service_pb2.ListOsLoginsRequest,
        yandex.cloud.priv.iam.v1.compute.os_login_service_pb2.ListOsLoginsResponse,
    ]
    """DEPRECATED"""

    ListProfiles: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.compute.os_login_service_pb2.ListOsLoginProfilesRequest,
        yandex.cloud.priv.iam.v1.compute.os_login_service_pb2.ListOsLoginProfilesResponse,
    ]

class OsLoginServiceAsyncStub:
    GetUserInfo: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.compute.os_login_service_pb2.GetUserInfoRequest,
        yandex.cloud.priv.iam.v1.compute.os_login_service_pb2.GetUserInfoResponse,
    ]
    """DEPRECATED"""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.compute.os_login_service_pb2.GetOsLoginRequest,
        yandex.cloud.priv.iam.v1.compute.os_login_service_pb2.GetOsLoginResponse,
    ]

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.compute.os_login_service_pb2.ListOsLoginsRequest,
        yandex.cloud.priv.iam.v1.compute.os_login_service_pb2.ListOsLoginsResponse,
    ]
    """DEPRECATED"""

    ListProfiles: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.compute.os_login_service_pb2.ListOsLoginProfilesRequest,
        yandex.cloud.priv.iam.v1.compute.os_login_service_pb2.ListOsLoginProfilesResponse,
    ]

class OsLoginServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetUserInfo(
        self,
        request: yandex.cloud.priv.iam.v1.compute.os_login_service_pb2.GetUserInfoRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.iam.v1.compute.os_login_service_pb2.GetUserInfoResponse, collections.abc.Awaitable[yandex.cloud.priv.iam.v1.compute.os_login_service_pb2.GetUserInfoResponse]]:
        """DEPRECATED"""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.priv.iam.v1.compute.os_login_service_pb2.GetOsLoginRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.iam.v1.compute.os_login_service_pb2.GetOsLoginResponse, collections.abc.Awaitable[yandex.cloud.priv.iam.v1.compute.os_login_service_pb2.GetOsLoginResponse]]: ...

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.priv.iam.v1.compute.os_login_service_pb2.ListOsLoginsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.iam.v1.compute.os_login_service_pb2.ListOsLoginsResponse, collections.abc.Awaitable[yandex.cloud.priv.iam.v1.compute.os_login_service_pb2.ListOsLoginsResponse]]:
        """DEPRECATED"""

    @abc.abstractmethod
    def ListProfiles(
        self,
        request: yandex.cloud.priv.iam.v1.compute.os_login_service_pb2.ListOsLoginProfilesRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.iam.v1.compute.os_login_service_pb2.ListOsLoginProfilesResponse, collections.abc.Awaitable[yandex.cloud.priv.iam.v1.compute.os_login_service_pb2.ListOsLoginProfilesResponse]]: ...

def add_OsLoginServiceServicer_to_server(servicer: OsLoginServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
