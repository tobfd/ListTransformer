from enum import Enum


class Splits(Enum):
    comma = 0
    space = 1


class Typ(Enum):
    auto = 0
    comma = 1
    space = 2


class Tools(Enum):
    same = 0
    no_same = 1
