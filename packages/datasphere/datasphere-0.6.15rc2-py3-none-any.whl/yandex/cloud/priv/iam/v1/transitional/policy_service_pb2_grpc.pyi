"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.priv.iam.v1.transitional.policy_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class PolicyServiceStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.ListPoliciesRequest,
        yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.ListPoliciesResponse,
    ]

    ListCompat: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.ListPoliciesCompatRequest,
        yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.ListPoliciesResponse,
    ]

    Set: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.SetPolicyRequest,
        yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.SetPolicyResponse,
    ]

    SetCompat: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.SetPolicyCompatRequest,
        yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.SetPolicyResponse,
    ]

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.DeletePolicyRequest,
        yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.DeletePolicyResponse,
    ]

    DeleteCompat: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.DeletePolicyCompatRequest,
        yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.DeletePolicyResponse,
    ]

class PolicyServiceAsyncStub:
    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.ListPoliciesRequest,
        yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.ListPoliciesResponse,
    ]

    ListCompat: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.ListPoliciesCompatRequest,
        yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.ListPoliciesResponse,
    ]

    Set: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.SetPolicyRequest,
        yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.SetPolicyResponse,
    ]

    SetCompat: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.SetPolicyCompatRequest,
        yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.SetPolicyResponse,
    ]

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.DeletePolicyRequest,
        yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.DeletePolicyResponse,
    ]

    DeleteCompat: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.DeletePolicyCompatRequest,
        yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.DeletePolicyResponse,
    ]

class PolicyServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.ListPoliciesRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.ListPoliciesResponse, collections.abc.Awaitable[yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.ListPoliciesResponse]]: ...

    @abc.abstractmethod
    def ListCompat(
        self,
        request: yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.ListPoliciesCompatRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.ListPoliciesResponse, collections.abc.Awaitable[yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.ListPoliciesResponse]]: ...

    @abc.abstractmethod
    def Set(
        self,
        request: yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.SetPolicyRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.SetPolicyResponse, collections.abc.Awaitable[yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.SetPolicyResponse]]: ...

    @abc.abstractmethod
    def SetCompat(
        self,
        request: yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.SetPolicyCompatRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.SetPolicyResponse, collections.abc.Awaitable[yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.SetPolicyResponse]]: ...

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.DeletePolicyRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.DeletePolicyResponse, collections.abc.Awaitable[yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.DeletePolicyResponse]]: ...

    @abc.abstractmethod
    def DeleteCompat(
        self,
        request: yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.DeletePolicyCompatRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.DeletePolicyResponse, collections.abc.Awaitable[yandex.cloud.priv.iam.v1.transitional.policy_service_pb2.DeletePolicyResponse]]: ...

def add_PolicyServiceServicer_to_server(servicer: PolicyServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
