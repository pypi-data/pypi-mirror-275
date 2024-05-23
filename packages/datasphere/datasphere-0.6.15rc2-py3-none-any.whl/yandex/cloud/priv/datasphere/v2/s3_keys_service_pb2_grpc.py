# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.priv.datasphere.v2 import s3_keys_service_pb2 as yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_s3__keys__service__pb2


class S3KeysServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetS3Keys = channel.unary_unary(
                '/yandex.cloud.priv.datasphere.v2.S3KeysService/GetS3Keys',
                request_serializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_s3__keys__service__pb2.GetS3KeysRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_s3__keys__service__pb2.GetS3KeysResponse.FromString,
                )


class S3KeysServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetS3Keys(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_S3KeysServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetS3Keys': grpc.unary_unary_rpc_method_handler(
                    servicer.GetS3Keys,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_s3__keys__service__pb2.GetS3KeysRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_s3__keys__service__pb2.GetS3KeysResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.priv.datasphere.v2.S3KeysService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class S3KeysService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetS3Keys(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.datasphere.v2.S3KeysService/GetS3Keys',
            yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_s3__keys__service__pb2.GetS3KeysRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_s3__keys__service__pb2.GetS3KeysResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
