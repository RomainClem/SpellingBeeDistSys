import logging
import grpc

import spelling_bee_game_pb2 as spelling_bee_game_pb2
import spelling_bee_game_pb2_grpc as spelling_bee_game_pb2_grpc


def run():
    channel = grpc.insecure_channel('127.0.0.1:50055')
    stub = spelling_bee_game_pb2_grpc.SpellingBeeGameStub(channel)
    name = input("Input username => ")
    game = stub.CreateGame(spelling_bee_game_pb2.GameRequest(userName=name, gameType="Spelling Bee Single player")).gameId
    pangram = stub.FinalizeGame(spelling_bee_game_pb2.FinalizeRequest(gameId=game)).pangram

    while True:
        print(pangram)
        word_input = input("suggestion => ")
        my_suggestion = spelling_bee_game_pb2.Word(word=word_input.lower())
        response = stub.ProcessSuggestion(spelling_bee_game_pb2.SuggestionRequest(gameId=game, playerIndex=0, suggestion=my_suggestion))
        print(response.message)
        if response.result:
            print("Game over")
            break

        
if __name__ == '__main__':
    logging.basicConfig()
    run()
