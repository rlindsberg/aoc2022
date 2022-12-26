from string import ascii_letters

from aocd.models import Puzzle

from helpers import get_day_and_part, submit_answer


def find_wrong_items(data) -> dict:
    wrong_item_occurrence = {}
    for char in ascii_letters:
        wrong_item_occurrence[char] = 0

    input_list = data.split("\n")
    for rucksack in input_list:
        mid = len(rucksack) // 2
        first_compartment = rucksack[:mid]
        last_compartment = rucksack[mid:]

        assert len(first_compartment) == len(last_compartment)

        # The Elf that did the packing failed to follow this rule for exactly one item type per rucksack.
        # find the wrong item
        first = set(first_compartment)
        last = set(last_compartment)
        for item in first:
            if item in last:
                # wrong item found
                wrong_item_occurrence[item] += 1

    return wrong_item_occurrence


def sum_of_priorities(wrong_item_occurrence) -> int:
    sum_prio = 0
    for val, char in enumerate(ascii_letters):
        occurrence = wrong_item_occurrence[char]

        # Lowercase item types a through z have priorities 1 through 26.
        # Uppercase item types A through Z have priorities 27 through 52.
        sum_prio += occurrence * (val + 1)

    return sum_prio


def main():
    day, part = get_day_and_part(__file__)

    puzzle = Puzzle(year=2022, day=day)
    data = puzzle.input_data

    wrong_item_occurrence = find_wrong_items(data)
    ans = sum_of_priorities(wrong_item_occurrence)

    submit_answer(ans, day, part)


if __name__ == '__main__':
    main()
