from aocd.models import Puzzle
from sympy import solve, sympify

from helpers import get_day_and_part, submit_answer

yell_dict = {}


def build_yell_dict(data):
    """Stores the input data into internal data structure for further reference"""
    input_list = data.split("\n")

    for line in input_list:
        line_list = line.split(': ')
        monkey_name = line_list[0]
        yell = line_list[1]

        # convert to int if it is a number
        if yell.isnumeric():
            yell_num = int(yell)
            yell_dict[monkey_name] = yell_num
        else:
            yell_list = yell.split(' ')
            yell_dict[monkey_name] = yell_list

    return yell_dict


def build_equation(monkey_name):
    """A recursive function to build a math expr, by resolving unknown monkey name"""

    # humn is the unknown variable x
    if monkey_name == 'humn':
        return 'x'

    # resolved an unknown monkey name. So it returns its value
    if type(yell_dict[monkey_name]) == int:
        return yell_dict[monkey_name]

    yell_list = yell_dict[monkey_name]
    operand_1 = yell_list[0]
    operator = yell_list[1]
    operand_2 = yell_list[2]

    return f'({build_equation(operand_1)} {operator} {build_equation(operand_2)})'


def main():
    day, part = get_day_and_part(__file__)

    puzzle = Puzzle(year=2022, day=day)
    data = puzzle.input_data

    # solution
    build_yell_dict(data)

    yell_list = yell_dict['root']
    yell_dict['root'] = [yell_list[0], yell_list[2]]
    yell_dict['humn'] = 'x'

    left_str = build_equation(yell_list[0])
    right_str = build_equation(yell_list[2])

    # convert a string to math expr
    left_eq = sympify(left_str)
    right_eq = sympify(right_str)

    expr = left_eq - right_eq

    sol = solve(expr)
    ans = sol[0]

    # submit
    submit_answer(ans, day, part)


if __name__ == '__main__':
    main()
