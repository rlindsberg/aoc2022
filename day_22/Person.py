import re

import numpy as np

from day_22.util_functions import Facing, SquareType, get_key_facing_to_np_map, check_boundary, facing_to_np_map

_left_90_np = np.array([0, -1, 1, 0]).reshape(2, 2)
_right_90_np = np.array([0, 1, -1, 0]).reshape(2, 2)


class Person:
    """
    This class represents the player, or "you" as the AOC Puzzle says.
    """
    def __init__(self, my_map):
        self.my_map = my_map
        x, y = self.compute_init_position()
        self.position = np.array([x, y])
        self.facing = Facing.EAST

    def compute_init_position(self):
        """The init position is the first tile on the first row"""
        x = 0
        y = self.my_map.get_start_end_by_row[0][0]
        return x, y

    def move_by_instruction(self, instruction: str):
        """
        Break down the inst string into an iter, and move the player accordingly
        Turn left and turn right using transition matrix and matrix multiplication.
        Move step using an helper function.
        """
        for instr in instruction.replace("L", " L ").replace("R", " R ").split(" "):
            print(instr)
            if instr == 'R':
                # turn right
                # if self.facing == Facing.EAST:
                #     self.facing = Facing.SOUTH
                # elif self.facing == Facing.SOUTH:
                #     self.facing = Facing.WEST
                # elif self.facing == Facing.WEST:
                #     self.facing = Facing.NORTH
                next_facing_np = _right_90_np @ facing_to_np_map[self.facing]

                # update direction
                self.facing = get_key_facing_to_np_map(next_facing_np)

            elif instr == 'L':
                # turn left
                next_facing_np = _left_90_np @ facing_to_np_map[self.facing]

                # update direction
                self.facing = get_key_facing_to_np_map(next_facing_np)

            else:
                self.move(int(instr))

    def move(self, n_steps: int):
        """Move forward with n steps"""
        for i in range(n_steps):
            try:
                """Outcomes:
                1. the next step is a tile, everything ok
                2. a wall, they stays
                3. a empty space, then check if next position is a wall.
                    if not,
                        go to row start if facing east;
                        or go to row end if facing west;
                        or go to col start if facing south;
                        or go to col end if facing north
                """
                self.move_one_step()
            except ValueError:
                # do wrap around
                current_position = self.position
                current_facing = self.facing

                try_next_position = current_position + facing_to_np_map[current_facing]

                if self.my_map.map_array[try_next_position[0], try_next_position[1]] == 1:
                    return
                else:
                    current_row = current_position[0]
                    current_col = current_position[1]

                    row_start = self.my_map.get_start_end_by_row[current_row][0]
                    row_end = self.my_map.get_start_end_by_row[current_row][1]
                    col_start = self.my_map.get_start_end_by_column[current_col][0]
                    col_end = self.my_map.get_start_end_by_column[current_col][1]

                    """
                        go to row start if facing east;
                        or go to row end if facing west;
                        or go to col start if facing south;
                        or go to col end if facing north"""
                    if current_facing == Facing.EAST:
                        self.position[1] = row_start
                    elif current_facing == Facing.WEST:
                        self.position[1] = row_end
                    elif current_facing == Facing.NORTH:
                        self.position[0] = col_end
                    else:
                        self.position[0] = col_start

    @check_boundary
    def move_one_step(self):
        # will check boundary before moving
        self.position += facing_to_np_map[self.facing]

    def compute_score(self) -> int:
        """The puzzle uses 1-index, thus plus 1"""
        x = self.position[0] + 1
        y = self.position[1] + 1
        facing_value = self.facing.value

        # The final password is the sum of 1000 times the row, 4 times the column, and the facing.
        score = 1000 * x + 4 * y + facing_value

        return int(score)
