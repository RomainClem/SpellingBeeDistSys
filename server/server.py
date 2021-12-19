import logging
import time
from concurrent import futures
from google.protobuf import message

import grpc

import gameimpl.spelling_bee_single as spelling_bee_single
from spelling_bee_game_pb2 import GameResponse, FinalizeResponse, SuggestionResponse, Word, RegisterResponse, StatusResponse
from spelling_bee_game_pb2_grpc import SpellingBeeGameServicer, add_SpellingBeeGameServicer_to_server
from game_registry import GameRegistry
from domain import spelling_bee_game, suggestion
from pattern import object_factory
from datatype.enums import GameStatus

class SpellingBeeServer(SpellingBeeGameServicer):

    def __init__(self):
        self.game_type = "Spelling Bee Single player"
        self.factory = object_factory.ObjectFactory()
        self.factory.register_builder(
            "Spelling Bee Single player", spelling_bee_single.SpellingBeeGameBuilder())
        self.registry = GameRegistry.get_instance()

    def CreateGame(self, request, context):
        print("in create game")
        new_game = self.factory.create(request.gameType)
        game = spelling_bee_game.SpellingBeeGame()
        game.register_player(request.userName)
        new_game.set_game(game)
        game_id = self.registry.add_game(new_game)
        print("Created game: " + game_id)
        return GameResponse(gameId=game_id)
    
    def RegisterPlayer(self, request, context):
        print("in register player")
        game = self.registry.get_game(request.gameId)
        playerIndex = -1 if game == -1 else game.game.register_player(request.userName)
        return RegisterResponse(playerIndex=playerIndex)
    
    def GameStatus(self, request, context):
        # print("in game status") # commented out to avoid spam in server
        game = self.registry.get_game(request.gameId)
        myPangram = game.retrieve_pangram() if game.retrieve_pangram() else ""
        status = True if game.game.status == GameStatus.IN_PROGRESS else False
        playerCount = len(game.game.players);
        return StatusResponse(playerCount=playerCount, pangram=myPangram, status=status)
    
    def FinalizeGame(self, request, context):
        print("in finalize")
        game = self.registry.get_game(request.gameId)
        game.finalize_setup()
        return FinalizeResponse()
    
    def ProcessSuggestion(self, request, context):
        print("In 'visit' for: " + str(request.gameId))
        my_suggestion = suggestion.Suggestion(request.suggestion)
        game = self.registry.get_game(request.gameId)
        result, response = game.process_suggestion(
            request.playerIndex, my_suggestion)
        return SuggestionResponse(result=result, message=response)
        
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_SpellingBeeGameServicer_to_server(SpellingBeeServer(), server)
    server.add_insecure_port('[::]:50055')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
