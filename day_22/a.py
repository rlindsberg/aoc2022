from aocd.models import Puzzle

from day_22.Map import Map
from day_22.Person import Person
from helpers import get_day_and_part, submit_answer

from day_22.util_functions import SquareType


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
    my_map = Map(data)
    # instruction, max_x, max_y = draw_map(data)
    # me = Person(my_map, max_x, max_y)
    # me.move_by_instructions(instruction)
    #
    # ans = compute_score(me.position, me.facing)
    #
    # submit
    # submit_answer(ans, day, part)


if __name__ == '__main__':
    main()
