from datatype.enums import WordBonus
from datetime import datetime

class Suggestion:
    def __init__(self, word):
        self.word = word
        self.score = 1 if len(word) == 4 else len(word)
    
    def get_score(self):
        return self.score if self.score < 7 else self.score + WordBonus.PANGRAM 

    def to_string(self):
        return self.word + '-' + self.get_score

class Game:
    def __init__(self):
        self.suggestions = []   # No limits at the moment
        self.timestamp = datetime.now()

    def add_suggestion(self, suggestion):
        self.suggestions.append(Suggestion(suggestion.word))

    def get_total(self):
        total = 0
        for sug in self.suggestions:
            total += sug.get_score()
        return total

    def to_string(self):
        output = ""
        for sug in self.suggestions:
            output += sug.to_string() + " "
        return output