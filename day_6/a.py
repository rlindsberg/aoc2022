from aocd.models import Puzzle

from helpers import get_day_and_part, submit_answer


def find_start_of_packet_marker_index(data, n_distinct_chars=4):
    for i in range(len(data) - 3):
        sub_str = data[i:i + n_distinct_chars]

        if len(set(sub_str)) == n_distinct_chars:
            return i + n_distinct_chars

    return 0


def main():
    day, part = get_day_and_part(__file__)

    puzzle = Puzzle(year=2022, day=day)
    data = puzzle.input_data

    ans = find_start_of_packet_marker_index(data)

    submit_answer(ans, day, part)


if __name__ == '__main__':
    main()
