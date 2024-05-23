# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from yandex.cloud.priv.iam.v1.mfa import totp_profile_pb2 as yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_mfa_dot_totp__profile__pb2
from yandex.cloud.priv.iam.v1.mfa import totp_profile_service_pb2 as yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_mfa_dot_totp__profile__service__pb2
from yandex.cloud.priv.operation import operation_pb2 as yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2


class TotpProfileServiceStub(object):
    """A set of methods for managing time-based one time passwords (TOTP).
    The user credentials should be passed in the authorization header.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.mfa.TotpProfileService/Get',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_mfa_dot_totp__profile__pb2.TotpProfile.FromString,
                )
        self.Create = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.mfa.TotpProfileService/Create',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_mfa_dot_totp__profile__service__pb2.CreateTotpProfileRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Delete = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.mfa.TotpProfileService/Delete',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_mfa_dot_totp__profile__service__pb2.DeleteTotpProfileRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.ListOperations = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.mfa.TotpProfileService/ListOperations',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_mfa_dot_totp__profile__service__pb2.ListTotpProfileOperationsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_mfa_dot_totp__profile__service__pb2.ListTotpProfileOperationsResponse.FromString,
                )
        self.Verify = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.mfa.TotpProfileService/Verify',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_mfa_dot_totp__profile__service__pb2.VerifyTotpRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_mfa_dot_totp__profile__service__pb2.VerifyTotpResponse.FromString,
                )
        self.GetForSubject = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.mfa.TotpProfileService/GetForSubject',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_mfa_dot_totp__profile__service__pb2.GetTotpProfileForSubjectRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_mfa_dot_totp__profile__pb2.TotpProfile.FromString,
                )
        self.DeleteForSubject = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.mfa.TotpProfileService/DeleteForSubject',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_mfa_dot_totp__profile__service__pb2.DeleteTotpProfileForSubjectRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
                )


class TotpProfileServiceServicer(object):
    """A set of methods for managing time-based one time passwords (TOTP).
    The user credentials should be passed in the authorization header.
    """

    def Get(self, request, context):
        """Returns the TOTP profile for the user.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates a new TOTP profile for the user. This method will fail, if the user
        already has an active TOTP profile.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the TOTP profile for the user.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOperations(self, request, context):
        """Retrieves the list of Operations for the specified TOTP profile.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Verify(self, request, context):
        """Verifies user-supplied TOTP value. See https://tools.ietf.org/html/rfc6238#section-5.2 for the reference.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetForSubject(self, request, context):
        """Returns the TOTP profile for the specified user.
        This method requires `iam.totpProfiles.manage` permission.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteForSubject(self, request, context):
        """Deletes the TOTP profile for the specified user.
        This method requires `iam.totpProfiles.manage` permission.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TotpProfileServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_mfa_dot_totp__profile__pb2.TotpProfile.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_mfa_dot_totp__profile__service__pb2.CreateTotpProfileRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_mfa_dot_totp__profile__service__pb2.DeleteTotpProfileRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListOperations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOperations,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_mfa_dot_totp__profile__service__pb2.ListTotpProfileOperationsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_mfa_dot_totp__profile__service__pb2.ListTotpProfileOperationsResponse.SerializeToString,
            ),
            'Verify': grpc.unary_unary_rpc_method_handler(
                    servicer.Verify,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_mfa_dot_totp__profile__service__pb2.VerifyTotpRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_mfa_dot_totp__profile__service__pb2.VerifyTotpResponse.SerializeToString,
            ),
            'GetForSubject': grpc.unary_unary_rpc_method_handler(
                    servicer.GetForSubject,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_mfa_dot_totp__profile__service__pb2.GetTotpProfileForSubjectRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_mfa_dot_totp__profile__pb2.TotpProfile.SerializeToString,
            ),
            'DeleteForSubject': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteForSubject,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_mfa_dot_totp__profile__service__pb2.DeleteTotpProfileForSubjectRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.priv.iam.v1.mfa.TotpProfileService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TotpProfileService(object):
    """A set of methods for managing time-based one time passwords (TOTP).
    The user credentials should be passed in the authorization header.
    """

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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.mfa.TotpProfileService/Get',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_mfa_dot_totp__profile__pb2.TotpProfile.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.mfa.TotpProfileService/Create',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_mfa_dot_totp__profile__service__pb2.CreateTotpProfileRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.mfa.TotpProfileService/Delete',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_mfa_dot_totp__profile__service__pb2.DeleteTotpProfileRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.mfa.TotpProfileService/ListOperations',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_mfa_dot_totp__profile__service__pb2.ListTotpProfileOperationsRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_mfa_dot_totp__profile__service__pb2.ListTotpProfileOperationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Verify(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.mfa.TotpProfileService/Verify',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_mfa_dot_totp__profile__service__pb2.VerifyTotpRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_mfa_dot_totp__profile__service__pb2.VerifyTotpResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetForSubject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.mfa.TotpProfileService/GetForSubject',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_mfa_dot_totp__profile__service__pb2.GetTotpProfileForSubjectRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_mfa_dot_totp__profile__pb2.TotpProfile.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteForSubject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.mfa.TotpProfileService/DeleteForSubject',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_mfa_dot_totp__profile__service__pb2.DeleteTotpProfileForSubjectRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
