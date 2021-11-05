class Suggestion:
    def __init__(self, Word):
        self.word = Word.word
        self.score = 1 if len(Word.word) == 4 else len(Word.word)
    
    def get_score(self):
        return self.score

    def to_string(self):
        return self.word + '-' + self.get_score