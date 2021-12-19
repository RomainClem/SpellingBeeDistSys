class SpellingBeeGame:

    def __init__(self):
        self.active = True
        self.status = None
        self.players = []
        self.last_player_index = -1
        self.suggestions = []
        self.words = []
        self.scores = []
        self.winning_suggestions = -1
        self.winning_player_index = -1

    def register_player(self, username):
        print(self.players)
        if username not in self.players:
            index = len(self.players)
            self.players.append(username)
            self.suggestions.append([])
            self.words.append({})
            self.scores.append(0)
            return index
        else:
            return -1


"""
This is designed to accomodate multiple player for a single game. 
This could be updated and simplified for a single player Spelling Bee.
I will keep it as is for now, as I'd like to use the same or very similar logic for multi player and single player Spelling Bee.
"""
