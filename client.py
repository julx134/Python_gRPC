import sys

import grpc

import GET_COMMANDS_pb2
import GET_COMMANDS_pb2_grpc
import GET_MAP_pb2
import GET_MAP_pb2_grpc
import ast


# function that sends a request to grpc server to get map
def get_map():
    # establish channel and stub
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = GET_MAP_pb2_grpc.MapStub(channel)
        # send request
        response = stub.GetMap(GET_MAP_pb2.MapRequest(name="map.txt"))

        # return response -- ast.literal_eval is to clean-up string formatting to be converted back to list
        return response.row, response.col, list(ast.literal_eval(response.map))


# function to get stream of commands for rover
def get_rover_moves(rover_num):
    # establish channel and stub
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = GET_COMMANDS_pb2_grpc.RoverCommandsStub(channel)
        # send request
        response = stub.GetRoverMoves(GET_COMMANDS_pb2.RoverNum(rover_name=str(rover_num)))
        return response.commands


if __name__ == '__main__':
    rover_num = sys.argv[1]
    print(rover_num)
    row, col, map_list = get_map()
    rover_moves = get_rover_moves(rover_num)

    print(rover_moves)
