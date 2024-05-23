# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.priv.iam.v1.console import access_binding_service_pb2 as yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_console_dot_access__binding__service__pb2


class AccessBindingServiceStub(object):
    """Console-specific AccessBindingService.
    Analogous to the regular ABS from private API, but to be used by service facades when serving
    console-specific access bindings calls.
    Usage scenario:
    [end user] --access-bindings-UI--> [console] --> [console folder service] --> [console ABS]

    Important thing to note here is that access bindings listing response is leaking information.
    By providing "inherited_from" field, access bindings from resources other than specified one
    are inadvertently disclosed. Those are the access bindings the user might not have had permissions
    to read.
    It was decided however to greenlight this approach since it was considered more "harmful" to
    not let the end user see that other subjects might have access to his generally private resources,
    rather than trying to maximize security on a method level.

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListAccessBindings = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.console.AccessBindingService/ListAccessBindings',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_console_dot_access__binding__service__pb2.ListAccessBindingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_console_dot_access__binding__service__pb2.ListAccessBindingsResponse.FromString,
                )


class AccessBindingServiceServicer(object):
    """Console-specific AccessBindingService.
    Analogous to the regular ABS from private API, but to be used by service facades when serving
    console-specific access bindings calls.
    Usage scenario:
    [end user] --access-bindings-UI--> [console] --> [console folder service] --> [console ABS]

    Important thing to note here is that access bindings listing response is leaking information.
    By providing "inherited_from" field, access bindings from resources other than specified one
    are inadvertently disclosed. Those are the access bindings the user might not have had permissions
    to read.
    It was decided however to greenlight this approach since it was considered more "harmful" to
    not let the end user see that other subjects might have access to his generally private resources,
    rather than trying to maximize security on a method level.

    """

    def ListAccessBindings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AccessBindingServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListAccessBindings': grpc.unary_unary_rpc_method_handler(
                    servicer.ListAccessBindings,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_console_dot_access__binding__service__pb2.ListAccessBindingsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_console_dot_access__binding__service__pb2.ListAccessBindingsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.priv.iam.v1.console.AccessBindingService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AccessBindingService(object):
    """Console-specific AccessBindingService.
    Analogous to the regular ABS from private API, but to be used by service facades when serving
    console-specific access bindings calls.
    Usage scenario:
    [end user] --access-bindings-UI--> [console] --> [console folder service] --> [console ABS]

    Important thing to note here is that access bindings listing response is leaking information.
    By providing "inherited_from" field, access bindings from resources other than specified one
    are inadvertently disclosed. Those are the access bindings the user might not have had permissions
    to read.
    It was decided however to greenlight this approach since it was considered more "harmful" to
    not let the end user see that other subjects might have access to his generally private resources,
    rather than trying to maximize security on a method level.

    """

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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.console.AccessBindingService/ListAccessBindings',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_console_dot_access__binding__service__pb2.ListAccessBindingsRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_console_dot_access__binding__service__pb2.ListAccessBindingsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
