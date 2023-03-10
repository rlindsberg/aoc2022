import re

from day_11.Monkey import Monkey
from helpers import get_day_and_part, submit_answer, get_input_data


def parse_input_and_create_monkeys(data) -> list:
    monkey_list = []
    input_list = data.split("\n\n")

    for raw_monkey_input in input_list:
        raw_monkey_list = raw_monkey_input.split('\n')

        item_list = list(map(int, re.findall(r'\d+', raw_monkey_list[1])))

        op_list = raw_monkey_list[2].split('=')
        op = op_list[1]

        test_list = raw_monkey_list[3].split('by')
        test = 'new %' + test_list[1]

        next_monkey_if_true = re.search(r'\d+', raw_monkey_list[4]).group()
        next_monkey_if_false = re.search(r'\d+', raw_monkey_list[5]).group()

        monkey = Monkey(item_list, op, test, int(next_monkey_if_true), int(next_monkey_if_false))
        monkey_list.append(monkey)

    return monkey_list


def main():
    # get input data
    day, part = get_day_and_part(__file__)
    data = get_input_data(day)

    # solution
    monkey_list = parse_input_and_create_monkeys(data)

    # 20 rounds
    for round_ in range(10000):
        print(round_)
        for monkey in monkey_list:
            while len(monkey.item_list) != 0:
                # Monkey inspects an item with a worry level of 79.
                item = monkey.item_list.pop(0)
                monkey.n_inspection += 1

                # Worry level is multiplied by 19 to 1501.
                old = item
                new = eval(monkey.op)

                # Worry level is divided by 3 to 500.
                new = new % (13*2*7*17*5*11*3*19)

                # Current worry level is not divisible by 23
                res = eval(monkey.test_func)
                next_monkey_id = None
                if res == 0:
                    # true
                    next_monkey_id = monkey.next_monkey_if_true
                else:
                    next_monkey_id = monkey.next_monkey_if_false

                # throws
                next_monkey: Monkey = monkey_list[next_monkey_id]
                next_monkey.item_list.append(new)

    # result
    n_inspection_list = [m.n_inspection for m in monkey_list]
    n_inspection_list.sort()

    ans = n_inspection_list[-1] * n_inspection_list[-2]

    # submit
    submit_answer(ans, day, part)


if __name__ == '__main__':
    main()
