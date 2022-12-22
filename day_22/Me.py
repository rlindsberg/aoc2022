import numpy as np

from enums import Facing, SquareType

_left_90_np = np.array([0, -1, 1, 0]).reshape(2, 2)
_right_90_np = np.array([0, 1, -1, 0]).reshape(2, 2)

class Me:
    def __init__(self, my_map):
        self.map_ = my_map
        x, y = self.compute_init_position()
        self.position = np.array([x, y])
        self.facing = Facing.EAST

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
                self.position = _right_90_np @ self.position

            elif inst == 'L':
                self.position = _left_90_np @ self.position

            else:
                self.move_step(int(inst))

    def move_step(self, n_steps):
        # for i in range(n_steps):

        pass


