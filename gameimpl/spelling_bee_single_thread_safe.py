from service.game_service import GameSuggestionTemplate
from service.game_service import GameManager
from datatype.enums import GameStatus
from dao.spelling_bee_dao_thread_safe import SpellingBeeDao
from datatype.enums import WordBonus
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
        self.dao = SpellingBeeDao().get_instance()
        self.pangram, self.letter = self.dao.get_pangram()
        self.game.status = GameStatus.IN_PROGRESS
    
    def get_pangram(self):
        unique_chars = list(set(self.pangram))
        unique_chars[unique_chars.index(self.letter)] = f"[{self.letter}]"
        return "".join(unique_chars)

    def validate_suggestion(self, player_index, suggestion):
        if self.game.status is not GameStatus.IN_PROGRESS:
            return False, "Game is not in progress."

        if len(suggestion.word) < 4:
            return False, "Word must be 4 letters minimum."

        if not self.dao.check_word(suggestion.word):
            return False, "This is not a valid word."

        if not (set(suggestion.word).issubset(set(self.pangram))):
            return False, "Only use letters from the pangram."

        if self.letter not in suggestion.word:
            return False, f"Only must use {self.letter}."

        if suggestion.word in self.words:
            return False, "You already made that suggestion."

        return True, None

    def check_ending_condition(self, player_index, suggestion):
        """returns True when it's the last suggestion or False if it keeps going
        :param player_index: position of player
        :param suggestion: the word with it's score
        :return: True or False
        """
        bonus = 0
        if len(suggestion.word) > 6:
            if (len(set(suggestion.word).difference(set(self.pangram))) == 0):
                bonus = WordBonus.PANGRAM 

        self.score += suggestion.get_score() + bonus

        self.words[suggestion.word] = ""
        print(f"Found word: {self.words.keys()}\nTotal score: {self.score}")

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
            f"\nYou can suggest {30 - len(self.words)} additional words." \
            f"\nTotal score = {self.score}, found words {self.words.keys()}."


class SpellingBeeGameBuilder:
    """
    This could be extended to include dynamic key-value pair parameters (see object_factory.py),
    or make it a singleton, etc.
    """

    def __init__(self):
        pass

    def __call__(self):
        return SpellingBeeGameSingle()
