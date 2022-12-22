from aocd.models import Puzzle

from day_22.Me import Me
from helpers import get_day_and_part, submit_answer

from day_22.enums import SquareType

my_map = {}


def draw_map(data):
    input_list = data.split("\n")
    max_x = 0,
    max_y = 0

    for idx, row in enumerate(input_list):
        # reached the end
        if row == '':
            instruction = input_list[-1]
            max_x = idx + 1
            return instruction, max_x, max_y

        row_idx = idx + 1
        for idx2, element in enumerate(row):
            column_idx = idx2 + 1
            if column_idx > max_y:
                max_y = column_idx

            # empty
            if element == ' ':
                my_map[(row_idx, column_idx)] = SquareType.EMPTY
            elif element == '.':
                my_map[(row_idx, column_idx)] = SquareType.TILE
            elif element == '#':
                my_map[(row_idx, column_idx)] = SquareType.WALL


def compute_score(position_list, facing) -> int:
    x = int(position_list[0])
    y = int(position_list[1])
    facing_value = facing.value

    # The final password is the sum of 1000 times the row, 4 times the column, and the facing.
    score = 1000 * x + 4 * y + facing_value

    return score


def main():
    day, part = get_day_and_part(__file__)

    puzzle = Puzzle(year=2022, day=day)
    data = puzzle.input_data
    print(data)

    # solution
    instruction, max_x, max_y = draw_map(data)
    me = Me(my_map, max_x, max_y)
    me.move_by_instructions(instruction)

    ans = compute_score(me.position, me.facing)

    # submit
    submit_answer(ans, day, part)


if __name__ == '__main__':
    main()
