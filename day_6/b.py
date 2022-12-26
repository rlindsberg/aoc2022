from aocd.models import Puzzle

from day_6.a import find_start_of_packet_marker_index
from helpers import get_day_and_part, submit_answer


def main():
    day, part = get_day_and_part(__file__)

    puzzle = Puzzle(year=2022, day=day)
    data = puzzle.input_data

    ans = find_start_of_packet_marker_index(data, 14)

    submit_answer(ans, day, part)


if __name__ == '__main__':
    main()
