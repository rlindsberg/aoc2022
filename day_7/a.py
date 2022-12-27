from helpers import get_day_and_part, submit_answer, get_input_data


def something(data):

    return 0


def main():
    # get input data
    day, part = get_day_and_part(__file__)
    data = get_input_data(day)

    # solution
    ans = something(data)

    # submit
    submit_answer(ans, day, part)


if __name__ == '__main__':
    main()
