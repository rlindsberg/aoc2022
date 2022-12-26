from aocd.models import Puzzle

from helpers import get_day_and_part, submit_answer


def find_start_of_packet_marker_index(data):
    for i in range(len(data) - 3):
        sub_str = data[i:i+4]

        if len(set(sub_str)) == 4:
            return i + 4

    return 0


def main():
    day, part = get_day_and_part(__file__)

    puzzle = Puzzle(year=2022, day=day)
    data = puzzle.input_data

    ans = find_start_of_packet_marker_index(data)

    submit_answer(ans, day, part)


if __name__ == '__main__':
    main()
