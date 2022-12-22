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
        for inst in instr_str:
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
                self.move_step(int(inst))

    @check_boundary
    def move_step(self, n_steps):
        for i in range(n_steps):
            try:
                # will check boundary before moving
                self.position += facing_to_np_map[self.facing]
            except ValueError:
                # do wrap around
                print(self.map_)
        pass
