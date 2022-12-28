from day_9.knot import Knot
from helpers import get_day_and_part, submit_answer, get_input_data


def move_head_tail_according_to_input(data):
    """Simulate your complete hypothetical series of motions"""
    head = Knot()
    tail = Knot()

    input_list = data.split("\n")
    for input_ in input_list:
        cmd = input_[0]
        n_steps = int(input_[2:])

        for _ in range(n_steps):
            head.move(direction=cmd)

            tail.follow(head)

    return 0


def main():
    # get input data
    day, part = get_day_and_part(__file__)
    data = get_input_data(day)

    # solution
    ans = move_head_tail_according_to_input(data)

    # submit
    # submit_answer(ans, day, part)


if __name__ == '__main__':
    main()
