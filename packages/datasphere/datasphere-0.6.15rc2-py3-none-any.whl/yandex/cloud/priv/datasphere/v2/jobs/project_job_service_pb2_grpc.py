# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from yandex.cloud.priv.datasphere.v2.jobs import jobs_pb2 as yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_jobs__pb2
from yandex.cloud.priv.datasphere.v2.jobs import project_job_service_pb2 as yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2
from yandex.cloud.priv.operation import operation_pb2 as yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2


class ProjectJobServiceStub(object):
    """Header in each request: `Authorization: Bearer <IAM token>`.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/yandex.cloud.priv.datasphere.v2.jobs.ProjectJobService/Create',
                request_serializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.CreateProjectJobRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Clone = channel.unary_unary(
                '/yandex.cloud.priv.datasphere.v2.jobs.ProjectJobService/Clone',
                request_serializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.CloneProjectJobRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Execute = channel.unary_unary(
                '/yandex.cloud.priv.datasphere.v2.jobs.ProjectJobService/Execute',
                request_serializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.ExecuteProjectJobRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.ReadLogs = channel.unary_stream(
                '/yandex.cloud.priv.datasphere.v2.jobs.ProjectJobService/ReadLogs',
                request_serializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.ReadProjectJobLogsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.ReadProjectJobLogsResponse.FromString,
                )
        self.DownloadJobFiles = channel.unary_unary(
                '/yandex.cloud.priv.datasphere.v2.jobs.ProjectJobService/DownloadJobFiles',
                request_serializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.DownloadProjectJobFilesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.DownloadProjectJobFilesResponse.FromString,
                )
        self.List = channel.unary_unary(
                '/yandex.cloud.priv.datasphere.v2.jobs.ProjectJobService/List',
                request_serializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.ListProjectJobRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.ListProjectJobResponse.FromString,
                )
        self.Get = channel.unary_unary(
                '/yandex.cloud.priv.datasphere.v2.jobs.ProjectJobService/Get',
                request_serializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.GetProjectJobRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_jobs__pb2.Job.FromString,
                )
        self.GetStorageCostEstimation = channel.unary_unary(
                '/yandex.cloud.priv.datasphere.v2.jobs.ProjectJobService/GetStorageCostEstimation',
                request_serializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.GetProjectJobStorageCostEstimationRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.GetProjectJobStorageCostEstimationResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/yandex.cloud.priv.datasphere.v2.jobs.ProjectJobService/Delete',
                request_serializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.DeleteProjectJobRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.DeleteData = channel.unary_unary(
                '/yandex.cloud.priv.datasphere.v2.jobs.ProjectJobService/DeleteData',
                request_serializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.DeleteProjectJobDataRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.DeleteAllData = channel.unary_unary(
                '/yandex.cloud.priv.datasphere.v2.jobs.ProjectJobService/DeleteAllData',
                request_serializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.DeleteAllProjectJobDataRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.SetDataTtl = channel.unary_unary(
                '/yandex.cloud.priv.datasphere.v2.jobs.ProjectJobService/SetDataTtl',
                request_serializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.SetProjectJobDataTtlRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.SetProjectJobDataTtlResponse.FromString,
                )
        self.Cancel = channel.unary_unary(
                '/yandex.cloud.priv.datasphere.v2.jobs.ProjectJobService/Cancel',
                request_serializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.CancelProjectJobRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.CancelAllJobs = channel.unary_unary(
                '/yandex.cloud.priv.datasphere.v2.jobs.ProjectJobService/CancelAllJobs',
                request_serializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.CancelAllJobsRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.Start = channel.unary_unary(
                '/yandex.cloud.priv.datasphere.v2.jobs.ProjectJobService/Start',
                request_serializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.StartRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Stop = channel.unary_unary(
                '/yandex.cloud.priv.datasphere.v2.jobs.ProjectJobService/Stop',
                request_serializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.StopRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.StartJobsConfigEncryptionMigration = channel.unary_unary(
                '/yandex.cloud.priv.datasphere.v2.jobs.ProjectJobService/StartJobsConfigEncryptionMigration',
                request_serializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.StartJobsConfigEncryptionMigrationRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
                )


class ProjectJobServiceServicer(object):
    """Header in each request: `Authorization: Bearer <IAM token>`.
    """

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Clone(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Execute(self, request, context):
        """Status, cancel - through OperationService. `JobResult` with output files will be inside Operation.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadLogs(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DownloadJobFiles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStorageCostEstimation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAllData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetDataTtl(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Cancel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelAllJobs(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Start(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stop(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartJobsConfigEncryptionMigration(self, request, context):
        """TODO: remove this endpoint after migration is finished
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProjectJobServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.CreateProjectJobRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Clone': grpc.unary_unary_rpc_method_handler(
                    servicer.Clone,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.CloneProjectJobRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Execute': grpc.unary_unary_rpc_method_handler(
                    servicer.Execute,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.ExecuteProjectJobRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ReadLogs': grpc.unary_stream_rpc_method_handler(
                    servicer.ReadLogs,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.ReadProjectJobLogsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.ReadProjectJobLogsResponse.SerializeToString,
            ),
            'DownloadJobFiles': grpc.unary_unary_rpc_method_handler(
                    servicer.DownloadJobFiles,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.DownloadProjectJobFilesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.DownloadProjectJobFilesResponse.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.ListProjectJobRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.ListProjectJobResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.GetProjectJobRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_jobs__pb2.Job.SerializeToString,
            ),
            'GetStorageCostEstimation': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStorageCostEstimation,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.GetProjectJobStorageCostEstimationRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.GetProjectJobStorageCostEstimationResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.DeleteProjectJobRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'DeleteData': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteData,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.DeleteProjectJobDataRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'DeleteAllData': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAllData,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.DeleteAllProjectJobDataRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'SetDataTtl': grpc.unary_unary_rpc_method_handler(
                    servicer.SetDataTtl,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.SetProjectJobDataTtlRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.SetProjectJobDataTtlResponse.SerializeToString,
            ),
            'Cancel': grpc.unary_unary_rpc_method_handler(
                    servicer.Cancel,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.CancelProjectJobRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'CancelAllJobs': grpc.unary_unary_rpc_method_handler(
                    servicer.CancelAllJobs,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.CancelAllJobsRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'Start': grpc.unary_unary_rpc_method_handler(
                    servicer.Start,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.StartRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Stop': grpc.unary_unary_rpc_method_handler(
                    servicer.Stop,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.StopRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'StartJobsConfigEncryptionMigration': grpc.unary_unary_rpc_method_handler(
                    servicer.StartJobsConfigEncryptionMigration,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.StartJobsConfigEncryptionMigrationRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.priv.datasphere.v2.jobs.ProjectJobService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProjectJobService(object):
    """Header in each request: `Authorization: Bearer <IAM token>`.
    """

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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.datasphere.v2.jobs.ProjectJobService/Create',
            yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.CreateProjectJobRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Clone(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.datasphere.v2.jobs.ProjectJobService/Clone',
            yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.CloneProjectJobRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Execute(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.datasphere.v2.jobs.ProjectJobService/Execute',
            yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.ExecuteProjectJobRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadLogs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/yandex.cloud.priv.datasphere.v2.jobs.ProjectJobService/ReadLogs',
            yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.ReadProjectJobLogsRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.ReadProjectJobLogsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DownloadJobFiles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.datasphere.v2.jobs.ProjectJobService/DownloadJobFiles',
            yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.DownloadProjectJobFilesRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.DownloadProjectJobFilesResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.datasphere.v2.jobs.ProjectJobService/List',
            yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.ListProjectJobRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.ListProjectJobResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.datasphere.v2.jobs.ProjectJobService/Get',
            yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.GetProjectJobRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_jobs__pb2.Job.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStorageCostEstimation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.datasphere.v2.jobs.ProjectJobService/GetStorageCostEstimation',
            yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.GetProjectJobStorageCostEstimationRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.GetProjectJobStorageCostEstimationResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.datasphere.v2.jobs.ProjectJobService/Delete',
            yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.DeleteProjectJobRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.datasphere.v2.jobs.ProjectJobService/DeleteData',
            yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.DeleteProjectJobDataRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteAllData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.datasphere.v2.jobs.ProjectJobService/DeleteAllData',
            yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.DeleteAllProjectJobDataRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetDataTtl(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.datasphere.v2.jobs.ProjectJobService/SetDataTtl',
            yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.SetProjectJobDataTtlRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.SetProjectJobDataTtlResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Cancel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.datasphere.v2.jobs.ProjectJobService/Cancel',
            yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.CancelProjectJobRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CancelAllJobs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.datasphere.v2.jobs.ProjectJobService/CancelAllJobs',
            yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.CancelAllJobsRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Start(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.datasphere.v2.jobs.ProjectJobService/Start',
            yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.StartRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Stop(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.datasphere.v2.jobs.ProjectJobService/Stop',
            yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.StopRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartJobsConfigEncryptionMigration(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.datasphere.v2.jobs.ProjectJobService/StartJobsConfigEncryptionMigration',
            yandex_dot_cloud_dot_priv_dot_datasphere_dot_v2_dot_jobs_dot_project__job__service__pb2.StartJobsConfigEncryptionMigrationRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
