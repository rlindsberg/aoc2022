import numpy as np

from helpers import get_day_and_part, submit_answer, get_input_data


def compute_scenic_score(data):
    tree_2d_list = [[int(tree) for tree in row] for row in data.split("\n")]
    tree_array = np.array(tree_2d_list)

    highest_scenic_score = 0
    for y in range(len(tree_array)):
        for x in range(len(tree_array)):
            if y == 3 and x == 2:
                print('')
            tree = tree_array[y][x]
            north_score, south_score, east_score, west_score = 0, 0, 0, 0

            north_trees = tree_array[:y, x]
            south_trees = tree_array[y + 1:, x]
            east_trees = tree_array[y, x + 1:]
            west_trees = tree_array[y, :x]

            # look up
            for north_tree in reversed(north_trees):
                north_score += 1
                if north_tree >= tree:
                    # view is blocked
                    break

            # look down
            for south_tree in south_trees:
                south_score += 1
                if south_tree >= tree:
                    break

            # look right
            for east_tree in east_trees:
                east_score += 1
                if east_tree >= tree:
                    break

            # look left
            for west_tree in reversed(west_trees):
                west_score += 1
                if west_tree >= tree:
                    break

            scenic_score = north_score * east_score * south_score * west_score

            if scenic_score > highest_scenic_score:
                highest_scenic_score = scenic_score

    return highest_scenic_score


def main():
    # get input data
    day, part = get_day_and_part(__file__)
    data = get_input_data(day)

    # solution
    ans = compute_scenic_score(data)

    # submit
    submit_answer(ans, day, part)


if __name__ == '__main__':
    main()
