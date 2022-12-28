import numpy as np

from helpers import get_day_and_part, submit_answer, get_input_data


def count_visible_trees(data):
    tree_2d_list = [[int(tree) for tree in row] for row in data.split("\n")]
    tree_array = np.array(tree_2d_list)

    n_visible_tree = 4 * (len(tree_array) - 2) + 4
    # second row - second last row
    for y in range(1, len(tree_array) - 1):
        # second column - second last column
        for x in range(1, len(tree_array) - 1):
            tree = tree_array[y][x]

            north_trees = tree_array[:y, x]
            south_trees = tree_array[y + 1:, x]
            east_trees = tree_array[y, x + 1:]
            west_trees = tree_array[y, :x]

            north = max(north_trees)
            south = max(south_trees)
            east = max(east_trees)
            west = max(west_trees)
            if tree <= min(north, east, south, west):
                print('potential tree')
                pass
            else:
                # visible tree
                n_visible_tree += 1

    return n_visible_tree


def main():
    # get input data
    day, part = get_day_and_part(__file__)
    data = get_input_data(day)

    # solution
    ans = count_visible_trees(data)

    # submit
    # submit_answer(ans, day, part)


if __name__ == '__main__':
    main()
