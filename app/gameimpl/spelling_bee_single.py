from service.game_service import GameSuggestionTemplate
from service.game_service import GameManager
from datatype.enums import GameStatus

STARTING_TOTAL = 0

class SpellingBeeGameSingle(GameManager, GameSuggestionTemplate):

    def __init__(self):
        super().__init__()
        self.pangram = ""
        self.letter = ""
        self.scores = 0 
        self.words = {}
        self.averageLength = 0 # List of average word length for each players

    def post_init(self):
        # self.pangram, self.letter = 
        # self.scores.append(STARTING_TOTAL)  # Might want to parameterize the starting total
        # self.averageLength.append(None)
        self.game.status = GameStatus.IN_PROGRESS

    def validate_suggestion(self, player_index, suggestion):
        if self.game.status is not GameStatus.IN_PROGRESS:
            return False, "Game is not in progress."

        if len(suggestion.word) < 4:
            return False, "Word must be 4 letters minimum."
        
        if suggestion.word in self.words:
            return False, "You already made that suggestion."

        

