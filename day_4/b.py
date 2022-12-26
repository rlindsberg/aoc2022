from aocd.models import Puzzle

from day_4.a import compute_elv_start_end
from helpers import get_day_and_part, submit_answer


def calculate_n_overlapping_sections(data) -> int:
    input_list = data.split("\n")

    n_overlapping = 0
    for line in input_list:
        pair = line.split(',')

        elv_1_start, elv_1_end, elv_2_start, elv_2_end = compute_elv_start_end(pair)

        if elv_2_start > elv_1_end or (elv_2_start < elv_1_start and elv_2_end < elv_1_start):
            # no overlapping
            continue

        n_overlapping += 1

    return n_overlapping


def main():
    day, part = get_day_and_part(__file__)

    puzzle = Puzzle(year=2022, day=day)
    data = puzzle.input_data

    ans = calculate_n_overlapping_sections(data)

    submit_answer(ans, day, part)


if __name__ == '__main__':
    main()
