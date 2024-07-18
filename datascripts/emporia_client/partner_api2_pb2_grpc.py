# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import partner_api2_pb2 as partner__api2__pb2


class PartnerApiStub(object):
    """*
    The methods available from the Emporia Energy Partner API.  The Emporia API is available via gRPC at
    URL:  partner-api.emporiaenergy.com 
    PORT: 50052				

    The deprecated V1 of the API is available on port 50051

    Clients should be prepared to handle the following errors:
    		Status.UNAUTHENTICATED if the auth_token is invalid
    		Status.INVALID_ARGUMENT and a description of the problem if the request is invalid

    The changes from the v1 of the PartnerApi:
    		the package name changed from protos to emporiaenergy.partner_api_2
    		methods no longer include a ResultStatus enum, authorization errors are indicated via onError
    		Adding support for listing and controlling Emporia EVChargers and Batteries

    The Update methods for EVChargers and Batteries take a settings structure that allows the caller to specify one 
    or more settings to change.  Anything that is not specified isn't changed by the update call.  This requires using
    Google's protobuf wrappers such as BoolValue rather than bool since with a plain bool we can't tell if it was 
    set to false or not set at all.     
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Authenticate = channel.unary_unary(
                '/emporiaenergy.partner_api_2.PartnerApi/Authenticate',
                request_serializer=partner__api2__pb2.AuthenticationRequest.SerializeToString,
                response_deserializer=partner__api2__pb2.AuthenticationResponse.FromString,
                )
        self.GetDevices = channel.unary_unary(
                '/emporiaenergy.partner_api_2.PartnerApi/GetDevices',
                request_serializer=partner__api2__pb2.DeviceInventoryRequest.SerializeToString,
                response_deserializer=partner__api2__pb2.DeviceInventoryResponse.FromString,
                )
        self.GetUsageData = channel.unary_unary(
                '/emporiaenergy.partner_api_2.PartnerApi/GetUsageData',
                request_serializer=partner__api2__pb2.DeviceUsageRequest.SerializeToString,
                response_deserializer=partner__api2__pb2.DeviceUsageResponse.FromString,
                )
        self.ListUtilityConnects = channel.unary_unary(
                '/emporiaenergy.partner_api_2.PartnerApi/ListUtilityConnects',
                request_serializer=partner__api2__pb2.ListDevicesRequest.SerializeToString,
                response_deserializer=partner__api2__pb2.UtilityConnectsResponse.FromString,
                )
        self.ListOutlets = channel.unary_unary(
                '/emporiaenergy.partner_api_2.PartnerApi/ListOutlets',
                request_serializer=partner__api2__pb2.ListDevicesRequest.SerializeToString,
                response_deserializer=partner__api2__pb2.OutletsResponse.FromString,
                )
        self.UpdateOutlets = channel.unary_unary(
                '/emporiaenergy.partner_api_2.PartnerApi/UpdateOutlets',
                request_serializer=partner__api2__pb2.UpdateOutletsRequest.SerializeToString,
                response_deserializer=partner__api2__pb2.OutletsResponse.FromString,
                )
        self.ListEVChargers = channel.unary_unary(
                '/emporiaenergy.partner_api_2.PartnerApi/ListEVChargers',
                request_serializer=partner__api2__pb2.ListDevicesRequest.SerializeToString,
                response_deserializer=partner__api2__pb2.EVChargersResponse.FromString,
                )
        self.UpdateEVChargers = channel.unary_unary(
                '/emporiaenergy.partner_api_2.PartnerApi/UpdateEVChargers',
                request_serializer=partner__api2__pb2.UpdateEVChargersRequest.SerializeToString,
                response_deserializer=partner__api2__pb2.EVChargersResponse.FromString,
                )
        self.ListBatteries = channel.unary_unary(
                '/emporiaenergy.partner_api_2.PartnerApi/ListBatteries',
                request_serializer=partner__api2__pb2.ListDevicesRequest.SerializeToString,
                response_deserializer=partner__api2__pb2.BatteriesResponse.FromString,
                )
        self.UpdateBatteries = channel.unary_unary(
                '/emporiaenergy.partner_api_2.PartnerApi/UpdateBatteries',
                request_serializer=partner__api2__pb2.UpdateBatteriesRequest.SerializeToString,
                response_deserializer=partner__api2__pb2.BatteriesResponse.FromString,
                )


class PartnerApiServicer(object):
    """*
    The methods available from the Emporia Energy Partner API.  The Emporia API is available via gRPC at
    URL:  partner-api.emporiaenergy.com 
    PORT: 50052				

    The deprecated V1 of the API is available on port 50051

    Clients should be prepared to handle the following errors:
    		Status.UNAUTHENTICATED if the auth_token is invalid
    		Status.INVALID_ARGUMENT and a description of the problem if the request is invalid

    The changes from the v1 of the PartnerApi:
    		the package name changed from protos to emporiaenergy.partner_api_2
    		methods no longer include a ResultStatus enum, authorization errors are indicated via onError
    		Adding support for listing and controlling Emporia EVChargers and Batteries

    The Update methods for EVChargers and Batteries take a settings structure that allows the caller to specify one 
    or more settings to change.  Anything that is not specified isn't changed by the update call.  This requires using
    Google's protobuf wrappers such as BoolValue rather than bool since with a plain bool we can't tell if it was 
    set to false or not set at all.     
    """

    def Authenticate(self, request, context):
        """login with the email and password you use on the portal website and get back an auth_token
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDevices(self, request, context):
        """get the collection of devices associated to your partner account, 
        optionally limited to devices related to one or more customer emails
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUsageData(self, request, context):
        """get usage data for one or more devices
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListUtilityConnects(self, request, context):
        """get the details for one or more Utility Connect devices
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOutlets(self, request, context):
        """get the details for one or more Outlets, specifically if they are on or off
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateOutlets(self, request, context):
        """Set one or more Outlets to be on or off.  
        Only the devices that were changed will be included in the response; devices that
        aren't connected to the cloud or were already in the requested state won't be included
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListEVChargers(self, request, context):
        """returns details about the specified EVChargers
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateEVChargers(self, request, context):
        """change the settings for one or more EVChargers
        Only the devices that were changed will be included in the response; devices that
        aren't connected to the cloud or were already in the requested state won't be included
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListBatteries(self, request, context):
        """returns details about the specified Batteries
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateBatteries(self, request, context):
        """change the settings for a single Battery 
        Only the devices that were changed will be included in the response; devices that
        aren't connected to the cloud or were already in the requested state won't be included
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PartnerApiServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Authenticate': grpc.unary_unary_rpc_method_handler(
                    servicer.Authenticate,
                    request_deserializer=partner__api2__pb2.AuthenticationRequest.FromString,
                    response_serializer=partner__api2__pb2.AuthenticationResponse.SerializeToString,
            ),
            'GetDevices': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDevices,
                    request_deserializer=partner__api2__pb2.DeviceInventoryRequest.FromString,
                    response_serializer=partner__api2__pb2.DeviceInventoryResponse.SerializeToString,
            ),
            'GetUsageData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUsageData,
                    request_deserializer=partner__api2__pb2.DeviceUsageRequest.FromString,
                    response_serializer=partner__api2__pb2.DeviceUsageResponse.SerializeToString,
            ),
            'ListUtilityConnects': grpc.unary_unary_rpc_method_handler(
                    servicer.ListUtilityConnects,
                    request_deserializer=partner__api2__pb2.ListDevicesRequest.FromString,
                    response_serializer=partner__api2__pb2.UtilityConnectsResponse.SerializeToString,
            ),
            'ListOutlets': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOutlets,
                    request_deserializer=partner__api2__pb2.ListDevicesRequest.FromString,
                    response_serializer=partner__api2__pb2.OutletsResponse.SerializeToString,
            ),
            'UpdateOutlets': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateOutlets,
                    request_deserializer=partner__api2__pb2.UpdateOutletsRequest.FromString,
                    response_serializer=partner__api2__pb2.OutletsResponse.SerializeToString,
            ),
            'ListEVChargers': grpc.unary_unary_rpc_method_handler(
                    servicer.ListEVChargers,
                    request_deserializer=partner__api2__pb2.ListDevicesRequest.FromString,
                    response_serializer=partner__api2__pb2.EVChargersResponse.SerializeToString,
            ),
            'UpdateEVChargers': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateEVChargers,
                    request_deserializer=partner__api2__pb2.UpdateEVChargersRequest.FromString,
                    response_serializer=partner__api2__pb2.EVChargersResponse.SerializeToString,
            ),
            'ListBatteries': grpc.unary_unary_rpc_method_handler(
                    servicer.ListBatteries,
                    request_deserializer=partner__api2__pb2.ListDevicesRequest.FromString,
                    response_serializer=partner__api2__pb2.BatteriesResponse.SerializeToString,
            ),
            'UpdateBatteries': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateBatteries,
                    request_deserializer=partner__api2__pb2.UpdateBatteriesRequest.FromString,
                    response_serializer=partner__api2__pb2.BatteriesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'emporiaenergy.partner_api_2.PartnerApi', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PartnerApi(object):
    """*
    The methods available from the Emporia Energy Partner API.  The Emporia API is available via gRPC at
    URL:  partner-api.emporiaenergy.com 
    PORT: 50052				

    The deprecated V1 of the API is available on port 50051

    Clients should be prepared to handle the following errors:
    		Status.UNAUTHENTICATED if the auth_token is invalid
    		Status.INVALID_ARGUMENT and a description of the problem if the request is invalid

    The changes from the v1 of the PartnerApi:
    		the package name changed from protos to emporiaenergy.partner_api_2
    		methods no longer include a ResultStatus enum, authorization errors are indicated via onError
    		Adding support for listing and controlling Emporia EVChargers and Batteries

    The Update methods for EVChargers and Batteries take a settings structure that allows the caller to specify one 
    or more settings to change.  Anything that is not specified isn't changed by the update call.  This requires using
    Google's protobuf wrappers such as BoolValue rather than bool since with a plain bool we can't tell if it was 
    set to false or not set at all.     
    """

    @staticmethod
    def Authenticate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/emporiaenergy.partner_api_2.PartnerApi/Authenticate',
            partner__api2__pb2.AuthenticationRequest.SerializeToString,
            partner__api2__pb2.AuthenticationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDevices(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/emporiaenergy.partner_api_2.PartnerApi/GetDevices',
            partner__api2__pb2.DeviceInventoryRequest.SerializeToString,
            partner__api2__pb2.DeviceInventoryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUsageData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/emporiaenergy.partner_api_2.PartnerApi/GetUsageData',
            partner__api2__pb2.DeviceUsageRequest.SerializeToString,
            partner__api2__pb2.DeviceUsageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListUtilityConnects(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/emporiaenergy.partner_api_2.PartnerApi/ListUtilityConnects',
            partner__api2__pb2.ListDevicesRequest.SerializeToString,
            partner__api2__pb2.UtilityConnectsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListOutlets(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/emporiaenergy.partner_api_2.PartnerApi/ListOutlets',
            partner__api2__pb2.ListDevicesRequest.SerializeToString,
            partner__api2__pb2.OutletsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateOutlets(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/emporiaenergy.partner_api_2.PartnerApi/UpdateOutlets',
            partner__api2__pb2.UpdateOutletsRequest.SerializeToString,
            partner__api2__pb2.OutletsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListEVChargers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/emporiaenergy.partner_api_2.PartnerApi/ListEVChargers',
            partner__api2__pb2.ListDevicesRequest.SerializeToString,
            partner__api2__pb2.EVChargersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateEVChargers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/emporiaenergy.partner_api_2.PartnerApi/UpdateEVChargers',
            partner__api2__pb2.UpdateEVChargersRequest.SerializeToString,
            partner__api2__pb2.EVChargersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListBatteries(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/emporiaenergy.partner_api_2.PartnerApi/ListBatteries',
            partner__api2__pb2.ListDevicesRequest.SerializeToString,
            partner__api2__pb2.BatteriesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateBatteries(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/emporiaenergy.partner_api_2.PartnerApi/UpdateBatteries',
            partner__api2__pb2.UpdateBatteriesRequest.SerializeToString,
            partner__api2__pb2.BatteriesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
