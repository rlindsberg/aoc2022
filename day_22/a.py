from aocd.models import Puzzle

from day_22.Me import Me
from helpers import get_day_and_part, submit_answer

from enums import Facing, SquareType

my_map = {}


def draw_map(data):
    input_list = data.split("\n")
    for idx, row in enumerate(input_list):
        # reached the end
        if row == '':
            instruction = input_list[-1]
            return instruction

        row_idx = idx + 1
        for idx2, element in enumerate(row):
            column_idx = idx2 + 1

            # empty
            if element == ' ':
                my_map[(row_idx, column_idx)] = SquareType.EMPTY
            elif element == '.':
                my_map[(row_idx, column_idx)] = SquareType.TILE
            elif element == '#':
                my_map[(row_idx, column_idx)] = SquareType.WALL

        print(row)

    return None


def main():
    day, part = get_day_and_part(__file__)

    puzzle = Puzzle(year=2022, day=day)
    data = puzzle.input_data

    # solution
    instruction = draw_map(data)
    me = Me(my_map)
    me.move_by_instructions(instruction)
    ans = 0

    # submit
    submit_answer(ans, day, part)


if __name__ == '__main__':
    main()
