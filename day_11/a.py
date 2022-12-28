import re

from day_11.Monkey import Monkey
from helpers import get_day_and_part, submit_answer, get_input_data


def parse_input_and_create_monkeys(data) -> list:
    monkey_list = []
    input_list = data.split("\n\n")

    for raw_monkey_input in input_list:
        raw_monkey_list = raw_monkey_input.split('\n')

        monkey_id_str = raw_monkey_list[0]
        monkey_id = re.search(r'\d+', monkey_id_str).group()

        item_list = list(map(int, re.findall(r'\d+', raw_monkey_list[1])))

        op_list = raw_monkey_list[2].split('=')
        op = op_list[1]

        test_list = raw_monkey_list[3].split('by')
        test = 'new %' + test_list[1]

        next_monkey_if_true = re.search(r'\d+', raw_monkey_list[4]).group()
        next_monkey_if_false = re.search(r'\d+', raw_monkey_list[5]).group()

        monkey = Monkey(op, test, next_monkey_if_true, next_monkey_if_false)
        monkey_list.append(monkey)

    return monkey_list


def main():
    # get input data
    day, part = get_day_and_part(__file__)
    data = get_input_data(day)

    # solution
    monkey_list = parse_input_and_create_monkeys(data)

    # submit
    # submit_answer(ans, day, part)


if __name__ == '__main__':
    main()
