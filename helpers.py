""" This file collects some helper functions for solving puzzles.
"""
from aocd import submit
from aocd.models import Puzzle


def get_day_and_part(file_name: str) -> (int, str):
    """for automated submission"""
    day_and_part = file_name.partition('_')[2]
    part = day_and_part[-4]
    day = day_and_part[:-5]

    return int(day), part


def get_input_data(day: str):
    """Get input data from adventofcode.com"""
    puzzle = Puzzle(year=2022, day=day)

    return puzzle.input_data


def submit_answer(my_answer, day: int, part: str):
    """Submit your answer to adventofcode.com"""
    res = submit(my_answer, part=part, day=day, year=2022)
    print(res)
