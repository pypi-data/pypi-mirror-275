# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.priv.datasphere.v2 import admin_pb2 as yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_admin__pb2
from yandex.cloud.priv.datasphere.v2 import admin_service_pb2 as yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_admin__service__pb2


class AdminServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAdminProjectInfo = channel.unary_unary(
                '/yandex.cloud.priv.datasphere.v2.AdminService/GetAdminProjectInfo',
                request_serializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_admin__service__pb2.GetAdminProjectInfoRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_admin__pb2.AdminProjectInfo.FromString,
                )


class AdminServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetAdminProjectInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AdminServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAdminProjectInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAdminProjectInfo,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_admin__service__pb2.GetAdminProjectInfoRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_admin__pb2.AdminProjectInfo.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.priv.datasphere.v2.AdminService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AdminService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetAdminProjectInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.datasphere.v2.AdminService/GetAdminProjectInfo',
            yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_admin__service__pb2.GetAdminProjectInfoRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_admin__pb2.AdminProjectInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
