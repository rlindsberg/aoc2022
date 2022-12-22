from aocd.models import Puzzle

from day_22.Map import Map
from day_22.Person import Person
from helpers import get_day_and_part, submit_answer


def main():
    day, part = get_day_and_part(__file__)

    puzzle = Puzzle(year=2022, day=day)
    data = puzzle.input_data
    print(data)

    # solution
    my_map = Map(data)

    me = Person(my_map)

    instruction = data.split('\n')[-1]
    me.move_by_instruction(instruction)

    ans = me.compute_score()

    # submit
    submit_answer(ans, day, part)


if __name__ == '__main__':
    main()
