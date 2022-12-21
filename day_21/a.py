from aocd.models import Puzzle

from day_21.b import build_yell_dict
from helpers import get_day_and_part, submit_answer

yell_dict = {}


def do_math_if_ready(monkey_name, yell_list):
    """This function calculates the expression if yell_list is a valid math expr"""
    operand_1 = yell_list[0]
    operator = yell_list[1]
    operand_2 = yell_list[2]

    if type(operand_1) == int and type(operand_2) == int:
        # do math
        if operator == '+':
            yell_dict[monkey_name] = operand_1 + operand_2
        elif operator == '-':
            yell_dict[monkey_name] = operand_1 - operand_2
        elif operator == '*':
            yell_dict[monkey_name] = operand_1 * operand_2
        else:
            yell_dict[monkey_name] = operand_1 // operand_2


def resolve_root(data):
    """This function resolves when the root monkey should yell"""
    build_yell_dict(data)

    # resolve
    while type(yell_dict['root']) != int:
        for key, val in yell_dict.items():
            if type(val) == int:

                # update all keys
                for k, v in yell_dict.items():
                    # skip if already a number
                    if type(v) == int:
                        continue

                    if v[0] == key:
                        v[0] = val
                        do_math_if_ready(k, v)

                    elif v[2] == key:
                        v[2] = val
                        do_math_if_ready(k, v)

    return yell_dict['root']


def main():
    day, part = get_day_and_part(__file__)

    puzzle = Puzzle(year=2022, day=day)
    data = puzzle.input_data

    # solution
    ans = resolve_root(data)

    # submit
    submit_answer(ans, day, part)


if __name__ == '__main__':
    main()
