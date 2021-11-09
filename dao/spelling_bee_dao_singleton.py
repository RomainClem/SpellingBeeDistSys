import json
import threading
from random import choice


class SpellingBeeDao:
    __instance = None

    @staticmethod
    def get_instance():
        if SpellingBeeDao.__instance is None:
            with threading.Lock():
                if SpellingBeeDao.__instance is None:  # Double locking mechanism
                    SpellingBeeDao()
        return SpellingBeeDao.__instance

    def __init__(self):
        if SpellingBeeDao.__instance is not None:
            raise Exception("This is a singleton!")
        else:
            SpellingBeeDao.__instance = self
        super().__init__()
        self.lock = threading.Lock()
        self.wordDictionnary = {}
        with open('../assets/words_dictionary.json') as f:
            self.wordDictionnary = json.load(f)
        self.pangramsDictionnary = {}
        with open('../assets/pangrams.json') as f:
            self.pangramsDictionnary = json.load(f)

    def get_pangram(self):
        self.lock.acquire()
        random_pangram = choice(list(self.pangramsDictionnary.keys()))
        random_letter = choice(list(set(random_pangram)))
        self.lock.release()
        return random_pangram, random_letter

    def check_word(self, word):
        self.lock.acquire()
        res = True if word in self.wordDictionnary else False
        self.lock.release()
        return res
