from aocd.models import Puzzle

from helpers import get_day_and_part

day, part = get_day_and_part(__file__)

puzzle = Puzzle(year=2022, day=13)
data = puzzle.input_data

print(data)
