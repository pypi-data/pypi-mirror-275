# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from _qwak_proto.qwak.audience.v1 import audience_api_pb2 as qwak_dot_audience_dot_v1_dot_audience__api__pb2


class AudienceAPIStub(object):
    """Audience API
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateAudience = channel.unary_unary(
                '/qwak.audience.v1.AudienceAPI/CreateAudience',
                request_serializer=qwak_dot_audience_dot_v1_dot_audience__api__pb2.CreateAudienceRequest.SerializeToString,
                response_deserializer=qwak_dot_audience_dot_v1_dot_audience__api__pb2.CreateAudienceResponse.FromString,
                )
        self.UpdateAudience = channel.unary_unary(
                '/qwak.audience.v1.AudienceAPI/UpdateAudience',
                request_serializer=qwak_dot_audience_dot_v1_dot_audience__api__pb2.UpdateAudienceRequest.SerializeToString,
                response_deserializer=qwak_dot_audience_dot_v1_dot_audience__api__pb2.UpdateAudienceResponse.FromString,
                )
        self.GetAudience = channel.unary_unary(
                '/qwak.audience.v1.AudienceAPI/GetAudience',
                request_serializer=qwak_dot_audience_dot_v1_dot_audience__api__pb2.GetAudienceRequest.SerializeToString,
                response_deserializer=qwak_dot_audience_dot_v1_dot_audience__api__pb2.GetAudienceResponse.FromString,
                )
        self.ListAudience = channel.unary_unary(
                '/qwak.audience.v1.AudienceAPI/ListAudience',
                request_serializer=qwak_dot_audience_dot_v1_dot_audience__api__pb2.ListAudienceRequest.SerializeToString,
                response_deserializer=qwak_dot_audience_dot_v1_dot_audience__api__pb2.ListAudienceResponse.FromString,
                )
        self.DeleteAudience = channel.unary_unary(
                '/qwak.audience.v1.AudienceAPI/DeleteAudience',
                request_serializer=qwak_dot_audience_dot_v1_dot_audience__api__pb2.DeleteAudienceRequest.SerializeToString,
                response_deserializer=qwak_dot_audience_dot_v1_dot_audience__api__pb2.DeleteAudienceResponse.FromString,
                )
        self.SyncAudiences = channel.unary_unary(
                '/qwak.audience.v1.AudienceAPI/SyncAudiences',
                request_serializer=qwak_dot_audience_dot_v1_dot_audience__api__pb2.SyncAudiencesRequest.SerializeToString,
                response_deserializer=qwak_dot_audience_dot_v1_dot_audience__api__pb2.SyncAudiencesResponse.FromString,
                )


class AudienceAPIServicer(object):
    """Audience API
    """

    def CreateAudience(self, request, context):
        """Create audience
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateAudience(self, request, context):
        """Update audience by ID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAudience(self, request, context):
        """Get audience by ID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAudience(self, request, context):
        """List audiences by model ID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAudience(self, request, context):
        """Delete audience by ID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SyncAudiences(self, request, context):
        """Sync DB <-> Proxy configuration for a specific environment
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AudienceAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateAudience': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateAudience,
                    request_deserializer=qwak_dot_audience_dot_v1_dot_audience__api__pb2.CreateAudienceRequest.FromString,
                    response_serializer=qwak_dot_audience_dot_v1_dot_audience__api__pb2.CreateAudienceResponse.SerializeToString,
            ),
            'UpdateAudience': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateAudience,
                    request_deserializer=qwak_dot_audience_dot_v1_dot_audience__api__pb2.UpdateAudienceRequest.FromString,
                    response_serializer=qwak_dot_audience_dot_v1_dot_audience__api__pb2.UpdateAudienceResponse.SerializeToString,
            ),
            'GetAudience': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAudience,
                    request_deserializer=qwak_dot_audience_dot_v1_dot_audience__api__pb2.GetAudienceRequest.FromString,
                    response_serializer=qwak_dot_audience_dot_v1_dot_audience__api__pb2.GetAudienceResponse.SerializeToString,
            ),
            'ListAudience': grpc.unary_unary_rpc_method_handler(
                    servicer.ListAudience,
                    request_deserializer=qwak_dot_audience_dot_v1_dot_audience__api__pb2.ListAudienceRequest.FromString,
                    response_serializer=qwak_dot_audience_dot_v1_dot_audience__api__pb2.ListAudienceResponse.SerializeToString,
            ),
            'DeleteAudience': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAudience,
                    request_deserializer=qwak_dot_audience_dot_v1_dot_audience__api__pb2.DeleteAudienceRequest.FromString,
                    response_serializer=qwak_dot_audience_dot_v1_dot_audience__api__pb2.DeleteAudienceResponse.SerializeToString,
            ),
            'SyncAudiences': grpc.unary_unary_rpc_method_handler(
                    servicer.SyncAudiences,
                    request_deserializer=qwak_dot_audience_dot_v1_dot_audience__api__pb2.SyncAudiencesRequest.FromString,
                    response_serializer=qwak_dot_audience_dot_v1_dot_audience__api__pb2.SyncAudiencesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'qwak.audience.v1.AudienceAPI', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AudienceAPI(object):
    """Audience API
    """

    @staticmethod
    def CreateAudience(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qwak.audience.v1.AudienceAPI/CreateAudience',
            qwak_dot_audience_dot_v1_dot_audience__api__pb2.CreateAudienceRequest.SerializeToString,
            qwak_dot_audience_dot_v1_dot_audience__api__pb2.CreateAudienceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateAudience(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qwak.audience.v1.AudienceAPI/UpdateAudience',
            qwak_dot_audience_dot_v1_dot_audience__api__pb2.UpdateAudienceRequest.SerializeToString,
            qwak_dot_audience_dot_v1_dot_audience__api__pb2.UpdateAudienceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAudience(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qwak.audience.v1.AudienceAPI/GetAudience',
            qwak_dot_audience_dot_v1_dot_audience__api__pb2.GetAudienceRequest.SerializeToString,
            qwak_dot_audience_dot_v1_dot_audience__api__pb2.GetAudienceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListAudience(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qwak.audience.v1.AudienceAPI/ListAudience',
            qwak_dot_audience_dot_v1_dot_audience__api__pb2.ListAudienceRequest.SerializeToString,
            qwak_dot_audience_dot_v1_dot_audience__api__pb2.ListAudienceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteAudience(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qwak.audience.v1.AudienceAPI/DeleteAudience',
            qwak_dot_audience_dot_v1_dot_audience__api__pb2.DeleteAudienceRequest.SerializeToString,
            qwak_dot_audience_dot_v1_dot_audience__api__pb2.DeleteAudienceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SyncAudiences(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qwak.audience.v1.AudienceAPI/SyncAudiences',
            qwak_dot_audience_dot_v1_dot_audience__api__pb2.SyncAudiencesRequest.SerializeToString,
            qwak_dot_audience_dot_v1_dot_audience__api__pb2.SyncAudiencesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
