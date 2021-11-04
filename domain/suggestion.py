from datetime import datetime

class Suggestion:
    def __init__(self, Word):
        self.word = Word.word
        self.score = 1 if len(Word.word) == 4 else len(Word.word)
    
    def get_score(self):
        return self.score

    def to_string(self):
        return self.word + '-' + self.get_score

# class Game:
#     def __init__(self):
#         self.suggestions = [] 
#         self.timestamp = datetime.now()

#     def add_suggestion(self, suggestion):
#         self.suggestions.append(Suggestion(suggestion.word))

#     def get_total(self):
#         total = 0
#         for sug in self.suggestions:
#             total += sug.get_score()
#         return total

#     def to_string(self):
#         output = ""
#         for sug in self.suggestions:
#             output += sug.to_string() + " "
#         return output
