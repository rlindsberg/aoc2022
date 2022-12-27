from day_7.Finder import Finder
from day_7.Folder import Folder
from helpers import get_day_and_part, submit_answer, get_input_data


def sum_all_sub_folder_sizes(finder, data, at_most):
    input_list = data.split("$ ")[1:]

    # parse input and build dir map
    for cmd_str in input_list:

        finder.exec_cmd(cmd_str)

    sum_ = 0
    print('sum')
    for k, v in finder.folder_name_to_obj_map.items():
        if type(v) == Folder:
            my_folder: Folder = v
            if my_folder.name != '/':

                # sum
                if my_folder.size <= at_most:
                    sum_ += my_folder.size

    return sum_


def main():
    # get input data
    day, part = get_day_and_part(__file__)
    data = get_input_data(day)

    # solution
    ans = sum_all_sub_folder_sizes(data, at_most=100000)

    # submit
    # submit_answer(ans, day, part)


if __name__ == '__main__':
    main()
