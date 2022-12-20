""" This file collects some helper functions for solving puzzles.
"""


def get_day_and_part(file_name: str) -> (int, str):
    """for automated submission"""
    day_and_part = file_name.partition('_')[2]
    part = day_and_part[-4]
    day = day_and_part[:-5]

    return int(day), part
