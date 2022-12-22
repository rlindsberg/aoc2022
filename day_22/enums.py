import functools
from enum import Enum, auto

import numpy as np


class Facing(Enum):
    NORTH = auto()
    EAST = auto()
    SOUTH = auto()
    WEST = auto()


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
        map_ = args[0].map_
        current_position = args[0].position
        current_facing = args[0].facing

        max_coordinate_x = args[0].max_x
        max_coordinate_y = args[0].max_y

        try_next_position = current_position + facing_to_np_map[current_facing]

        # ok
        if 1 <= try_next_position[0] <= max_coordinate_x and 1 <= try_next_position[1] <= max_coordinate_y:
            # do move one step
            func(*args, **kwargs)
        # wrap around
        elif try_next_position[0] > max_coordinate_x or try_next_position[0] <= 0 or \
                try_next_position[1] > max_coordinate_y or try_next_position[1] <= 0:
            raise ValueError('Out of map exception')

        # wall
        elif map_[(try_next_position[0], try_next_position[1])] == SquareType.WALL:
            print('cannot move into wall')
            return

    return my_wrapper
