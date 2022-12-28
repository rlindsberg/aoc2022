from day_9.a import move_head_tail_and_compute_n_visited_pos
from day_9.knot import Knot
from helpers import get_day_and_part, get_input_data, submit_answer


def main():
    # get input data
    day, part = get_day_and_part(__file__)
    data = get_input_data(day)

    # solution
    head = Knot()
    tail_list = [Knot() for _ in range(9)]

    ans = move_head_tail_and_compute_n_visited_pos(data, head, tail_list)

    # submit
    submit_answer(ans, day, part)


if __name__ == '__main__':
    main()
