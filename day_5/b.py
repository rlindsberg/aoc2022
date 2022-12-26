from aocd.models import Puzzle

from day_5.a import load_stacks, compute_message
from helpers import get_day_and_part, submit_answer


def move_crates(data):
    stacks_input_list, instructions_list = (line.splitlines() for line in data.split("\n\n"))

    stacks = load_stacks(stacks_input_list)

    for instruction in instructions_list:
        inst_list = instruction.split(' ')
        n_move_per_inst = int(inst_list[1])
        source = int(inst_list[3])
        dest = int(inst_list[-1])

        # move
        raise NotImplemented
    
    return stacks


def main():
    day, part = get_day_and_part(__file__)

    puzzle = Puzzle(year=2022, day=day)
    data = puzzle.input_data

    final_stacks = move_crates(data)

    ans = compute_message(final_stacks)

    submit_answer(ans, day, part)


if __name__ == '__main__':
    main()
