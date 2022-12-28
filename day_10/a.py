from day_10.CPU import CPU
from helpers import get_day_and_part, submit_answer, get_input_data


def parse_and_exec_cmd(data, cpu):
    input_list = data.split("\n")

    for input_ in input_list:
        cpu.parse_and_exec_cmd(input_)

    return 0


def main():
    # get input data
    day, part = get_day_and_part(__file__)
    data = get_input_data(day)

    # solution
    cpu = CPU()
    parse_and_exec_cmd(data, cpu)

    # submit
    # submit_answer(cpu.sum_signal_strength, day, part)


if __name__ == '__main__':
    main()
