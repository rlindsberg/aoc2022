from aocd.models import Puzzle

from helpers import get_day_and_part, submit_answer

shape_score_dict = {'rock': 1, 'paper': 2, 'scissors': 3}
outcome_score_dict = {'win': 6, 'draw': 3, 'lost': 0}
letter_shape_dict = {'A': 'rock', 'X': 'rock', 'B': 'paper', 'Y': 'paper', 'C': 'scissors', 'Z': 'scissors'}
win_shape_list = [('rock', 'paper'), ('paper', 'scissors'), ('scissors', 'rock')]


def compute_scores(data):
    input_list = data.split("\n")

    sum_ = 0
    for round_ in input_list:
        opponent_letter = round_[0]
        ours_letter = round_[-1]

        opponent = letter_shape_dict[opponent_letter]
        ours = letter_shape_dict[ours_letter]

        # draw
        if opponent == ours:
            shape_score = shape_score_dict[ours]
            outcome_score = outcome_score_dict['draw']
            sum_ = sum_ + shape_score + outcome_score
        # win
        elif (opponent, ours) in win_shape_list:
            shape_score = shape_score_dict[ours]
            outcome_score = outcome_score_dict['win']
            sum_ = sum_ + shape_score + outcome_score
        else:
            shape_score = shape_score_dict[ours]
            outcome_score = outcome_score_dict['lost']
            sum_ = sum_ + shape_score + outcome_score

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
