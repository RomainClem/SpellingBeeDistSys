import logging
import time
from concurrent import futures
from google.protobuf import message

import grpc

from app.gameimpl import spelling_bee_single
from spelling_bee_game_pb2 import GameResponse, RegisterResponse, FinalizeResponse, SuggestionResponse, WatchRequest, WatchResponse, Player, Word

from spelling_bee_game_pb2_grpc import SpellingBeeGameServicer, add_SpellingBeeGameServicer_to_server
from app.server.game_registry import GameRegistry
from domain import spelling_bee_game, suggestion
from pattern import object_factory


class SpellingBeeServer(SpellingBeeGameServicer):

    def __init__(self):
        self.game_type = "Spelling Bee Single player"
        self.factory = object_factory.ObjectFactory()
        self.factory.register_builder(
            "Spelling Bee Single player", spelling_bee_single.SpellingBeeGameBuilder())
        self.registry = GameRegistry.get_instance()

    def ProcessSuggestion(self, request):
        print("In 'visit' for: " + str(request.gameId))
        my_suggestion = suggestion.Suggestion(request.suggestion)
        game = self.registry.get_game(request.gameId)
        result, response = game.process_suggestion(
            request.playerIndex, my_suggestion)
        return GameResponse(result=result, message=response)

    def RegisterPlayer(self, request):
        print("in register player")
        game = self.registry.get_game(request.gameId)
        player_index = game.game.register_player(request.userName)
        print(game.game.players)
        return RegisterResponse(player_index=player_index)

    def FinalizeGame(self, request):
        print("in finalize")
        self.registry.get_game(request.gameId).finalize_setup()
        return FinalizeResponse()

    def CreateGame(self, request):
        """
        This is stateless, i.e. no dedicated session for the game; must return the unique id of the game and this
        must be sent as a paramater with all requests. Like sessions on a multi-threaded webserver.
        :param request:
        :param context:
        :return game_id:
        """
        print("in create game")
        new_game = self.factory.create(request.gameType)
        game = spelling_bee_game.SpellingBeeGame()
        game.register_player(request.userName)
        new_game.set_game(game)
        game_id = self.registry.add_game(new_game)
        print("Created game: " + str(game_id.bytes))
        return GameResponse(gameId=game_id.bytes)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_SpellingBeeGameServicer_to_server(SpellingBeeServer(), server)
    server.add_insecure_port('[::]:50055')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
