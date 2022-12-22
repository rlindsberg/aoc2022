import re

import numpy as np

from day_22.util_functions import Facing, SquareType, get_key_facing_to_np_map, check_boundary, facing_to_np_map

_left_90_np = np.array([0, -1, 1, 0]).reshape(2, 2)
_right_90_np = np.array([0, 1, -1, 0]).reshape(2, 2)


class Person:
    def __init__(self, my_map, max_x, max_y):
        self.map_ = my_map
        x, y = self.compute_init_position()
        self.position = np.array([x, y])
        self.facing = Facing.EAST

        self.max_x = max_x
        self.max_y = max_y

    def compute_init_position(self):
        for k, v in self.map_.items():
            if v == SquareType.TILE:
                # this is the start position
                return k[0], k[1]
