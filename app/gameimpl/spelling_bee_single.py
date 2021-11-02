from service.game_service import GameSuggestionTemplate
from service.game_service import GameManager
from datatype.enums import GameStatus
from dao.spelling_bee_dao import SpellingBeeDao
STARTING_TOTAL = 0


class SpellingBeeGameSingle(GameManager, GameSuggestionTemplate):

    def __init__(self):
        super().__init__()
        self.pangram = ""
        self.letter = ""
        self.score = 0
        self.dao = None
        self.words = {}

    def post_init(self):
        self.dao = SpellingBeeDao.get_instance()
        self.pangram, self.letter = self.dao.get_pangram()
        self.game.status = GameStatus.IN_PROGRESS

    def validate_suggestion(self, player_index, suggestion):
        if self.game.status is not GameStatus.IN_PROGRESS:
            return False, "Game is not in progress."

        if len(suggestion.word) < 4:
            return False, "Word must be 4 letters minimum."

        if not self.dao.check_word(suggestion.word):
            return False, "This is not a valid word."

        if suggestion.word in self.words:
            return False, "You already made that suggestion."

        return True, None

    def check_ending_condition(self, player_index, suggestion):
        """returns True when it's the last suggestion or False if it keeps going
        :param player_index: position of player
        :param suggestion: the word with it's score
        :return: True or False
        """
        self.score += suggestion.get_score()
        self.words[suggestion.word] = ""
        print(f"Adding {self.words} for {suggestion.get_score()} points.")

        if len(self.words) == 30:
            self.game.status = GameStatus.FINISHED
            return True

        return False

    def record_statistics(self, player_index, suggestion, result):
        self.game.suggestions[player_index].append(suggestion)

        if result is True:
            self.game.winning_word = suggestion.word
            self.game.winning_player_index = player_index

    def format_summary(self, player_index, suggestion):
        return f"Last word was {suggestion.word} with a score of {suggestion.get_score()} points." \
            f"\nYou can suggest {len(self.words) - 30} more words."


class SpellingBeeGameBuilder:
    """
    This could be extended to include dynamic key-value pair parameters (see object_factory.py),
    or make it a singleton, etc.
    """

    def __init__(self):
        pass

    def __call__(self):
        return SpellingBeeGameSingle()
