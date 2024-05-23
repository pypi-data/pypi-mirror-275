# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from yandex.cloud.priv.oauth.v1 import login_history_service_pb2 as yandex_dot_cloud_dot_priv_dot_oauth_dot_v1_dot_login__history__service__pb2


class LoginHistoryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_unary(
                '/yandex.cloud.priv.oauth.v1.LoginHistoryService/List',
                request_serializer=yandex_dot_cloud_dot_priv_dot_oauth_dot_v1_dot_login__history__service__pb2.ListLoginsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_oauth_dot_v1_dot_login__history__service__pb2.ListLoginsResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/yandex.cloud.priv.oauth.v1.LoginHistoryService/Delete',
                request_serializer=yandex_dot_cloud_dot_priv_dot_oauth_dot_v1_dot_login__history__service__pb2.DeleteDeviceLoginRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class LoginHistoryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """Returns the device's login history by client's cookies.

        gRPC error codes
        InvalidArgument: the Cookie header field is malformed.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Removes the specified record from the device's login history.

        gRPC error codes
        InvalidArgument: the Cookie header field is malformed.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LoginHistoryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_oauth_dot_v1_dot_login__history__service__pb2.ListLoginsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_oauth_dot_v1_dot_login__history__service__pb2.ListLoginsResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_oauth_dot_v1_dot_login__history__service__pb2.DeleteDeviceLoginRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.priv.oauth.v1.LoginHistoryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class LoginHistoryService(object):
    """Missing associated documentation comment in .proto file."""

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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.oauth.v1.LoginHistoryService/List',
            yandex_dot_cloud_dot_priv_dot_oauth_dot_v1_dot_login__history__service__pb2.ListLoginsRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_oauth_dot_v1_dot_login__history__service__pb2.ListLoginsResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.oauth.v1.LoginHistoryService/Delete',
            yandex_dot_cloud_dot_priv_dot_oauth_dot_v1_dot_login__history__service__pb2.DeleteDeviceLoginRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
