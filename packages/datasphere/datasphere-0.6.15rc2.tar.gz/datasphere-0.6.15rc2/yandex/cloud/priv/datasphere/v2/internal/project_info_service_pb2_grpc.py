# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.priv.datasphere.v2.internal import project_info_pb2 as yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_internal_dot_project__info__pb2
from yandex.cloud.priv.datasphere.v2.internal import project_info_service_pb2 as yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_internal_dot_project__info__service__pb2


class ProjectInfoServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAuthModel = channel.unary_unary(
                '/yandex.cloud.priv.datasphere.v2.internal.ProjectInfoService/GetAuthModel',
                request_serializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_internal_dot_project__info__service__pb2.GetProjectAuthModelRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_internal_dot_project__info__pb2.ProjectAuthModel.FromString,
                )
        self.GetFullInfo = channel.unary_unary(
                '/yandex.cloud.priv.datasphere.v2.internal.ProjectInfoService/GetFullInfo',
                request_serializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_internal_dot_project__info__service__pb2.GetProjectFullInfoRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_internal_dot_project__info__pb2.ProjectFullInfo.FromString,
                )
        self.GetIdeModel = channel.unary_unary(
                '/yandex.cloud.priv.datasphere.v2.internal.ProjectInfoService/GetIdeModel',
                request_serializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_internal_dot_project__info__service__pb2.GetProjectIdeModelRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_internal_dot_project__info__pb2.ProjectIdeModel.FromString,
                )


class ProjectInfoServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetAuthModel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFullInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetIdeModel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProjectInfoServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAuthModel': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAuthModel,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_internal_dot_project__info__service__pb2.GetProjectAuthModelRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_internal_dot_project__info__pb2.ProjectAuthModel.SerializeToString,
            ),
            'GetFullInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFullInfo,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_internal_dot_project__info__service__pb2.GetProjectFullInfoRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_internal_dot_project__info__pb2.ProjectFullInfo.SerializeToString,
            ),
            'GetIdeModel': grpc.unary_unary_rpc_method_handler(
                    servicer.GetIdeModel,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_internal_dot_project__info__service__pb2.GetProjectIdeModelRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_internal_dot_project__info__pb2.ProjectIdeModel.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.priv.datasphere.v2.internal.ProjectInfoService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProjectInfoService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetAuthModel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.datasphere.v2.internal.ProjectInfoService/GetAuthModel',
            yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_internal_dot_project__info__service__pb2.GetProjectAuthModelRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_internal_dot_project__info__pb2.ProjectAuthModel.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFullInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.datasphere.v2.internal.ProjectInfoService/GetFullInfo',
            yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_internal_dot_project__info__service__pb2.GetProjectFullInfoRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_internal_dot_project__info__pb2.ProjectFullInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetIdeModel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.datasphere.v2.internal.ProjectInfoService/GetIdeModel',
            yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_internal_dot_project__info__service__pb2.GetProjectIdeModelRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_internal_dot_project__info__pb2.ProjectIdeModel.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
