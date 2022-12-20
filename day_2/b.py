import numpy as np
from aocd.models import Puzzle
from numpy import sqrt, cos, sin, pi

from helpers import get_day_and_part, submit_answer

# A means rock, B means paper and C means scissors
letter_score_dict = {'A': 1, 'B': 2, 'C': 3}
outcome_score_dict = {'Z': 6, 'Y': 3, 'X': 0}

# win means go forward, lost means go backward in letter_score_dict
win_step = 1
lost_step = -1

letter_to_coordinates_map = {'A': np.array([0, 1]), 'B': np.array([sqrt(3) / 2, -1 / 2]),
                             'C': np.array([-sqrt(3) / 2, -1 / 2])}

# cos(theta), -sin(theta)
# sin(theta), cos(theta)
rotate_left_120 = np.array([cos(2 * pi / 3), -sin(2 * pi / 3), sin(2 * pi / 3), cos(2 * pi / 3)]).reshape(2, 2)
rotate_right_120 = np.array([cos(-2 * pi / 3), -sin(-2 * pi / 3), sin(-2 * pi / 3), cos(-2 * pi / 3)]).reshape(2, 2)


def get_letter_from_coordinates(coordinates_np) -> str:
    for key, val in letter_to_coordinates_map.items():
        tolerance = 0.001

        # np.array_equal
        is_equal = (abs(val - coordinates_np) <= tolerance).all()
        if is_equal:
            return key


def compute_scores(data):
    input_list = data.split("\n")

    sum_ = 0
    for round_ in input_list:
        opponent_letter = round_[0]
        outcome_letter = round_[-1]

        # X means lost, Y means draw and Z means win"
        # draw
        if outcome_letter == 'Y':
            shape_score = letter_score_dict[opponent_letter]
            outcome_score = 3
            sum_ = sum_ + shape_score + outcome_score

        # win, rotate forwards (to the right) by 120 degrees
        elif outcome_letter == 'Z':
            our_letter_np = rotate_right_120 @ letter_to_coordinates_map[opponent_letter]
            our_letter = get_letter_from_coordinates(our_letter_np)
            shape_score = letter_score_dict[our_letter]
            outcome_score = 6
            sum_ = sum_ + shape_score + outcome_score

        # lost, rotate backwards
        else:
            our_letter_np = rotate_left_120 @ letter_to_coordinates_map[opponent_letter]
            our_letter = get_letter_from_coordinates(our_letter_np)
            shape_score = letter_score_dict[our_letter]
            sum_ += shape_score

    return sum_


def main():
    day, part = get_day_and_part(__file__)

    puzzle = Puzzle(year=2022, day=day)
    data = puzzle.input_data

    # solution
    ans = compute_scores(data)

    # submit
    submit_answer(ans, day, part)


if __name__ == '__main__':
    main()
