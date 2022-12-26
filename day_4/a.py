from aocd.models import Puzzle

from helpers import get_day_and_part, submit_answer


def compute_elv_start_end(pair: list) -> (int, int, int, int):
    # pair is e.g. '4-90,1-4'
    elv_1_range = pair[0]
    elv_2_range = pair[1]

    elv_1 = elv_1_range.split('-')
    elv_2 = elv_2_range.split('-')

    elv_1_start = int(elv_1[0])
    elv_1_end = int(elv_1[1])
    elv_2_start = int(elv_2[0])
    elv_2_end = int(elv_2[1])

    return elv_1_start, elv_1_end, elv_2_start, elv_2_end


def calculate_n_fully_contained_sections(data) -> int:
    input_list = data.split("\n")

    n_fully_contained = 0
    for line in input_list:
        pair = line.split(',')

        elv_1_start, elv_1_end, elv_2_start, elv_2_end = compute_elv_start_end(pair)

        if (elv_2_start >= elv_1_start) and (elv_2_end <= elv_1_end):
            # elv 2 is included in elv 1
            n_fully_contained += 1
            continue

        if (elv_2_start <= elv_1_start) and (elv_2_end >= elv_1_end):
            # elv 1 is included in elv 2
            n_fully_contained += 1
            continue

    return n_fully_contained


def main():
    day, part = get_day_and_part(__file__)

    puzzle = Puzzle(year=2022, day=day)
    data = puzzle.input_data

    ans = calculate_n_fully_contained_sections(data)

    submit_answer(ans, day, part)


if __name__ == '__main__':
    main()
