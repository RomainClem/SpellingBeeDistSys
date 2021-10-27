from service.game_service import GameSuggestionTemplate
from service.game_service import GameManager
from datatype.enums import GameStatus, WordBonus, MatchStatus

STARTING_TOTAL = 0

class SpellingBeeGame(GameManager, GameSuggestionTemplate):

    def __init__(self):
        super().__init__()
        self.scores = [] # List of each players scores
        self.words = [] # List of list of each players found word
        self.averageLength = [] # List of average word length for each players

    def post_init(self):
        for i in range(0, len(self.match.players)):
            self.scores.append(STARTING_TOTAL)  # Might want to parameterize the starting total
            self.words.append(None)
            self.averageLength.append(None)
        self.game.status = GameStatus.IN_PROGRESS
