""" This file collects some helper functions for solving puzzles.
"""
from aocd import submit


def get_day_and_part(file_name: str) -> (int, str):
    """for automated submission"""
    day_and_part = file_name.partition('_')[2]
    part = day_and_part[-4]
    day = day_and_part[:-5]

    return int(day), part


def submit_answer(my_answer, day: int, part: str):
    res = submit(my_answer, part=part, day=day, year=2022)
    print(res)
