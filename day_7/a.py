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

    sum_ = 0
    print('sum')
    for k, v in finder.inode_name_to_obj_map.items():
        if type(v) == Folder:
            my_folder: Folder = v
            if my_folder.name != '/':
                sum_ += my_folder.size

    return sum_


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
