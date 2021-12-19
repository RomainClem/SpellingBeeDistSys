from service.game_service import GameSuggestionTemplate
from service.game_service import GameManager
from datatype.enums import GameStatus
from dao.spelling_bee_dao_singleton import SpellingBeeDao
from datatype.enums import WordBonus

class SpellingBeeGameSingle(GameManager, GameSuggestionTemplate):

    def __init__(self):
        super().__init__()
        self.pangram = ""
        self.letter = ""
        self.dao = None

    def post_init(self):
        self.dao = SpellingBeeDao.get_instance()
        self.pangram, self.letter = self.dao.get_pangram()
        self.game.status = GameStatus.IN_PROGRESS
    
    def get_pangram(self):
        if self.pangram == "": return "" # Security if pangram hasn't been set yet
        unique_chars = list(set(self.pangram))
        unique_chars[unique_chars.index(self.letter)] = f"[{self.letter}]"
        return "".join(unique_chars)

    def check_game_status(self):
        return self.game.status == GameStatus.FINISHED
    
    def validate_suggestion(self, suggestion, player_index):
        if self.game.status is not GameStatus.IN_PROGRESS:
            return False, "Game is not in progress."

        if len(suggestion.word) < 4:
            return False, "Word must be 4 letters minimum."

        if not self.dao.check_word(suggestion.word):
            return False, "This is not a valid word."

        if not (set(suggestion.word).issubset(set(self.pangram))):
            return False, "Only use letters from the pangram."

        if self.letter not in suggestion.word:
            return False, f"You must use {self.letter} in your suggestion."

        if suggestion.word in self.game.words[player_index]:
            return False, "You already made that suggestion."

        return True, None

    def check_ending_condition(self, suggestion, player_index):
        """returns True when it's the last suggestion or False if it keeps going
        :param player_index: position of player
        :param suggestion: the word with it's score
        :return: True or False
        """
        self.game.suggestions[player_index].append(suggestion)
        if len(self.game.words[player_index]) == 30:
            self.game.status = GameStatus.FINISHED
            self.winning_suggestions = player_index
            self.game.winning_player_index = player_index
            return True

        return False

    def record_statistics(self, player_index, suggestion, result):
        """Records the statistics on the suggestion 
        Args:
            player_index ([int]): position of player
            suggestion ([object]): suggestion made by the player
            result ([bool]): result from ending condition (True - game over / False - Game continue)
        """        
        bonus = 0
        if len(suggestion.word) > 6:
            if (len(set(suggestion.word).difference(set(self.pangram))) == 0):
                bonus = WordBonus.PANGRAM 

        self.game.scores[player_index] += suggestion.get_score() + bonus

        self.game.words[player_index][suggestion.word] = ""
        print(f"Found word: {self.game.words[player_index].keys()}\nTotal score: {self.game.scores[player_index]}")

        return bonus > 0

    def format_summary(self, suggestion, player_index, pangram):
        score = suggestion.get_score()
        bonusWord = ""
        
        if pangram:
            score += WordBonus.PANGRAM
            bonusWord = "Pangram! "
            
        return f"{bonusWord}\"{suggestion.word}\" Score: {score}" \
            f"\nRemaining suggestions: {30 - len(self.game.words[player_index])}" \
            f"\nTotal score => {self.game.scores[player_index]}, found words: {list(self.game.words[player_index])}."


class SpellingBeeGameBuilder:
    """
    This could be extended to include dynamic key-value pair parameters (see object_factory.py),
    or make it a singleton, etc.
    """

    def __init__(self):
        pass

    def __call__(self):
        return SpellingBeeGameSingle()
