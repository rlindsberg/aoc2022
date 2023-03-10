from day_9.knot import Knot
from helpers import get_day_and_part, submit_answer, get_input_data


def move_head_tail_and_compute_n_visited_pos(data, head, tail_list):
    """Simulate your complete hypothetical series of motions"""

    input_list = data.split("\n")
    for input_ in input_list:
        cmd = input_[0]
        n_steps = int(input_[2:])

        for _ in range(n_steps):
            head.move(direction=cmd)

            for idx, tail in enumerate(tail_list):
                if idx == 0:
                    tail.follow(head)
                else:
                    tail.follow(tail_list[idx - 1])
            tail_list[-1].register_visited_position()

    return len(tail_list[-1].visited_positions)


def main():
    # get input data
    day, part = get_day_and_part(__file__)
    data = get_input_data(day)

    # solution
    head = Knot()
    tail = [Knot()]

    ans = move_head_tail_and_compute_n_visited_pos(data, head, tail)

    # submit
    submit_answer(ans, day, part)


if __name__ == '__main__':
    main()
