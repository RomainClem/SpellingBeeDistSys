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
        """returns result (0 meaning game goes on, >0 meaning more than 30 guess has been done), response (info messages)
        Skeleton of operations to perform. DON'T override me.

        The Template Method defines a skeleton of an algorithm in an operation,
        and defers some steps to subclasses.
        """

        status, message = self.validate_suggestion(player_index, suggestion)
        if status is False:
            return -1, message

        # result stores which, if any, of the word that stop the game
        result = self.check_winning_condition(player_index, suggestion)

        self.record_statistics(player_index, suggestion, result)

        # Note: this violates the separation of concerns principle (we are mixing presentation logic in
        # with service / business logic - we should refactor, especially if we move to a GUI front-end
        return result, self.format_summary(player_index, suggestion)

    @abstractmethod
    def validate_suggestion(self, player_index, suggestion):
        """Primitive operation. You HAVE TO override me, I'm a placeholder."""
        pass

    @abstractmethod
    def check_winning_condition(self, player_index, suggestion):
        """Primitive operation. You HAVE TO override me, I'm a placeholder."""
        pass

    @abstractmethod
    def record_statistics(self, player_index, suggestion, result):
        """Primitive operation. You HAVE TO override me, I'm a placeholder."""
        pass

    @abstractmethod
    def format_summary(self, player_index, suggestion):
        """Primitive operation. You HAVE TO override me, I'm a placeholder."""
        pass

