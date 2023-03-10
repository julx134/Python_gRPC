# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import POST_STATUS_pb2 as POST__STATUS__pb2


class RoverStatusStub(object):
    """define PIN service
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendStatus = channel.unary_unary(
                '/RoverStatus/SendStatus',
                request_serializer=POST__STATUS__pb2.MessageStatus.SerializeToString,
                response_deserializer=POST__STATUS__pb2.AcknowledgementStatus.FromString,
                )


class RoverStatusServicer(object):
    """define PIN service
    """

    def SendStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RoverStatusServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.SendStatus,
                    request_deserializer=POST__STATUS__pb2.MessageStatus.FromString,
                    response_serializer=POST__STATUS__pb2.AcknowledgementStatus.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'RoverStatus', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RoverStatus(object):
    """define PIN service
    """

    @staticmethod
    def SendStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RoverStatus/SendStatus',
            POST__STATUS__pb2.MessageStatus.SerializeToString,
            POST__STATUS__pb2.AcknowledgementStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
