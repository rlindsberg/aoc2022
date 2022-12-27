from day_7.Finder import Finder
from day_7.Folder import Folder
from day_7.a import sum_all_sub_folder_sizes
from helpers import get_day_and_part, submit_answer, get_input_data


def main():
    # get input data
    day, part = get_day_and_part(__file__)
    data = get_input_data(day)

    # solution
    finder = Finder()
    sum_all_sub_folder_sizes(finder, data, at_most=100000)

    ans = finder.find_which_dir_to_delete()

    # submit
    submit_answer(ans, day, part)


if __name__ == '__main__':
    main()
