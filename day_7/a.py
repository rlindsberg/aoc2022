from day_7.Finder import Finder
from day_7.Folder import Folder
from helpers import get_day_and_part, submit_answer, get_input_data


def sum_all_sub_folder_sizes(data, at_most):
    input_list = data.split("$ ")[1:]

    # some preparation
    finder = Finder()

    # parse input and build dir map
    for cmd_str in input_list:

        finder.exec_cmd(cmd_str)

    return 0


def main():
    # get input data
    day, part = get_day_and_part(__file__)
    data = get_input_data(day)

    # solution
    ans = sum_all_sub_folder_sizes(data)

    # submit
    # submit_answer(ans, day, part)


if __name__ == '__main__':
    main()
