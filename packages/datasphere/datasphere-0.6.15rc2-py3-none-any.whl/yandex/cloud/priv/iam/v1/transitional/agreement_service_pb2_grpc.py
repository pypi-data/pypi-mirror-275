# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.priv.iam.v1.transitional import agreement_service_pb2 as yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_agreement__service__pb2


class AgreementServiceStub(object):
    """TODO console
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AcceptAgreements = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.transitional.AgreementService/AcceptAgreements',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_agreement__service__pb2.AcceptAgreementsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_agreement__service__pb2.AcceptAgreementsResponse.FromString,
                )
        self.AcceptAgreementsOauth = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.transitional.AgreementService/AcceptAgreementsOauth',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_agreement__service__pb2.AcceptAgreementsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_agreement__service__pb2.AcceptAgreementsResponse.FromString,
                )
        self.AcceptAgreementsLogin = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.transitional.AgreementService/AcceptAgreementsLogin',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_agreement__service__pb2.AcceptAgreementsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_agreement__service__pb2.AcceptAgreementsResponse.FromString,
                )


class AgreementServiceServicer(object):
    """TODO console
    """

    def AcceptAgreements(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AcceptAgreementsOauth(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AcceptAgreementsLogin(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AgreementServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AcceptAgreements': grpc.unary_unary_rpc_method_handler(
                    servicer.AcceptAgreements,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_agreement__service__pb2.AcceptAgreementsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_agreement__service__pb2.AcceptAgreementsResponse.SerializeToString,
            ),
            'AcceptAgreementsOauth': grpc.unary_unary_rpc_method_handler(
                    servicer.AcceptAgreementsOauth,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_agreement__service__pb2.AcceptAgreementsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_agreement__service__pb2.AcceptAgreementsResponse.SerializeToString,
            ),
            'AcceptAgreementsLogin': grpc.unary_unary_rpc_method_handler(
                    servicer.AcceptAgreementsLogin,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_agreement__service__pb2.AcceptAgreementsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_agreement__service__pb2.AcceptAgreementsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.priv.iam.v1.transitional.AgreementService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AgreementService(object):
    """TODO console
    """

    @staticmethod
    def AcceptAgreements(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.transitional.AgreementService/AcceptAgreements',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_agreement__service__pb2.AcceptAgreementsRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_agreement__service__pb2.AcceptAgreementsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AcceptAgreementsOauth(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.transitional.AgreementService/AcceptAgreementsOauth',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_agreement__service__pb2.AcceptAgreementsRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_agreement__service__pb2.AcceptAgreementsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AcceptAgreementsLogin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.transitional.AgreementService/AcceptAgreementsLogin',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_agreement__service__pb2.AcceptAgreementsRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_agreement__service__pb2.AcceptAgreementsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
