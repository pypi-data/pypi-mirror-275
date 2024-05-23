# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.priv.iam.v1 import role_pb2 as yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__pb2
from yandex.cloud.priv.iam.v1 import role_service_pb2 as yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__service__pb2
from yandex.cloud.priv.operation import operation_pb2 as yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2


class RoleServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.RoleService/Get',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__service__pb2.GetRoleRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__pb2.Role.FromString,
                )
        self.List = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.RoleService/List',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__service__pb2.ListRolesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__service__pb2.ListRolesResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.RoleService/Create',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__service__pb2.CreateRoleRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Update = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.RoleService/Update',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__service__pb2.UpdateRoleRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Delete = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.RoleService/Delete',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__service__pb2.DeleteRoleRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.GetCategory = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.RoleService/GetCategory',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__service__pb2.GetRoleCategoryRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__pb2.RoleCategory.FromString,
                )
        self.ListCategories = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.RoleService/ListCategories',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__service__pb2.ListRoleCategoriesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__service__pb2.ListRoleCategoriesResponse.FromString,
                )
        self.CreateCategory = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.RoleService/CreateCategory',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__service__pb2.CreateRoleCategoryRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.UpdateCategory = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.RoleService/UpdateCategory',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__service__pb2.UpdateRoleCategoryRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.DeleteCategory = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.RoleService/DeleteCategory',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__service__pb2.DeleteRoleCategoryRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
                )


class RoleServiceServicer(object):
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

    def GetCategory(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCategories(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateCategory(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCategory(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteCategory(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RoleServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__service__pb2.GetRoleRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__pb2.Role.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__service__pb2.ListRolesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__service__pb2.ListRolesResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__service__pb2.CreateRoleRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__service__pb2.UpdateRoleRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__service__pb2.DeleteRoleRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'GetCategory': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCategory,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__service__pb2.GetRoleCategoryRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__pb2.RoleCategory.SerializeToString,
            ),
            'ListCategories': grpc.unary_unary_rpc_method_handler(
                    servicer.ListCategories,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__service__pb2.ListRoleCategoriesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__service__pb2.ListRoleCategoriesResponse.SerializeToString,
            ),
            'CreateCategory': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateCategory,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__service__pb2.CreateRoleCategoryRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'UpdateCategory': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateCategory,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__service__pb2.UpdateRoleCategoryRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'DeleteCategory': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteCategory,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__service__pb2.DeleteRoleCategoryRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.priv.iam.v1.RoleService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RoleService(object):
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.RoleService/Get',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__service__pb2.GetRoleRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__pb2.Role.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.RoleService/List',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__service__pb2.ListRolesRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__service__pb2.ListRolesResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.RoleService/Create',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__service__pb2.CreateRoleRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.RoleService/Update',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__service__pb2.UpdateRoleRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.RoleService/Delete',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__service__pb2.DeleteRoleRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCategory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.RoleService/GetCategory',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__service__pb2.GetRoleCategoryRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__pb2.RoleCategory.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListCategories(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.RoleService/ListCategories',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__service__pb2.ListRoleCategoriesRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__service__pb2.ListRoleCategoriesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateCategory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.RoleService/CreateCategory',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__service__pb2.CreateRoleCategoryRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateCategory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.RoleService/UpdateCategory',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__service__pb2.UpdateRoleCategoryRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteCategory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.RoleService/DeleteCategory',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_role__service__pb2.DeleteRoleCategoryRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
