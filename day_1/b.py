from aocd.models import Puzzle

from day_1.a import sum_calories_for_each_elf
from helpers import get_day_and_part, submit_answer


def main():
    day, part = get_day_and_part(__file__)

    puzzle = Puzzle(year=2022, day=day)
    data = puzzle.input_data

    sorted_calorie_dict = sum_calories_for_each_elf(data)

    largest_calories_list = list(sorted_calorie_dict.values())[-3:]
    sum_largest_three_elves = sum(largest_calories_list)

    submit_answer(sum_largest_three_elves, day, part)


if __name__ == '__main__':
    main()
