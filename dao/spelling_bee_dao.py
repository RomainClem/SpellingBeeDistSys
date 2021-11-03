import json
from random import choice


class SpellingBeeDao:

    def __init__(self):
        super().__init__()
        self.wordDictionnary = {}
        self.pangramsDictionnary = {}

    def post_init(self):
        with open('assets/words_dictionary.json') as f:
            self.wordDictionnary = json.load(f)
        with open('assets/pangrams.json') as f:
            self.pangramsDictionnary = json.load(f)
        
    def get_pangram(self):
        random_pangram = choice(list(self.pangramsDictionnary.keys())) 
        random_letter = choice(list(set(random_pangram)))
        return random_pangram, random_letter

    def check_word(self, word):
        res = True if word in self.wordDictionnary else False
        return res
