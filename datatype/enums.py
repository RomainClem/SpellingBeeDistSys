from enum import IntEnum


class WordBonus(IntEnum):
    PANGRAM = 7


class GameStatus(IntEnum):
    INVALID = 0
    WAITING = 1
    IN_PROGRESS = 2
    FINISHED = 3