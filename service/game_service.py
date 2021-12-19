from abc import ABC, abstractmethod

class GameManager(ABC):

    def __init__(self):
        self.game = None

    def set_game(self, game):
        self.game = game
        # self.post_init()    # initialise whatever is specific to the match type

    def end_game(self):
        self.game.active = False
    
    def finalize_setup(self):
        self.post_init()


    @abstractmethod
    def post_init(self):
        pass


class GameSuggestionTemplate(ABC):

    def process_suggestion(self, player_index, suggestion):
        """returns result (True meaning game goes on, False meaning more than 30 guess has been done), response (info messages)
        Skeleton of operations to perform. DON'T override me.

        The Template Method defines a skeleton of an algorithm in an operation,
        and defers some steps to subclasses.
        """

        status, player = self.check_game_status()
        if status:
            return True, f"{player} finished the game!"
        
        result, message = self.validate_suggestion(suggestion, player_index)
        
        if result is False:
            return False, message
        
        # Here return if the word is a pangram. This could be updated to return a 'bonus' enum and allow more scaling
        pangram = self.record_statistics(player_index, suggestion)

        # result stores if the game is over
        result = self.check_ending_condition(suggestion, player_index)

        # Note: this violates the separation of concerns principle (we are mixing presentation logic in
        # with service / business logic - we should refactor, especially if we move to a GUI front-end
        return result, self.format_summary(suggestion, player_index, pangram)

    def retrieve_pangram(self):
        return self.get_pangram()

    @abstractmethod
    def get_pangram(self):
        """Primitive operation. You HAVE TO override me, I'm a placeholder."""
        pass
    
    @abstractmethod
    def validate_suggestion(self, suggestion, player_index):
        """Primitive operation. You HAVE TO override me, I'm a placeholder."""
        pass

    @abstractmethod
    def check_ending_condition(self, suggestion,player_index):
        """Primitive operation. You HAVE TO override me, I'm a placeholder."""
        pass

    @abstractmethod
    def record_statistics(self, player_index, suggestion):
        """Primitive operation. You HAVE TO override me, I'm a placeholder."""
        pass

    @abstractmethod
    def format_summary(self, suggestion, player_index, pangram):
        """Primitive operation. You HAVE TO override me, I'm a placeholder."""
        pass

    @abstractmethod
    def check_game_status(self):
        """Primitive operation. You HAVE TO override me, I'm a placeholder."""
        pass
