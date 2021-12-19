import logging
import grpc
import tools
import time
import spelling_bee_game_pb2 as spelling_bee_game_pb2
import spelling_bee_game_pb2_grpc as spelling_bee_game_pb2_grpc

# export PYTHONPATH="/home/emer/Assignments/DistSystPrg/ass1SpellingBee"

def onStart():
    menu = "Choose an option:\n" \
            "- 1. Create Game\n- 2. Join Game\n- 3. Exit.\n"\
            "=> " 
    return tools.rangeInt(menu, 1, 3)
    
    
def createGame(stub, name):
    response = stub.CreateGame(spelling_bee_game_pb2.GameRequest(userName=name, gameType="Spelling Bee Multi player"))
    print(f"Game created with id: {response.gameId}")
    while True:
        print("Waiting for players to join the lobby.")
        time.sleep(4)
        gameStatus = stub.GameStatus(spelling_bee_game_pb2.StatusRequest(gameId=response.gameId))
        if (gameStatus.playerCount>1):
            choice = tools.binaryOption(f"{gameStatus.playerCount} players are in the lobby.\nStart the Game (y, n)?\n=> ", "y", "n")
            if (choice == "y"):
                stub.FinalizeGame(spelling_bee_game_pb2.FinalizeRequest(gameId=response.gameId))
                print("Game is starting!")
                return response.playerIndex, response.gameId


def joinGame(stub, name):
    while True:
        game = tools.readNonemptyString("Please input game Id:\n=> ")
        response = stub.RegisterPlayer(spelling_bee_game_pb2.RegisterRequest(gameId=game, userName=name))
        if (response.playerIndex != -1):
            print("Joined lobby!")
            while True:
                time.sleep(4)
                gameStatus = stub.GameStatus(spelling_bee_game_pb2.StatusRequest(gameId=game))
                if (gameStatus.status):
                    print("Joining game!")
                    return response.playerIndex, game, gameStatus.pangram
                else:
                    print("Waiting for the game to start")  
        else:
            print(f"Game with Id '{game}' couldn't be found or username '{name}' is already used in the game!")


def startGame(stub, name, playerIndex, pangram, game):
    while True:
        print('\n'+pangram)
        word_input = input("suggestion => ")
        my_suggestion = spelling_bee_game_pb2.Word(word=word_input.lower())
        response = stub.ProcessSuggestion(spelling_bee_game_pb2.SuggestionRequest(gameId=game, playerIndex=playerIndex, suggestion=my_suggestion))
        print(f"\n{response.message}")
        if response.result:
            print(f"\nGame over {name}!")
            break
    

def run():
    channel = grpc.insecure_channel('127.0.0.1:50055')
    stub = spelling_bee_game_pb2_grpc.SpellingBeeGameStub(channel)
    name = input("Input username => ")
    print(f"Welcome {name}, let's have a game of multi player spelling bee!\n" \
        f"You can guess up to 30 words. Have a good game :)")
    
    choice = onStart()
    playerIndex = None
    
    if (choice == 1):
        playerIndex, game = createGame(stub, name)
        pangram = stub.GameStatus(spelling_bee_game_pb2.StatusRequest(gameId=game)).pangram
    elif (choice == 2):
        playerIndex, game, pangram = joinGame(stub, name)
    
    startGame(stub, name, playerIndex, pangram, game)
    
        
if __name__ == '__main__':
    logging.basicConfig()
    run()
