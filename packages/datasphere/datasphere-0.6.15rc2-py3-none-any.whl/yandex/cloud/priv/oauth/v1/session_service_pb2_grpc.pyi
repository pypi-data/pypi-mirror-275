"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.priv.oauth.v1.session_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class SessionServiceStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Check: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.oauth.v1.session_service_pb2.CheckSessionRequest,
        yandex.cloud.priv.oauth.v1.session_service_pb2.CheckSessionResponse,
    ]
    """Verify the identity of a subject for services, authenticated via Yandex.Cloud IdP.
    IAM-token authorization is required.

    gRPC error codes

    Unauthenticated: authorization iam_token are invalid or may have expired.
    InvalidArgument: the provided cookies are invalid or may have expired.
         Additional information can be found in details at AuthorizationRequired message - in this case user should be redirected to specified URL
    """

    CheckPassport: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.oauth.v1.session_service_pb2.CheckPassportSessionRequest,
        yandex.cloud.priv.oauth.v1.session_service_pb2.CheckPassportSessionResponse,
    ]
    """Verify the identity of a subject for services, authenticated via Yandex.ID (Yandex.Passport).
    IAM-token authorization is required.
    Usage of this API is limited and will be deprecated.

    gRPC error codes

    Unauthenticated: authorization iam_token are invalid or may have expired.
    InvalidArgument: the provided cookies are invalid or may have expired.
    """

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.oauth.v1.session_service_pb2.CreateSessionRequest,
        yandex.cloud.priv.oauth.v1.session_service_pb2.CreateSessionResponse,
    ]
    """Create per-service session

    gRPC error codes
    Unauthenticated: authorization iam_token are invalid or may have expired.
    InvalidArgument: the provided access_token is invalid or may have expired.
         Additional information can be found in details at AuthorizationRequired message - in this case user should be redirected to specified URL
    FailedPrecondition: openid scope is missed for specified access_token
    """

    Logout: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.oauth.v1.session_service_pb2.LogoutRequest,
        yandex.cloud.priv.oauth.v1.session_service_pb2.LogoutResponse,
    ]
    """Logout from parent session"""

    AcceptEula: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.oauth.v1.session_service_pb2.AcceptEulaRequest,
        yandex.cloud.priv.oauth.v1.session_service_pb2.AcceptEulaResponse,
    ]
    """Accept EULA"""

    GetOpenIDConfiguration: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.oauth.v1.session_service_pb2.GetOpenIDConfigurationRequest,
        yandex.cloud.priv.oauth.v1.session_service_pb2.GetOpenIDConfigurationResponse,
    ]
    """Get urls of openid Oauth2 endpoints"""

class SessionServiceAsyncStub:
    Check: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.oauth.v1.session_service_pb2.CheckSessionRequest,
        yandex.cloud.priv.oauth.v1.session_service_pb2.CheckSessionResponse,
    ]
    """Verify the identity of a subject for services, authenticated via Yandex.Cloud IdP.
    IAM-token authorization is required.

    gRPC error codes

    Unauthenticated: authorization iam_token are invalid or may have expired.
    InvalidArgument: the provided cookies are invalid or may have expired.
         Additional information can be found in details at AuthorizationRequired message - in this case user should be redirected to specified URL
    """

    CheckPassport: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.oauth.v1.session_service_pb2.CheckPassportSessionRequest,
        yandex.cloud.priv.oauth.v1.session_service_pb2.CheckPassportSessionResponse,
    ]
    """Verify the identity of a subject for services, authenticated via Yandex.ID (Yandex.Passport).
    IAM-token authorization is required.
    Usage of this API is limited and will be deprecated.

    gRPC error codes

    Unauthenticated: authorization iam_token are invalid or may have expired.
    InvalidArgument: the provided cookies are invalid or may have expired.
    """

    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.oauth.v1.session_service_pb2.CreateSessionRequest,
        yandex.cloud.priv.oauth.v1.session_service_pb2.CreateSessionResponse,
    ]
    """Create per-service session

    gRPC error codes
    Unauthenticated: authorization iam_token are invalid or may have expired.
    InvalidArgument: the provided access_token is invalid or may have expired.
         Additional information can be found in details at AuthorizationRequired message - in this case user should be redirected to specified URL
    FailedPrecondition: openid scope is missed for specified access_token
    """

    Logout: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.oauth.v1.session_service_pb2.LogoutRequest,
        yandex.cloud.priv.oauth.v1.session_service_pb2.LogoutResponse,
    ]
    """Logout from parent session"""

    AcceptEula: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.oauth.v1.session_service_pb2.AcceptEulaRequest,
        yandex.cloud.priv.oauth.v1.session_service_pb2.AcceptEulaResponse,
    ]
    """Accept EULA"""

    GetOpenIDConfiguration: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.oauth.v1.session_service_pb2.GetOpenIDConfigurationRequest,
        yandex.cloud.priv.oauth.v1.session_service_pb2.GetOpenIDConfigurationResponse,
    ]
    """Get urls of openid Oauth2 endpoints"""

class SessionServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Check(
        self,
        request: yandex.cloud.priv.oauth.v1.session_service_pb2.CheckSessionRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.oauth.v1.session_service_pb2.CheckSessionResponse, collections.abc.Awaitable[yandex.cloud.priv.oauth.v1.session_service_pb2.CheckSessionResponse]]:
        """Verify the identity of a subject for services, authenticated via Yandex.Cloud IdP.
        IAM-token authorization is required.

        gRPC error codes

        Unauthenticated: authorization iam_token are invalid or may have expired.
        InvalidArgument: the provided cookies are invalid or may have expired.
             Additional information can be found in details at AuthorizationRequired message - in this case user should be redirected to specified URL
        """

    @abc.abstractmethod
    def CheckPassport(
        self,
        request: yandex.cloud.priv.oauth.v1.session_service_pb2.CheckPassportSessionRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.oauth.v1.session_service_pb2.CheckPassportSessionResponse, collections.abc.Awaitable[yandex.cloud.priv.oauth.v1.session_service_pb2.CheckPassportSessionResponse]]:
        """Verify the identity of a subject for services, authenticated via Yandex.ID (Yandex.Passport).
        IAM-token authorization is required.
        Usage of this API is limited and will be deprecated.

        gRPC error codes

        Unauthenticated: authorization iam_token are invalid or may have expired.
        InvalidArgument: the provided cookies are invalid or may have expired.
        """

    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.priv.oauth.v1.session_service_pb2.CreateSessionRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.oauth.v1.session_service_pb2.CreateSessionResponse, collections.abc.Awaitable[yandex.cloud.priv.oauth.v1.session_service_pb2.CreateSessionResponse]]:
        """Create per-service session

        gRPC error codes
        Unauthenticated: authorization iam_token are invalid or may have expired.
        InvalidArgument: the provided access_token is invalid or may have expired.
             Additional information can be found in details at AuthorizationRequired message - in this case user should be redirected to specified URL
        FailedPrecondition: openid scope is missed for specified access_token
        """

    @abc.abstractmethod
    def Logout(
        self,
        request: yandex.cloud.priv.oauth.v1.session_service_pb2.LogoutRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.oauth.v1.session_service_pb2.LogoutResponse, collections.abc.Awaitable[yandex.cloud.priv.oauth.v1.session_service_pb2.LogoutResponse]]:
        """Logout from parent session"""

    @abc.abstractmethod
    def AcceptEula(
        self,
        request: yandex.cloud.priv.oauth.v1.session_service_pb2.AcceptEulaRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.oauth.v1.session_service_pb2.AcceptEulaResponse, collections.abc.Awaitable[yandex.cloud.priv.oauth.v1.session_service_pb2.AcceptEulaResponse]]:
        """Accept EULA"""

    @abc.abstractmethod
    def GetOpenIDConfiguration(
        self,
        request: yandex.cloud.priv.oauth.v1.session_service_pb2.GetOpenIDConfigurationRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.oauth.v1.session_service_pb2.GetOpenIDConfigurationResponse, collections.abc.Awaitable[yandex.cloud.priv.oauth.v1.session_service_pb2.GetOpenIDConfigurationResponse]]:
        """Get urls of openid Oauth2 endpoints"""

def add_SessionServiceServicer_to_server(servicer: SessionServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
