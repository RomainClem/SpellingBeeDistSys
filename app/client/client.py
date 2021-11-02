import logging
import grpc

import spelling_bee_game_pb2 as spelling_bee_game_pb2
import spelling_bee_game_pb2_grpc as spelling_bee_game_pb2_grpc


def run():
    channel = grpc.insecure_channel('127.0.0.1:50055')
    stub = spelling_bee_game_pb2_grpc.SpellingBeeGameStub(channel)


if __name__ == '__main__':
    logging.basicConfig()
    run()
