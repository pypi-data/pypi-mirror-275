# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.priv.iam.v1.transitional import policy_service_pb2 as yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_policy__service__pb2


class PolicyServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.transitional.PolicyService/List',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_policy__service__pb2.ListPoliciesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_policy__service__pb2.ListPoliciesResponse.FromString,
                )
        self.ListCompat = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.transitional.PolicyService/ListCompat',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_policy__service__pb2.ListPoliciesCompatRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_policy__service__pb2.ListPoliciesResponse.FromString,
                )
        self.Set = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.transitional.PolicyService/Set',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_policy__service__pb2.SetPolicyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_policy__service__pb2.SetPolicyResponse.FromString,
                )
        self.SetCompat = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.transitional.PolicyService/SetCompat',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_policy__service__pb2.SetPolicyCompatRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_policy__service__pb2.SetPolicyResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.transitional.PolicyService/Delete',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_policy__service__pb2.DeletePolicyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_policy__service__pb2.DeletePolicyResponse.FromString,
                )
        self.DeleteCompat = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.transitional.PolicyService/DeleteCompat',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_policy__service__pb2.DeletePolicyCompatRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_policy__service__pb2.DeletePolicyResponse.FromString,
                )


class PolicyServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCompat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Set(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetCompat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteCompat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PolicyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_policy__service__pb2.ListPoliciesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_policy__service__pb2.ListPoliciesResponse.SerializeToString,
            ),
            'ListCompat': grpc.unary_unary_rpc_method_handler(
                    servicer.ListCompat,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_policy__service__pb2.ListPoliciesCompatRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_policy__service__pb2.ListPoliciesResponse.SerializeToString,
            ),
            'Set': grpc.unary_unary_rpc_method_handler(
                    servicer.Set,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_policy__service__pb2.SetPolicyRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_policy__service__pb2.SetPolicyResponse.SerializeToString,
            ),
            'SetCompat': grpc.unary_unary_rpc_method_handler(
                    servicer.SetCompat,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_policy__service__pb2.SetPolicyCompatRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_policy__service__pb2.SetPolicyResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_policy__service__pb2.DeletePolicyRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_policy__service__pb2.DeletePolicyResponse.SerializeToString,
            ),
            'DeleteCompat': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteCompat,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_policy__service__pb2.DeletePolicyCompatRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_policy__service__pb2.DeletePolicyResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.priv.iam.v1.transitional.PolicyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PolicyService(object):
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.transitional.PolicyService/List',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_policy__service__pb2.ListPoliciesRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_policy__service__pb2.ListPoliciesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListCompat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.transitional.PolicyService/ListCompat',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_policy__service__pb2.ListPoliciesCompatRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_policy__service__pb2.ListPoliciesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Set(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.transitional.PolicyService/Set',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_policy__service__pb2.SetPolicyRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_policy__service__pb2.SetPolicyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetCompat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.transitional.PolicyService/SetCompat',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_policy__service__pb2.SetPolicyCompatRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_policy__service__pb2.SetPolicyResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.transitional.PolicyService/Delete',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_policy__service__pb2.DeletePolicyRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_policy__service__pb2.DeletePolicyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteCompat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.transitional.PolicyService/DeleteCompat',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_policy__service__pb2.DeletePolicyCompatRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_transitional_dot_policy__service__pb2.DeletePolicyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
