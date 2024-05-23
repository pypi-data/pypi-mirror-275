# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.priv.iam.v1 import membership_service_pb2 as yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_membership__service__pb2


class MembershipServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListResourceMembers = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.MembershipService/ListResourceMembers',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_membership__service__pb2.ListResourceMembersRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_membership__service__pb2.ListResourceMembersResponse.FromString,
                )
        self.ListMemberResources = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.MembershipService/ListMemberResources',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_membership__service__pb2.ListMemberResourcesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_membership__service__pb2.ListMemberResourcesResponse.FromString,
                )
        self.FilterResourceMembers = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.MembershipService/FilterResourceMembers',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_membership__service__pb2.FilterResourceMembersRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_membership__service__pb2.FilterResourceMembersResponse.FromString,
                )


class MembershipServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListResourceMembers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListMemberResources(self, request, context):
        """List member resources for specified resource type. Response resources are sorted by resource_id.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FilterResourceMembers(self, request, context):
        """Filter resource members for specified resource. Only resource members are returned in response.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MembershipServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListResourceMembers': grpc.unary_unary_rpc_method_handler(
                    servicer.ListResourceMembers,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_membership__service__pb2.ListResourceMembersRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_membership__service__pb2.ListResourceMembersResponse.SerializeToString,
            ),
            'ListMemberResources': grpc.unary_unary_rpc_method_handler(
                    servicer.ListMemberResources,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_membership__service__pb2.ListMemberResourcesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_membership__service__pb2.ListMemberResourcesResponse.SerializeToString,
            ),
            'FilterResourceMembers': grpc.unary_unary_rpc_method_handler(
                    servicer.FilterResourceMembers,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_membership__service__pb2.FilterResourceMembersRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_membership__service__pb2.FilterResourceMembersResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.priv.iam.v1.MembershipService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MembershipService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListResourceMembers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.MembershipService/ListResourceMembers',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_membership__service__pb2.ListResourceMembersRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_membership__service__pb2.ListResourceMembersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListMemberResources(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.MembershipService/ListMemberResources',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_membership__service__pb2.ListMemberResourcesRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_membership__service__pb2.ListMemberResourcesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FilterResourceMembers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.MembershipService/FilterResourceMembers',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_membership__service__pb2.FilterResourceMembersRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_membership__service__pb2.FilterResourceMembersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
