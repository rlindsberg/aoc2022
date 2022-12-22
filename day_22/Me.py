import re

import numpy as np

from day_22.enums import Facing, SquareType, get_key_facing_to_np_map, check_boundary, facing_to_np_map

_left_90_np = np.array([0, -1, 1, 0]).reshape(2, 2)
_right_90_np = np.array([0, 1, -1, 0]).reshape(2, 2)


class Me:
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

    def move_by_instructions(self, instr_str):
        instr_list = re.findall(r'[A-Za-z]+|\d+', instr_str)

        for inst in instr_list:
            print(inst)
            if inst == 'R':
                # if self.facing == Facing.EAST:
                #     self.facing = Facing.SOUTH
                # elif self.facing == Facing.SOUTH:
                #     self.facing = Facing.WEST
                # elif self.facing == Facing.WEST:
                #     self.facing = Facing.NORTH
                next_facing_np = _right_90_np @ facing_to_np_map[self.facing]

                # update robot direction
                self.facing = get_key_facing_to_np_map(next_facing_np)

            elif inst == 'L':
                next_facing_np = _left_90_np @ facing_to_np_map[self.facing]

                # update robot direction
                self.facing = get_key_facing_to_np_map(next_facing_np)

            else:
                self.move(int(inst))

    def compute_wrap_around_x_y(self) -> (int, int):
        # next_x, next_y = self.position[0], self.position[1]
        if self.facing == Facing.NORTH:
            next_y = self.position[1]
            for i in reversed(range(self.max_x)):
                if (i, next_y) in self.map_:
                    next_x = i
                    return next_x, next_y

        elif self.facing == Facing.SOUTH:
            next_y = self.position[1]
            for i in range(self.max_x):
                if (i, next_y) in self.map_:
                    next_x = i
                    return next_x, next_y

        elif self.facing == Facing.EAST:
            next_x = self.position[0]
            for j in range(self.max_y):
                if (next_x, j) in self.map_:
                    next_y = j
                    return next_x, next_y
        else:
            next_x = self.position[0]
            for j in reversed(range(self.max_y)):
                if (next_x, j) in self.map_:
                    next_y = j
                    return next_x, next_y

        # return
        # if self.map_[(next_x, next_y)] == SquareType.WALL:
        #     return self.position
        # return next_x, next_y

    @check_boundary
    def move_one_step(self):
        # will check boundary before moving
        self.position += facing_to_np_map[self.facing]

    def move(self, n_steps):
        if n_steps == 8 and self.facing == Facing.WEST:
            # position is 189,1
            print('now')
        for i in range(n_steps):
            try:
                self.move_one_step()
            except ValueError:
                # do wrap around
                next_x, next_y = self.compute_wrap_around_x_y()
                self.position = np.array([next_x, next_y])
