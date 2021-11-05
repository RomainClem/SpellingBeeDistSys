class SpellingBeeGame:

    def __init__(self):
        self.active = True
        self.players = []
        self.last_player_index = -1
        self.suggestions = []
        self.winning_word = -1
        self.winning_player_index = -1

    def register_player(self, username):
        print(self.players)
        if username not in self.players:
            index = len(self.players)
            self.players.append(username)
            self.suggestions.append([])
            return index
        else:
            return -1


# Remove unnecessary information here. Either store something or do a minimum.