""" This file collects some helper functions for solving puzzles.
"""
import functools

import numpy as np
from aocd import submit

from day_22.enums import Facing, SquareType


def get_day_and_part(file_name: str) -> (int, str):
    """for automated submission"""
    day_and_part = file_name.partition('_')[2]
    part = day_and_part[-4]
    day = day_and_part[:-5]

    return int(day), part


def submit_answer(my_answer, day: int, part: str):
    res = submit(my_answer, part=part, day=day, year=2022)
    print(res)


facing_to_np_map = {Facing.NORTH: np.array([0, 1]),
                    Facing.EAST: np.array([1, 0]),
                    Facing.SOUTH: np.array([0, -1]),
                    Facing.WEST: np.array([-1, 0])}


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
        # wall
        elif map_[(try_next_position[0], try_next_position[1])] == SquareType.WALL:
            print('cannot move into wall')
            return

        # wrap around
        else:
            raise ValueError('Out of map exception')
    return my_wrapper
