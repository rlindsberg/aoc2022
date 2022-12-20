from aocd.models import Puzzle

from helpers import get_day_and_part, submit_answer


def sum_calories_for_each_elf(data):
    """Each Elf is carrying some Calories separated by a blank line, and this function sums them up"""
    calorie_dict = {}
    input_list = data.split("\n")

    sum_ = 0
    for idx, calorie in enumerate(input_list):
        if calorie != '':
            sum_ += int(calorie)
        else:
            # finished
            calorie_dict[idx] = sum_
            sum_ = 0

    # return sorted_calorie_dict
    return {k: v for k, v in sorted(calorie_dict.items(), key=lambda item: item[1])}


def main():
    day, part = get_day_and_part(__file__)

    puzzle = Puzzle(year=2022, day=day)
    data = puzzle.input_data

    sorted_calorie_dict = sum_calories_for_each_elf(data)

    largest_calories = list(sorted_calorie_dict.values())[-1]

    submit_answer(largest_calories, day, part)


if __name__ == '__main__':
    main()
