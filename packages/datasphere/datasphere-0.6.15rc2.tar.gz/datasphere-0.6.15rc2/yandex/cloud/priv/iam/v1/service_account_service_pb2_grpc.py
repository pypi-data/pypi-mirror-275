# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.priv.access import access_pb2 as yandex_dot_cloud_dot_priv_dot_access_dot_access__pb2
from yandex.cloud.priv.iam import restriction_pb2 as yandex_dot_cloud_dot_priv_dot_iam_dot_restriction__pb2
from yandex.cloud.priv.iam.v1 import service_account_pb2 as yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__pb2
from yandex.cloud.priv.iam.v1 import service_account_service_pb2 as yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__service__pb2
from yandex.cloud.priv.iam.v1.token import iam_token_pb2 as yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_token_dot_iam__token__pb2
from yandex.cloud.priv.operation import operation_pb2 as yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2


class ServiceAccountServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.ServiceAccountService/Get',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__service__pb2.GetServiceAccountRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__pb2.ServiceAccount.FromString,
                )
        self.List = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.ServiceAccountService/List',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__service__pb2.ListServiceAccountsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__service__pb2.ListServiceAccountsResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.ServiceAccountService/Create',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__service__pb2.CreateServiceAccountRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Update = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.ServiceAccountService/Update',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__service__pb2.UpdateServiceAccountRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Delete = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.ServiceAccountService/Delete',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__service__pb2.DeleteServiceAccountRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.ListAccessBindings = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.ServiceAccountService/ListAccessBindings',
                request_serializer=yandex_dot_cloud_dot_priv_dot_access_dot_access__pb2.ListAccessBindingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_access_dot_access__pb2.ListAccessBindingsResponse.FromString,
                )
        self.SetAccessBindings = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.ServiceAccountService/SetAccessBindings',
                request_serializer=yandex_dot_cloud_dot_priv_dot_access_dot_access__pb2.SetAccessBindingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.UpdateAccessBindings = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.ServiceAccountService/UpdateAccessBindings',
                request_serializer=yandex_dot_cloud_dot_priv_dot_access_dot_access__pb2.UpdateAccessBindingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.ListRestrictions = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.ServiceAccountService/ListRestrictions',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_restriction__pb2.ListRestrictionsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_restriction__pb2.ListRestrictionsResponse.FromString,
                )
        self.GetRestriction = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.ServiceAccountService/GetRestriction',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_restriction__pb2.GetRestrictionRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_restriction__pb2.Restriction.FromString,
                )
        self.AddRestriction = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.ServiceAccountService/AddRestriction',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_restriction__pb2.AddRestrictionRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.RemoveRestriction = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.ServiceAccountService/RemoveRestriction',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_restriction__pb2.RemoveRestrictionRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.ListOperations = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.ServiceAccountService/ListOperations',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__service__pb2.ListServiceAccountOperationsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__service__pb2.ListServiceAccountOperationsResponse.FromString,
                )
        self.IssueToken = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.ServiceAccountService/IssueToken',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__service__pb2.IssueTokenRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_token_dot_iam__token__pb2.IamToken.FromString,
                )
        self.ListReferences = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.ServiceAccountService/ListReferences',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__service__pb2.ListServiceAccountReferencesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__service__pb2.ListServiceAccountReferencesResponse.FromString,
                )
        self.UpdateReferences = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.ServiceAccountService/UpdateReferences',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__service__pb2.UpdateServiceAccountReferencesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
                )


class ServiceAccountServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAccessBindings(self, request, context):
        """access

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAccessBindings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateAccessBindings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListRestrictions(self, request, context):
        """restrictions

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRestriction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddRestriction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveRestriction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOperations(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IssueToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListReferences(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateReferences(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ServiceAccountServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__service__pb2.GetServiceAccountRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__pb2.ServiceAccount.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__service__pb2.ListServiceAccountsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__service__pb2.ListServiceAccountsResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__service__pb2.CreateServiceAccountRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__service__pb2.UpdateServiceAccountRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__service__pb2.DeleteServiceAccountRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListAccessBindings': grpc.unary_unary_rpc_method_handler(
                    servicer.ListAccessBindings,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_access_dot_access__pb2.ListAccessBindingsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_access_dot_access__pb2.ListAccessBindingsResponse.SerializeToString,
            ),
            'SetAccessBindings': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAccessBindings,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_access_dot_access__pb2.SetAccessBindingsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'UpdateAccessBindings': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateAccessBindings,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_access_dot_access__pb2.UpdateAccessBindingsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListRestrictions': grpc.unary_unary_rpc_method_handler(
                    servicer.ListRestrictions,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_restriction__pb2.ListRestrictionsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_restriction__pb2.ListRestrictionsResponse.SerializeToString,
            ),
            'GetRestriction': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRestriction,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_restriction__pb2.GetRestrictionRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_restriction__pb2.Restriction.SerializeToString,
            ),
            'AddRestriction': grpc.unary_unary_rpc_method_handler(
                    servicer.AddRestriction,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_restriction__pb2.AddRestrictionRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'RemoveRestriction': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveRestriction,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_restriction__pb2.RemoveRestrictionRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListOperations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOperations,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__service__pb2.ListServiceAccountOperationsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__service__pb2.ListServiceAccountOperationsResponse.SerializeToString,
            ),
            'IssueToken': grpc.unary_unary_rpc_method_handler(
                    servicer.IssueToken,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__service__pb2.IssueTokenRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_token_dot_iam__token__pb2.IamToken.SerializeToString,
            ),
            'ListReferences': grpc.unary_unary_rpc_method_handler(
                    servicer.ListReferences,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__service__pb2.ListServiceAccountReferencesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__service__pb2.ListServiceAccountReferencesResponse.SerializeToString,
            ),
            'UpdateReferences': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateReferences,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__service__pb2.UpdateServiceAccountReferencesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.priv.iam.v1.ServiceAccountService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ServiceAccountService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.ServiceAccountService/Get',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__service__pb2.GetServiceAccountRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__pb2.ServiceAccount.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.ServiceAccountService/List',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__service__pb2.ListServiceAccountsRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__service__pb2.ListServiceAccountsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.ServiceAccountService/Create',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__service__pb2.CreateServiceAccountRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.ServiceAccountService/Update',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__service__pb2.UpdateServiceAccountRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.ServiceAccountService/Delete',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__service__pb2.DeleteServiceAccountRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListAccessBindings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.ServiceAccountService/ListAccessBindings',
            yandex_dot_cloud_dot_priv_dot_access_dot_access__pb2.ListAccessBindingsRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_access_dot_access__pb2.ListAccessBindingsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetAccessBindings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.ServiceAccountService/SetAccessBindings',
            yandex_dot_cloud_dot_priv_dot_access_dot_access__pb2.SetAccessBindingsRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateAccessBindings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.ServiceAccountService/UpdateAccessBindings',
            yandex_dot_cloud_dot_priv_dot_access_dot_access__pb2.UpdateAccessBindingsRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListRestrictions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.ServiceAccountService/ListRestrictions',
            yandex_dot_cloud_dot_priv_dot_iam_dot_restriction__pb2.ListRestrictionsRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_iam_dot_restriction__pb2.ListRestrictionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRestriction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.ServiceAccountService/GetRestriction',
            yandex_dot_cloud_dot_priv_dot_iam_dot_restriction__pb2.GetRestrictionRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_iam_dot_restriction__pb2.Restriction.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddRestriction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.ServiceAccountService/AddRestriction',
            yandex_dot_cloud_dot_priv_dot_iam_dot_restriction__pb2.AddRestrictionRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveRestriction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.ServiceAccountService/RemoveRestriction',
            yandex_dot_cloud_dot_priv_dot_iam_dot_restriction__pb2.RemoveRestrictionRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListOperations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.ServiceAccountService/ListOperations',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__service__pb2.ListServiceAccountOperationsRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__service__pb2.ListServiceAccountOperationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def IssueToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.ServiceAccountService/IssueToken',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__service__pb2.IssueTokenRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_token_dot_iam__token__pb2.IamToken.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListReferences(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.ServiceAccountService/ListReferences',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__service__pb2.ListServiceAccountReferencesRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__service__pb2.ListServiceAccountReferencesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateReferences(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.ServiceAccountService/UpdateReferences',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_service__account__service__pb2.UpdateServiceAccountReferencesRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
