from enum import Enum, auto


class Facing(Enum):
    NORTH = auto()
    EAST = auto()
    SOUTH = auto()
    WEST = auto()


class SquareType(Enum):
    TILE = auto()
    WALL = auto()
    EMPTY = auto()
