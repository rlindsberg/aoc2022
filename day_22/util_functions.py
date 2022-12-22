import functools
from enum import Enum, auto

import numpy as np


# Facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^).
class Facing(Enum):
    NORTH = 3
    EAST = 0
    SOUTH = 1
    WEST = 2


class SquareType(Enum):
    TILE = auto()
    WALL = auto()
    EMPTY = auto()


facing_to_np_map = {Facing.NORTH: np.array([-1, 0]),
                    Facing.EAST: np.array([0, 1]),
                    Facing.SOUTH: np.array([1, 0]),
                    Facing.WEST: np.array([0, -1])}


# facing_to_np_map = {Facing.NORTH: np.array([0, 1]),
#                     Facing.EAST: np.array([1, 0]),
#                     Facing.SOUTH: np.array([0, -1]),
#                     Facing.WEST: np.array([-1, 0])}

def get_key_facing_to_np_map(next_direction_np) -> Facing or None:
    """
    This bad function is needed because ndarray is not hashable,
    so it's not possible to map from ndarray to enum.
    :param next_direction_np: a 2x2 numpy ndarray
    :return: the key of the matching key-value pair in facing_to_np_map
    """
    for key, val in facing_to_np_map.items():
        if np.array_equal(next_direction_np, val):
            return key
    return None


def check_boundary(func):
    """
    This decorator function makes sure that the player does not run into wall, or into empty space
    """
    # this preserves the function identity of func.
    @functools.wraps(func)
    def my_wrapper(*args, **kwargs):
        me = args[0]
        my_map = me.my_map

        current_position = me.position
        current_facing = me.facing

        try_next_position = current_position + facing_to_np_map[current_facing]

        # wrap around if this fails (raise exception)
        if my_map.map_array[try_next_position[0]][try_next_position[1]] == -1:
            # next is an empty space
            raise ValueError('Out of map exception')

        # wall
        if my_map.map_array[try_next_position[0]][try_next_position[1]] == 1:
            print('cannot move into wall')
            return

        # ok
        # do move one step
        func(*args, **kwargs)

    return my_wrapper
