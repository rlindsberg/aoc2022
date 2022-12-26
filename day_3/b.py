from string import ascii_letters

from aocd.models import Puzzle

from helpers import get_day_and_part, submit_answer


def sum_of_priorities(data):
    input_list = data.split("\n")

    sum_prio = 0
    for i in range(0, len(input_list), 3):
        rucksacks = input_list[i:i + 3]

        for val, char in enumerate(ascii_letters):
            first = rucksacks[0]
            second = rucksacks[1]
            last = rucksacks[2]

            if char in first and char in second and char in last:
                # found badge
                sum_prio += val + 1

    return sum_prio


def main():
    day, part = get_day_and_part(__file__)

    puzzle = Puzzle(year=2022, day=day)
    data = puzzle.input_data

    ans = sum_of_priorities(data)

    submit_answer(ans, day, part)


if __name__ == '__main__':
    main()
