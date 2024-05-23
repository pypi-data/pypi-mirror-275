"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.priv.iam.v1.service_control_pb2
import yandex.cloud.priv.iam.v1.service_control_service_pb2
import yandex.cloud.priv.operation.operation_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class ServiceControlServiceStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.GetServiceRequest,
        yandex.cloud.priv.iam.v1.service_control_pb2.Service,
    ]

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.ListServicesRequest,
        yandex.cloud.priv.iam.v1.service_control_service_pb2.ListServicesResponse,
    ]

    Enable: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.EnableServiceRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

    EnableDefaultServices: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.EnableDefaultServicesRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

    Resume: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.ResumeServiceRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

    Pause: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.PauseServiceRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

    Disable: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.DisableServiceRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.DeleteServiceRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

    Upgrade: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.UpgradeServiceRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

    ResolveAgent: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.ResolveServiceAgentRequest,
        yandex.cloud.priv.iam.v1.service_control_pb2.ServiceAgent,
    ]

    ListSystemFolders: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.ListSystemFoldersRequest,
        yandex.cloud.priv.iam.v1.service_control_service_pb2.ListSystemFoldersResponse,
    ]

    ListSystemServiceAccounts: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.ListSystemServiceAccountsRequest,
        yandex.cloud.priv.iam.v1.service_control_service_pb2.ListSystemServiceAccountsResponse,
    ]

    DeleteSystemFolder: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.DeleteSystemFolderRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

    SetupDelegation: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.SetupDelegationRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

    RevokeDelegation: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.RevokeDelegationRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

    ListReferences: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.ListServiceReferencesRequest,
        yandex.cloud.priv.iam.v1.service_control_service_pb2.ListServiceReferencesResponse,
    ]

    UpdateReferences: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.UpdateServiceReferencesRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

    GetSettings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.GetServiceControlSettingsRequest,
        yandex.cloud.priv.iam.v1.service_control_pb2.ServiceControlSettings,
    ]

    UpdateSettings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.UpdateServiceControlSettingsRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

    EnsureEnabled: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.EnsureServicesEnabledRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

    ListOperations: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.ListServiceOperationsRequest,
        yandex.cloud.priv.iam.v1.service_control_service_pb2.ListServiceOperationsResponse,
    ]

class ServiceControlServiceAsyncStub:
    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.GetServiceRequest,
        yandex.cloud.priv.iam.v1.service_control_pb2.Service,
    ]

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.ListServicesRequest,
        yandex.cloud.priv.iam.v1.service_control_service_pb2.ListServicesResponse,
    ]

    Enable: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.EnableServiceRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

    EnableDefaultServices: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.EnableDefaultServicesRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

    Resume: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.ResumeServiceRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

    Pause: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.PauseServiceRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

    Disable: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.DisableServiceRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.DeleteServiceRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

    Upgrade: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.UpgradeServiceRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

    ResolveAgent: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.ResolveServiceAgentRequest,
        yandex.cloud.priv.iam.v1.service_control_pb2.ServiceAgent,
    ]

    ListSystemFolders: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.ListSystemFoldersRequest,
        yandex.cloud.priv.iam.v1.service_control_service_pb2.ListSystemFoldersResponse,
    ]

    ListSystemServiceAccounts: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.ListSystemServiceAccountsRequest,
        yandex.cloud.priv.iam.v1.service_control_service_pb2.ListSystemServiceAccountsResponse,
    ]

    DeleteSystemFolder: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.DeleteSystemFolderRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

    SetupDelegation: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.SetupDelegationRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

    RevokeDelegation: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.RevokeDelegationRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

    ListReferences: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.ListServiceReferencesRequest,
        yandex.cloud.priv.iam.v1.service_control_service_pb2.ListServiceReferencesResponse,
    ]

    UpdateReferences: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.UpdateServiceReferencesRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

    GetSettings: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.GetServiceControlSettingsRequest,
        yandex.cloud.priv.iam.v1.service_control_pb2.ServiceControlSettings,
    ]

    UpdateSettings: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.UpdateServiceControlSettingsRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

    EnsureEnabled: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.EnsureServicesEnabledRequest,
        yandex.cloud.priv.operation.operation_pb2.Operation,
    ]

    ListOperations: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.priv.iam.v1.service_control_service_pb2.ListServiceOperationsRequest,
        yandex.cloud.priv.iam.v1.service_control_service_pb2.ListServiceOperationsResponse,
    ]

class ServiceControlServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.priv.iam.v1.service_control_service_pb2.GetServiceRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.iam.v1.service_control_pb2.Service, collections.abc.Awaitable[yandex.cloud.priv.iam.v1.service_control_pb2.Service]]: ...

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.priv.iam.v1.service_control_service_pb2.ListServicesRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.iam.v1.service_control_service_pb2.ListServicesResponse, collections.abc.Awaitable[yandex.cloud.priv.iam.v1.service_control_service_pb2.ListServicesResponse]]: ...

    @abc.abstractmethod
    def Enable(
        self,
        request: yandex.cloud.priv.iam.v1.service_control_service_pb2.EnableServiceRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.priv.operation.operation_pb2.Operation]]: ...

    @abc.abstractmethod
    def EnableDefaultServices(
        self,
        request: yandex.cloud.priv.iam.v1.service_control_service_pb2.EnableDefaultServicesRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.priv.operation.operation_pb2.Operation]]: ...

    @abc.abstractmethod
    def Resume(
        self,
        request: yandex.cloud.priv.iam.v1.service_control_service_pb2.ResumeServiceRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.priv.operation.operation_pb2.Operation]]: ...

    @abc.abstractmethod
    def Pause(
        self,
        request: yandex.cloud.priv.iam.v1.service_control_service_pb2.PauseServiceRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.priv.operation.operation_pb2.Operation]]: ...

    @abc.abstractmethod
    def Disable(
        self,
        request: yandex.cloud.priv.iam.v1.service_control_service_pb2.DisableServiceRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.priv.operation.operation_pb2.Operation]]: ...

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.priv.iam.v1.service_control_service_pb2.DeleteServiceRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.priv.operation.operation_pb2.Operation]]: ...

    @abc.abstractmethod
    def Upgrade(
        self,
        request: yandex.cloud.priv.iam.v1.service_control_service_pb2.UpgradeServiceRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.priv.operation.operation_pb2.Operation]]: ...

    @abc.abstractmethod
    def ResolveAgent(
        self,
        request: yandex.cloud.priv.iam.v1.service_control_service_pb2.ResolveServiceAgentRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.iam.v1.service_control_pb2.ServiceAgent, collections.abc.Awaitable[yandex.cloud.priv.iam.v1.service_control_pb2.ServiceAgent]]: ...

    @abc.abstractmethod
    def ListSystemFolders(
        self,
        request: yandex.cloud.priv.iam.v1.service_control_service_pb2.ListSystemFoldersRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.iam.v1.service_control_service_pb2.ListSystemFoldersResponse, collections.abc.Awaitable[yandex.cloud.priv.iam.v1.service_control_service_pb2.ListSystemFoldersResponse]]: ...

    @abc.abstractmethod
    def ListSystemServiceAccounts(
        self,
        request: yandex.cloud.priv.iam.v1.service_control_service_pb2.ListSystemServiceAccountsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.iam.v1.service_control_service_pb2.ListSystemServiceAccountsResponse, collections.abc.Awaitable[yandex.cloud.priv.iam.v1.service_control_service_pb2.ListSystemServiceAccountsResponse]]: ...

    @abc.abstractmethod
    def DeleteSystemFolder(
        self,
        request: yandex.cloud.priv.iam.v1.service_control_service_pb2.DeleteSystemFolderRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.priv.operation.operation_pb2.Operation]]: ...

    @abc.abstractmethod
    def SetupDelegation(
        self,
        request: yandex.cloud.priv.iam.v1.service_control_service_pb2.SetupDelegationRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.priv.operation.operation_pb2.Operation]]: ...

    @abc.abstractmethod
    def RevokeDelegation(
        self,
        request: yandex.cloud.priv.iam.v1.service_control_service_pb2.RevokeDelegationRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.priv.operation.operation_pb2.Operation]]: ...

    @abc.abstractmethod
    def ListReferences(
        self,
        request: yandex.cloud.priv.iam.v1.service_control_service_pb2.ListServiceReferencesRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.iam.v1.service_control_service_pb2.ListServiceReferencesResponse, collections.abc.Awaitable[yandex.cloud.priv.iam.v1.service_control_service_pb2.ListServiceReferencesResponse]]: ...

    @abc.abstractmethod
    def UpdateReferences(
        self,
        request: yandex.cloud.priv.iam.v1.service_control_service_pb2.UpdateServiceReferencesRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.priv.operation.operation_pb2.Operation]]: ...

    @abc.abstractmethod
    def GetSettings(
        self,
        request: yandex.cloud.priv.iam.v1.service_control_service_pb2.GetServiceControlSettingsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.iam.v1.service_control_pb2.ServiceControlSettings, collections.abc.Awaitable[yandex.cloud.priv.iam.v1.service_control_pb2.ServiceControlSettings]]: ...

    @abc.abstractmethod
    def UpdateSettings(
        self,
        request: yandex.cloud.priv.iam.v1.service_control_service_pb2.UpdateServiceControlSettingsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.priv.operation.operation_pb2.Operation]]: ...

    @abc.abstractmethod
    def EnsureEnabled(
        self,
        request: yandex.cloud.priv.iam.v1.service_control_service_pb2.EnsureServicesEnabledRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.priv.operation.operation_pb2.Operation]]: ...

    @abc.abstractmethod
    def ListOperations(
        self,
        request: yandex.cloud.priv.iam.v1.service_control_service_pb2.ListServiceOperationsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.priv.iam.v1.service_control_service_pb2.ListServiceOperationsResponse, collections.abc.Awaitable[yandex.cloud.priv.iam.v1.service_control_service_pb2.ListServiceOperationsResponse]]: ...

def add_ServiceControlServiceServicer_to_server(servicer: ServiceControlServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
