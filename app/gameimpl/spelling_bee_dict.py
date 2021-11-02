import json
from random import choice

class SpellingBeeDictionnary():
    
    def __init__(self):
        super().__init__()
        self.wordDictionnary = {}
        self.pangramsDictionnary = {}

    def post_init(self):
        with open('./assets/pangrams.json') as f:
            self.pangramsDictionnary = json.load(f)
        
        with open('./assets/words_dictionary.json') as f:
            self.wordDictionnary = json.load(f)




random_pangram = choice(list(pangrams.keys()))
random_letter = choice(list(set(random_pangram)))

