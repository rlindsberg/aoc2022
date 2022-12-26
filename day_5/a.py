import queue

from aocd.models import Puzzle

from helpers import get_day_and_part, submit_answer


def load_stacks(stacks_input_list) -> list:
    # the second last char in the last line is the number of stacks
    n_stacks = int(stacks_input_list[-1][-2])

    # create stack 1 - 9; set stacks[0] to None
    stacks = [queue.LifoQueue() if i > 0 else None for i in range(n_stacks + 1)]

    n_layers = len(stacks_input_list) - 1
    for i in reversed(range(n_layers)):
        layer_str = stacks_input_list[i]

        for char_idx in range(1, len(layer_str), 4):
            char = layer_str[char_idx]

            if char != ' ':
                # found crate
                stack_idx = (char_idx - 1) // 4
                # stack is one-indexed
                stack_idx += 1
                stacks[stack_idx].put(char)

    return stacks


def move_crates(data):
    stacks_input_list, instructions_list = (line.splitlines() for line in data.split("\n\n"))

    stacks = load_stacks(stacks_input_list)

    for instruction in instructions_list:
        inst_list = instruction.split(' ')
        n_move_per_inst = int(inst_list[1])
        source = int(inst_list[3])
        dest = int(inst_list[-1])

        # move
        for i in range(n_move_per_inst):
            crate_to_move = stacks[source].get()
            stacks[dest].put(crate_to_move)

    return stacks


def compute_message(final_stacks) -> str:
    message = ''

    for stack_idx in range(1, len(final_stacks)):
        last_crate = final_stacks[stack_idx].get()
        message += last_crate

    return message


def main():
    day, part = get_day_and_part(__file__)

    puzzle = Puzzle(year=2022, day=day)
    data = puzzle.input_data

    final_stacks = move_crates(data)

    ans = compute_message(final_stacks)

    submit_answer(ans, day, part)


if __name__ == '__main__':
    main()
