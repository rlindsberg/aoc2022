import numpy as np

from helpers import get_day_and_part, submit_answer, get_input_data


def build_map(data):
    heightmap = []
    input_list = data.split("\n")

    # use reversed because I want the (0, 0) to be the bottom-left corner
    for input_ in reversed(input_list):
        heightmap.append([h for h in input_])

    # use transpose so that all heights are indexed (x, y)
    heightmap_np = np.array(heightmap).transpose()

    return heightmap_np


def main():
    # get input data
    # day, part = get_day_and_part(__file__)
    # data = get_input_data(day)

    data = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

    # solution
    heightmap = build_map(data)

    # submit
    # submit_answer(ans, day, part)


if __name__ == '__main__':
    main()
